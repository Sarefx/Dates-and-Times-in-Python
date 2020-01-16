import datetime
import random

from questions import Add, Multiply

class Quiz:
    questions = []
    answers = []

    def __init__(self, questions_quantity, number_range):
        questions_types = (Add, Multiply)
        # generate questions_quantity random questions with numbers from 1 to number_range
        for _ in range(questions_quantity):  # underscore just counts to questions_quantity without storing the value anywhere
            num1 = random.randint(1, number_range)
            num2 = random.randint(1, number_range)
            question = random.choice(questions_types)(num1, num2)
            # add these qs into self.questions
            self.questions.append(question)
    
    def take_quiz(self):
        # log the start time
        self.start_time = datetime.datetime.now()

        # ask all of the questions
        for question in self.questions:
            # log if they got the questions right
            self.answers.append(self.ask(question))
        else:
            # log the end time
            self.end_time = datetime.datetime.now()  # else is here for when for loop ends it goes to else
        
        # show a summary
        return self.summary()

    def ask(self, question):
        correct = False
        # log the start time
        question_start = datetime.datetime.now()
        # capture the answer
        answer = input(question.text + " = ")

        # check the answer
        if answer == str(question.answer):
            correct = True
        # log the end time
        question_end = datetime.datetime.now()

        print("It took you {} seconds to answer this question.".format((question_end - question_start).seconds))
        # if the answer's right, send back True
        # otherwise, send back False
        # send back the elapsed time, too
        return correct, question_end - question_start
        
    def total_correct(self):
        # return the total # of correct answers
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many you got right and the total # of questions, like 5/10
        print("You got {} out of {} right.".format(
            self.total_correct(), len(self.questions)
        ))
        # print the total time for the quiz: 30 seconds!
        print("It took you {} seconds total.".format(
            (self.end_time-self.start_time).seconds
        ))

Quiz(3, 3).take_quiz()

# additional suggestions/challenges:

# 1: Change the app so it takes a number of questions to generate.
# 1: solved

# 2: Make it so that a user can specify the range they want the numbers to come from.
# 2: solved

# 3: Or add in some further stats that tell you how long it took to answer each question.
# 3: solved
