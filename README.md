# README - TP MULTITHREADING 

---
Membres du binôme : <br>
SAÏDI Rahim <br>
COULIBALY Nahaclan Maxime 

---

Ce dépôt a été créé dans le cadre des enseignements de l'UPSSITECH : TP multi threading
Les TPs ont été découpés en 4 séances. 

### **Séance 1** 
* La première consiste à explorer les fonctionnalités de git et de uv. 
* Création et configuration d'un dépot distant
* Configuration de l'environnement avec uv (fichier de precommit par exemple puis les differentes commandes de uv)

### **Séance 2**
La deuxieme consiste à implementer une architecture pour réaliser des taches en multiprocessing.
Un objet Queue_manager (voir QM.py) possède deux listes, une liste de tâches à réaliser et une liste de taches réalisées. 
Un objet boss peut ajouter des tâches à réaliser et récupérer les taches accomplies. 
Enfin un ou plusieurs objet Minions récupère dans les première liste, une tâche qu'il va réaliser avant de l'ajouter a la seconde liste. 
Ce procédé permet d'avoir plusieurs Minions qui réalisent differentes tâches en parallèle. 

### **Séance 3 et 4**
Les deux dernieres séances consistent à implementer la classe task en C++ ainsi qu'un moyen de communiquer entre le C++ et le Python
La communication entre les codes de differents langages se fais via un proxy et en utilisant le format de données JSON.
La classe Task en C++ réalise les mêmes fonctions que la classe en python, ceci permet ainsi de comparer les deux langages.

# **Objectif global des trois dernières séances**

le but de ce projet est de comparer les temps d'exécution des tâches effectuées dans deux langages : C++ et Python. Les tâches à effectuer sont des tâches de calcul matriciel qui  consistent à résoudre un système d'équations linéaires de la forme `Ax = B`, où `A` est une matrice carrée générée aléatoirement, et `B` est un vecteur.

# **Instruction d'exécution**

### **Python :**  
Réaliser les actions suivantes dans différents terminaux : 
1. Lancer le Queue Manager 
```bash
python QM.py
```
2. Lancer le(s) Boss
 ```bash
python boss.py
```

3. Lancer le(s) Minion(s)
 ```bash
python minions.py
```
---
### **C++** : 
Réaliser les actions suivantes dans différents terminaux : 
1. Lancer le Queue Manager 
```bash
python QM.py
```
2. Lancer le proxy 
 ```bash
python proxy.py
```
3. Lancer le(s) Boss
 ```bash
python boss.py

# **Tests de performance**
```
4. Lancer le "Minion C++"
 ```bash
./build/low_level
```
# **Tests et performances**

e
