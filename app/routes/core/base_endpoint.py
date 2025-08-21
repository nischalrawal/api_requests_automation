import os
import httpx

from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN=os.getenv("BEARER")
BASE_URL=os.getenv("BASE_URL")

# This is a base class and will be inherited to the features class like remix, deecho etc
class BaseEndpoint:
    def __init__(self,endpoint_key,endpoint_data):
        self.endpoint_key = endpoint_key
        self.endpoint_data = endpoint_data
        self.url = f"{BASE_URL}{endpoint_key}"
        self.headers={
            "Authorization" : f"Bearer {BEARER_TOKEN}"
        }
    print("Base class ran")

    # Not used right now
    async def send_request(self):
        async with httpx.AsyncClient(timeout=httpx.Timeout(60.0)) as client:
            if self.endpoint_data["payload_type"] == "json":
                resp = await client.post(self.url, json = self.endpoint_data, headers=self.headers)
        
            else:
                print("super coming")
                resp = await client.post(self.url, data = self.endpoint_data, headers = self.headers)
                print(resp)
    pass