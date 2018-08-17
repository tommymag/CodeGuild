# # Lab: Word Count

# Find a book on Project Gutenberg.
# Download it as a UTF-8 text file.

# Open the file.
# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values. If a word isn’t in your dictionary
# yet, add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the code below.

# # word_dict is a dictionary where the key is the word and the value is the count
# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])



file = open("../text/peter_pan.txt", "r", encoding="utf-8")  # Opens the text file
word_list = file.read().lower().replace('.', '').replace(',', '').replace('?',
                                                                          '').split()  # Replaces characters and puts everything into lower case
word_dict = {}
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your',
              'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
              'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
              'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were',
              'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a',
              'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
              'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during',
              'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
              'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
              'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
              'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
              'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm',
              'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn',
              'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn',
              'weren', 'won', 'wouldn', '“i']

for word in word_list:
    if word not in stop_words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])



    #
