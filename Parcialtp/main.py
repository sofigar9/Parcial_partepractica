from operaciones import validar_numero
from operaciones import (por_porcentaje, sumar_vector)

def menu ():
    nombres_distribuidora = ['NOA', 'NEA', 'Pampeana', 'Cuyo', 'Patagonia', 'GBA']
    ventas_regiones = []
    datos_ingresados = False

    opcion = 0
    while opcion !=11:
      print('  Sistema de gestion de ventas  ')  
      print('1-  Cargar ventas' )
      print('2-  Mostrar ventas' )
      print('3-  Regiones con menos del 5%' 'de ventas' )
      print('4-  Regiones con menos del 25%' 'de ventas' )
      print('5-  Regiones con mas de 500' 'ventas' )
      print('6-  Regiones con mas de 3000' 'ventas' )
      print('7-  Regiones por encima del promedio' )
      print('8-  Regiones mas compradoras' )
      print('9- Harcodear vector')
      print('10- Ordenar region por nombre (de la A-Z)')
      print('11- Salir')
      
      opcion_entrada =input('Seleccione alguna opcion: ')

      if len(opcion_entrada)>0:
        valido = True
        for c in opcion_entrada:
            if c<='0' and c>='9':
                pass
            else:
                valido ==false

        if valido == True:
            opcion= int(opcion_entrada)
        else:
            opcion=0    

      else:
        opcion = 0      

      if opcion == 1:
        ventas_regiones = [0] * 6
        i=0
        while i <len(nombres_distribuidora):
            print ('region', i+1, ':', nombres_distribuidora[i])

            productos= validar_numero(
                'Numero no admitido, ingrese productos vendidos',
                'Error: ingrese un numero valido'
            )
            ventas_regiones[i] =productos
            i = i+1
        datos_ingresados =True
        print('Ventas cargadas ')

        elif opcion>=2 and opcion<=9:
            if datos_ingresados ==  False:
                print('debe cargarse las ventas primero')
            else:
                total = sumar_vector(ventas_regiones, 0)


                match opcion:
                    case 2:
                        print ('  Ventas   ')
                        i=0
                        while i < len(nombres_distribuidora):
                            porcentaje = (ventas_regiones[i] * 100/total_ventas)
                        print (
                            nombres_distribuidora[i],
                            ':',
                            ventas_regiones[i],
                            'productos('
                            porcentaje, '%',
                        )   
                        i= i+1
                        print('cantidad de regiones ')

                    case 3: print('Regiones con menos del 5%')
                    por_porcentaje(nombre, ventas, total, 5)

                    case 4: print('Regiones con menos del 10%') 
                    por_porcentaje(nombre, ventas, total, 10)

                    case 9:
                        nombres_distribuidora=
                        [
                            'PBA', 'CABA', 'La Pampa',
                            'Tucumán', 'Mendoza', 'Chubut', 'Corrientes', 'Neuquén', 'La Rioja', 'Jujuy'
                        ]            
                        ventas_regiones=[1800, 555, 2333, 1850, 3999, 777, 1410, 7180, 2500, 60]
                        datos_ingresados = True
                        print('Vector hardcodeado')



      elif opcion == 11:
        print ('Cerrando el sistema')
      else:
        if opcion !=0:
      print('Esta opcion no es valida') 







