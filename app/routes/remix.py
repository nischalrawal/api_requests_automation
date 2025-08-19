import httpx

from app.routes.base_endpoint import BaseEndpoint



### This class will be called in main and send the respons where the object will be called    


class RemixEndpoint(BaseEndpoint):
    async def execute(self):
        print("Request send to remix")
        async with httpx.AsyncClient() as client:
            if self.endpoint_data["payload_type"] == "form":
                
                resp = await client.post(self.url, data = self.endpoint_data["payload"], headers=self.headers)
            else :
                resp = await client.post(self.url, json = self.endpoint_data["payload"], headers = self.headers)
                
        print(f"[Remix] {self.endpoint_key} -> {resp.status_code}")
        
        return resp.json()