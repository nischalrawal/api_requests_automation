import asyncio
import json

from configs.config import API_ENDPOINTS
from utils.audio_handler import AudioHandler

# from app.routes.cover import CoverEndpoint
# from app.routes.deecho import DeechoEndpoint
from app.routes.conversions.remix import RemixEndpoint
# from app.routes.conversions.music_ai import Music_AI_Endpoints


download_path = "/default/downloadAudio"

Function_Map = {
    
    "music_gpt":{
         # "cover": CoverEndpoint,
         # "deecho": DeechoEndpoint,
    },
    
    "conversions":{
          "remix": RemixEndpoint
        # "music_ai" : Music_AI_Endpoints
    }
    
   
  
}


async def run_requests(target_group = None):
    tasks = []
    s3_filepath = None

    for endpoint_key, endpoint_data in API_ENDPOINTS.items():
        if endpoint_key == download_path:
            url_payload = endpoint_data["payload"]
            url_obj = AudioHandler(download_path, url_payload)
            try:
                s3_filepath = await url_obj.download_audio()
                print(f"s3_path from main: {s3_filepath}")
            except Exception as e:
                print(f"Download failed: {e}")
            break

    if s3_filepath:
        for endpoint_key, endpoint_data in API_ENDPOINTS.items():
            #Loop all other endpoints except download path
            if endpoint_key != download_path:
                #Insert the downloaded file path in audio_path
                if "audio_path" in endpoint_data["payload"]:
                    endpoint_data["payload"]["audio_path"] = s3_filepath

                endpoint_type = endpoint_data.get("type")
                if endpoint_type :
                    group, name = endpoint_type.split(".",1)
                    
                    #If the target group does not match the group then it skipped for that iteration
                    
                    if target_group and group != target_group:
                        continue
                    
                    #Function_Map wil get the class name
                    endpoint_class = Function_Map.get(group,{}).get(name)
                    if endpoint_class:
                        obj = endpoint_class(endpoint_key, endpoint_data)
                   
                        print(obj)
                        tasks.append(obj.execute())

    print("Webhook from the config:", API_ENDPOINTS["/musicgpt/cover"]["payload"]["webhook_url"])

    if tasks:
        results = await asyncio.gather(*tasks)
        print(results)
    else:
        print("No tasks to execute.")


async def main():
    while True:
        await run_requests(target_group="conversions")
        print("Waiting for 60 seconds before the next request cycle...\n")
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
