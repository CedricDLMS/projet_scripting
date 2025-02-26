#!/usr/bin/env python3
"""
analyse_scan.py
Ce script analyse le fichier de résultats généré par nmap et affiche les ports ouverts et les services associés.
"""

import re
import sys

if len(sys.argv) != 2:
    print("Usage: {} <fichier_scan>".format(sys.argv[0]))
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Fichier {} non trouvé.".format(file_path))
    sys.exit(1)

# Expression régulière pour extraire les lignes indiquant un port ouvert
pattern = re.compile(r'^(\d+)/tcp\s+open\s+(\S+)', re.MULTILINE)

print("Analyse des résultats du scan :")
for match in pattern.finditer(content):
    port = match.group(1)
    service = match.group(2)
    print("Port {} ouvert : service {}".format(port, service))
