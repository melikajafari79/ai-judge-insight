from hazm import Normalizer, word_tokenize
from transformers import pipeline

normalizer = Normalizer()
classifier = pipeline("sentiment-analysis", model="HooshvareLab/bert-base-parsbert-uncased-sentiment")

def analyze_text(text):
    normalized = normalizer.normalize(text)
    tokens = word_tokenize(normalized)
    sentiment = classifier(normalized)[0]
    return {
        "normalized_text": normalized,
        "tokens": tokens,
        "sentiment": sentiment
    }