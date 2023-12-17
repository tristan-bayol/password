import string
import hashlib
import json
import random

longueur = 8
majuscules = set(string.ascii_uppercase)
minuscules = set(string.ascii_lowercase)
chiffres = set(string.digits)
speciaux = set(string.punctuation)

mdp_json = "d:/WebDev/Projet/password/motdepass.json"

def user_choice():
    while True:
        choix = input("Que souhaitez-vous faire ? Choix 1 pour ajouter un mot de passe, choix 2 pour afficher ces derniers, choix 3 pour générer un mot de passe aléatoire : ")

        if choix == '1':
            new_password()
        elif choix == '2':
            read_password()
        elif choix == '3':
            generate_random_password()
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

def new_password():
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
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            print("Mot de passe valide!")
            print("Mot de passe crypté avec SHA-256 :", hashed_password)

            passwords_list = read_passwords_from_file()
            if not password_exists(hashed_password, passwords_list):
                passwords_list.append({"password_hache": hashed_password})
                write_passwords_to_file(passwords_list)
                break
            else:
                print("Ce mot de passe existe déjà. Veuillez en choisir un autre.")
        else:
            print("Mot de passe invalide. Assurez-vous d'avoir :", ", ".join(conditions_manquantes))

def password_exists(new_hashed_password, passwords_list):
    existing_hashes = [entry.get("password_hache", "") for entry in passwords_list]
    return new_hashed_password in existing_hashes

def read_password():
    passwords_list = read_passwords_from_file()
    
    if not passwords_list:
        print("Aucun mot de passe enregistré.")
    else:
        for index, password in enumerate(passwords_list, start=1):
            print(f"{index}. Mot de passe crypté avec SHA-256 : {password['password_hache']}")

def read_passwords_from_file():
    try:
        with open(mdp_json, "r") as json_file:
            passwords_list = json.load(json_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        passwords_list = []
    return passwords_list

def write_passwords_to_file(passwords_list):
    with open(mdp_json, "w") as json_file:
        json.dump(passwords_list, json_file, indent=2)


def generate_random_password():
    password = generate_valid_random_password()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    print("Mot de passe généré avec succès!")
    print("Mot de passe généré :", password)
    print("Mot de passe crypté avec SHA-256 :", hashed_password)

    passwords_list = read_passwords_from_file()
    passwords_list.append({"password_hache": hashed_password})
    write_passwords_to_file(passwords_list)

def generate_valid_random_password():
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longueur))
        if (
            any(c in majuscules for c in password) and
            any(c in minuscules for c in password) and
            any(c in chiffres for c in password) and
            any(c in speciaux for c in password)
        ):
            return password


user_choice()
