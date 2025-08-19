# import httpx

# from app.routes.base_endpoint import BaseEndpoint


# class DeechoEndpoint(BaseEndpoint):
#     async def execute(self):
#         async with httpx.AsyncClient() as client:
#             if self.endpoint_data["payload_type"] == "form":
#                 resp = await client.post(url = self.url, data = self.endpoint_data["payload"], headers = self.headers)
#             else :
#                 resp = await client.post(url=self.url, json = self.endpoint_data["payload"], headers=self.headers)
                
#                 result = resp.json()
                
#                 print(f"[Deecho] {self.endpoint_key} -> {resp.status_code}")
                
#                 return result