class text:
    def __init__(self):
        self.file_add = ""
        self.s = ""
        self.m = {}

    def getTextFromFile(self,file_add):
        f = open(file_add, encoding="utf8")
        self.file_add = file_add
        self.s = f.read()

    def splitText(self):
        punctuation_list = ",.!?:; \"“”-_\'(){}[]\n#1234567890$+-*/—%’‘"
        s = self.s
        for p in punctuation_list:
            s=s.replace(p,",")
        word_list = s.split(",")
        for word in word_list:
            if (word==""):
                continue
            word = word.lower()
            if word in self.m:
                self.m[word] += 1
            else:
                self.m[word] = 1

    def printWordList_wordList(self,reverse=False):
        pairs_keys = []
        for key in self.m:
            pairs_keys.append([key, self.m[key]])
        pairs_keys.sort(reverse = reverse)
        print(pairs_keys)

    def printWordList_Rank(self,reverse=False):
        pairs_values = []
        for key in self.m:
            pairs_values.append([self.m[key], key])
        pairs_values.sort(reverse = not reverse)
        print(pairs_values)

    # def save(self, save_add):
    # def load(self, load_add, b_load_str=False):


folder_name = r"C:\Users\s\Google Drive\s\dropbox_extention\helprobot_20200813\help_vocabulary_20200813\text_data\pride_and_prejudice"
# file_name = "chapter_1.txt"
file_name = "full_text.txt"

file_add = folder_name + "\\" + file_name
t = text()
t.getTextFromFile(file_add)
t.splitText()
t.printWordList_wordList()
t.printWordList_wordList(reverse=True)
t.printWordList_Rank()
t.printWordList_Rank(reverse=True)
