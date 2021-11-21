import spacy
from general_functions.global_general_functions import Timer


def load_str_from_filepath(file_path):
    with open(file_path, encoding="utf8") as f:
        data_str = f.read()
    return data_str


def extract_lemma_count_list_from_data_str(data_str):
    print('tokenize data, data_length: ' + str(len(data_str)) + '.')

    with Timer('doc = nlp(data_str)'):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(data_str)
        print('done. # of token: ' + str(len(doc)) + '.')

    with Timer('count_words'):
        lemma_count_list = {}
        word_count = 0
        for token in doc:
            # print(token)
            if not token.is_alpha:
                continue
            word_count = word_count + 1
            if token.lemma_ not in lemma_count_list:
                lemma_count_list[token.lemma_] = 0
            lemma_count_list[token.lemma_] = lemma_count_list[token.lemma_] + 1
        print('# of words: ' + str(word_count) + '.')
        print('# of lemmas: ' + str(len(lemma_count_list)) + '.')
    return lemma_count_list


def get_lemma_list_byCount(lemma_count_list):
    lemma_list_byCount = {}
    word_count = 0
    for word_text in lemma_count_list:
        freq_count = lemma_count_list[word_text]
        if freq_count not in lemma_list_byCount:
            lemma_list_byCount[freq_count] = []
        word_count = word_count + freq_count
        lemma_list_byCount[freq_count].append(word_text)
    print('# of word: ' + str(word_count) + ', # of lemma: ' + str(len(lemma_count_list)) + '.')

    num_count_list_sorted = list(lemma_list_byCount.keys())
    num_count_list_sorted.sort(reverse=1)
    showing_rank_list = list(range(0,10))
    showing_rank_list.append(len(num_count_list_sorted)-1)
    for rank_i in showing_rank_list:
        if rank_i>=len(num_count_list_sorted):
            continue
        freq_count = num_count_list_sorted[rank_i]
        freq_percent = freq_count / word_count
        this_rank_word_list = lemma_list_byCount[freq_count]
        text = str(rank_i) + 'th most frequent word(s): ' + str(freq_count) + ' times ('
        text = text + str(freq_percent * 10000 / 100) + '%), '
        if len(this_rank_word_list) < 5:
            text = text + str(this_rank_word_list) + '.'
        else:
            text = text + str(len(this_rank_word_list)) + ' such words.'
        print(text)
    return lemma_list_byCount


def combine_two_lemma_count_lists(lemma_count_list1, lemma_count_list2):
    for lemma in lemma_count_list2:
        if lemma not in lemma_count_list1:
            lemma_count_list1[lemma] = 0
        lemma_count_list1[lemma] = lemma_count_list1[lemma] + lemma_count_list2[lemma]
    return lemma_count_list1


def combine_two_lemma_count_lists(lemma_count_list1, lemma_count_list2):
    for lemma in lemma_count_list2:
        if lemma not in lemma_count_list1:
            lemma_count_list1[lemma] = 0
        lemma_count_list1[lemma] = lemma_count_list1[lemma] + lemma_count_list2[lemma]
    return lemma_count_list1


def combine_multiple_lemma_count_lists(lemma_count_list_list):
    l1 = lemma_count_list_list.pop()
    while (len(lemma_count_list_list) > 0):
        l2 = lemma_count_list_list.pop()
        l1 = combine_two_lemma_count_lists(l1, l2)
    return l1