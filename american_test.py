# input file format: question begins with big 'Q.'
#                    answers section starts with big 'A.'
#                    first answer is the good one, they would be shuffled on output
#                    between answers: ';'
# input parsed into: preamble, q&a, last words variants
# internal format: dict{question 1: list[answers of 1], ...}
import random
import docx2txt
from db_manager import DbManager as db


class AmericanTest:
    def __init__(self, path):
        self.data = self.word_reader(path)
        self.copy = self.data.copy()
        self.corrects = {question: answer[0] for question, answer in zip(self.data.copy(), self.copy.values())}
        self.answers = []
        self.id = {}

    def word_reader(self, path):
        data = {}
        file = docx2txt.process(path)
        sections = file.split('Q.')[1:]
        for section in sections:
            question, answer_sect = section.split('A.')
            answers = answer_sect.split(';')
            data[question] = answers
        return data

    def welcome(self):
        print("welcome to American-Test!")
        self.id['name'] = input("please enter your name")
        self.id['age'] = input("please enter your age")

    def test(self):
        for question in self.data:
            print(question)
            random.shuffle(self.data[question])
            print('\n'.join('{}: {}'.format(*k) for k in enumerate(self.data[question], start=1)))
            answer = int(input("you answer: 1/2/3..."))-1
            if 0 <= answer <= len(self.data[question]):
                if self.data[question][answer] == self.corrects[question]:
                    self.answers.append(answer)

    def evaluate(self):
        print(f" {self.id['name']}!you have being right in "+str(len(self.answers))
              + " times out of"+str(len(self.corrects)))

    def save(self):
        saver = db()
        saver.save_result(self.id['name'], self.id['age'], len(self.answers))

    def run(self):
        self.welcome()
        self.test()
        self.evaluate()
        self.save()



