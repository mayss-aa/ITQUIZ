import tkinter as tk
from functools import partial

class QuizInterface:
    def __init__(self, controller, player_name, level, on_complete, is_last=False):
        self.controller = controller
        self.player_name = player_name
        self.level = level
        self.on_complete = on_complete
        self.is_last = is_last

        self.window = tk.Tk()
        self.window.title(f"Quiz - {self.player_name}")
        self.window.geometry("600x400")
        self.window.config(bg="#1e1e2f")

        self.score_label = tk.Label(self.window, text="Score: 0", font=("Segoe UI", 12), fg="white", bg="#1e1e2f")
        self.score_label.pack(pady=10)

        self.question_text = tk.Label(self.window, text="", wraplength=500, font=("Segoe UI", 14), fg="white", bg="#1e1e2f", justify="center")
        self.question_text.pack(pady=20)

        self.feedback_label = tk.Label(self.window, text="", font=("Segoe UI", 10, "italic"), fg="#00b894", bg="#1e1e2f")
        self.feedback_label.pack()

        self.true_button = tk.Button(self.window, text="✔ Vrai", command=partial(self.submit_answer, "true"))
        self.true_button.pack(side="left", expand=True, padx=20)

        self.false_button = tk.Button(self.window, text="✖ Faux", command=partial(self.submit_answer, "false"))
        self.false_button.pack(side="right", expand=True, padx=20)

        self.result_label = tk.Label(self.window, bg="#1e1e2f", fg="white", font=("Segoe UI", 14))
        self.result_label.pack(pady=20)

        self.display_next_question()
        self.window.mainloop()

    def display_next_question(self):
        self.feedback_label.config(text="")
        if self.controller.has_more_questions():
            q = self.controller.next_question()
            self.question_text.config(text=q.text)
        else:
            self.end_quiz()

    def submit_answer(self, answer):
        correct, explanation = self.controller.check_answer(answer)
        if correct:
            self.controller.score += 1
            self.feedback_label.config(text="✅ Bonne réponse ! " + explanation)
        else:
            self.feedback_label.config(text="❌ Mauvaise réponse ! " + explanation)
        self.score_label.config(text=f"Score: {self.controller.score}")
        self.window.after(1200, self.display_next_question)

    def end_quiz(self):
        self.true_button.pack_forget()
        self.false_button.pack_forget()
        self.question_text.pack_forget()
        self.feedback_label.pack_forget()
        self.result_label.config(
            text=f"🏁 Fin du quiz\n{self.player_name} : {self.controller.score} points")

        btn_text = "Voir le résultat final" if self.is_last else "➡ Passer au joueur suivant"
        tk.Button(self.window, text=btn_text, command=self.quit_and_continue).pack(pady=20)

    def quit_and_continue(self):
        self.window.destroy()
        self.on_complete(self.controller.score)
