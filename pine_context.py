
import openai
import pinecone
import os
import time


from dotenv import load_dotenv
# Load the environment variables from the .env file
load_dotenv()  


# reference: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart

AZURE_OPENAI_ENDPOINT = "https://66E5F16B-0EA3-4D34-8FDD-F045F22EEC8E-eastus-team902.openai.azure.com/"
AZURE_OPENAI_KEY = "0a095db7d7704856bb81d83ee322d81a"
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2023-05-15"
openai.api_key = AZURE_OPENAI_KEY


# pinecone keys 
PINECONE_API_KEY=os.getenv('PINECONE_API_KEY')
PINECONE_ENV= os.getenv('PINECONE_ENV')
PINECONE_INDEX= os.getenv('PINECONE_INDEX')


# depolment name
embedding_model_name = os.getenv('EMBEDDING_MODEL_NAME')
chat_model_name = os.getenv('OPENAI_CHAT_MODEL_NAME')

def pine_query_context(query: str = "what is the first authors name?"):
    """
    This function is used to query the context of the question
    args:{
        query: the question you want to ask
        }
    return:{
        result: the context of the question
        }
    """
    # initialize pinecone
    pinecone.init(
        api_key=PINECONE_API_KEY,  # find at app.pinecone.io
        environment=PINECONE_ENV,  # next to api key in console
    )

    # connect to index
    index = pinecone.Index(PINECONE_INDEX)

    # inputs your question
    query= "what is the first authors name?"

    # calulate the embedding of the query 
    res = openai.Embedding.create(
        input=query,
        engine=embedding_model_name
    )

    # get the embedding of the query
    embed_query = [record['embedding'] for record in res['data']]

    # send the query to pinecone 
    result = index.query(
        vector=embed_query,
        # the top score of result should be return
        top_k=1,
        #   include_values=True,
        include_metadata=True
    )

    return result['matches'][0]['metadata']['text']

 





    





