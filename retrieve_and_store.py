from store_docs.fetch import fetch_url_sources, fetch_md_sources
from store_docs.init import initialize_pinecone
from store_docs.store import store_docs


def retrieve_and_store_docs():
    # Get all documents
    documents = fetch_url_sources() + fetch_md_sources()

    # Store to vector database
    initialize_pinecone()
    store_docs(documents)


if __name__ == '__main__':
    retrieve_and_store_docs()
