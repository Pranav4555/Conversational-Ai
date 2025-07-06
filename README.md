# Conversational AI Calendar Agent

This is a fully functional conversational assistant that books appointments directly into your Google Calendar using natural language. Users interact via a Streamlit chat interface, and the backend is powered by FastAPI, LangChain, and a large language model (LLM) like Groq (LLaMA 3).

## Features

- Conversational AI agent with tool-calling capabilities
- Google Calendar integration via Service Account (no OAuth needed)
- Natural language understanding using Groq LLM
- LangChain-powered reasoning and action execution
- FastAPI backend and Streamlit frontend for live interaction
- Secure handling of credentials via .env

## Project Structure

CONVERSATIONAL_AI/
├── backend/
│ ├── agent.py # LangChain agent logic
│ ├── calendar_utils.py # Google Calendar integration functions
│ ├── config.py # Loads environment variables
│ └── main.py # FastAPI app entrypoint
├── credentials/
│ └── service_account.json # Google service account key (keep private)
├── frontend/
│ └── app.py # Streamlit chat interface
├── bot.env # Environment variables
├── .gitignore # Git ignore rules
├── requirements.txt # Python dependencies
└── README.md # This documentation


## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/conversational_ai_agent.git
cd conversational_ai_agent
2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Requirements

pip install -r requirements.txt
4. Add Environment Variables
Create a file named bot.env in the root directory:
env
GROQ_API_KEY=your_groq_api_key
GOOGLE_CALENDAR_ID=your-calendar-id@group.calendar.google.com
GOOGLE_CREDENTIALS_PATH=credentials/service_account.json
5. Add Google Service Account Key
Download your service account JSON key from Google Cloud Console and place it inside the credentials/ folder.

Then, share your Google Calendar with the service account email (found inside the JSON key) with "Make changes and manage sharing" access.

How It Works
User types: "Book a meeting at 6 PM"

LangChain agent parses the intent and determines the tools to use

The agent calls CheckAvailability and, if free, proceeds to BookAppointment

Google Calendar event is created, and a link is returned to the user

Running the Project
Backend (FastAPI)
cd backend
uvicorn main:app --reload
Frontend (Streamlit)
cd frontend
streamlit run app.py
Deployment Instructions
You can deploy this on platforms like:

Render

Railway

Fly.io

When deploying:

Do not push .env, credentials/service_account.json, or venv

Set environment variables in the platform's dashboard

.gitignore
Make sure your .gitignore contains:
.env
bot.env
credentials/
venv/
__pycache__/
*.pyc
Services Used
Service	Purpose
Google Calendar API	Create and check calendar events
Groq (LLaMA 3)	Natural language understanding
LangChain	Agent orchestration and tool use
FastAPI	Backend server
Streamlit	Chat interface frontend

Author
Pranav Baitule
GitHub: github.com/Pranav4555
