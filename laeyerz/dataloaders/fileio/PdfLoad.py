# Created: Anil Variyar
# PDF Loader

from pypdf import PdfReader
import pdfplumber
import pymupdf # imports the pymupdf library
import os




class PdfLoad:

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

     