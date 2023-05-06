from model.DocSource import MdSource, UrlSource

md_sources = [
    MdSource('https://raw.githubusercontent.com/hwchase17/langchain/master/docs/modules/prompts/prompt_templates/getting_started.md'),
    MdSource('https://raw.githubusercontent.com/hwchase17/langchain-hub/master/README.md'),
]

url_sources = [
    UrlSource('https://docs.pinecone.io/docs/overview'),
    UrlSource('https://docs.pinecone.io/docs/semantic-text-search'),
    UrlSource('https://docs.pinecone.io/docs/python-client'),
    UrlSource('https://docs.pinecone.io/docs/indexes'),
    UrlSource('https://docs.pinecone.io/docs/hybrid-search'),
    UrlSource('https://docs.pinecone.io/docs/insert-data'),
    UrlSource('https://docs.pinecone.io/docs/manage-data'),
    UrlSource('https://docs.pinecone.io/docs/query-data'),
]
