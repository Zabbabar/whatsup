# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from twilio.twiml.messaging_response import MessagingResponse
from models import Review
from database import SessionLocal
from conversation import handle_message
import os

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/webhook/whatsapp")
async def whatsapp_webhook(From: str, Body: str, db: Session = Depends(get_db)):
    contact = From
    message = Body.strip()

    response_text = handle_message(contact, message)

    # If review is complete, save to DB
    if "has been recorded" in response_text:
        state_data = conversation_states.get(contact, {}).get("data", {})
        if state_data:
            review = Review(
                contact_number=contact,
                user_name=state_data["user_name"],
                product_name=state_data["product_name"],
                product_review=state_data["product_review"]
            )
            db.add(review)
            db.commit()

    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)


@app.get("/api/reviews")
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(Review).all()
    return [
        {
            "id": r.id,
            "contact_number": r.contact_number,
            "user_name": r.user_name,
            "product_name": r.product_name,
            "product_review": r.product_review,
            "created_at": r.created_at.isoformat()
        } for r in reviews
    ]
rom fastapi.middleware.cors import CORSMiddleware; app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

