from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

print(classifier("I Hate this!!"))

sentences = [
    "I'm so happy to see you!",
    "I miss my family.",
    "This is so annoying, I hate it.",
    "The meeting is at noon.",
]

for sentence in sentences:
    result = classifier(sentence)
    print(sentence, "->", result)