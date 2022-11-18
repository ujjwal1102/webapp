# from channels.consumer import SyncConsumer,AsyncConsumer
# from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer,JsonWebsocketConsumer,AsyncWebsocketConsumer
import time,openai
from . import bot

# import asyncio
# from asgiref.sync import async_to_sync
import json
# from chatbot_application import chatbot as bot
# count = 0
class MyWebsocketConsumer(AsyncWebsocketConsumer):
    count = 0
    
    async def connect(self):
        print("Websocket Connected...")
        await self.accept()
        openai.api_key = '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'
        
    
    async def receive(self, text_data):
        print("Client Says :- ",text_data)
        # prepro1 = text_data
        # if prepro1 != "q":
        #     reply = bot.insideloop(prepro1)
        #     print(reply,self.count)
        # que = ''
        response = openai.Completion().create(
            prompt=text_data, 
            engine="text-davinci-002", 
            temperature=0,
            top_p=1, 
            # frequency_penalty=0, 
            # presence_penalty=0.4, 
        
            max_tokens=30)
             
        ans = response.choices[0].text
        current_time = time.strftime("%H:%M:%S",time.localtime())
        await self.send(text_data=json.dumps({"message": ans,
            "count":self.count,"current_time": current_time[:5]}))
            
        self.count = self.count+1
            

    async def disconnect(self, close_code):
        print("Websocket Disconnected...",close_code)
        
        
        

    