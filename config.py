import os

FLAGS = {
    "new_checkout_flow": os.getenv("FF_NEW_CHECKOUT", "false") == "true",
    "ai_recommendations": os.getenv("FF_AI_RECS", "false") == "true",
}

def flag(name: str) -> bool:
    return FLAGS.get(name, False)