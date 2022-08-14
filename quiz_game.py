print("Bienvenido a la Pablo-trivia")

playing = input("Quieres jugar? ")

if playing.lower() != "si":
    quit()

print("Yas! :)")
score = 0

answer = input('Cuántos tatuajes tiene Pablo? ')
if answer.lower() == 'uno':
    print('correct0!')
    score += 1
else:
    print('incorrect0')

answer = input('Qué dice el tatuaje de Pablo? ')
if answer.lower() == 'grunge':
    print('correcto!')
    score += 1

else:
    print('incorrecto :(')

answer = input('De cuántas cuerdas es el bajo escarchado de Pablo? ')
if answer.lower() == 'cinco':
    print('uy, nerd!')
    score += 1

else:
    print('incorrect0')

answer = input('Cuál es el segundo nombre de Pablo? ')
if answer.lower() == 'josué':
    print('boaaaa!')
    score += 1

else:
    print('incorrecto')


if score == 1:
    print('Sacaste ' + str(score) + ' punto, valiste jeje')
elif score == 2:
    print('Sacaste 2 puntos, practica!')
elif score == 3:
    print('Sacaste 3 puntos de 4, ggs')
else:
    print('Le diste a todas, crá')
