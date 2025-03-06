# Laeyerz is an open source, easy to use self-learning, opinionated memory focussed, RAG framework. 
It is an attempt to make it easy for students and beginners to get started with RAG and Agentic applications.

## Getting started
Installing from git repo

You can find the source code in the [GitHub repository](https://github.com/pixagan/laeyerz).

Download the repository and install the dependencies.

```bash
git clone https://github.com/laeyerz/laeyerz.git
cd laeyerz
pip install -r requirements.txt
```

Now use pip install -e . to install the package locally.

```bash
pip install -e .
```

## Requirement
Laeyerz currently uses MongoDB for storing the session data.
The VectorDB for now supports Pinecone.
The LLM supports OpenAI.
The EmbeddingModel supports OpenAI and HuggingFace.

## To start using Laeyerz
Create an instance of Laeyerz.


```python

config = {
    "appname": "Example 1",
    "LLM": {"vendor": "OpenAI", "model": "gpt-4o"},
    "VectorDB": "Pinecone",
    "VectorDB_Params":{
        "index_name": "example2-index",
        "namespace": "example2-namespace",
        "dimension": 384,
        "metric": "cosine",
        "spec": "serverless"
    },
    "EmbeddingModel": {"vendor": "HuggingFace", "model_name": "paraphrase-MiniLM-L6-v2"},
    "NoSQL": "Mongo",
    "GraphDB": "None"
}

ly = Laeyerz(settings)
```

## Adding information to Laeyerz
Laeyers accepts information in the form of documents.

```python
ly.add_document("Example1.json",'report')
```

#Documents can be reports or conversations
As each document is added Laeyerz will store the document in its memory structure. You can directly start querying the documents.

#To ask questions create a session

```python
session = ly.create_session("Session Name")
```


## Loading an Existing Session

```python
session = ly.load_session("Session Name")
```



## Chatting with Layerz
Once the session is loaded chat with Laeyerz. It will use the memories and the LLM to respond to the query.

```python
response = curr_session.chat(

    {   
        "instructions":"Respond to the user's query based on the provided information.",
        "query":"What are the applications of RAG?"
    }
)
```

