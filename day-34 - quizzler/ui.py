from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text=f'Score: {self.quiz.score}', font=('Arial', 12), fg='white', background=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some question text',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
            )
        self.canvas.config()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=0)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.window.after(0, self.white)

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            score = self.quiz.score
            self.score.config(text=f'Score: {score}')
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of this quiz')
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.green()
            self.window.after(200, self.white)
            self.window.after(400, self.green)
            self.window.after(600, self.white)
            self.window.after(800, self.green)
            self.window.after(1000, self.white)
            self.window.after(1200, self.green)
        else:
            self.red()
            self.window.after(200, self.white)
            self.window.after(400, self.red)
            self.window.after(600, self.white)
            self.window.after(800, self.red)
            self.window.after(1000, self.white)
            self.window.after(1200, self.red)

        self.window.after(1400, self.get_next_question)
        # turns out only functions work and not one line codes
        # having events with same 'ms' value add them to the event que simultaneously, since window.mainloop() must
        # keep running and events with same delay time gets executed simultaneously since they were added so.
        # a delay between events must be stacked on the delay time as I did.

    def red(self):
        self.canvas.config(bg='red')

    def green(self):
        self.canvas.config(bg='green')

    def white(self):
        self.canvas.config(bg='white')
