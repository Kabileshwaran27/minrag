import re


DOCUMENTS = [
	"Python is a programming language used to build many kinds of software.",
	"FastAPI is a Python framework used to build web APIs.",
	"Django is a Python framework used to build web applications.",
	"PostgreSQL is a relational database used to store structured data.",
	"RAG means Retrieval Augmented Generation. It finds useful text before answering a question.",
]

STOP_WORDS = {
	"a", "an", "and", "are", "for", "how", "is", "of", "the", "to", "what", "with",
}


def get_words(text):
	"""Return the useful words in a piece of text."""
	words = re.findall(r"\b\w+\b", text.lower())
	return set(words) - STOP_WORDS


def retrieve(question, limit=2):
	"""Find the documents that share the most words with the question."""
	question_words = get_words(question)
	scored_documents = []

	for document in DOCUMENTS:
		score = len(question_words.intersection(get_words(document)))
		if score > 0:
			scored_documents.append((score, document))

	scored_documents.sort(key=lambda item: item[0], reverse=True)
	return scored_documents[:limit]


def answer_question(question):
	matches = retrieve(question)

	if not matches:
		print("I don't know based on the documents I have.")
		return

	print("\nRetrieved context:")
	for score, document in matches:
		print(f"- ({score} matching words) {document}")

	print("\nAnswer:")
	print(matches[0][1])


def main():
	print("Try: What is FastAPI used for?")
	question = input("Ask a question: ").strip()
	if question:
		answer_question(question)
	else:
		print("Please enter a question.")


if __name__ == "__main__":
	main()
