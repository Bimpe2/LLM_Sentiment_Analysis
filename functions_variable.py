import os
import pandas as pd
import pickle
import numpy as np
import string
import nltk
import re
from nltk.corpus import stopwords
from datasets import load_dataset
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

def remove_htmltags(text):
    """
    Removes all htmltags from a string.

    Parameters:
    text (string): movie review

    Returns:
    String: a movie review string with all htmltagsremoved.
    """
    clean = re.compile('<.*?>')
    return re.sub(clean,'',text)

def remove_punctuation(text):
    """
    Removes all the punctuation from a string.

    Parameters:
    text (string): movie review

    Returns:
    String: a movie review string with all punctuations removed.
    """
    punctuation = string.punctuation
    punctuation

    text_with_no_punctuation = "".join([word for word in text if word not in punctuation])
    return text_with_no_punctuation

def tokenize_remove_capitilization(text):
    """
    Removes all capitalization from strings and also tokenizes the words.

    Parameters:
    text (string): movie review string of words

    Returns:
    String: a movie review list with all capitilization removed and strings tokenized.
    """
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

def remove_stopwords(text):
   """
    Removes all stopwords from the list of words.

    Parameters:
    text (string): movie review list of words

    Returns:
    list: a movie review list with all capitilization removed and strings tokenized.
    """
   stop_words = stopwords.words('english')
   text_no_stopword = [word for word in text if word not in stop_words]
   return text_no_stopword

def lem_text(text,pos):
  """
    Removes all stopwords from the list of words.

    Parameters:
    text (string): movie review list of words

    Returns:
    list: a movie review list with all capitilization removed and strings tokenized.
    """
  lemm = WordNetLemmatizer()
  word_lemm = [lemm.lemmatize(word,pos) for word in text]
  return word_lemm
