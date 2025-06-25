# backend/email_fetcher.py

import os
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../config/.env'))

# Load environment variables
CLIENT_ID = os.getenv("GMAIL_CLIENT_ID")
CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("GMAIL_REFRESH_TOKEN")
USER_EMAIL = os.getenv("GMAIL_USER_EMAIL")

def fetch_emails():
    # Setup credentials
    creds = Credentials(
        None,
        refresh_token=REFRESH_TOKEN,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_uri="https://oauth2.googleapis.com/token"
    )

    service = build("gmail", "v1", credentials=creds)

    try:
        # Fetch message list
        results = service.users().messages().list(userId='me', maxResults=5).execute()
        messages = results.get('messages', [])

        email_list = []

        for msg in messages:
            msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
            payload = msg_detail.get("payload", {})
            headers = payload.get("headers", [])

            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), '(Unknown Sender)')
            snippet = msg_detail.get("snippet", '')

            email_list.append({
                "subject": subject,
                "from": sender,
                "body": snippet
            })

        return {"emails": email_list}

    except Exception as e:
        return {"error": str(e)}
