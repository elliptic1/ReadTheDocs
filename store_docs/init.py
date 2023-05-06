import pinecone
import os


def initialize_pinecone():
    pinecone.init(
        api_key=os.environ["RTD_PINECONE_API_KEY"],  # find at app.pinecone.io
        environment=os.environ["RTD_PINECONE_ENV"]  # next to api key in console
    )
