def list_of_words(f):
    """
    INPUT: file
    OUTPUT: list of words

    Create a list of all the unique words in the text file given.

    10 loops, best of 3: 92.2 ms per loop
    100 loops, best of 3: 2.64 ms per loop
    Sets are inherently unique so you don't need to check if it's already there
    and the 'in' operator works much faster going through sets than lists
    """

    words = set()
    for line in f:
        for word in line.strip().split():
            words.add(word)
    return words


def find_new_words(f, word_dict):
    """
    INPUT: file, dictionary
    OUTPUT: list

    Given a text file and a dictionary whose keys are words, return a list
    of the words in the file which are not in the dictionary.
    21.4 s per loop
    100 loops, best of 3: 2.72 ms per loop

    Removed .keys() from word_dict, which eliminates unnecessary iteration through keys
    """

    words = []
    for line in f:
        for word in line.strip().split():
            if word not in word_dict:
                words.append(word)
    return words


def get_average_score(f, word_dict):
    """
    INPUT: file, dictionary
    OUTPUT: float

    Given a text file and a dictionary whose keys are words and values are a
    score for the word, return the average score of all the words in the
    document. You should assume that missing words have a score of 1.

    100 loops, best of 3: 5.77 ms per loop
    100 loops, best of 3: 3.93 ms per loop


    """

    score = 0
    count = 0
    for line in f:
        for word in line.strip().split():
            value = word_dict.get(word, 1)
            '''try:
                value = word_dict[word]
            except KeyError:
                value = 1'''
            score += value
            count += 1
    return float(score) / count


def find_high_valued_words(word_dict, value):
    """
    INPUT: dict, float
    OUTPUT: list

    Return the items from word_dict whose values are larger than value.

    100 loops, best of 3: 9.37 ms per loop
    100 loops, best of 3: 9.37 ms per loop

    By using .iteritem() instead of .item() we have used a generator instead of a list so we are only using the values when we need them instead of creating them all at once.
    """

    return [key for key, val in word_dict.iteritems() if val > value]
