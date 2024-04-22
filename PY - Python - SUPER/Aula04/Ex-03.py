
def validat_turno(hora):
    if hora > 6 and hora < 12:
        print('Bom Dia!')
    elif hora > 12 and hora < 18:
        print('Boa Tarde!')
    else:
        print('Boa Noite!')

turno = int(input("Informe a hora: "))
    
validat_turno(turno)
