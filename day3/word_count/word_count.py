"""word count"""


# receive the text
# split to words and save in a list
# loop through the list counting and saving the out

def words(in_words):
    """
    Takes in a string of characters splits it to words and returns a dictionary
    of the words and the number the word occurs
    :param in_words: list
    :return: dictionary
    """
    try:
        in_words = in_words.split()
        dic_out = {}
        for word in in_words:
            if word.isdigit():
                if int(word) in dic_out:
                    dic_out[int(word)] = dic_out[int(word)] + 1
                else:
                    dic_out[int(word)] = 1
            else:
                if word in dic_out:
                    dic_out[word] = dic_out[word] + 1
                else:
                    dic_out[word] = 1
        return dic_out
    except Exception as e:
        return e
