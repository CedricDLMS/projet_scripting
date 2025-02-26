#!/bin/bash
# scan_ports.sh
# Ce script utilise nmap pour scanner un hôte ou un réseau et sauvegarder les résultats dans un fichier.

if [ -z "$1" ]; then
    echo "Usage: $0 <IP ou CIDR>"
    exit 1
fi

TARGET=$1
OUTPUT_FILE="nmap_scan_$(echo $TARGET | tr '/' '_').txt"

echo "Lancement du scan nmap sur $TARGET ..."
nmap -sV -O $TARGET -oN $OUTPUT_FILE

echo "Scan terminé. Les résultats sont sauvegardés dans $OUTPUT_FILE."
