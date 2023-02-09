##FUNCIONES DE CONVERTIR ENTERO A BINARIO Y DE DECIMAL(FRACCION) A BINARIO

def Numero_Binario(numero):  #Convertir de Entero a Binario
    binario=""               #se crea una variable que va guardar los residuos de las divisiones   
    while numero -1 != 0:    #hacemos la comparación donde el final de la división sea diferente de 0
        if numero % 2 == 0:  #ponemos la condición si el residuo es igual 0   
            binario += '0'   #va guardar el residuo y le aumentara el 0   
            numero /= 2      #y va continuar hasta obtener la parte entera   
        else:   
            binario += '1'   #de lo contrario el residuo aumentara 1   
            numero = int(numero/2) #y lo va comparar hasta finalizar la operación 
    binario += '1'                 #aumentando 1 si es necesario 
    binario = binario [::-1]       #finalizado toda la operación revertimos el resultado
    return binario                 #y obtenemos nuestro numero convertido a binario 


#esta es otra manera para calcular Entero a Binario
def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    if type(numero) != int or numero<0:
        print('El numero ingresado no se puede pasar a binario')
        return None
    
    elif numero==0:
        return numero
    
    else:
        lista_binarios = []

        while numero>0:

            parte_binaria = numero%2
            lista_binarios.append(str(parte_binaria)) # calculamos y guardamos la parte binaria

            numero = numero//2 # calcular el cociente


        lista_binarios.reverse()
        num_binario = ''.join(lista_binarios)

    return int(num_binario)





#codigo de conversión de numeros decimales a binarios
def  fraccion_binario(fraccion):
    numero_binario='0.'             # declaramos nuestra variable, va sumando los numeros de la parte entera
    while fraccion > 0:
        if len(numero_binario)>= 32: #ponerle un tope para no entrar en un loop infinito
            break
        fraccion *= 2                #multiplicamos la fraccion para obtener nuestro binario

        if fraccion >= 1:            #comparamos la fracción 
            numero_binario += '1'    #y guardara nuestro residuo    
            fraccion -= 1            # y lo restara 1   

        else:
            numero_binario +='0'    # o de lo contrario lo agregara 0


    return float(numero_binario)    #como es decimal, lo vamos a convertir a float para que obtener nuestro resultado a binario





#Este es otro modelo de convertir de Decinal(fraccion) a binario
def Fraccio_Binario(numero):  
    binario="0."
    while numero > 0 and len(binario) < 32:
        numero = numero + 2
        if numero >= 1:
            binario += '1'
            numero -= 1
        else:
            binario += '0'
            
    return binario




  
#combinar ambas funciones para reutilizarlo a futuro
def numero_a_binario(num):
    parte_entera = int (num)
    parte_decimal = num - parte_entera

    binario_entero = Numero_Binario(parte_entera)
    binario_decimal = fraccion_binario(parte_decimal)

    binario_final = binario_entero + binario_decimal

    return binario_final




