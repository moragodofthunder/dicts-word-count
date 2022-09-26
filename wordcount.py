
"""Count words in file."""



def word_count(filename):

    word_file = open(filename)
    

    word_counts = {}

    for line in word_file:
        words = line.split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    word_file.close()

    return word_counts

print(word_count("twain.txt"))