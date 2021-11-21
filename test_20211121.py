from general_functions.global_general_functions import Timer
from utils.loader_20211120 import load_str_from_filepath, extract_lemma_count_list_from_data_str, get_lemma_list_byCount
from utils.loader_20211120 import combine_two_lemma_count_lists, combine_multiple_lemma_count_lists

import spacy
import os
from class_VocabularyItem_20211121 import VocabularyItem
if 1:
    d0 = r'.\data'
    file_name = 'pride_and_prejudice.txt'
    file_path = os.path.join(d0, file_name)
    data = load_str_from_filepath(file_path)
    data_text = data[:100]
else:
    data_text = 'her, hers, he, his, him, mine, my, me, I, i, a, a, a, b, b, b, c, c, c, d, d, d'
lemma_count_list = extract_lemma_count_list_from_data_str(data_text)
lemma_list_byCount = get_lemma_list_byCount(lemma_count_list)

lemma_count_list1 = extract_lemma_count_list_from_data_str(data[:10000])
lemma_count_list2 = extract_lemma_count_list_from_data_str(data[10000:20000])
lemma_count_list_combine = combine_two_lemma_count_lists(lemma_count_list1, lemma_count_list2)
lemma_list_byCount = get_lemma_list_byCount(lemma_count_list_combine)

lemma_count_list3 = extract_lemma_count_list_from_data_str(data[:20000])
lemma_list_byCount = get_lemma_list_byCount(lemma_count_list3)

lemma_count_list_list = []
for t_i in range(0, 3):
    lemma_count_list = extract_lemma_count_list_from_data_str(data[(t_i)*10000:(t_i+1)*10000])
    lemma_count_list_list.append(lemma_count_list)


lemma_list_byCount = get_lemma_list_byCount(combine_multiple_lemma_count_lists(lemma_count_list_list))

lemma_count_list = extract_lemma_count_list_from_data_str(data[:30000])
lemma_list_byCount = get_lemma_list_byCount(lemma_count_list)
