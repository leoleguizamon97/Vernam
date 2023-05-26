def setClave():
	return input('Ingrese la clave: ').lower()

def setTextoProcesar():
	return input('Ingrese el texto a procesar: ').lower()

def xor(a, b):
	if a == b:
		return '0'
	return '1'

def textoaBinario(texto):
	resultado = ''
	for c in texto:
		resultado = resultado + aBinario(c)
		print(f'Caracter {c} - Binario {aBinario(c)}')
	return resultado


def aBinario(char):
	num = ord(char)
	cadena_binaria = bin(num)[2:]  # Convertir el número entero a binario y eliminar el prefijo '0b'
	return cadena_binaria.rjust(8,'0')

def aCaracter(binario):
	asciiCode = int(binario,2)
	return chr(asciiCode)

def vernamEncriptar(clave, texto):

	return

def vernamDesencriptar(clave, texto):

	return

def vernam(modo = 0):
	clave = setClave()
	texto = setTextoProcesar()
	#Definimos la clave binaria
	claveBinaria = textoaBinario(clave)
	#Pasamos el texto plano a binario
	textoBinario = textoaBinario(texto)

	print('Clave en binario: '+ claveBinaria)
	print('Texto en binario: '+ textoBinario)
	
	##Encriptamos o des-encriptamos
	while():
		if modo == 0:
			print (vernamEncriptar)
			break
		elif modo == 1:
			print (vernamEncriptar)
			break
		else:
			print('Modo no valido: [0 : Encriptar] [1 : Desencriptar]')
			modo = int('Ingrese la opcion correcta [0 o 1]')


vernam()