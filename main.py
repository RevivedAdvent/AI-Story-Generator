from kivy.app import App
from kivy.uix.screenmanager import Screen
import os
import google.generativeai as genai

API_KEY = "" #ADD YOUR API KEY HERE
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

class MainScreen(Screen):

    def generate_story(self):

        if self.ids.story_output.text.startswith("Story saved as"):
            return

        genre = self.ids.genre_input.text.strip()
        word_count = self.ids.word_count_input.text.strip()
        extra_info = self.ids.extra_info_input.text.strip()

        if not genre and not word_count and not extra_info:
            self.ids.story_output.text = "Please provide information in at least one field to generate a story."
            return

        prompt = f"Write a {genre or 'general'} story of about {word_count or 'an appropriate number of'} words. {extra_info or ''}".strip()

        try:

            response = model.generate_content(prompt)
            story = response.text.strip()

        except Exception as e:

            story = f"Error generating story: {e}"

        self.ids.story_output.text = story
    
    def save_story(self):

        story = self.ids.story_output.text.strip()

        if story == "Please provide information in at least one field to generate a story.":
            self.ids.story_output.text = "No story to save. Generate a story first."
            return
        
        if story == "No story to save. Generate a story first.":
            return
        
        if story.startswith("Story saved as"):
            return

        if story:

            if not os.path.exists('Stories'):
                os.makedirs('Stories')

            base_filename = 'story_'
            file_extension = '.txt'

            counter = 1
            while os.path.exists(os.path.join('Stories', f"{base_filename}{counter}{file_extension}")):
                counter += 1

            filename = os.path.join('Stories', f"{base_filename}{counter}{file_extension}")

            with open(filename, 'w') as file:
                file.write(story)

            self.ids.story_output.text = f"Story saved as {filename}, Refresh!"

        else:
            self.ids.story_output.text = "No story to save. Generate a story first."
    
    def refresh(self):

        self.ids.genre_input.text = ""
        self.ids.word_count_input.text = ""
        self.ids.extra_info_input.text = ""
        self.ids.story_output.text = ""

class StoryGeneratorApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    StoryGeneratorApp().run()
