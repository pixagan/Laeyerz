from laeyerz.flow.Flow import Flow
from laeyerz.flow.Node import Node
from laeyerz.flow.Edge import Edge
from laeyerz.flow.Model import Model

#importing the models
from laeyerz.utils.KeyManager import KeyManager

from laeyerz.embeddings.Embedding import Embedding
from laeyerz.memory.VectorStore import VectorStore


def fileloader(app_state):
    print("File Loader")



def text_splitter(app_state):
    print("Text Splitter")



def embedding(app_state):
    print("Embedding")



def vector_db(app_state):
    print("Vector DB")


#Flow
store_flow = Flow()

#------------Nodes
    
store_flow.add_node("FileLoader", fileloader)
store_flow.add_node("TextSplitter", text_splitter)
store_flow.add_node("Embedding", embedding)
store_flow.add_node("VectorDB", vector_db)


#------------Edges
store_flow.add_edge("FileLoader", "TextSplitter")
store_flow.add_edge("TextSplitter", "Embedding")
store_flow.add_edge("Embedding", "VectorDB")    


#Finalize/Freeze your Flow before evaluation
store_flow.finalize()


#based on the input node  
input_data = {   
        "filepath":"/Users/anilvariyar/Desktop/test.pdf"
    }


output = store_flow.evaluate(input_data)
print("FileSplitter : ",output)





