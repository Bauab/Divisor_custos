import math

def print_nomes(nomes):
	for i in range(len(nomes)):
		print("Participante ",i,": ", nomes[i])

def print_opcoes():
	print("Digite 0 para incluir despesa")
	print("Digite 1 para calcular resultado")
	print("Digite 2 para encerrar o programa")

def incluir_despesa(participantes, nomes):
	comprimento = len(nomes)
	print_nomes(nomes)
	pagador = -1
	while(True):
		try:
			pagador = int(input("Digite o numero de quem pagou a despesa: "))
			assert(not(pagador < 0 or pagador > comprimento - 1))
		except:
			print("**Digita um numero valido chupingole malcomido")
			continue
		break
	while(True):
		try:
			valor = float(input("Digite o valor da despesa: "))
		except:
			print("**Digita um valor valido filho da puta")
			continue
		break
		
	devedores = []
	for i in range(comprimento):
		devedores.append(0)
	contador = 0
	devedor = -3
	while(contador < comprimento):
		print_nomes(nomes)
		print("Digite o numero do devedor " + str(contador))
		print("Digite -1 se nao tiver mais devedores")
		print("Digite -2 se quiser incluir todos os participantes")
		try:
			devedor = int(input("Devedor " + str(contador)+": "))
			assert(not(devedor < -2 or devedor >= comprimento))
		except:
			print("**Digita um numero valido, retardado")
			continue
		if(devedor == -1):
			break;
		elif(devedor == -2):
			for i in range(comprimento):
				devedores[i] = 1
			contador = comprimento
			break
		elif(devedores[devedor] == 1):
			print("**Este devedor ja esta incluso")
			continue
		else:
			devedores[devedor] = 1
			contador+=1
	if(contador ==  comprimento):
		print("Todos foram inclusos como devedores")
	for i in range(comprimento):
		if(devedores[i] == 0):
			continue
		else:
			participantes[i][pagador] -= valor/contador
			participantes[pagador][i] += valor/contador
			
def print_resultados(participantes, nomes):
	comprimento = len(nomes)
	for i in range(comprimento):
		print("Participante ",i,": ",nomes[i],": ")
		for j in range(comprimento):
			if(j == i):
				continue
			print(j,"- ",nomes[j],": ", end='')
			if(participantes[i][j] < 0):
				print("Precisa pagar %5.2f" %(abs(participantes[i][j])),"reais para ele")
			elif(participantes[i][j] > 0):
				print("Precisa receber %5.2f" %(abs(participantes[i][j])), "reais dele")
			else:
				print("Nao possuem dividas entre si")
		print("---------------------------------------------------------------")
		
	
def main():
	print("---------------------------------------------------------------")
	print("ADD - Algoritimo de Divisao de Despesas; v.1.0.0")
	print("by Bauab")
	print("---------------------------------------------------------------")
	num = 0
	while(num < 2):
		try:
			num = int(input("Insira numero de participantes da divisao: "))
			assert(num > 1)
		except:
			print("**Digita um inteiro >=2 direito filho da puta")
			continue
	participantes = []
	nomes = []
	for i in range(num):
		participantes.append([])
		for j in range(num):
			participantes[i].append(0)
		nomes.append(input("Insira nome do participante " + str(i) + ": "))
	print_nomes(nomes)
	print(nomes)
	print(participantes)
	while(True):
		print_opcoes()
		try:
			opcao = int(input("Opcao: "))
			assert(not(opcao > 2 or opcao < 0))
		except:
			print("**Digita uma opcao valida seu cabaço")
			continue
		if(opcao == 1):
			print("Calculando resultados...")
			print_resultados(participantes, nomes)
		elif(opcao == 0):
			incluir_despesa(participantes, nomes)
		elif(opcao == 2):
			print("Encerrando...")
			break
		
	
main()