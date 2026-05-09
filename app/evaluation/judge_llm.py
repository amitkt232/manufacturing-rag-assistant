from app.llm.llm import llm

from app.retrieval.rag_pipeline import (
    generate_response
)


def judge_response(

    question,

    answer
):

    prompt = f"""

You are an expert RAG evaluator.

Evaluate whether the answer is:

1. Grounded in retrieved context
2. Relevant to the question
3. Hallucinated or not

Question:
{question}

Answer:
{answer}

Provide:

Groundedness Score: X/10
Relevance Score: X/10
Hallucination Risk: Low/Medium/High
Short Explanation:
"""

    result = llm.invoke(prompt)

    return result.content


if __name__ == "__main__":

    while True:

        query = input("\nEnter query: ")

        if query.lower() == "exit":
            break

        rag_result = generate_response(
            query
        )

        answer = rag_result["answer"]

        evaluation = judge_response(

            query,

            answer
        )

        print("\nANSWER:\n")

        print(answer)

        print("\nJUDGE EVALUATION:\n")

        print(evaluation)