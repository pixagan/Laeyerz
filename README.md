# Laeyerz is an open source, self-learning, RAG framework. 
It is an attempt to make it easy for students and beginners to get started with RAG and Agentic applications.

## Getting started
Installing from git repo

You can find the source code in the [GitHub repository](https://github.com/pixagan/laeyerz).

Download the repository and install the dependencies.

```bash
git clone https://github.com/pixagan/Laeyerz.git
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
```
 document = {
        "type": "report",
        "title": "Example 1",
        "chunks": [
            {"text": "Retrieval-Augmented Generation (RAG) is an AI framework that enhances large language models (LLMs) by integrating external knowledge retrieval into the text generation process. Instead of relying solely on pre-trained model parameters, RAG fetches relevant information from databases, knowledge bases, or document repositories to provide more accurate and context-aware responses. This approach reduces hallucinations and ensures outputs are grounded in up-to-date and factual data."},
            {"text": "Different LLMs and databases play crucial roles in RAG implementations. Models like GPT-4, LLaMA, and FLAN-T5 serve as the generative component, while vector databases such as Pinecone, Chroma, FAISS, and Weaviate store and retrieve relevant documents efficiently. The choice of LLM and database depends on factors like retrieval speed, domain specificity, and cost, with some setups optimizing for accuracy while others prioritize real-time query handling."},
            {"text": "RAG is widely used in applications that require dynamic and knowledge-intensive responses. It powers AI chatbots for customer support, assists legal and healthcare professionals in retrieving case law or medical literature, and enhances search engines by generating well-formed answers from indexed documents. In software development, RAG-based coding copilots help developers by pulling relevant documentation and examples, making it a versatile tool for improving AI’s reliability across industries."}
        ]
    }
```

```python
ly.add_document(document",'report')
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
## Examples
Examples of basic use cases will be added in the examples folder. 
