from docx import Document

class DocLoad:

    def __init__(self):
        print("Loading Doc")

    def load_doc(self, filename):
        print("Loading Doc")

        """
        Load and read a DOCX file
        Args:
            file_path (str): Path to the DOCX file
        Returns:
            str: Text content of the document
        """
        try:

            doc = Document(file_path)
            full_text = []
            
            # Extract text from paragraphs
            for para in doc.paragraphs:
                if para.text.strip():  # Only add non-empty paragraphs
                    full_text.append(para.text)
                    
            return '\n'.join(full_text)
            
        except ImportError:
            print("Please install python-docx: pip install python-docx")
            return None
        except Exception as e:
            print(f"Error loading document: {str(e)}")
            return None





