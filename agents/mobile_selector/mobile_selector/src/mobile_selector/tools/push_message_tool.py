from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from typing import Type
import os
import requests
from dotenv import load_dotenv
load_dotenv(override=True)

class PushNotificationInput(BaseModel):
    """Input schema for PushNotification."""
    message: str = Field(..., description="The message content to be sent via push notification.")

class PushNotification(BaseTool):
    name: str = "Push Notification"
    description: str = "Useful for sending push notifications to the user via Pushover app."
    args_schema: Type[BaseModel] = PushNotificationInput

    def _run(self, message: str) -> str:
        # Implementation goes here
        return self.push_to_pushover(message)
    
    def push_to_pushover(self, message: str) -> str:
        pushover_user = os.getenv("PUSHOVER_USER")
        pushover_token = os.getenv("PUSHOVER_TOKEN")
        pushover_url = "https://api.pushover.net/1/messages.json"

        print(f"Push: {message}")
        payload = {"user": pushover_user, "token": pushover_token, "message": message}
        requests.post(pushover_url, data=payload)
        return '{"notification": "ok"}'
