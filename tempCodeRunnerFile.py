
import asyncio
import json

from configs.config import API_ENDPOINTS
# from app.routes.cover import CoverEndpoint
# from app.routes.deecho import DeechoEndpoint
from app.routes.conversions.remix import RemixEndpoint
from utils.audio_handler import AudioHandler


download_path = "/default/downloadAudio"

Function_Map = {
    
    # "cover" : CoverEndpoint,
    # "deecho" : DeechoEndpoint
    "remix" : RemixEndpoint
    
}

async def main():
    tasks = []
    s3_filepath = None
    
    
    
    for endpoint_key, endpoint_data in API_ENDPOINTS.items():
        
        #audio download logic
        if endpoint_key == download_path:
            url_payload = endpoint_data["payload"]
            url_obj = AudioHandler(download_path,url_payload)
            try:
                
             s3_filepath = await url_obj.download_audio()
             print(f"s3_path from main: {s3_filepath}")
            
            except Exception as e: 
                
             print(f"Download failed {e}")
            
            break
            
    if s3_filepath:
        
        for endpoint_key, endpoint_data in API_ENDPOINTS.items():
            
            if endpoint_key!= download_path:
                if "audio_path" in endpoint_data["payload"]:
                    endpoint_data["payload"]["audio_path"] = s3_filepath
                    # print(endpoint_data["payload"]["audio_path"])
        

             
              
     ### Filter the type in config.py and check if available in Function_Map and if available then the related type class will be called from app/routes       
            endpoint_type = endpoint_data.get("type")
            if endpoint_type in Function_Map:
                obj = Function_Map[endpoint_type](endpoint_key, endpoint_data)
                # print(endpoint_data['payload'])
                
                print(obj)
                tasks.append(obj.execute())
        
    print("Audio path from the config", API_ENDPOINTS["/musicgpt/cover"]["payload"]["audio_path"]) #Check if audio has been sucessfully inserted in audio_path in config.py
    
    results = await asyncio.gather(*tasks)    
    print(results)


if __name__ == "__main__":
    asyncio.run(main())