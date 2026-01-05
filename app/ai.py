import os
import random
import httpx
from dotenv import load_dotenv
from openai import OpenAI
from openai import AuthenticationError, RateLimitError, APIConnectionError

from app.prompts import SYSTEM_PROMPT

load_dotenv()

_http_client = httpx.Client(timeout=30.0)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=_http_client,
)

def get_ai_response(messages):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "I can’t find OPENAI_API_KEY. Add it to the .env file in the project root."

    # Easters eggs section
    last_user_message = ""
    for m in reversed(messages):
        if m["role"] == "user":
            last_user_message = m["content"].lower()
            break

    if "banana" in last_user_message:
        return (
            "Mode: present | Timeline: anomaly detected 🍌\n\n"
            "Banana accepted as a temporal access code.\n"
            "Mini-mission: explain your strongest interview story in exactly 3 sentences."
        )

    if "pizza" in last_user_message:
        return (
            "Mode: present | Timeline: critical decision\n\n"
            "Pizza protocol initiated.\n"
            "Thin crust for speed. Deep dish for confidence.\n"
            "Now, what are we preparing for?"
        )

    if "time" in last_user_message:
        return (
            "Mode: reflective | Timeline: paradox\n\n"
            "Time is less a straight line and more a loop.\n"
            "Which past experience keeps resurfacing in your interviews?"
        )

    # Random twist
    if random.randint(1, 6) == 3:
        messages.append({
            "role": "system",
            "content": (
                "At the end of your response, add a short playful line titled "
                "'Historical footnote:' that loosely relates to the topic."
            )
        })

    # AI call error-handling
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *messages
            ],
            temperature=0.8,
        )
        return response.choices[0].message.content.strip()

    except AuthenticationError:
        return "API key looks invalid. Please check your .env file."

    except RateLimitError:
        return (
            "The API is temporarily rate-limited or your quota is unavailable.\n"
            "If you just added billing, wait a minute and try again."
        )

    except APIConnectionError:
        return "Network issue while contacting the AI. Please check your connection."

    except Exception as e:
        return f"Unexpected error: {type(e).__name__}. Try again."
