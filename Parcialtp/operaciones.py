def sumar_vector(indice, vector):

    if indice == len(vector):
        return =0
    return vector[indice] + sumar_vector(vector, indice+1)
       

def por_porcentaje(nombres, ventas, total, limite_por):
    i=0
    encontrados =0
    porcentaje_acum=0
    while i<len(ventas):
        porcentaje_region = (ventas[i]*100)/total
        if porcentaje_region<limite_por:
            porcentaje_men =int(porcentaje_region*100)/100
            print(nombres[i],':', ventas[i], 'productos(' porcentaje_men, '%)')
            porcentaje_acum=porcentaje_acum+porcentaje_region
            encontrados= encontrados+1

        i=i+1

    if encontrados ==0:
        print('error')

    else:
        acum    

