

<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="py.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">PY-KINTER</h3>

  <p align="center">
   TKINTER SNAKE GAME WITH PROCEDURAL PYTHON
    <br />
  
  </p>
</p>


```code

Principes généraux
Déplacement d’un serpent sur une grille virtuelle dont chaque case est repérable de 3
manières différentes : le numéro de la case dans l’ordre gauche/droite et haut/bas, les
numéros de ligne et de colonne de la case, les coordonnées x et y du coin supérieur gauche
de la case.

description complète : subject.pdf
fichier à utiliser : snake_pattern.py

```

#### Contrainte imposée

```code 

Utilisation du fichier snake_pattern.py
respect des fonctions et de la structure du programme proposées
orgaisation des éléments du programme et ajouts dans les sections dédiées.

```

#### Structure du snake pattern

```js 

# Importations
from tkinter import *

# Constantes du monde

# variables globales serpent

# variables globales interface
fenApp = Tk()


# Fonctions coordonnées grille et direction (num_case = num_lig * nb_col + num_col)
def case_to_lc(num_case):
    pass


def lc_to_case(num_lig, num_col):
    pass


def case_to_xy(num_case):
    pass


def xy_to_case(x, y):
    pass


def xy_to_lc(x, y):
    pass


def lc_to_xy(num_lig, num_col):
    pass


def case_suivante(num_case, sens, nb_cases=1):  # sur un tore
    pass


def pivot_horaire(nb=1):
    pass


# callbacks
def quitter():
    pass


def reset():
    pass


def lancer(_):  # avec la barre espace
    pass


def tourne_gauche(_):  # flèche fauche ou bouton gauche souris
    pass


def tourne_droite(_):  # flèche droite ou bouton droite souris
    pass


# Construction graphique du jeu
def peuble_frames(fen):
    pass


def peuple_gestion(fen):
    pass


def peuple_jeu(fen):
    pass


def peuple_score(fen):
    pass


def reset_interface():
    pass


def build_interface():
    fenApp.title("Petit snake 2020")
    peuble_frames(fenApp)


# Initialisations des variables globales
def init_globals():
    pass


# Construction du serpent
def init_serpent():
    pass


def avance():
    pass


def test_fonctions():
    pass


if __name__ == "__main__":
    test_fonctions()
    build_interface()
    fenApp.mainloop()


```
