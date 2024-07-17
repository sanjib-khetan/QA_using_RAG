from langchain_community.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

class RAG():

    def __init__(self, pages):

        self.pages = pages
        self.embedding = []
        self.docs = []
        self.vector_store = []



    def create_vector_store(self):

        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.docs = [Document(page_content=page) for page in self.pages]
        self.vector_store = Chroma.from_documents(self.docs, self.embeddings)

    def answer_questions(self, questions, max_doc):

        for question in questions:
            # Retrieve relevant documents
            relevant_docs = self.vector_store.similarity_search(question, k=max_doc)
        return relevant_docs

