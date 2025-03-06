# Created: Anil Variyar
# Quickstart Dataloader

from laeyerz.Laeyerz import Laeyerz

import os
from dotenv import load_dotenv
load_dotenv()


#laeyers
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

#Setup a Laeyerz Instance
ly = Laeyerz(config)


 document = {
        "type": "report",
        "title": "Example 1",
        "chunks": [
            {"text": "Retrieval-Augmented Generation (RAG) is an AI framework that enhances large language models (LLMs) by integrating external knowledge retrieval into the text generation process. Instead of relying solely on pre-trained model parameters, RAG fetches relevant information from databases, knowledge bases, or document repositories to provide more accurate and context-aware responses. This approach reduces hallucinations and ensures outputs are grounded in up-to-date and factual data."},
            {"text": "Different LLMs and databases play crucial roles in RAG implementations. Models like GPT-4, LLaMA, and FLAN-T5 serve as the generative component, while vector databases such as Pinecone, Chroma, FAISS, and Weaviate store and retrieve relevant documents efficiently. The choice of LLM and database depends on factors like retrieval speed, domain specificity, and cost, with some setups optimizing for accuracy while others prioritize real-time query handling."},
            {"text": "RAG is widely used in applications that require dynamic and knowledge-intensive responses. It powers AI chatbots for customer support, assists legal and healthcare professionals in retrieving case law or medical literature, and enhances search engines by generating well-formed answers from indexed documents. In software development, RAG-based coding copilots help developers by pulling relevant documentation and examples, making it a versatile tool for improving AI’s reliability across industries."}
        ]
    }


#adding documents to Laeyerz
ly.add_document(document,'report')
