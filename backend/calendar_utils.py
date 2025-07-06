from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from backend.config import GOOGLE_CALENDAR_ID, GOOGLE_CREDENTIALS_PATH

def get_calendar_service():
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_CREDENTIALS_PATH,
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    service = build("calendar", "v3", credentials=credentials)
    return service

def check_availability(start_time: str, end_time: str) -> bool:
    service = get_calendar_service()
    events_result = service.events().list(
        calendarId=GOOGLE_CALENDAR_ID,
        timeMin=start_time,
        timeMax=end_time,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    return len(events) == 0  # True = free, False = busy

def create_event(summary: str, start_time: str, end_time: str):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time, 'timeZone': 'Asia/Kolkata'},
    }
    created_event = service.events().insert(calendarId=GOOGLE_CALENDAR_ID, body=event).execute()
    return created_event.get('htmlLink')
