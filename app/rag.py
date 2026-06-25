from pathlib import Path

from langchain_community.document_loaders import TextLoader
#from langchain_community.document_loaders import pypdfloader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from app.embeddings import embedding_model

def load_documents():

    data_folder = Path("data")

    documents = []

    for file in data_folder.glob("*.txt"):

        loader = TextLoader(file)

        documents.extend(loader.load())

    return documents


#chunking
def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30
    )

    chunks = splitter.split_documents(documents)

    return chunks


#vector store creation
def create_vector_store(chunks):

    vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="vector_store"
)

    return vector_store 

def ingest_documents():

    documents = load_documents()

    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    return vector_store

#Create Retrieval Function
def get_retriever():

    vector_store = Chroma(
        persist_directory="vector_store",
        embedding_function=embedding_model
    )

    retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":3}
)

    return retriever


# Create retrieve_context()
def retrieve_context(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context, docs