cadena="nif;nombre;email;teléfono;descuento\n01234567;Luis González;luisgonzalez@mail.com;656343576;12.5\n\
71476342J;MacarenaRamírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;\
juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

dic={}
lineas = cadena.split("\n")

encabezados = lineas[0].split(";")

for l in lineas[1:]:
    objetos2 = l.split(";")  
    dic[objetos2[0]] = {  
        encabezados[1]: objetos2[1],  
        encabezados[2]: objetos2[2],  
        encabezados[3]: objetos2[3],  
        encabezados[4]: objetos2[4],  
    }

dic2={}
for c,v in dic.items():
    print()
    print("Cliente - " + c)
    print(v)
    print("------------------------------------------")
