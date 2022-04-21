import os
import timeit
import math

# more efficient
sqrt = math.sqrt
stopwatch = timeit.default_timer

def txt_file_to_list(filepath):
    my_file = open(filepath, "r")
    data = my_file.read()
    data_into_list = data.split("\n")
    my_file.close()
    return data_into_list


def highest_scoring_pair(words_l):
    sorted_words = sorted(words_l, key=len, reverse=True)
    last_index, i, max_score = len(sorted_words) - 1, 0, 0
    # If a word's length is less then the square root of the max score
    # it cannot possibly achieve a higher score, so it can be skipped
    while (i <= last_index) and (len(sorted_words[i]) >= sqrt(max_score)):
        j, found = i + 1, 0
        while (j <= last_index) and (found in [0]) and (len(sorted_words[i]) * len(sorted_words[j]) >= max_score):
            for character in sorted_words[i]:
                if character in sorted_words[j]:
                    score = 0
                    break
            else:
                score = len(sorted_words[i]) * len(sorted_words[j])

            if score > max_score:
                w1, w2, max_score, found = sorted_words[i], sorted_words[j], score, True
            elif score > 0:
                found = 1

            j += 1
        i += 1
    if max_score not in [0]:
        return [w1, w2]
    else:
        # if the max score is 0 then every word in the list has at least 1 character in common so we return the first two words as one pair which achieves the highgest score of 0
        return (sorted_words[0], sorted_words[1])

# loading input data to list
words_l = txt_file_to_list(os.path.join(os.getcwd(), 'words.txt'))

# test of max_score = 0 edge case
#words_l = ['a', 'a']

# Execution
start = stopwatch()
word_pair = highest_scoring_pair(words_l)
stop = stopwatch()
execution_time = stop - start

print(word_pair)
print(execution_time)