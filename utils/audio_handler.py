import os
import json

import httpx
from dotenv import load_dotenv

from app.routes.base_endpoint import BaseEndpoint
from configs.config import API_ENDPOINTS, Handler_Data

load_dotenv()
# endpoint_path = "/musicgpt/download"
# short_audio = Handler_Data["short_audio"]

    
class AudioHandler(BaseEndpoint):
    async def download_audio(self):
        
        
        params = self.endpoint_data
        
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
            resp = await client.get(self.url , params=params ,headers =self.headers)
            print(f"Response: {resp.status_code}")
            
            if resp.status_code !=200:
                raise Exception(f"Download Failed from audio handler: {resp.text}")

            
            # print(f"[Download] {self.endpoint_key} -> {resp.status_code}")
            
            
            data =  resp.json()
            print(data)
            return data["audio_path"]

        
              
            
     
        
        