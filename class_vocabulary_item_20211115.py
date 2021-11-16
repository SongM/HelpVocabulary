class vocabulary_item:
    def __init__(self, word):
        self.item_entry = word
        self.count = 0
        self.example_sentences = []

    def add_one_count(self, sentence):
        self.count = self.count + 1
        self.example_sentences.append(sentence)

    def print(self, example_sentence_i=0):
        print(self.item_entry + ': #count=' + str(self.count))
        if example_sentence_i<0:
            for s in self.example_sentences:
                print(s)
        else:
            s = self.example_sentences[example_sentence_i]
            print(s)