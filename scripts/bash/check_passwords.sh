#!/bin/bash
# check_password.sh
# Ce script vérifie la robustesse d'un mot de passe en contrôlant sa longueur et sa complexité.

read -sp "Entrez le mot de passe à vérifier : " password
echo

# Vérification de la longueur minimale (8 caractères)
if [ ${#password} -lt 8 ]; then
    echo "Erreur : Le mot de passe doit contenir au moins 8 caractères."
    exit 1
fi

# Vérification de la présence d'une majuscule, minuscule, chiffre et caractère spécial
if ! [[ "$password" =~ [A-Z] ]]; then
    echo "Erreur : Le mot de passe doit contenir au moins une lettre majuscule."
    exit 1
fi

if ! [[ "$password" =~ [a-z] ]]; then
    echo "Erreur : Le mot de passe doit contenir au moins une lettre minuscule."
    exit 1
fi

if ! [[ "$password" =~ [0-9] ]]; then
    echo "Erreur : Le mot de passe doit contenir au moins un chiffre."
    exit 1
fi

if ! [[ "$password" =~ [\!\@\#\$\%\^\&\*\(\)\_\+\-=\{\}\[\]\:\;\"\'\<\>\,\.\?\/] ]]; then
    echo "Erreur : Le mot de passe doit contenir au moins un caractère spécial."
    exit 1
fi

echo "Le mot de passe respecte les exigences de sécurité."
