# Calculateur de Suite de Fibonacci avec Mémorisation

Ce projet implémente un calculateur de nombres de Fibonacci utilisant la technique de mémorisation (memoization) pour optimiser les performances.

## Description

Le fichier `main.py` contient deux éléments principaux :

1. **Classe Value**
   - Gère la persistance des données via un fichier JSON
   - Charge et sauvegarde automatiquement les résultats calculés
   - Utilise `value.json` comme fichier de stockage

2. **Fonction fibo**
   - Calcule le n-ième nombre de la suite de Fibonacci
   - Utilise la mémorisation pour éviter les calculs redondants
   - Stocke les résultats intermédiaires dans un fichier JSON

## Fonctionnement

Le programme utilise une approche récursive avec mémorisation pour calculer les nombres de Fibonacci. Les résultats déjà calculés sont stockés dans un fichier JSON pour éviter de recalculer les mêmes valeurs lors des prochaines exécutions.

## Utilisation

```python
from main import Value, fibo

# Créer une instance de Value pour la mémorisation
memory = Value()

# Calculer le 10ème nombre de Fibonacci
result = fibo(10, memory)

print(result)
```

Ce code calculera le 10ème nombre de Fibonacci et affichera le résultat. Les résultats intermédiaires seront stockés dans le fichier `value.json` pour une utilisation future.