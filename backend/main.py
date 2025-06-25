from fastapi import FastAPI
from email_fetcher import fetch_emails

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Email Sorting Bot is running."}

@app.get("/emails/")
def get_emails():
    return fetch_emails()
