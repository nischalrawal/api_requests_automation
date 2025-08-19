import asyncio
import json
from configs.config import API_ENDPOINTS
# from app.routes.cover import CoverEndpoint
# from app.routes.deecho import DeechoEndpoint
# from app.routes.remix import RemixEndpoint
from app.routes.music_ai import Music_AI_Endpoints
from utils.audio_handler import AudioHandler

download_path = "/default/downloadAudio"

Function_Map = {
    # "cover": CoverEndpoint,
    # "deecho": DeechoEndpoint,
    # "remix": RemixEndpoint,
    "music_ai" : Music_AI_Endpoints
}


async def run_requests():
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
                if endpoint_type in Function_Map:
                    obj = Function_Map[endpoint_type](endpoint_key, endpoint_data)
                    print(obj)
                    tasks.append(obj.execute())

    # print("Audio path from the config:", API_ENDPOINTS["/musicgpt/cover"]["payload"]["audio_path"])

    if tasks:
        results = await asyncio.gather(*tasks)
        print(results)
    else:
        print("No tasks to execute.")


async def main():
    while True:
        await run_requests()
        print("Waiting for 40 seconds before the next request cycle...\n")
        await asyncio.sleep(40)


if __name__ == "__main__":
    asyncio.run(main())
