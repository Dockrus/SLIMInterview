from transformers import pipeline

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

CONFIDENCE_THRESHOLD = 0.5

GESTURES = {"joy": "wave",
    "anger": "back_away",
    "sadness": "lower_head",
    "fear": "back_away",
    "surprise": "tilt_head",
    "disgust": "turn_away",
    "neutral": "idle"}

def classifyEmotion(text: str) -> str:
    out = classifier(text)
    into = out[0]
    result = into[0]
    label = result['label']
    score = result['score']

    if score <= CONFIDENCE_THRESHOLD:
        label = "neutral"


    print(label)
    print(score)
    return "label"

if __name__ == "__main__":
    for s in ["I'm so happy to see you!", "I miss my family.",
               "This is so annoying, I hate it.", "The meeting is at noon."]:
        classifyEmotion(s)

    
