from python_code.RAG.rag import RAG
from python_code.utils.pdf_parser import pdf_parser
from python_code.utils.post_slack import post_to_slack
from python_code.LLM.llm_call_rag import llm



def process_input(pdf_path, questions):
    k = 5
    parser_obj = pdf_parser(pdf_path)
    pages = parser_obj.parse_pdf()

    rag_obj = RAG(pages)
    rag_obj.create_vector_store()
    relevant_docs = rag_obj.answer_questions(questions, k)

    llm_obj = llm(relevant_docs, questions)
    answers = llm_obj.call_llm()

    message = "\n".join([f"Q: {q}\nA: {a}" for q, a in answers.items()])
    print(message)
    slack_webhook_url = "https://hooks.slack.com/services/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"
    post_to_slack(slack_webhook_url, message)