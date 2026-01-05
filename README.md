* Chrono Copilot *

Chrono Copilot is a lightweight AI-powered command-line assistant designed to help users prepare for interviews by reflecting on past experiences, organizing present thoughts, and thinking strategically about future steps. It combines structured conversation, contextual memory, and a small touch of personality to keep the interaction engaging but focused.

The project was built as a coding sample to demonstrate simplicity, clarity, AI integration, and thoughtful design within a small scope.

* What It Does? *

Chrono Copilot runs as a CLI chatbot with three intentional thinking modes:

Past mode: Reflective and lessons-oriented

Present mode: Practical and structured

Future mode: Strategic and forward-looking

It remembers recent conversation context across runs using a lightweight local memory file and occasionally responds with playful Easter eggs triggered by specific keywords.

*  Features of Chrono Co-pilot *

  1.Command-line interface (CLI)

  2.AI-powered responses using OpenAI’s API

  3.Mode switching (past, present, future)

  4.Short-term memory persistence using JSON

  5.Controlled creativity (Easter eggs and playful behavior)

  6.Handles missing API keys and API errors



* Setup Instructions for this *
  1. Create a virtual enviroment.
    python -m venv .venv
    source .venv/bin/activate

  2. Install dependencies
    pip install -r requirements.txt

  3. Configure environment variables

  4.Create a .env file in the project root and add your OpenAI API key:

    OPENAI_API_KEY=your_api_key_here

* Running the Application *

python -m app.main


You should see this:

Chrono Copilot (CLI)
Type /help for commands. Type /quit to exit.

* Available Commands *

 1./help — Show available commands

 2./mode past — Reflect on past experiences

 3./mode present — Focus on current thinking

 4./mode future — Think about next steps

 5./quit — Exit the program (conversation is saved)



