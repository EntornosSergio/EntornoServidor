directorioclientes="nif;nombre;email;teléfono;descuento\n01234567;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;MacarenaRamírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

valores = directorioclientes.split('\n')

valores2 = valores[0].split(';')

valores3 = {}

for line in valores[1:]:

    l = line.split(';')
    
    dic = {
        valores2[1]: l[1],  
        valores2[2]: l[2],  
        valores2[3]: l[3],  
        valores2[4]: l[4]   
    }
    
    valores3[l[0]] = dic

for clave,valor in valores3.items():
        print("-------------------------")
        print(f"Cliente - {clave}")
        print(f"{valor}")
