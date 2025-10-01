from setuptools import setup, find_packages

setup(
    name="laeyerz",
    version="0.2.0", 
    author="Anil Variyar",
    author_email="pixagan@gmail.com",
    description="Building Graph based AI Agentic Workflows",
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
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
)
