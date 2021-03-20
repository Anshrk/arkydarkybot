import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()
start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''

class AI(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def ask(self, ctx, question, chat_log=None):
        """ASK IT SHIT"""
        if chat_log == None:
            chat_log = start_chat_log
        
        prompt = f'{chat_log} Human: {question}\nAI:'
        response = completion.create(
            prompt=prompt, engine="davince", stop=['\nHuman'], temperature=0.9,
            top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
            max_tokens=150
        )
        answer=response.choice[0].text.strip()
        ctx.send(answer)

