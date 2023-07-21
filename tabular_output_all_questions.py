import assemblyai as aai
import pandas as pd
# Set API Key
aai.settings.api_key = "262d4d69ccb24d33ad66fcd6fe320e66"


# Define our questions
questions = [
      aai.LemurQuestion(question="What is the Townsquare Interactive On Boarding Specialist name?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive.",
                        answer_format="<name>"),
      aai.LemurQuestion(question="What is the Company Name? - Besides townsquare interactive or town square",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding.",
                        answer_format="<company name>"),
      aai.LemurQuestion(question="Does this package contain any of the following features / options? F - Social Ads, T - Retargeting, E - Ecommerce, V - Townsquare App",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_format="<features / options>"),
      aai.LemurQuestion(question="What is the Primary Business Email, Is this email used in Forms?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_format="<email>"),
      aai.LemurQuestion(question="What is the Primary Business Phone?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_format="<phone number>"),
      aai.LemurQuestion(question="What is the Full Business Address?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options=["<Address>", "N/A"]),
      aai.LemurQuestion(question="Would they like to hide the Primary Address?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options = ["Yes", "No"]),
      aai.LemurQuestion(question="Does the client need additional locations listed?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options = ["Yes", "No"]),
      aai.LemurQuestion(question="Do you need to provide additional contact details?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options = ["Yes", "No"]),
      aai.LemurQuestion(question="What are the Hours of Operation? (list by day)",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_format= "<Day>\n<Hours>"),
      aai.LemurQuestion(question="What are the clients Top Services?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_format= "<Services>"),
      aai.LemurQuestion(question="Does the client have an existing website?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options = ["Yes", "No"]),
      aai.LemurQuestion(question="What is the status of the logo?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options = ["Logo Attatched", "Sending Later", "Create Logo"]),
      aai.LemurQuestion(question="What is the client views on Stock Photos",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options = ["YES - USE ONLY STOCK PHOTOS", "YES - USE STOCK PHOTOS AND CLIENT PHOTOS", "NO - USE ONLY CLIENT PHOTOS"]),
      aai.LemurQuestion(question="Does the client have any preference of overall design prefences or an Example Site URL.",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options= ["<URL>", "N/A"]),
      aai.LemurQuestion(question="Does the client have any Client Particulars/Design Preferences?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_format= "<Preferences>"),
      aai.LemurQuestion(question="Are additional design notes required?",
                        context="This is a transcript from an onboarding call for the company Townsquare Interactive. The beginning of every single one of these calls should be a 3-party (Sales-Onboarding-Agent) interaction to hand off the customer smoothly into their onboarding. The answer is likely a combination of options.",
                        answer_options = ["Yes", "No"])
  ]

"""#### Add you Audio URL's
Make sure these links are publicly acessible!
"""

audio_urls = ['https://admin5.ringio.com/launcher-app/af/Jo0nio', 'http://admin5.ringio.com/af/f730wj']

"""#### Setup API Key and Imports"""



"""###### This is a work-around solution we are using due to the limitations of LeMUR EA"""

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
chunks = split_into_chunks(questions, 4)

"""#### Transcribe Audio: We want to only transcribe the audio once as we experiment with LeMUR"""

# First step is to loop over each transcript, we want to ask these questions per transcript as opposed to over a set of transcripts.
transcripts = []
for url in audio_urls:
    transcriber = aai.Transcriber()
    # Creating a transcript object will automatically transcribe and wait for the process to complete.
    transcript = transcriber.transcribe(url, config={"webhook_url": ""})
    transcripts.append(transcript)

"""#### Setup Dataframe: Each row is indexed by a unique transcript_id"""

columns = ['transcript_id']
# for index,i in enumerate(questions):
#     columns.append('question_' + str(index + 1))
df = pd.DataFrame(columns=columns)

df.head()

"""#### For each transcript we should create a row with the transcript_id"""

for transcript in transcripts:
  if transcript.id not in df['transcript_id'].values:
      new_row = {'transcript_id': transcript.id}
      df = df.append(new_row, ignore_index=True)

df.head()

"""#### Now we loop through the transcripts and ask the questions outlined above"""

for transcript in transcripts:
  if transcript.id not in df['transcript_id'].values:
      new_row = {'transcript_id': transcript.id}
      df = df.append(new_row, ignore_index=True)
  # Generate question chunks
  chunks = split_into_chunks(questions, 3)
  question_no = 1
  for chunk_index, c in enumerate(chunks):
    # Ask the set of questions
    results = transcript.lemur.question(c)
    for index, result in enumerate(results):
        df.loc[df['transcript_id'] == transcript.id, 'question_' + str(question_no)] = str(result.answer)
        print(transcript.id, 'question_' + str(question_no),result.answer)
        question_no+= 1
df.rename(columns={'question_1':'OBS Name', 'question_2':'Company Name', 'question_3':'Package Feature Options',
                'question_4':'Email', 'question_5':'Phone', 'question_6':'Address',
                  'question_7':'Hide Address', 'question_8':'Additional Locations', 'question_9':'Additional Contact Details',
                  'question_10':'Hours of Operation', 'question_11':'Top Services', 'question_12':'Existing Website',
                  'question_13':'Logo Status', 'question_14':'Views on Stock Photos', 'question_15':'Overall Design Preferences / Example Website',
                  'question_16':'Particulars / Specific Design Preferences', 'question_17':'Additional Design Notes Required'
                }, inplace=True)

"""#### Read Results"""

df.head()