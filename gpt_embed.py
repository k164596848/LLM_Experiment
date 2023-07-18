
import openai
import pinecone
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

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
EMBEDDING_MODEL_NAME = os.getenv('EMBEDDING_MODEL_NAME')
OPENAI_CHAT_MODEL_NAME = os.getenv('OPENAI_CHAT_MODEL_NAME')

# Test the embedding model
# This is a long document we can split up.
loader = TextLoader("localdata/Paper.txt")

documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 500,
    chunk_overlap  = 100,
    length_function = len,
)

docs = text_splitter.split_documents(documents)

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV,  # next to api key in console
)

# connect to index
index = pinecone.Index(PINECONE_INDEX)
upsert_list = []

ids_count = 0
for  doc in docs:
    # use azure openai to embedding the doc(text) chunk
    res = openai.Embedding.create(
        input=doc.page_content,
        engine=EMBEDDING_MODEL_NAME
    )

    embeds = [record['embedding'] for record in res['data']]
    
    ids = ids_count
  
    # prep metadata and upsert batch
    metadata = [{'text': doc.page_content} ]
    # zip ids, embeddings, and metadata together
    to_upsert = zip(str(ids),embeds,metadata)
    # convert to list then extend to upsert_list
    upsert_list.extend(list(to_upsert))
    # increse ids_count
    ids_count += 1

# upsert to Pinecone vector store 
index.upsert(upsert_list)



    





