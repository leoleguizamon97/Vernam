def setClave():
    return input('Ingrese la clave: ').lower()

def setTextoaCifrar():
    return input('Ingrese el texto a cifrar: ').lower()

def xor(a, b):
    if a == b:
        return False
    return True

def aBinario(char):
    num = ord(char)
    cadena_binaria = bin(num)[2:]  # Convertir el número entero a binario y eliminar el prefijo '0b'
    return cadena_binaria

