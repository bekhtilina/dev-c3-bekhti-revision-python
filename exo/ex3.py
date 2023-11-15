operation = input("Entrez une opération mathématique (+ ou - ou * ou /) : ")

def calcul(chaine):
    operateurs = set("+-*/")
    for op in operateurs:
        if op in chaine:
            operateur = op
            operande1, operande2 = map(int, chaine.split(operateur))
            break

    if operateur == '+':
        resultat = operande1 + operande2
    elif operateur == '-':
        resultat = operande1 - operande2
    elif operateur == '*':
        resultat = operande1 * operande2
    elif operateur == '/':
        if operande2 != 0:
            resultat = operande1 / operande2
        else:
            return "Erreur : Division par zéro"

    return resultat

try:
    resultat = calcul(operation)
    print("Résultat :", resultat)
except Exception as e:
    print("Erreur : {e}")
