# la idea de este es generar un número random, luego preguntarle a un usuario
# el número que se ha generado, y calcular cuanto demoró el usuario en adivinar el número

import random
# con esto importas el módulo random, (instalado automáticamente con python)
# te sirve para generar números random, como ves abajo
# le tienes que pasar el rango, dos argumentos.
r = random.randrange(-5, 11)
# en este caso eso te genera un numero entre -5 y 10 (Si, 10)
print(r)

q = random.randint(-5, 11)
# este en cambio, si incluye el 11

# ---------- AHORA SI EL CODIGO ----------

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time')
        quit()

else:
    print('Please type a number next time')
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    else:
        if user_guess > random_number:
            print('You were above the number')
        else:
            print('You were below the bumber')

print('You got it in', guesses, 'guesses')

# primero se verifica si lo que ingresa el usuario es digito, con el metodo isdigit()
# ese metodo o regresa true o false

# luego se convierte esa respuesta a numero entero, ya que en realidad es una string inicialmente
# el metodo int sirve para transformar un numero que es string, como por ejemplo "25", y transformarlo a
# numero entero 25.

# luego verificamos si lo que puso el usuario, es un numero mayor a 0
