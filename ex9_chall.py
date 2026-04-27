"""
Exercice 9 — Queue vs split manuel

L’utilisation de queue.Queue permet de distribuer le travail
entre les threads de manière sûre.

Chaque appel à queue.get() est atomique :
un mot de passe ne peut être récupéré que par un seul thread.

Cela permet :
- d’éviter les doublons
- d’éviter les race conditions
- d’avoir un bon équilibrage de charge

Le découpage manuel en morceaux statiques est moins efficace car :
- la charge n’est pas équilibrée
- l’arrêt anticipé est difficile
- la gestion est plus complexe
"""