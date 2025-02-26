#!/usr/bin/env python3
"""
analyse_logs.py
Ce script analyse le fichier /var/log/auth.log pour regrouper les tentatives de connexion échouées par adresse IP.
"""

import re
from collections import defaultdict

log_file = "/var/log/auth.log"
failed_attempts = defaultdict(int)

try:
    with open(log_file, "r") as f:
        for line in f:
            if "Failed password" in line:
                # Extraction de l'adresse IP
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1
except FileNotFoundError:
    print("Erreur : Le fichier {} n'a pas été trouvé.".format(log_file))
    exit(1)

print("Tentatives de connexion échouées par IP :")
for ip, count in failed_attempts.items():
    print("IP {} : {} tentative(s)".format(ip, count))

# Générer une alerte pour une IP ayant plus de 5 échecs
print("\nAlertes potentielles :")
for ip, count in failed_attempts.items():
    if count > 5:
        print("Attention : L'IP {} présente {} tentatives échouées.".format(ip, count))
