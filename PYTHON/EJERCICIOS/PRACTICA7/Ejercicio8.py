saludos=['hola','hello','hi']
nombres =['albertostas','pinilla','davidburges']

resultado=[x.split() + y.split() for x in saludos for y in nombres]

print(resultado)