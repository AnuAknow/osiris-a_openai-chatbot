from scripts.osiris_chain import create_osiris_chain
from scripts.osiris_loader import getSelectiveDataDF, loadLangChain
from scripts.osiris_chain_modern import create_osiris_chain

from dotenv import load_dotenv
load_dotenv()

def main():
    print("🜃 OSIRIS-A Awakening...")
    df=getSelectiveDataDF('oaidata/conversations.json')
    docs = loadLangChain(df)
    chain = create_osiris_chain(docs)

    print("Type your query (or 'exit' to quit):")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        response = chain.invoke(query)
        print(f"OSIRIS-A: {response}\n")

if __name__ == "__main__":
    main()
