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
    map_template = """<s>[INST] The following is a part of an article from
    a website :
    {docs}
    Based on this, please identify the main theme and key points of it
    Answer: [/INST]</s>"""
    map_prompt = PromptTemplate.form_template(map_template)
    map_chain = LLMChain(llm=llm, prompt=map_prompt)
    # Reduce template and chain
    reduce_template = """<s>[INST] The following is set of summaries from
    the article:
    {doc_summaries}
    Take these as a input and condense it into a final, consolidated summary
    of all the main points.
    Construct it as a well organized summary of the main points and it hould
    be between 2 and 6 paragraphs.
    Answer: [/INST]</s>"""
    reduce_prompt = PromptTemplate.from_template(reduce_template)
    reduce_chain = LLMChain(llm,prompt=reduce_prompt)
    # Take a list of documents, combines them into a single string, and passes this to an LLMChain
    combine_documents_chain = StuffDocumentsChain(llm_chain=reduce_chain, document_variable_name="doc_summaries")
    # Combines and iteratively reduces the mapped documents
    reduce_documents_chain = ReduceDocumentsChain(
        # This is final chain that is called.
        combine_documents_chain=combine_documents_chain,
        # If documents exceed context for 'StuffDocumentsChain'
        collapse_documents_chain=combine_documents_chain,
        # The maximum number of tokens to group documents into
        tokens_max=4000,
    )
    # Combinen documents by mapping a chain over them, then combining results
    map_reduce_chain = MapReduceDocumentsChain(
        # Map chain
        llm_chain=map_chain,
        # Reduce chain
        reduce_documents_chain=reduce_documents_chain,
        # The variable name in the llm_chain to put the documents in 
        document_variable_name="docs",
        # Return the results of the map steps in the output
        return_intermediate_steps=True,
    )
    

