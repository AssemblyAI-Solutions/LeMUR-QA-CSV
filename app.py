import os
import time
from logging_config import logger
import endpoint
import assemblyai
from aiohttp import web
import json
import asyncio

# Create tunnel with ngrok
webhook_url = endpoint.start_tunnel(8080)

transcript_ids = []

# Fork process to run HTTP server and transcribe files
pid = os.fork()

if pid == 0:
    # Transcribe all files in audio folder
    def transcribe_all_files():
        time.sleep(5)
        # Open audio_url.json
        with open('audio_url.json') as json_file:
            audio_urls = json.load(json_file).get('audio')
            logger.info('Transcribing all files in audio folder: ./audio_url.json')
            for url in audio_urls:
                assemblyai.create_transcript(url, webhook_url)
    transcribe_all_files()
    
else:
    
    # HTTP server to receive update when transcript is complete
    async def webhook(request):
        body = await request.json()
        transcript_id = body.get('transcript_id')
        status = body.get('status')
        logger.info('Received webhook for transcript_id: {}'.format(transcript_id))
        if status == 'completed' and transcript_id not in transcript_ids:
            transcript_ids.append(transcript_id)
            print("Running ask_all_questions")
            task = asyncio.create_task(assemblyai.ask_all_questions(transcript_id))
            print("Done")
        print("Returning")
        return web.Response(text="Webhook received", status=200)

    app = web.Application()
    app.add_routes([web.post('/', webhook)])
    web.run_app(app)
