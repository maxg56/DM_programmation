class Element:
    """Classe auxiliaire représentant un maillon d'une liste chaînée"""

    def __init__(self, valeur):
        self.valeur = valeur
        self.successeur = None

    def __str__(self):
        return str(self.valeur)

    def __repr__(self):
        return str(self.valeur)


class Pile:
    def __init__(self):
        """Crée une pile vide"""
        self.tete = None

    def est_vide(self):
        """Renvoie True si la pile est vide, False sinon"""
        return self.tete is None

    def empile(self, valeur):
        """Empile valeur en haut de la pile"""
        nouveau = Element(valeur)
        nouveau.successeur = self.tete
        self.tete = nouveau

    def depile(self):
        """Dépile une valeur et le renvoie
        Lève une erreur si la pile est vide
        """
        assert not self.est_vide(), "La pile est vide"

        x = self.tete.valeur
        self.tete = self.tete.successeur
        return x

    def __str__(self):
        if self.est_vide():
            return "La pile est vide"
        chaine = "(Bas) "
        valeurs = []
        actuel = self.tete
        while actuel is not None:
            valeurs.append(str(actuel.valeur))
            actuel = actuel.successeur
        valeurs.reverse()
        chaine += " - ".join(valeurs) + " (Haut)"
        return chaine

    def __repr__(self):
        return str(self)
