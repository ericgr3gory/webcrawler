from openai import OpenAI
import shelve
from dotenv import load_dotenv
import os
import time

load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
ASSITANT_ID = os.getenv("ASSITANT_ID")
client = OpenAI(api_key=OPEN_AI_API_KEY)


# --------------------------------------------------------------
# Upload file
# --------------------------------------------------------------
def upload_file(path):
    files = ['wallet-cli']
    # Upload a file with an "assistants" purpose
    for file in files:
        client.files.create(file=open(f'{path}{file}', "rb"), purpose="assistants")
        print(f'{path}{file}')
        time.sleep(3)
    return files

def delete_files():
    file_list = client.files.list()
    
    for file in file_list:
        print(file.id)
        client.files.delete(file.id)
        time.sleep(2)
    
def retrieve_files():
    file_list = client.files.list()
    file_ids =[]
    for file in file_list:
        file_ids.append(file.id)
    
    return file_ids
     
#file = upload_file("chia-docs/")



# --------------------------------------------------------------
# Create assistant
# --------------------------------------------------------------
def create_assistant(file):
    """
    You currently cannot set the temperature for Assistant via the API.
    """
    assistant = client.beta.assistants.create(
        name="chia blockchain assitant",
        instructions="You're a helpful chia blockchain assistant that can provide useful information. Use your knowledge base to best respond to queries. If you don't know the answer, say simply that you cannot help with question and advise user to visit chia.net Be friendly and funny.",
        tools=[{"type": "retrieval"}],
        model="gpt-4-1106-preview",
        file_ids=file,
    )
    return assistant
