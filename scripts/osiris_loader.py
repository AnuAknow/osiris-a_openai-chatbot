import pandas as pd
from langchain_community.document_loaders import DataFrameLoader

def getSelectiveDataDF(file_path):
    df = pd.read_json(file_path)
    return df
  
    
def loadLangChain(dataframe):
    loader = DataFrameLoader(dataframe, page_content_column="title")
    doc = loader.load()
    return doc 