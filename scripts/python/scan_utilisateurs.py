#!/usr/bin/env python3
"""
scan_unused_users.py
Ce script analyse les utilisateurs du système et détecte ceux qui n'ont pas un shell de connexion interactif.
"""

import pwd

# Liste des shells non interactifs (souvent utilisés pour les comptes système ou inactifs)
non_interactive_shells = ["/usr/sbin/nologin", "/bin/false"]

print("Utilisateurs avec des shells non interactifs (potentiellement inutiles) :")
for user in pwd.getpwall():
    # On considère uniquement les comptes utilisateurs normaux (UID >= 1000)
    if user.pw_uid >= 1000 and user.pw_shell in non_interactive_shells:
        print("Utilisateur : {:20s} | Shell : {}".format(user.pw_name, user.pw_shell))
