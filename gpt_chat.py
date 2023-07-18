
import openai
import os
from pine_context import pine_query_context

from dotenv import load_dotenv
# Load the environment variables from the .env file
load_dotenv()  

openai.api_type = os.getenv('API_TYPE')
openai.api_base = os.getenv('AZURE_OPENAI_ENDPOINT')
openai.api_version = os.getenv('API_VERSOIN')
openai.api_key = os.getenv('AZURE_OPENAI_KEY')
# reference: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart


# pinecone keys 
PINECONE_API_KEY=os.getenv('PINECONE_API_KEY')
PINECONE_ENV= os.getenv('PINECONE_ENV')
PINECONE_INDEX= os.getenv('PINECONE_INDEX')


# depolment name
OPENAI_CHAT_MODEL_NAME = os.getenv('OPENAI_CHAT_MODEL_NAME')


role_setting = "Assistant is an intelligent chatbot designed to help users answer technical questions. Only answer questions using the context below and if you're not sure of an answer, you can say 'I don't know'."

# you can change the query here
user_query ="what is the second auther of the paper?"

context_find_from_pinecron = pine_query_context(query=user_query)


response = openai.ChatCompletion.create(
    engine=OPENAI_CHAT_MODEL_NAME, # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
    messages=[
        {"role": "system", 
         "content": f"""{role_setting}
            Context:{context_find_from_pinecron}
         """
        },
        {"role": "user", "content": user_query}
    ]
)

print(response['choices'][0]['message']['content'])


