def aplatir(conteneur) -> list:
    """Renvoie la liste des entiers présents dans conteneur."""
    resultat = []
    for i in range(len(conteneur)):
        if isinstance(conteneur[i], list):
            resultat.extend(aplatir(conteneur[i]))
        else:
            resultat.append(conteneur[i])
    return resultat

# Tests
a = [3, 8, [5, [7]]]
assert aplatir(a) == [3, 8, 5, 7]
b = [[5, [7], 6]]
assert aplatir(b) == [5, 7, 6]
c = [3, 8, [5, [7], 6, [1, [8, 0]]], 2]
assert aplatir(c) == [3, 8, 5, 7, 6, 1, 8, 0, 2]
d = [[[[[[[[[[[[[[[[[[[[[[1]]]]]]]]]]]]]]]]]]]]]]
assert aplatir(d) == [1]
e = [k for k in range(5)]
for i in range(5):
    e[i] = e[:i] + [e[i]]
assert aplatir(e) == [0, 0, 1, 0, 0, 1, 2, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 1, 0, 0, 1, 2, 0, 0, 1, 0, 0, 1, 2, 3, 4]


