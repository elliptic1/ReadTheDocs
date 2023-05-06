from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

from store_docs.constants import index_name
from store_docs.init import initialize_pinecone


def main(query):
    resp = do_query(query)
    print(resp)


def do_query(query):
    import os
    from langchain.llms import OpenAI
    from langchain.chains.question_answering import load_qa_chain

    initialize_pinecone()
    llm = OpenAI(temperature=0, openai_api_key=os.environ['RTD_OPENAI_API_KEY'])
    chain = load_qa_chain(llm, chain_type="stuff")
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.environ['RTD_OPENAI_API_KEY'],
    )
    docsearch = Pinecone.from_existing_index(index_name, embeddings)

    docs = docsearch.similarity_search(query, include_metadata=True)

    return chain.run(input_documents=docs, question=query)


if __name__ == '__main__':
    main("What is a collection, and how is it different than an index?")
