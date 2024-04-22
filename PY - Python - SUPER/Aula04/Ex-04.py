from auxiliary import *

# print(students[0]["coeficiente acadêmico"])
# print('students', students)


maior = students[0]["coeficiente acadêmico"]
new_students = {}

notas = {}
# recuperar as notas
for n in range(len(students)):
    if students[n]["coeficiente acadêmico"] > maior:
        notas[students[n]["coeficiente acadêmico"]] = students[n]
    
print('notas', sorted(notas, reverse=True))

maior =  sorted(notas, reverse=True)[0]

print('maior', maior)

tamanho = len(students)
for n in range(len(students)):
    if students[n]["coeficiente acadêmico"] > maior:
        notas[students[n]["coeficiente acadêmico"]] = students[n]
        






