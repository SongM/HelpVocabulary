class VocabularyItem:
    def __init__(self, word):
        self.word = word
        self.count = 0
        self.understanding_level = 1
        self.example_sentences = []

    def add_count(self, adding_count=1):
        self.count = self.count + adding_count

    def change_understanding_level(self, new_level):
        self.understanding_level = new_level

    def add_example_sentences(self, example_sentence):
        self.example_sentences.append(example_sentence)

    def getTxt_word_info(self):
        return self.word + ': level(' + str(self.understanding_level) + '), count(' + str(self.count) + ')'


class VocabularyList:
    def __init__(self):
        self.VocabularyItem_list = {}

    def add_word(self, word, adding_count=1):
        if word not in self.VocabularyItem_list:
            self.VocabularyItem_list[word] = VocabularyItem(word)
        self.VocabularyItem_list[word].add_count(adding_count=adding_count)

    def change_understanding_level(self, word, new_level):
        self.VocabularyItem_list[word].change_understanding_level(new_level)

    def print_list(self):
        for word in self.VocabularyItem_list:
            print(self.VocabularyItem_list[word].getTxt_word_info())

