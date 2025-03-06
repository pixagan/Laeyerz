from setuptools import setup, find_packages

setup(
    name="laeyerz",  # Replace with your package name
    version="0.1.0",    # Initial version
    author="Anil Variyar",
    author_email="pixagan@gmail.com",
    description="An Attempt to create a Simplified easy to use RAG  Library for students and Beginners",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pixagan/Laeyerz",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        "numpy", 
        "pandas",
        "pinecone",
        "chromadb",
        "sentence_transformers",
        "openai",
        "pinecone",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
)
