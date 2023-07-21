import os
import requests
import json
from logging_config import logger
from questions import questions
import pandas as pd

columns = ['transcript_id']
df = pd.DataFrame(columns=columns)

ASSEMBLYAI_API_TOKEN = os.environ.get('ASSEMBLYAI_API_TOKEN')

if not ASSEMBLYAI_API_TOKEN:
    raise Exception("Please set the ASSEMBLYAI_API_TOKEN environment variable")

def create_transcript(url, webhook_url):
    logger.info('Creating transcript for: {}'.format(url))
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": url,
        "webhook_url": webhook_url
    }
    headers = {
        "authorization": ASSEMBLYAI_API_TOKEN,
    }
    response = requests.post(endpoint, json=json, headers=headers)
    return response.json()



def get_transcript(id):
    logger.info('Getting transcript for: {}'.format(id))
    endpoint = "https://api.assemblyai.com/v2/transcript/{}".format(id)
    headers = {'authorization': ASSEMBLYAI_API_TOKEN}
    response = requests.get(endpoint, headers=headers)
    return response.json()
    


def ask_question(transcript_id, questions):
    url = "https://api.assemblyai.com/v2/generate/question-answer"
    payload = json.dumps({
        "transcript_ids": [
        transcript_id
    ],
        "questions": questions
    })
    headers = {
        'Authorization': ASSEMBLYAI_API_TOKEN,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def split_into_chunks(array, chunk_size):
    chunks = []
    chunk = []
    for index, i in enumerate(array):
      if index % chunk_size == 0 and index:
        chunk.append(i)
        chunks.append(chunk)
        chunk = []
      else:
        chunk.append(i)

    return chunks

async def ask_all_questions(transcript_id):
    global df
    question_no = 1
    chunks = split_into_chunks(questions, 3)
    answers = {'transcript_id': transcript_id}
    for chunk_index, c in enumerate(chunks):
        # Ask the set of questions
        results = ask_question(transcript_id, c).get("response")
        indexs = ["transcript_id"]
        for index, result in enumerate(results):
            answers['question_' + str(question_no)] = result.get("answer")
            indexs.append('question_' + str(question_no))
            print(transcript_id, 'question_' + str(question_no),result.get("answer"))
            question_no+= 1
   
    new_row = pd.DataFrame([answers])
    # Reset the index of the df DataFrame
    df.reset_index(drop=True, inplace=True)
    df = pd.concat([df,new_row], ignore_index=True)
    # df.rename(columns={}, inplace=True)
    df.to_csv('output.csv', index=False)

