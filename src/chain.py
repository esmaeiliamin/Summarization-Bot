import os
import time
from langchain.chains import MapReduceDocumentsChain, LLMChain, ReduceDocumentsChain, StuffDocumentsChain
from langchain.document_loaders import NewsURLLoader
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter


def summarizer(article_url):
    # Load article
    loader = NewsURLLoader([article_url])
    docs = loader.load()
    # Load LLM
    config = {'max_new_tokens': 4096, 'temperature': 0.3, 'context_length': 4096}
    llm = CTransformers(model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
                        model_file = "mistral-7b-instruct-v0.1.Q4_K_M.gguf",
                        config = config,
                        threads = os.cpu_count())
    # Map template and chain
    
