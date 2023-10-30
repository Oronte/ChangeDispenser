def rendre_monnaie(somme_a_rendre):
    pieces_dispo = [200, 100, 50, 20, 10, 5, 2, 1]
    pieces_a_rendre = []
    for piece in pieces_dispo:
        while somme_a_rendre >= piece:
            pieces_a_rendre.append(piece)
            somme_a_rendre -= piece
    return pieces_a_rendre

assert rendre_monnaie(528)==[200, 200, 100, 20, 5, 2, 1]
assert rendre_monnaie(0)==[]