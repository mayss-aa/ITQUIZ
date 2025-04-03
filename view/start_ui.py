import tkinter as tk
from model.question import Question
from controller.quiz_controller import QuizController
from view.quiz_ui import QuizInterface
from database.score_db import save_score, get_top_scores, get_all_scores

class StartUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ITQUIZ - Accueil")
        self.window.geometry("420x480")
        self.window.config(bg="#2c3e50")

        self.level_var = tk.StringVar(value="debutant")
        self.player1_var = tk.StringVar()
        self.player2_var = tk.StringVar()

        tk.Label(self.window, text="🎮 ITQUIZ", font=("Segoe UI", 20), bg="#2c3e50", fg="white").pack(pady=10)
        tk.Label(self.window, text="Choisissez un niveau :", bg="#2c3e50", fg="white").pack()

        levels = [("Débutant", "debutant"), ("Intermédiaire", "intermediaire"), ("Difficile", "difficile")]
        for text, value in levels:
            tk.Radiobutton(self.window, text=text, variable=self.level_var, value=value, bg="#2c3e50", fg="white").pack()

        tk.Label(self.window, text="Nom du joueur 1 :", bg="#2c3e50", fg="white").pack(pady=(10, 0))
        tk.Entry(self.window, textvariable=self.player1_var).pack()

        tk.Label(self.window, text="Nom du joueur 2 :", bg="#2c3e50", fg="white").pack(pady=(10, 0))
        tk.Entry(self.window, textvariable=self.player2_var).pack()

        tk.Button(self.window, text="Démarrer le Quiz", bg="#27ae60", fg="white", command=self.start_game).pack(pady=10)
        tk.Button(self.window, text="📊 Voir le classement", bg="#2980b9", fg="white", command=self.show_scores).pack()

        self.window.mainloop()

    def start_game(self):
        level = self.level_var.get()
        p1 = self.player1_var.get()
        p2 = self.player2_var.get()

        if not p1 or not p2:
            return

        self.players = [p1, p2]
        self.selected_level = level
        self.questions = self.get_questions_by_level(level)
        self.index = 0
        self.scores = []
        self.window.destroy()
        self.launch_player()

    def launch_player(self):
        if self.index < len(self.players):
            question_bank = [Question(q["text"], q["answer"], q["explanation"]) for q in self.questions]
            quiz = QuizController(question_bank)
            QuizInterface(quiz, self.players[self.index], self.selected_level,
                          self.next_player if self.index == 0 else self.show_winner, is_last=self.index == 1)

    def next_player(self, score):
        self.scores.append(score)
        self.index += 1
        self.launch_player()

    def show_winner(self, score):
        self.scores.append(score)
        result = tk.Tk()
        result.title("Résultat final")
        result.geometry("400x350")
        result.config(bg="#1e1e2f")

        p1, p2 = self.players
        s1, s2 = self.scores

        if s1 > s2:
            winner = p1
        elif s2 > s1:
            winner = p2
        else:
            winner = "Égalité !"

        if winner != "Égalité !":
            save_score(winner, max(s1, s2), self.selected_level)

        msg = f"🏁 {p1} : {s1} points\n{p2} : {s2} points\n\n🎉 Gagnant : {winner}"
        tk.Label(result, text=msg, bg="#1e1e2f", fg="white", font=("Segoe UI", 12)).pack(pady=20)

        tk.Button(result, text="🔁 Rejouer", command=lambda: [result.destroy(), StartUI()], bg="#27ae60", fg="white").pack(pady=5)
        tk.Button(result, text="📊 Classement", command=self.show_scores, bg="#2980b9", fg="white").pack(pady=5)
        tk.Button(result, text="❌ Quitter", command=result.destroy, bg="#c0392b", fg="white").pack(pady=5)


    def get_questions_by_level(self,level):
        if level == "debutant":
            return [
                {"text": "Python est un langage interprété.", "answer": "true", "explanation": "Python est interprété."},
                {"text": "HTML est un langage de programmation.", "answer": "false", "explanation": "C'est un langage de balisage."},
                {"text": "C est un langage bas niveau.", "answer": "false", "explanation": "C est un langage de bas niveau intermédiaire."},
                {"text": "CSS permet de structurer les données.", "answer": "false", "explanation": "CSS sert à styliser, pas structurer."},
                {"text": "Python utilise l'indentation pour les blocs.", "answer": "true", "explanation": "L'indentation est obligatoire en Python."},
                {"text": "Un algorithme est une suite d'étapes logiques.", "answer": "true", "explanation": "Il sert à résoudre un problème."},
                {"text": "Un fichier HTML finit souvent par .py", "answer": "false", "explanation": "Il finit par .html"},
                {"text": "C++ est orienté objet.", "answer": "true", "explanation": "C++ supporte l’OOP."},
                {"text": "print() permet d'afficher un résultat en Python.", "answer": "true", "explanation": "C’est la fonction d’affichage."},
                {"text": "La RAM est une mémoire permanente.", "answer": "false", "explanation": "La RAM est volatile."}
            ]
        elif level == "intermediaire":
            return [
                {"text": "JavaScript et Java sont le même langage.", "answer": "false", "explanation": "Ils sont différents."},
                {"text": "SQL est utilisé pour interroger une base de données.", "answer": "true", "explanation": "C’est son but principal."},
                {"text": "Un commit Git modifie le dépôt distant.", "answer": "false", "explanation": "Il modifie le dépôt local."},
                {"text": "Flask est un framework Python.", "answer": "true", "explanation": "Utilisé pour le développement web."},
                {"text": "Un tableau commence toujours à l’index 1.", "answer": "false", "explanation": "Il commence à 0."},
                {"text": "HTTP est un protocole.", "answer": "true", "explanation": "Il permet la communication web."},
                {"text": "CSS signifie Computer Style Sheet.", "answer": "false", "explanation": "Cascading Style Sheets."},
                {"text": "La balise <a> crée un lien en HTML.", "answer": "true", "explanation": "Elle permet de créer un hyperlien."},
                {"text": "Python est compilé comme C.", "answer": "false", "explanation": "Il est interprété."},
                {"text": "Un IDE est un environnement de développement.", "answer": "true", "explanation": "IDE = Integrated Development Environment."}
            ]
        elif level == "difficile":
            return [
                {"text": "async/await en Python est utilisé pour le multithreading.", "answer": "false", "explanation": "C’est pour l’asynchrone."},
                {"text": "Django est plus complet que Flask.", "answer": "true", "explanation": "Il est full-stack."},
                {"text": "Big O exprime la complexité mémoire.", "answer": "false", "explanation": "Elle exprime la complexité en temps."},
                {"text": "Python peut être compilé en bytecode.", "answer": "true", "explanation": "Les fichiers .pyc en sont la preuve."},
                {"text": "TCP est un protocole fiable.", "answer": "true", "explanation": "Il garantit l'ordre et l'arrivée."},
                {"text": "Linux est un système d'exploitation.", "answer": "true", "explanation": "Il est open source et très utilisé."},
                {"text": "Un fichier JSON est un format de base de données.", "answer": "false", "explanation": "C’est un format de données, pas une base."},
                {"text": "L'algorithme de Dijkstra est utilisé pour trier.", "answer": "false", "explanation": "Il est utilisé pour les graphes."},
                {"text": "Un DNS traduit les noms de domaine.", "answer": "true", "explanation": "Il retourne une adresse IP."},
                {"text": "La programmation orientée objet repose sur des objets.", "answer": "true", "explanation": "Elle modélise des entités logiques."}
            ]
        return []
    def show_scores(self):
        score_window = tk.Toplevel()
        score_window.title("🏆 Classement et historique")
        score_window.geometry("500x400")
        score_window.config(bg="#1e1e2f")

        tk.Label(score_window, text="🎯 Top 5 joueurs :", font=("Segoe UI", 14), fg="white", bg="#1e1e2f").pack(pady=10)
        for user, score, level, date in get_top_scores():
            tk.Label(score_window, text=f"{user} - {score} pts ({level}) - {date}", fg="white", bg="#1e1e2f").pack()

        tk.Label(score_window, text="🕓 Historique :", font=("Segoe UI", 12), fg="white", bg="#1e1e2f").pack(pady=10)
        for user, score, level, date in get_all_scores():
            tk.Label(score_window, text=f"{user} - {score} pts ({level}) - {date}", fg="white", bg="#1e1e2f").pack()

        tk.Button(score_window, text="Fermer", command=score_window.destroy).pack(pady=20)


# 🔽 Intégré automatiquement depuis questions_by_level.py
