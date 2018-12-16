# Project 2 - Text sentiment analysis
# MCS260 - Danko Adrovic
# By Clayton Smiley
# 10/26/2018


def get_neg_words(file):

    L = []
    text = ''
    with open(file, 'r', errors="ignore") as f:
        text = f.read()

    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("'", "")
    text = text.replace('"', "")
    text = text.replace('`', "")
    text = text.replace("\n", " ")
    text = text.lower()
    L = text.split(" ")
    return L


def get_text(s):
    L = []
    text = ""
    with open(s, 'r', errors="ignore") as f:  # open the file
        text = f.read()
        text = text.replace("\n", " ")
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace("-", " ")
        text = text.replace(",", "")
        text = text.replace("â", "")
        text = text.replace("€", "")
        text = text.replace("™", "")
        text = text.replace("œ", "")
        text = text.replace(";", "")
    text = text.lower()
    return text


#  parameters: the novel, the list of positive words and list of negative words
def analyze_sentiment(hound, pos, neg):
    positive = 0
    negative = 0
    neutral = 0
    sentences = hound.split(".")

    for i in range(len(sentences)-1):
        sentiment = 0
        word = sentences[i].split(" ")
        for j in range(len(word)-1):
            if len(word[j]) > 1:
                #  check if each word in the sentence is in pos or neg word file
                if word[j] in pos:
                    sentiment += 1
                elif word[j] in neg:
                    sentiment -= 1
                else:
                    sentiment += 0
        #  Now we have the current sentence as a sentiment value
        if sentiment > 0:
            positive += 1
        elif sentiment < 0:
            negative += 1
        else:
            neutral += 1

    return positive, negative, neutral


def main():

    P = get_neg_words("positivesentimentwords.txt")
    N = get_neg_words("negativesentimentwords.txt")

    pos, neg, neutral = analyze_sentiment(get_text("thehoundofthebaskervilles.txt"), P, N)

    print("Positive: %d \nNegative: %d \nNeutral:  %d" % (pos, neg, neutral))


main()
