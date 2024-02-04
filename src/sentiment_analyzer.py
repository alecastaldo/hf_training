from transformers import pipeline

def analyze_sentiment(text):
    # load the sentiment-analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")

    # perform sentiment analysis

    result = sentiment_pipeline(text)

    return result