from pile import Pile

def est_gagnante(pile):
    """Détermine si la pile est gagnante"""
    while not pile.est_vide():
        sommet1 = pile.depile() 
        if pile.est_vide():
            return True
        else:
            
            sommet2 = pile.depile()

            if sommet1 // 2 == sommet2 // 2:
                pile.empile((sommet1 + sommet2) // 2)
            else:
                return False

    return False  

# Test 1
pile1 = Pile()
valeurs1 = (2, 4, 6, 3, 5)
for x in valeurs1:
    pile1.empile(x)

assert est_gagnante(pile1) is False

# Test 2
pile2 = Pile()
valeurs2 = (165, 135, 962, 111, 126, 89, 132, 203, 105)
for x in valeurs2:
    pile2.empile(x)

assert est_gagnante(pile2) is True

# Test 3
pile3 = Pile()
valeurs3 = (851, 1994, 934, 1307, 671, 1296, 1812, 435, 1718, 730, 264, 340, 208, 1780, 1716, 572, 592, 973, 462, 1976)
for x in valeurs3:
    pile3.empile(x)

assert est_gagnante(pile3) is True
