def setClave():
	return input('Ingrese la clave: ').upper()

def setTextoProcesar():
	return input('Ingrese el texto a procesar: ').upper()

def xor(a, b):
	if a == b:
		return '0'
	return '1'

def textoaBinario(texto):
	resultado = ''
	for c in texto:
		resultado = resultado + aBinario(c)
		#print(f'Caracter {c} - Binario {aBinario(c)}')
	return resultado

def binarioaTexto(texto = ''):
	resultado = ''
	caracter = ''
	for c in texto:
		
		caracter = caracter + c
		if len(caracter) == 8:
			resultado = resultado + aCaracter(caracter)
			print(f'Binario {caracter} - Caracter {aCaracter(caracter)}')
			caracter = ''
	return resultado

def aBinario(char):
	global alfabeto
	num = alfabeto.index(char)
	cadena_binaria = bin(num)[2:]  # Convertir el número entero a binario y eliminar el prefijo '0b'
	return cadena_binaria.rjust(8,'0')

def aCaracter(binario):
	global alfabeto
	asciiCode = int(binario,2)
	return alfabeto[asciiCode]

def vernamEncriptar(clave, texto):
	resultadoBin = ''
	i = 0
	for b in texto:
		a = clave[i%len(clave)]
		resultadoBin = resultadoBin + xor(a,b)
		i+=1
	return resultadoBin

def vernam():
	clave = setClave().replace(' ','')
	texto = setTextoProcesar().replace(' ','')
	#Definimos la clave binaria
	claveBinaria = textoaBinario(clave)
	#Pasamos el texto plano a binario
	textoBinario = textoaBinario(texto)

	print('Clave en binario: '+ claveBinaria)
	print('Texto en binario: '+ textoBinario)
	
	##Encriptamos o des-encriptamos
	cadenaProcesada = vernamEncriptar(claveBinaria,textoBinario)
	print('Texto bin encrip: '+cadenaProcesada)
	print('RESULTADO'.center(25,'*'))
	print(texto)
	print(binarioaTexto(cadenaProcesada))

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
vernam()