import json
import os
import uuid

from dotenv import load_dotenv

load_dotenv()

# WEB_HOOK="e4e8313c6c0c"
WEB_HOOK=os.getenv("WEBHOOK_ID")

# Generate a uuid 
uuid1 = str(uuid.uuid4())
uuid2 = str(uuid.uuid4())



# with open("/home/nischal/automation/audio_path.txt", "r") as f:
#     youtube_url = f.readline().strip()

#     if "file" in youtube_url:
#         print("URL Found")
#     else:
#         print("URL Not Found")

#     print("YouTube URL:", youtube_url)


Handler_Data={
        "short_audio" : "https://youtu.be/u6lihZAcy4s?si=DXxlMEdwGgtYnhh5",
        "Long_audio" :  "https://youtu.be/tAGnKpE4NCI?si=Or1R9BB-vSkqdFoi"

}
    
   

# API payload
API_ENDPOINTS={
    "/musicgpt/cover":{
        "type" : "muscigpt.cover",
        "payload_type" : "form",
        "payload" : {
            "audio_path": "",
            "voice_id" : "TaylorSwift",
            "conversion_id": "dbdb8ba3-9fc9-4361-bb0a-29791c816275",
            "audio_duration": 70,
            "webhook_url" : f"https://{WEB_HOOK}.ngrok-free.app/nis_hook"
         
        }
    },
    
    "/musicgpt/deecho":{
        "type":"musicgpt.deecho",
        "payload_type" : "json",
        "payload" : {
            "audio_path" : "",
            "conversion_id" : "" ,
            "audio_duration" : 176,
            # "webhook_url" : f"https://{WEB_HOOk}.ngrok-free.app/deecho"
            "webhook_url" : "https://nischaltest.requestcatcher.com/"
        }
    },
    
    "/conversions/Remix":{
         "type":"conversions.remix",
        "payload_type" : "form",
        "payload" : {
            "audio_path" : "",
            "prompt" : "Remix in pop and metal style",
            "conversion_id_1" : uuid1,
            "conversion_id_2" : uuid2,
            
            "audio_duration" : 222,
            # "webhook_url" : f"https://{WEB_HOOk}.ngrok-free.app/deecho"
            "webhook_url" :  f"https://{WEB_HOOK}.ngrok-free.app/remix"
        }
    },
    
    "/default/downloadAudio":{
        "payload":{
            "url" : Handler_Data["short_audio"],
            "webhook": f"https://{WEB_HOOK}.ngrok-free.app/nis_test"
        }
    }
    
}



# Youtube url data

