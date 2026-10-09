# Sentiment Reactive Robot

The robot responds to how you say something rather than what you say. A happy sentence makes it wave, an angry one makes it back away, and a sad one makes it lower its head.

How it works: This is the same pipeline shape, but the middle module runs a Hugging Face sentiment or emotion classifier, for example a model that labels text as joy, anger, sadness, and so on. A robot module maps each emotion to a gesture. It’s simpler than intent recognition because you don’t need to define a list of commands, and it connects naturally to human-robot interaction, which is the focus of Kennington’s research.

## Model

I decided to use this model

[Emotion-English-Model](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
j-hartmann/emotion-english-distilroberta-base

With this model, you can classify emotions in English text data. The model was trained on 6 diverse datasets (see Appendix below) and predicts Ekman's 6 basic emotions, plus a neutral class:

1. anger 🤬
2. disgust 🤢
3. fear 😨
4. joy 😀
5. neutral 😐
6. sadness 😭
7. surprise 😲

How to run the model

```
from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
classifier("I love this!")
```