import string
import hashlib

longueur = 8
majuscules = set(string.ascii_uppercase)
minuscules = set(string.ascii_lowercase)
chiffres = set(string.digits)
speciaux = set(string.punctuation)

def user_choice():
    while True:
        choix = input("Que souhaitez-vous faire ? Choix 1 pour ajouter un mot de passe, choix 2 pour afficher ces derniers : ")

        if choix == '1':
            new_password()
        elif choix == '2':
            read_password()
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")

def new_password ():
    while True:
        password = input("Veuillez entrer votre mot de passe : ")

        conditions_manquantes = []

        # Vérification de la présence de caractères dans le mot de passe
        if len(password) < longueur:
            conditions_manquantes.append(f"une longueur d'au moins {longueur} caractères")
        if not any(c in majuscules for c in password):
            conditions_manquantes.append("au moins une majuscule")
        if not any(c in minuscules for c in password):
            conditions_manquantes.append("au moins une minuscule")
        if not any(c in chiffres for c in password):
            conditions_manquantes.append("au moins un chiffre")
        if not any(c in speciaux for c in password):
            conditions_manquantes.append("au moins un caractère spécial")

        if not conditions_manquantes:
            # Cryptage du mot de passe avec SHA-256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            print("Mot de passe valide!")
            print("Mot de passe crypté avec SHA-256 :", hashed_password)
            break  # Sort de la boucle si le mot de passe est valide
        else:
            print("Mot de passe invalide. Assurez-vous d'avoir :", ", ".join(conditions_manquantes))

def read_password():
    # Fonction a écrire
    pass


user_choice()