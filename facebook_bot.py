import requests
import time
import os

ACCESS_TOKEN = os.getenv("EAA4SghyFqQABO8WEY9mddtV1tt4qoWRZAYcqNERXEh6WtZCYxowHlTSX5cA8AQYwMdiAsy0YdkRjAiAB0plUaiZAi0A5ETMOFZBRHYxKytdmHUySgk9IdqhSb5ZAGQTR7jyzYTZCJiVvQKNSsZBA1dlJUCSpNmexZCtYRbEEUcq2ZA6ZBCKVNmgplZAQ8ZCkbFJVGNEDGLBKqAHlVh9rCg1ozgZDZD")
PAGE_ID = os.getenv("330385883501389")

def post_to_facebook():
    url = f"https://graph.facebook.com/330385883501389/feed"
    params = {
        "message": "منشور تلقائي عبر البوت!",
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, params=params)
    return response.json()

# نشر منشور جديد كل ساعة
if __name__ == "__main__":
    while True:
        print("⏳ يتم نشر منشور جديد على فيسبوك...")
        post_to_facebook()
        time.sleep(3600)
