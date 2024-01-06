def arrivee(graphe, depart, chemin):
    """Renvoie le sommet atteint à l'issue du parcours"""
    pass


def nombre_visites(graphe, depart, chemin):
    """Renvoie le nombre de sommets distincts rencontrés lors du parcours"""
    pass


graphe_1 = {
    0: [8, 1],
    1: [2, 6],
    2: [3, 7],
    3: [9, 5],
    4: [7, 8],
    5: [0, 9],
    6: [4, 0],
    7: [5, 2],
    8: [6, 3],
    9: [1, 4],
}
chemin_1 = [0, 1, 1]
assert arrivee(graphe_1, 0, chemin_1) == 5
assert arrivee(graphe_1, 1, chemin_1) == 2
assert nombre_visites(graphe_1, 0, chemin_1) == 4
assert nombre_visites(graphe_1, 1, chemin_1) == 3

graphe_2 = {
    0: [6, 4, 8],
    1: [5, 6, 0],
    2: [1, 5, 7],
    3: [0, 9, 1],
    4: [9, 8, 6],
    5: [7, 0, 9],
    6: [8, 2, 3],
    7: [3, 1, 4],
    8: [2, 7, 5],
    9: [4, 3, 2],
}
chemin_2 = [0, 2, 1, 0, 0, 1, 2, 0, 1, 1, 0, 2, 2]
attendus_2 = (
    (0, 7, 9),
    (1, 5, 9),
    (2, 9, 9),
    (3, 2, 10),
    (4, 8, 10),
    (5, 4, 9),
    (6, 3, 8),
    (7, 0, 10),
    (8, 6, 8),
    (9, 1, 9),
)
for depart, arrivee_attendue, etapes_attendue in attendus_2:
    assert arrivee(graphe_2, depart, chemin_2) == arrivee_attendue
    assert nombre_visites(graphe_2, depart, chemin_2) == etapes_attendue

graphe_3 = {
    0: [13, 6, 4, 3],
    1: [8, 10, 13, 11],
    2: [7, 11, 10, 5],
    3: [11, 0, 9, 8],
    4: [14, 7, 2, 12],
    5: [4, 14, 8, 13],
    6: [3, 8, 11, 7],
    7: [1, 3, 12, 6],
    8: [9, 5, 1, 0],
    9: [0, 2, 6, 14],
    10: [6, 4, 3, 2],
    11: [2, 1, 7, 9],
    12: [10, 9, 5, 1],
    13: [5, 12, 14, 4],
    14: [12, 13, 0, 10],
}
chemin_3 = [3, 2, 0, 1, 1, 3, 2, 2, 3, 0, 0, 1, 1, 1, 2, 0, 2, 3, 1, 0, 2]
attendus_3 = (
    (0, 8, 11),
    (1, 5, 12),
    (2, 12, 11),
    (3, 4, 11),
    (4, 13, 12),
    (5, 10, 14),
    (6, 11, 9),
    (7, 9, 12),
    (8, 1, 11),
    (9, 0, 10),
    (10, 6, 13),
    (11, 14, 11),
    (12, 2, 11),
    (13, 3, 14),
    (14, 7, 12),
)
for depart, arrivee_attendue, etapes_attendue in attendus_3:
    assert arrivee(graphe_3, depart, chemin_3) == arrivee_attendue
    assert nombre_visites(graphe_3, depart, chemin_3) == etapes_attendue
