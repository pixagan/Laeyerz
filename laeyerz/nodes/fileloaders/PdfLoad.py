# Copyright 2025 Pixagan Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
PdfLoad module for PDF document loading
in the Laeyerz framework.
"""

from pypdf import PdfReader
import pdfplumber
import pymupdf # imports the pymupdf library
import os

from laeyerz.flow.Node import Node

class PyPdfConnector:
    
    def __init__(self):
        self.reader = PdfReader()

    def load_pdf(self, filename):
        return self.reader.read(filename)




class PyMuPdfConnector(Node):

    def __init__(self):
        print("Loading Pdf")


    def run(self, filename):

        #text = self.extract_text_pypdf(filename)
        text = self.extract_text_pymypdf(filename)
        paragraphs = self.split_into_paragraphs(text)

        return text, paragraphs


    def split_into_paragraphs(self, text):
        # Split text into paragraphs using double newlines as separator
        # Filter out empty strings and strip whitespace
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        return paragraphs


    def extract_clean_text_pymupdf(self, pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text")  # Extract text properly
        return "\n".join(line.strip() for line in text.split("\n") if line.strip())



    # Extract text using PyPDF
    def extract_text_pypdf(self, file_path):

        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

        return text

     

    # Extract images using pdfplumber
    def extract_images_pdfplumber(self, file_path, output_folder="extracted_images"):
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                images = page.images
                if images:
                    os.makedirs(output_folder, exist_ok=True)
                    for j, img in enumerate(images):
                        img_data = page.images[j]["stream"].get_data()
                        img_path = os.path.join(output_folder, f"page_{i+1}_image_{j+1}.jpg")
                        with open(img_path, "wb") as f:
                            f.write(img_data)
        print(f"Images saved to folder: {output_folder}")


    

    # Extract tables using pdfplumber
    def extract_tables_pdfplumber(self, file_path):
        with pdfplumber.open(file_path) as pdf:
            tables = []
            for i, page in enumerate(pdf.pages):
                page_tables = page.extract_tables()
                for table in page_tables:
                    tables.append(table)
            return tables




#----------------------------------------------------------------------



def main():

    filename = 'Swiggy_Sample.pdf'
    pdf1 = PdfLoad()
    text, paragraphs = pdf1.run(filename)

    print("nParagraphs : ", len(paragraphs))
    



#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

     