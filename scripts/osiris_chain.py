from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate


def create_osiris_chain(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)
    retriever = vector_store.as_retriever()

    prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")

    llm = OpenAI(model="gpt-4")

    qa_chain = load_qa_chain(
        llm=llm,
        chain_type="stuff",
        prompt=prompt_template
    )

    return RetrievalQA(retriever=retriever, combine_documents_chain=qa_chain )