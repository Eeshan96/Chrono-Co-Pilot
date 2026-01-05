Chrono Copilot

Chrono Copilot is a lightweight AI-powered command-line assistant designed to help users prepare for interviews by reflecting on past experiences, organizing present thoughts, and thinking strategically about future steps. It combines structured conversation, contextual memory, and a small touch of personality to keep the interaction engaging but focused.

The project was built as a coding sample to demonstrate simplicity, clarity, AI integration, and thoughtful design within a small scope.

What It Does?

Chrono Copilot runs as a CLI chatbot with three intentional thinking modes:

Past mode: Reflective and lessons-oriented

Present mode: Practical and structured

Future mode: Strategic and forward-looking

It remembers recent conversation context across runs using a lightweight local memory file and occasionally responds with playful Easter eggs triggered by specific keywords.

Features of Chrono Co-pilot

Command-line interface (CLI)

AI-powered responses using OpenAI’s API

Mode switching (past, present, future)

Short-term memory persistence using JSON

Controlled creativity (Easter eggs and playful behavior)

Graceful handling of missing API keys and API errors



Setup Instructions for this-
1. Create a virtual enviroment.
python -m venv .venv
source .venv/bin/activate

2. Install dependencies
pip install -r requirements.txt

3. Configure environment variables

Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here


4.Running the Application

python -m app.main


You should see:

Chrono Copilot (CLI)
Type /help for commands. Type /quit to exit.

Available Commands

/help — Show available commands

/mode past — Reflect on past experiences

/mode present — Focus on current thinking

/mode future — Think about next steps

/quit — Exit the program (conversation is saved)


Memory Behavior

Chrono Copilot stores a limited number of recent messages locally in a JSON file to maintain conversational context across runs. The memory size is intentionally capped to keep behavior predictable and avoid excessive API usage.

