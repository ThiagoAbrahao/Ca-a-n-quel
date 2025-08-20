import time
import random

print ("Rodando as bobinas...")

# pausa de uns 2 segundos para dar suspense.
time.sleep(3)

# bobinas para sortear
simbolos = ("🍒", "🍋", "🍇")
bobina1 = random.choice(simbolos)
bobina2 = random.choice(simbolos)
bobina3 = random.choice(simbolos)

# Mostra os resultados
print(f"Resultado: {bobina1} {bobina2} {bobina3}")

# Condição para determinar vitória ou derrota
if bobina1 == bobina2 == bobina3:
    print("Parabéns, você ganhou 🎉")
else:
    print("Você perdeu, tente novamente.")
