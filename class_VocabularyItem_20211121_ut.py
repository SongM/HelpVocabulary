from class_VocabularyItem_20211121 import VocabularyItem
vi = VocabularyItem('test')
vi.add_count()
vi.change_understanding_level(3)
print(vi.getTxt_word_info())

from class_VocabularyItem_20211121 import VocabularyList
v_list = VocabularyList()
known_list = ['known_a', 'known_b', 'known_c', 'known_d']
unknown_list = ['unknown_a', 'unknown_b', 'unknown_c', 'unknown_d']
for word in known_list:
    v_list.add_word(word)
v_list.print_list()

for word in known_list:
    v_list.add_word(word)
    v_list.change_understanding_level(word,3)
for word in unknown_list:
    v_list.add_word(word)
v_list.add_word('unknown_a')
v_list.print_list()

