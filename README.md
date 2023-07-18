# LLM_Experiment
this repo is for Trend ai contest Azure open ai contest api key experiment.


## Table of Contents

- [Installation](#installation)
- [Credential](#credential)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

Instructions on how to install the project. You can include any prerequisites or dependencies needed.

```shell
$ pip install pipenv
``` 
Activate the virtual env for your python, then install the packages 

```shell
pipenv shell 

pip install -r requirements.txt
```

## Credential
Create your own `.env` file with those information below:
```shell 
API_TYPE = "azure"
API_VERSOIN = "2023-05-15"

AZURE_OPENAI_KEY = ""
AZURE_OPENAI_ENDPOINT ="" 

# depolment name
EMBEDDING_MODEL_NAME = 'text-embedding-ada-002_team902'
OPENAI_CHAT_MODEL_NAME =' gpt-35-turbo_team902'

PINECONE_API_KEY=""
PINECONE_ENV=""
PINECONE_INDEX=""
```

## Usage
1. extract your data( here I use a paper.pdf from 2022 as demo) to txt file. You can get the result by execute the cmd :
```shell 
python pdf2txt.py
```
2. Create your [Pinecron](https://www.pinecron.com) (Vecotor Store), it's free! and you can get your `PINECONE_API_KEY`, `PINECONE_ENV`, `PINECONE_INDEX` in the pinecron dashboard.
After that, we can execute the embedding txt chunks and upsert it to the Pinecron Vector store. 

- Sign up pinecorn, then cilick Indexes, you can see `+Create Index`.

- Enter name you want to have and that would be your `PINECONE_INDEX`.

- Dimensions is `1536` , it's openai embedding dimensions (Very important！)

```shell 
python gpt_embed.py
```
3. Get the azure opne ai key 

`AZURE_OPENAI_KEY`= {{Key1}} or {{Key2}}

`AZURE_OPENAI_ENDPOINT` "https://{{Resource Group}}.openai.azure.com/" from [ai contest](https://2023aicontest.trendmicro.com/Competitions/Details/3)

```shell 
python gpt_chat.py
```
you can modify the query that you want to ask about your own data. 

