import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text :str) -> list[str]:
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split(" ")


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable : list[str]) -> dict:
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    frequencies = dict()
    for text in input_iterable:
        frequencies[text] = frequencies.get(text,0) + 1
    
    return frequencies



### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1 : dict, freq_dict2 : dict):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    unique_elements = list(set(freq_dict1.keys()).union(set(freq_dict2.keys())))

    delta = 0
    epsilon = 0
    for element in unique_elements:
        delta += abs(freq_dict1.get(element, 0) - freq_dict2.get(element, 0))
        epsilon += freq_dict1.get(element, 0) + freq_dict2.get(element, 0)
    
    similarity = round(1 - delta / epsilon, 2)

    return similarity

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    unique_elements = list(set(freq_dict1.keys()).union(set(freq_dict2.keys())))
    
    element_counts = [(el,freq_dict1.get(el, 0) + freq_dict2.get(el, 0)) for el in unique_elements]
    max_count = max([freq_dict1.get(el, 0) + freq_dict2.get(el, 0) for el in unique_elements])

    element_counts.sort(key= lambda x : x[1], reverse=True)

    return [el[0] for el in element_counts if el[1] == max_count]



### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    word_list = text_to_list(load_file(file_path))
    word_count = len(word_list)
    freq = get_frequencies(word_list)

    return {key : freq[key]/word_count for key in freq.keys()}


def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """

    number_of_documents = len(file_paths) 

    master_list = []
    for file in file_paths:
        word_list = text_to_list(load_file(file))
        word_list_deduped = list(set(word_list))
        master_list.extend(word_list_deduped)
    
    return {key : math.log10(number_of_documents / value) for key,value in get_frequencies(master_list).items()}
 

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    
    tf = get_tf(tf_file_path)
    idf = get_idf(idf_file_paths)
    tfidf = dict()

    for word in tf.keys():
        tfidf[word] = tf[word] * idf[word]

    return sorted([(key,value) for (key,value) in tfidf.items()], key= lambda x: x[1])



if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    #test_directory = "tests/student_tests/"
    #hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    #world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    #print(world)      # should print ['hello', 'world', 'hello']
    #print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    #freq1 = get_letter_frequencies('hello')
    #freq2 = get_letter_frequencies('that')
    #print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    #print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    #freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    #most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    #print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    #tf_text_file = 'tests/student_tests/hello_world.txt'
    #idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    #tf = get_tf(tf_text_file)
    #idf = get_idf(idf_text_files)
    #tf_idf = get_tfidf(tf_text_file, idf_text_files)
    #print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    #print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    #print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]