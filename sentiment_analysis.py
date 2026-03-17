import csv
import os



punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# function which removes characters considered punctuation from everywhere in the word.
def strip_punctuation(word):
    for p in punctuation_chars:
        word=word.replace(p,"")  # "replace()" method for strings.
    return word



# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#function which calculates how many words in the string are considered positive words. 
pos_int=0
def get_pos(s):
    pos_int=0
    word=s.lower().split()
    for i in word:
        i=strip_punctuation(i)
        if i in positive_words:
          pos_int+=1
    return pos_int
print(get_pos("I feel great and happy"))
print(get_pos("what a truly wonderful day it is today! #incredible"))



# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#function which calculates how many words in the string are considered negative words. 
def get_neg(word_neg):
    word=0
    word_neg=word_neg.lower().split()
    for i in word_neg:
        i=strip_punctuation(i)
        if i in negative_words:
            word+=1
    return word
print(get_neg("i angray and hate you"))



print(os.listdir())




# a csv file called `resulting_data.csv`, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order.
with open("project_twitter_data.csv","r") as input_file:
    reader=csv.reader(input_file)
    header=next(reader)
    with open("resulting_data.csv","w") as output_file:
        writer=csv.writer(output_file)
        writer.writerow(["Number of Retweets","Number of Replies","Positive Score","Negative Score","Net Score"])
    
        for row in reader:
            tweet_text=row[0]
            retweet=row[1]
            replies=row[2]
            
            pos_score=get_pos(tweet_text)
            neg_score=get_neg(tweet_text)
            net_score=pos_score - neg_score
        
            writer.writerow([retweet,replies,pos_score,neg_score,net_score])
    










