class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_li = q_list

    def next_question(self):
        current_question = self.question_li[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question n. {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else: 
            print("Wrong answer!")
        print(f"Correct answer is: {correct_answer}.")
        print(f"Your score is: {self.score} / {self.question_number}")

    def has_question(self):
        if self.question_number < len(self.question_li):
            return True
        else:
            return False
   
        