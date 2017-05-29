import nltk, matplotlib
# Read in entire file of tweets

# Create List to keep adding lines to
list = []

# Open file of tweets, appending each line to List
with open("sarcastictweets.txt") as f:
    for line in f:
        list.append(line)
# Tokenize and assign POS tags to each word one tweet at a time

tagged_list = []

for i in list:
    tweet = nltk.word_tokenize(i)
    tweet = nltk.pos_tag(tweet)
    tagged_list.append(tweet)
# Iterate through all tweets, extracting only the POS tags

list2 = []

iter = 0
for i in tagged_list:
    length = len(i)
    for j in range(0,length):
        list2.append(tagged_list[iter][j][1])
    iter+=1
    list2.append("\n") # Note: this adds two newline characters for some reason
print(list2)
