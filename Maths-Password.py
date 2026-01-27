import secrets
import string
import pyfiglet

letras_minusculas = string.ascii_lowercase
letras_maiusculas = string.ascii_uppercase
numeros = string.digits
especiais = "#*&"

todos_caracteres = (letras_minusculas + letras_maiusculas + numeros + especiais)

tamanho = 16

senha = ''.join(secrets.choice(todos_caracteres) for _ in range(tamanho))

ascii_art = pyfiglet.figlet_format("Maths-Password", font="doom")

print(ascii_art)
print("Sua nova senha:")
print(senha)
