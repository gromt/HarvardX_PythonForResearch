# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# text = "Learn how' to write your: own; function to count the number! of times? a unique word appears in a given string text. Learn about how to use the Counter tool from the collections module to accomplish the same task."

from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

def count_words(text):    
    """ 
    Parameters
    ----------
    text : TYPE
        DESCRIPTION.

    Returns
    -------
    word_counts : Count of unique word in text within punctuation strings.
                  All words returns in lowercase.

    """
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']    #"?", "!", 
    for ch in skips:
        text = text.replace(ch, "")        
    word_counts = {}    
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def count_words_fast(text):
    
    """    
    Parameters
    ----------
    text : TYPE
        DESCRIPTION.

    Returns
    -------
    word_counts : Count of unique word in text within punctuation strings.
                  All words returns in lowercase.

    """
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']    # "?", "!",
    for ch in skips:
        text = text.replace(ch, "")            
    word_counts = Counter(text.split(" "))    
    return word_counts

def read_book(title_path):
    
    """
        Read a book and retuns as a string.        
    """
    
    with open(title_path, "r", encoding = "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    
    """" 
        Return number of unique words.
    """
    
    num_unique = len(word_counts)
    counts  = word_counts.values()
    return (num_unique, counts)


book_dir = "./Books"

stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            #print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words_fast(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

plt.plot(stats.length, stats.unique, "bo")
plt.loglog(stats.length, stats.unique, "bo")

plt.figure(figsize = (10, 10))

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")

subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")

subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "orange")

subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")

plt.legend()
plt.xlabel("Book lenght")
plt.ylabel("Number of unique words")
plt.savefig("leng_plot.pdf")


# stats[stats.language == "English"]
# stats[stats.language == "French"]
            
# text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
# word_counts = count_words(text)
# (num_unique, counts) = word_stats(word_counts)
# print (num_unique, sum(counts))

# text = read_book("./Books/German/shakespeare/Romeo und Julia.txt")
# word_counts = count_words(text)
# (num_unique, counts) = word_stats(word_counts)
# print (num_unique, sum(counts))