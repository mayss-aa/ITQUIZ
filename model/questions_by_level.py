def get_questions_by_level(level):
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