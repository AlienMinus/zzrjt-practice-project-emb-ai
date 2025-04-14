from textblob import TextBlob

def sentiment_analyzer(text_to_analyze):
    """
    Analyzes the sentiment of the given text.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: A dictionary containing the overall polarity, subjectivity, sentiment label,
              and a breakdown of sentiment for each sentence.
    """
    if not text_to_analyze.strip():
        return {"error": "Input text cannot be empty. Please provide valid text to analyze."}

    # Create a TextBlob object
    blob = TextBlob(text_to_analyze)

    # Overall sentiment analysis
    polarity = blob.sentiment.polarity  # Polarity ranges from -1 (negative) to 1 (positive)
    subjectivity = blob.sentiment.subjectivity  # Subjectivity ranges from 0 (objective) to 1 (subjective)

    # Determine overall sentiment label
    if polarity > 0:
        overall_sentiment = "Positive"
    elif polarity < 0:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"

    # Sentence-level sentiment analysis
    sentence_breakdown = []
    for sentence in blob.sentences:
        sentence_polarity = sentence.sentiment.polarity
        sentence_subjectivity = sentence.sentiment.subjectivity
        if sentence_polarity > 0:
            sentence_sentiment = "Positive"
        elif sentence_polarity < 0:
            sentence_sentiment = "Negative"
        else:
            sentence_sentiment = "Neutral"
        sentence_breakdown.append({
            "sentence": str(sentence),
            "polarity": sentence_polarity,
            "subjectivity": sentence_subjectivity,
            "sentiment": sentence_sentiment
        })

    # Return the results as a dictionary
    return {
        "overall_polarity": polarity,
        "overall_subjectivity": subjectivity,
        "overall_sentiment": overall_sentiment,
        "sentence_breakdown": sentence_breakdown
    }

# Example usage
if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    result = sentiment_analyzer(text)

    if "error" in result:
        print(result["error"])
    else:
        print(f"Overall Polarity: {result['overall_polarity']}")
        print(f"Overall Subjectivity: {result['overall_subjectivity']}")
        print(f"Overall Sentiment: {result['overall_sentiment']}")
        print("\nSentence Breakdown:")
        for sentence in result["sentence_breakdown"]:
            print(f"  Sentence: {sentence['sentence']}")
            print(f"    Polarity: {sentence['polarity']}")
            print(f"    Subjectivity: {sentence['subjectivity']}")
            print(f"    Sentiment: {sentence['sentiment']}")