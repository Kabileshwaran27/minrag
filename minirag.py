import re


# --------------------------------
# 1. Knowledge Base
# --------------------------------

documents = [
    "Python is a high-level programming language used for software development.",
    "FastAPI is a Python framework used to build REST APIs.",
    "Django is a Python web framework used to build web applications.",
    "PostgreSQL is a relational database used to store structured data.",
    "Redis is an in-memory database commonly used for caching.",
    "RAG stands for Retrieval Augmented Generation."
]


# --------------------------------
# 2. Convert text into words
# --------------------------------

def get_words(text):
    return set(re.findall(r"\b\w+\b", text.lower()))


# --------------------------------
# 3. Retrieve relevant document
# --------------------------------

def retrieve(question):

    question_words = get_words(question)

    results = []

    for document in documents:

        document_words = get_words(document)

        common_words = question_words.intersection(document_words)

        score = len(common_words)

        results.append((score, document))

    results.sort(reverse=True)

    return results


# --------------------------------
# 4. Ask user
# --------------------------------

question = input("Ask a question: ")


# --------------------------------
# 5. Retrieval
# --------------------------------

results = retrieve(question)


# --------------------------------
# 6. Get best result
# --------------------------------

best_score, best_document = results[0]


# --------------------------------
# 7. Check if answer is available
# --------------------------------

if best_score == 0:

    print("\nAnswer:")
    print("I don't know.")

else:

    print("\n--- Retrieved Context ---")
    print("Score:", best_score)
    print("Document:", best_document)

    print("\n--- Answer ---")
    print(best_document)