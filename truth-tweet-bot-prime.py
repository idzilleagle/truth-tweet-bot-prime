import tweepy
import random
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

URL = "https://legalnamefraud.carrd.co"
BASE_HASHTAGS = "#BCCRSS #legalnamefraud #truthbillboards #crssnow #judgebows"

OPENERS = [
    "The truth is simple:", "Quick reminder:", "They don't want you to know this:",
    "Did you know?", "Here's a thought for your day:", "Unplug from the matrix:",
    "Consider this:", "The system is based on this deception:", "Fact check this:",
    "It's hidden in plain sight:", "Time to wake up.", "Here is a foundational truth:",
]
CORE_STATEMENTS = [
    "It's illegal to use a legal name.", "The legal name is crown copyright property.",
    "Using a legal name is participating in fraud.", "You are not a legal name.",
    "A birth certificate creates a dead corporate fiction in your name.",
    "The legal name is the mark of the beast.", "Slavery by consent is still slavery.",
    "The legal system is a commercial system based on contracts and control.",
    "The legal name ties you to a system designed to exploit you.",
]
CALLS_TO_ACTION = [
    "Read the #BCCRSS to understand.", "Share this with everyone.",
    "Learn the facts, break the spell.", "Read and share the #BCCRSS.",
    "Remove your consent by understanding the fraud.", "The truth will set you free.",
    "Go to the website and learn more.", "Spread the word.",
]

def generate_tweet_text():
    while True:
        opener, statement, cta = random.choice(OPENERS), random.choice(CORE_STATEMENTS), random.choice(CALLS_TO_ACTION)
        formats = [f"{opener} {statement} {cta}", f"{statement} {cta}", f"{opener} {statement}", f"{cta} {statement}"]
        message = random.choice(formats)
        full_tweet = f"{message} {URL} {BASE_HASHTAGS}".strip()
        if len(full_tweet) <= 280:
            return full_tweet

def post_tweet():
    if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        print("❌ ERROR: Missing Twitter credentials in your .env file. Please check it.")
        return
    try:
        print("Authenticating with Twitter network...")
        client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
        print("Authentication successful.")
        tweet_text = generate_tweet_text()
        print(f"\nBroadcasting this transmission:\n---\n{tweet_text}\n---")
        response = client.create_tweet(text=tweet_text)
        print(f"✅ Transmission successful. Signal ID: {response.data['id']}")
    except Exception as e:
        print(f"❌ An error occurred during transmission: {e}")

if __name__ == "__main__":
    post_tweet()