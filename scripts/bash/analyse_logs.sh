#!/bin/bash
# analyse_logs.sh
# Ce script surveille le fichier /var/log/auth.log pour afficher les 10 dernières tentatives de connexion échouées.

LOG_FILE="/var/log/auth.log"

if [ ! -f "$LOG_FILE" ]; then
    echo "Erreur : Le fichier $LOG_FILE n'existe pas."
    exit 1
fi

echo "Affichage des 10 dernières tentatives de connexion échouées :"
grep "Failed password" $LOG_FILE | tail -n 10
