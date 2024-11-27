# AI-Story-Generator
This is an AI-powered story generation application built with Kivy and Google Generative AI. The app allows users to create creative stories based on input genres, word count, and additional prompts. It also provides functionality to save generated stories and refresh the input fields for new stories.

Features-

  Dynamic Story Generation:
      Generate creative stories based on user-defined inputs like genre, word count, and extra details.
  Story Saving:
      Save generated stories automatically with a unique filename in the Stories/ folder.
  Input Reset:
      Clear inputs and start fresh using the refresh functionality.
      
Prerequisites-

    Python 3.7+
    A Google Generative AI API Key.
    Required Python libraries:
        kivy
        google-generativeai

Installation and Setup -

  Clone the Repository:

    git clone https://github.com/yourusername/ai-story-generator.git
    cd ai-story-generator

  Install Dependencies: Use pip to install the required libraries:

    pip install kivy google-generativeai

  Configure API Key:

    Replace the API_KEY in the code with your Google Generative AI API Key:

    API_KEY = "your_api_key_here"

  Run the Application:

    python main.py

Usage -

    Launch the application.
    Input the desired:
        Genre: Type of story (e.g., "science fiction", "mystery").
        Word Count: Approximate length of the story.
        Extra Info: Any specific details or themes for the story.
    Click Generate Story to create your story.
    View the generated story in the output area.
    Save the story to the Stories/ folder by clicking Save Story.
    Use Refresh to clear inputs and the generated story for a new session.

Example Workflow -

    Input:
        Genre: Fantasy
        Word Count: 500
        Extra Info: "Include a dragon and a magical amulet."
    Output:
        A custom story is generated based on the inputs.
    Save the generated story.
        The saved story file will appear in the Stories/ folder, e.g., Stories/story_1.txt.
  
