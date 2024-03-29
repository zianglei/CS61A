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

    return accuracy * 100 / length


def analyze(sample_paragraph, typed_string, start_time, end_time):
    """This function outputs a list containing two values: words per minute and accuracy percentage
    start_time and end_time are measured in seconds
    """

    result = []
    result.append(calc_words_per_minute(typed_string, start_time, end_time))
    result.append(calc_accuracy_percentage(sample_paragraph, typed_string))
    return result


def pig_latin(word):
    if type(word) != str: return
    if len(word) == 0: return word
    for i in range(len(word)):
        if not word[i].isalpha(): continue
        if word[i] in ['a', 'e', 'i', 'o', 'u']: break

    if i == 0:
        newword = word + "way"
    elif i == len(word) - 1:
        newword = word + "ay"
    else:
        newword = lower(word[i:]) + lower(word[0: i]) + 'ay'
    if ord('A') <= ord(word[0]) <= ord('Z'):
        return newword.capitalize()
    else:
        return newword


def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    else:
        return min(words_list, key=lambda x: score_function(x, user_input))


def swap_score(string_one, string_two):
    if len(string_one) == 0 or len(string_two) == 0: return 0
    if string_one[0] != string_two[0]:
        return 1 + swap_score(string_one[1:], string_two[1:])
    else:
        return swap_score(string_one[1:], string_two[1:])


# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1 == "" or word2 == "":
        return max(len(word1), len(word2))

    elif word1[0] == word2[0]:  # Feel free to remove or add additional cases
        # BEGIN Q6
        return score_function(word1[1:], word2[1:])
        # END Q6

    else:
        add_char = score_function(word1, word2[1:])  # Fill in these lines
        remove_char = score_function(word1[1:], word2)
        substitute_char = score_function(word1[1:], word2[1:])
        # BEGIN Q6
        # END Q6
        return 1 + min(add_char, remove_char, substitute_char)


KEY_DISTANCES = get_key_distances()


# BEGIN Q7-8
def score_function_accurate(word1, word2):
    if word1 == "" or word2 == "":
        return max(len(word1), len(word2))
    elif word1[0] == word2[0]:  # Feel free to remove or add additional cases
        return score_function_accurate(word1[1:], word2[1:])
    else:
        add_char = 1 + score_function_accurate(word1, word2[1:])  # Fill in these lines
        remove_char = 1 + score_function_accurate(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word2[0], word1[0]] + score_function_accurate(word1[1:], word2[1:])

        return min(add_char, remove_char, substitute_char)


score_mem = {}

def score_function_final(word1, word2):
    if word1 == "" or word2 == "":
        return max(len(word1), len(word2))

    if (word1, word2) in score_mem.keys():
        return score_mem[word1, word2]
    elif (word2, word1) in score_mem.keys():
        return score_mem[word2, word1]

    elif word1[0] == word2[0]:
        return score_function_final(word1[1:], word2[1:])
    else:
        add_char = 1 + score_function_final(word1, word2[1:])  # Fill in these lines
        remove_char = 1 + score_function_final(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word2[0], word1[0]] + score_function_final(word1[1:], word2[1:])

        accuracy = min(add_char, remove_char, substitute_char)
        score_mem[word1, word2] = accuracy
        score_mem[word2, word1] = accuracy

        return accuracy

# END Q7-8