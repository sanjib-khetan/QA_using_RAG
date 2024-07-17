


import openai
from openai import OpenAI

OPENAI_API_KEY = "<give your key>"
client = OpenAI(api_key=OPENAI_API_KEY)



class llm():

    def __init__(self, relevant_docs, questions):

        self.relevant_docs = relevant_docs
        self.questions = questions.split("\n")
        self.questions = [qns.strip() for qns in self.questions]

    def call_llm(self):
        answers = {}

        for question in self.questions:
            if self.relevant_docs:
                # Use LLM to generate an answer based on the retrieved documents
                context = self.relevant_docs[0].page_content
                messages = [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"Based on the following document:\n\n{context}\n\nAnswer the question: {question}"}
                ]
                response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                          messages=messages,
                                                          max_tokens=150,
                                                          temperature=0.5
                                                          )
                answers[question] = response.choices[0].message.content.strip() if response.choices else "Data Not Available"
            else:
                answers[question] = "Data Not Available"
        return answers
