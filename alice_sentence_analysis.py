import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

nltk.download('punkt_tab')

chapters = [
    "down_the_rabbit_hole.txt",
    "mad_tea_party.txt",
    "queens_croquet_ground.txt"
]


for chapter in chapters:
    with open(chapter, "r", encoding="utf-8") as f:
        text = f.read()

        text = text.replace("CHAPTER I.", "")
        text = text.replace("Down the Rabbit-Hole", "")

        text = text.replace("CHAPTER VII.", "")
        text = text.replace("A Mad Tea-Party", "")

        text = text.replace("CHAPTER VIII.", "")
        text = text.replace("The Queen’s Croquet-Ground", "")

    sentences = nltk.sent_tokenize(text)

    positive_sentences = 0
    negative_sentences = 0
    neutral_sentences = 0

    for sentence in sentences:

        scores = sia.polarity_scores(sentence)

        compound = scores['compound']

        if compound > 0.05:
            positive_sentences += 1

        elif compound < -0.05:
            negative_sentences += 1

        else:
            neutral_sentences += 1

    print(chapter)
    print(f"Positive sentences: {positive_sentences}")
    print(f"Negative sentences: {negative_sentences}")
    print(f"Neutral sentences: {neutral_sentences}")
    print()



    
    
            
