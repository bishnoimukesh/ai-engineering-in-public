"""Day 2 mini-project: solve one problem the ML-engineer way and the AI-engineer way.

Task: classify short product reviews as "positive" or "negative".

ML engineer approach : collect labeled data -> train a model -> evaluate it.
AI engineer approach : take a pre-trained LLM -> write instructions -> evaluate it.

Run:
    pip install scikit-learn openai
    python two_approaches.py                  # ML part only
    OPENAI_API_KEY=sk-... python two_approaches.py   # both parts
"""

import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

# A tiny labeled dataset. Real ML projects need far more data than this.
TRAIN = [
    ("Absolutely love it, works perfectly", "positive"),
    ("Great quality and fast delivery", "positive"),
    ("Exceeded my expectations, highly recommend", "positive"),
    ("Five stars, would buy again", "positive"),
    ("Very happy with this purchase", "positive"),
    ("Excellent value for the price", "positive"),
    ("Works great, easy to set up", "positive"),
    ("Fantastic product, my family loves it", "positive"),
    ("Broke after two days, total waste", "negative"),
    ("Terrible quality, do not buy", "negative"),
    ("Arrived damaged and support ignored me", "negative"),
    ("Very disappointed, nothing like the photos", "negative"),
    ("Stopped working after a week", "negative"),
    ("Worst purchase I have made this year", "negative"),
    ("Cheap materials, fell apart quickly", "negative"),
    ("Refund please, it does not work", "negative"),
]

# Held-out test set, with wording the model has not seen.
TEST = [
    ("I'm thrilled, this is exactly what I needed", "positive"),
    ("The battery died on day one", "negative"),
    ("Not bad at all, pleasantly surprised", "positive"),
    ("Would not recommend to anyone", "negative"),
    ("Solid build and it looks beautiful", "positive"),
    ("Returned it, the screen kept flickering", "negative"),
]
test_texts = [t for t, _ in TEST]
test_labels = [label for _, label in TEST]


# --- ML engineer way: train your own model --------------------------------
def ml_engineer_approach() -> None:
    model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2)), LogisticRegression())
    model.fit([t for t, _ in TRAIN], [label for _, label in TRAIN])  # training step
    predictions = model.predict(test_texts)
    print("ML engineer (trained TF-IDF + logistic regression)")
    for text, pred in zip(test_texts, predictions):
        print(f"  {pred:8}  {text}")
    print(f"  accuracy: {accuracy_score(test_labels, predictions):.0%}\n")


# --- AI engineer way: use a pre-trained LLM -------------------------------
def ai_engineer_approach() -> None:
    from openai import OpenAI

    client = OpenAI()
    predictions = []
    for text in test_texts:
        response = client.responses.create(
            model="gpt-4o-mini",  # any chat model your account can use
            instructions=(
                "Classify the product review's sentiment. "
                "Answer with exactly one word: positive or negative."
            ),
            input=text,
            temperature=0,
        )
        label = response.output_text.strip().lower()
        predictions.append(label if label in ("positive", "negative") else "unknown")

    print("AI engineer (pre-trained LLM, no training)")
    for text, pred in zip(test_texts, predictions):
        print(f"  {pred:8}  {text}")
    print(f"  accuracy: {accuracy_score(test_labels, predictions):.0%}\n")


if __name__ == "__main__":
    ml_engineer_approach()
    if os.environ.get("OPENAI_API_KEY"):
        ai_engineer_approach()
    else:
        print("Set OPENAI_API_KEY to run the AI engineer approach too.")
