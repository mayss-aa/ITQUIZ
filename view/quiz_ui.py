
import tkinter as tk
from tkinter import PhotoImage
import os

class QuizInterface:
    def __init__(self, controller, start_window):
        self.controller = controller
        self.start_window = start_window
        self.start_window.destroy()

        self.time_left = 10
        self.timer_id = None

        self.window = tk.Tk()
        self.window.title("Coding Languages Quiz")
        self.window.geometry("700x500")
        self.window.config(bg="#1e1e2f")

        for i in range(6):
            self.window.rowconfigure(i, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        self.score_label = tk.Label(text="Score: 0", font=("Segoe UI", 12, "bold"),
                                    fg="#ffffff", bg="#1e1e2f")
        self.score_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)

        self.timer_label = tk.Label(text="Time: 10", font=("Segoe UI", 12, "bold"),
                                    fg="#ff5757", bg="#1e1e2f")
        self.timer_label.grid(row=0, column=1, sticky="e", padx=20, pady=10)

        self.question_text = tk.Label(text="", wraplength=600,
                                      font=("Segoe UI", 16),
                                      fg="#ffffff", bg="#1e1e2f", justify="center")
        self.question_text.grid(row=1, column=0, columnspan=2, pady=20, sticky="nsew")

        self.feedback_label = tk.Label(text="", font=("Segoe UI", 11, "italic"),
                                       fg="#00b894", bg="#1e1e2f", wraplength=600)
        self.feedback_label.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.true_button = tk.Button(text="✔ True", width=15,
                                     font=("Segoe UI", 12, "bold"),
                                     bg="#27ae60", fg="white", bd=0,
                                     activebackground="#219653",
                                     command=lambda: self.submit_answer("true"))
        self.true_button.grid(row=3, column=0, pady=15)

        self.false_button = tk.Button(text="✖ False", width=15,
                                      font=("Segoe UI", 12, "bold"),
                                      bg="#c0392b", fg="white", bd=0,
                                      activebackground="#e74c3c",
                                      command=lambda: self.submit_answer("false"))
        self.false_button.grid(row=3, column=1, pady=15)

        self.result_image_label = tk.Label(bg="#1e1e2f")
        self.end_message = tk.Label(bg="#1e1e2f", fg="white", font=("Segoe UI", 16, "bold"))
        self.final_score = tk.Label(bg="#1e1e2f", fg="white", font=("Segoe UI", 14, "italic"))
        self.return_button = tk.Button(text="↩ Retour à l'accueil", command=self.return_home,
                                       bg="#2980b9", fg="white", font=("Segoe UI", 11, "bold"))
        self.quit_button = tk.Button(text="❌ Quitter", command=self.window.destroy,
                                     bg="#e74c3c", fg="white", font=("Segoe UI", 11, "bold"))

        self.display_next_question()
        self.window.mainloop()

    def display_next_question(self):
        self.feedback_label.config(text="", fg="#00b894")
        if self.controller.has_more_questions():
            q = self.controller.next_question()
            self.question_text.config(text=q.text)
            self.reset_timer()
        else:
            self.end_quiz()

    def submit_answer(self, answer):
        if self.timer_id:
            self.window.after_cancel(self.timer_id)
        correct, explanation = self.controller.check_answer(answer)
        if correct:
            self.controller.score += 1
            self.score_label.config(text=f"Score: {self.controller.score}")
            self.feedback_label.config(text="✅ Correct! " + explanation, fg="#2ecc71")
        else:
            self.feedback_label.config(text="❌ Incorrect! " + explanation, fg="#e74c3c")

        if self.controller.has_more_questions():
            self.window.after(2000, self.display_next_question)
        else:
            self.window.after(2000, self.end_quiz)

    def reset_timer(self):
        self.time_left = 10
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Time: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.window.after(1000, self.update_timer)
        else:
            self.feedback_label.config(text="⏰ Temps écoulé !", fg="#f39c12")
            self.window.after(1500, self.end_quiz)

    def end_quiz(self):
        self.true_button.grid_forget()
        self.false_button.grid_forget()
        self.timer_label.grid_forget()
        self.score_label.grid_forget()
        self.feedback_label.grid_forget()
        self.question_text.grid_forget()

        self.result_image_label.grid(row=0, column=0, columnspan=2)
        self.end_message.grid(row=1, column=0, columnspan=2, sticky="n", pady=10)
        self.final_score.grid(row=2, column=0, columnspan=2, pady=5)
        self.return_button.grid(row=3, column=0, pady=20)
        self.quit_button.grid(row=3, column=1, pady=20)

        assets_path = os.path.join(os.path.dirname(__file__), "..", "assets")
        if self.controller.score > 6:
            result_img = PhotoImage(file=os.path.join(assets_path, "bravo.png"))
            self.end_message.config(text="🏆 Bravo !", fg="#2ecc71")
        else:
            result_img = PhotoImage(file=os.path.join(assets_path, "retry.png"))
            self.end_message.config(text="❌ Refaire le quiz", fg="#e74c3c")

        self.final_score.config(text=f"Score final : {self.controller.score}")
        self.result_image_label.config(image=result_img)
        self.result_image_label.image = result_img

    def return_home(self):
        self.window.destroy()
        from main import start_quiz_window
        start_quiz_window()
