from model.question import Question
from controller.quiz_controller import QuizController
from view.quiz_ui import QuizInterface
import tkinter as tk

def start_quiz_window():
    window = tk.Tk()
    window.title("ITQUIZ - Bienvenue")
    window.geometry("400x300")
    window.config(bg="#2c3e50")

    title = tk.Label(window, text="🎓 Bienvenue sur ITQUIZ", font=("Segoe UI", 16, "bold"), fg="white", bg="#2c3e50")
    title.pack(pady=30)

    info = tk.Label(window, text="Choisissez un niveau :", font=("Segoe UI", 12), fg="white", bg="#2c3e50")
    info.pack()

    def start_quiz(level):
        question_data = get_questions_by_level(level)
        question_bank = [Question(q["text"], q["answer"], q["explanation"]) for q in question_data]
        quiz = QuizController(question_bank)
        QuizInterface(quiz, window)

    tk.Button(window, text="Débutant", command=lambda: start_quiz("debutant"), width=20, bg="#27ae60", fg="white").pack(pady=10)
    tk.Button(window, text="Intermédiaire", command=lambda: start_quiz("intermediaire"), width=20, bg="#f39c12", fg="white").pack(pady=5)
    tk.Button(window, text="Difficile", command=lambda: start_quiz("difficile"), width=20, bg="#e74c3c", fg="white").pack(pady=5)

    window.mainloop()

def get_questions_by_level(level):
    if level == "debutant":
        return [
            {"text": "Python utilise l'indentation pour définir les blocs.", "answer": "true", "explanation": "C'est la base de la syntaxe Python."},
            {"text": "HTML est un langage de programmation.", "answer": "false", "explanation": "HTML est un langage de balisage."},
            {"text": "2 + 2 = 4", "answer": "true", "explanation": "C'est une addition simple !"},
            {"text": "CSS sert à structurer le contenu.", "answer": "false", "explanation": "CSS sert au style, pas à la structure."},
            {"text": "Un booléen peut être vrai ou faux.", "answer": "true", "explanation": "True / False, typique en logique."},
            {"text": "En C, on écrit les fonctions sans point-virgule.", "answer": "false", "explanation": "Chaque instruction doit se terminer par ;"},
            {"text": "JavaScript s’exécute côté serveur.", "answer": "false", "explanation": "Il s’exécute côté client (navigateur)."},
            {"text": "PHP est utilisé pour créer des pages dynamiques.", "answer": "true", "explanation": "Il est souvent utilisé côté serveur."}
        ]
    elif level == "intermediaire":
        return [
            {"text": "Python est un langage compilé.", "answer": "false", "explanation": "Python est interprété."},
            {"text": "Java est fortement typé.", "answer": "true", "explanation": "Tu dois déclarer les types."},
            {"text": "Un tableau en C peut changer de taille.", "answer": "false", "explanation": "Les tableaux C sont de taille fixe."},
            {"text": "Un script PHP commence par <?php", "answer": "true", "explanation": "C'est la balise d'ouverture PHP."},
            {"text": "Les fonctions JavaScript peuvent être stockées dans des variables.", "answer": "true", "explanation": "JS supporte les fonctions anonymes."},
            {"text": "Le CSS s'écrit dans des balises <style> uniquement.", "answer": "false", "explanation": "On peut aussi l’écrire en fichiers externes."},
            {"text": "La division entière de 5 // 2 donne 2 en Python.", "answer": "true", "explanation": "// signifie division entière."},
            {"text": "MySQL est un langage.", "answer": "false", "explanation": "C'est un système de gestion de base de données."}
        ]
    elif level == "difficile":
        return [
            {"text": "Le garbage collector existe en C.", "answer": "false", "explanation": "C est bas niveau, pas de GC."},
            {"text": "Le polymorphisme est un concept POO.", "answer": "true", "explanation": "C'est une base de la POO."},
            {"text": "HTML5 supporte les balises audio et vidéo.", "answer": "true", "explanation": "Elles ont été introduites en HTML5."},
            {"text": "Python supporte l’héritage multiple.", "answer": "true", "explanation": "Contrairement à Java, Python le permet."},
            {"text": "Une API REST utilise uniquement POST.", "answer": "false", "explanation": "Elle utilise aussi GET, PUT, DELETE…"},
            {"text": "L’opérateur == vérifie la référence mémoire en Java.", "answer": "true", "explanation": "Il compare les références, pas les contenus."},
            {"text": "Le DOM est une structure utilisée côté client.", "answer": "true", "explanation": "DOM = Document Object Model dans le navigateur."},
            {"text": "Un commit Git modifie directement le dépôt distant.", "answer": "false", "explanation": "Il reste local jusqu’à un push."}
        ]
    return []

start_quiz_window()
