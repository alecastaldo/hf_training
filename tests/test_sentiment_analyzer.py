from src.sentiment_analyzer import analyze_sentiment

def test_positive_sentiment():
    text = "I love this product!"
    result = analyze_sentiment(text)
    assert result[0]['label'] == 'POSITIVE', "The sentiment should be positive."

def test_negative_sentiment():
    text = "I hate this product!"
    result = analyze_sentiment(text)
    assert result[0]['label'] == 'NEGATIVE', "The sentiment should be negative."
