# Created: Anil Variyar
# Text Splitter

import re
from typing import List



class TextSplitter:

    def __init__(self):
        print("Splitting the Text for Vectorization")
        self.chunk_size = 200 #no of tokens
        self.token_overlap = 50
        self.separators = ["\n\n", "\n", ". ", " ", ""]



    def run(self, text):
        print("Split")

        sentences = self.into_sentences(text)
        chunks = self.into_chunks(sentences)

        return chunks


    def into_sentences(self, text):


        pattern = r'(?<=[.!?])(?=\s+[A-Z]|\s*$)'
        sentences = re.split(pattern, text)
    

        # Clean up sentences by removing extra whitespace
        sentences = [sentence.strip() for sentence in sentences]

        sentences = [' '.join(sentence.split()) for sentence in sentences]

        return sentences


    def into_chunks(self, sentences):
        # First split into sentences
        chunks = []
        current_chunk = []
        current_size = 0
        
        for sentence in sentences:
            # Count words in the sentence
            sentence_size = len(sentence.split())
            
            
            if current_size + sentence_size > self.chunk_size and current_chunk:
                # Join the current chunk sentences
                chunks.append(" ".join(current_chunk))
                
                
                overlap_size = 0
                overlap_sentences = []
                
                for prev_sentence in reversed(current_chunk):
                    sentence_words = len(prev_sentence.split())
                    if overlap_size + sentence_words <= self.token_overlap:
                        overlap_sentences.insert(0, prev_sentence)
                        overlap_size += sentence_words
                    else:
                        break
                
                current_chunk = overlap_sentences
                current_size = overlap_size
            
            # Add the current sentence to the chunk
            current_chunk.append(sentence)
            current_size += sentence_size
        
        # Add the last chunk if it's not empty
        if current_chunk:
            chunks.append(" ".join(current_chunk))
            
        return chunks