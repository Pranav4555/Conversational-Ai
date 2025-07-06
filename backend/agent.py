from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from backend.config import GROQ_API_KEY
from backend.calendar_utils import check_availability, create_event
from datetime import datetime, timedelta

# Initialize Groq LLM (Mixtral-8x7b)
llm = ChatGroq(
    temperature=0,
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-70b-8192"
)

# Tool 1: Check if a slot is available
def check_free_time(query: str) -> str:
    try:
        start = datetime.utcnow() + timedelta(hours=1)
        end = start + timedelta(minutes=30)
        available = check_availability(start.isoformat() + 'Z', end.isoformat() + 'Z')
        return "Available" if available else "Busy"
    except Exception as e:
        print(f"[CheckAvailability Error] {e}")
        return "Unable to check availability."

# Tool 2: Book a slot
def book_slot(query: str) -> str:
    try:
        start = datetime.utcnow() + timedelta(hours=1)
        end = start + timedelta(minutes=30)
        link = create_event("Appointment", start.isoformat() + 'Z', end.isoformat() + 'Z')
        return f"Event created: {link}"
    except Exception as e:
        print(f"[BookAppointment Error] {e}")
        return "Unable to create event."

# Define tools
tools = [
    Tool(
        name="CheckAvailability",
        func=check_free_time,
        description="Checks if the next available 30-minute slot is free."
    ),
    Tool(
        name="BookAppointment",
        func=book_slot,
        description="Books a meeting slot in your calendar 1 hour from now."
    )
]

# Initialize LangChain Agent
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(user_input: str):
    try:
        print(f"Query received: {user_input}")
        return agent_executor.run(user_input)
    except Exception as e:
        print(f"[Agent Error] {e}")
        return "Sorry, something went wrong. Please try again later."
