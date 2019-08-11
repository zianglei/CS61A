""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
def lines_from_file(path):
    if type(path) != str: return
    lines = []
    with open(path, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines

def new_sample(path, i):
    if type(path) != str: return
    if i < 0: return

    line_list = lines_from_file(path)
    if (i >= len(line_list)): return
    return line_list[i]

def calc_words_per_minute(typed_string, start_time, end_time):
    words_length = len(typed_string) / 5
    time = (end_time - start_time) / 60
    return words_length / time

def calc_accuracy_percentage(sample_paragraph, typed_string):
    sample_words = split(strip(sample_paragraph))
    typed_words = split(strip(typed_string))
    length = min(len(sample_words), len(typed_words))
    if length == 0: return 0.0

    accuracy = 0
    for i in range(length):
        if sample_words[i] == typed_words[i]:
            accuracy += 1
    
    return accuracy * 100/ length

def analyze(sample_paragraph, typed_string, start_time, end_time):
    """This function outputs a list containing two values: words per minute and accuracy percentage
    start_time and end_time are measured in seconds
    """
    
    result = []
    result.append(calc_words_per_minute(typed_string, start_time, end_time))
    result.append(calc_accuracy_percentage(sample_paragraph, typed_string))
    return result
# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6
    
    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________ 
        substitute_char = ______________ 
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8
