import openai
import gradio as gr
import csv

openai.api_key = "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"  # Replace with your actual API key

def register_chat(user_input, history=[]):
    prompt = f"""You are a friendly registration assistant for a gaming tournament.
Help collect player's full name, email, and the game they want to play (e.g., Valorant, PUBG, CS:GO).
Ask one question at a time. Confirm registration when you get all info."""

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response['choices'][0]['message']['content']

    # Basic saving logic if email and game name is found
    if "@" in user_input and any(game in user_input.lower() for game in ["valorant", "csgo", "pubg", "fifa", "cod"]):
        with open("registrations.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([user_input])

    return reply

gr.Interface(
    fn=register_chat,
    inputs="text",
    outputs="text",
    title="🎮 Game Tournament Registration Bot",
    description="Ask me to register for your game!"
).launch()
