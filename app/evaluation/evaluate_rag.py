import json

from app.retrieval.rag_pipeline import (
    generate_response
)

from app.utils.guardrails import (
    validate_query
)


def load_dataset():

    with open(
        "data/evaluation/evaluation_dataset.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def keyword_match_score(

    answer,

    expected_keywords
):

    answer_lower = answer.lower()

    matches = 0

    for keyword in expected_keywords:

        if keyword.lower() in answer_lower:

            matches += 1

    return matches / len(expected_keywords)


def evaluate():

    dataset = load_dataset()

    results = []

    for sample in dataset:

        question = sample["question"]

        if not validate_query(question):

            print(
                f"Blocked query: {question}"
            )

            continue

        rag_response = generate_response(
            question
        )

        answer = rag_response["answer"]

        score = keyword_match_score(

            answer,

            sample["expected_keywords"]
        )

        evaluation = {

            "question": question,

            "answer": answer,

            "score": score
        }

        results.append(evaluation)

    return results


if __name__ == "__main__":

    results = evaluate()

    print("\nEVALUATION RESULTS\n")

    for result in results:

        print("=" * 60)

        print(f"\nQuestion:")
        print(result["question"])

        print(f"\nScore:")
        print(result["score"])

        print(f"\nAnswer:")
        print(result["answer"])