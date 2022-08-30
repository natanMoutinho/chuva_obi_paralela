import random
import sys
from mpi4py import MPI

# Recebendo a lista de valores por parâmetro do sistema
tam_lista = int(sys.argv[1])
# Valor de soma atribuído
SOMA = int(sys.argv[2])

#Iniciando o MPI
comm = MPI.COMM_WORLD
pid = comm.Get_rank()  # PID do Processos atual
numProcs = comm.Get_size()  # total de processos iniciados
MaqNome = MPI.Get_processor_name()  # Nome da máquina

combinacoes = []  # Mudar legenda
intervalos = ((2 ** tam_lista)/numProcs) # Quantidade de veotres binários cada processo deverá calcular

#Serão gerados aleatóriamente uma quantidade de números definida por 'tam_lista'
sorteio = ''
if(pid == 0):
    for x in range(0,tam_lista):
        sorteio += str(random.randint(1,10)) + ' '
    sorteio = sorteio[:len(sorteio)-1].split(' ')
    for i in range(1,numProcs):
      comm.send(sorteio,i)
else :
  sorteio = comm.recv()

total = 0
def verificarBinario(binario):
    soma = 0
    solucao = list(binario)
    global total
    for pos in range(0, len(sorteio)):
        soma += int(solucao[pos]) * int(sorteio[pos])
    if soma == SOMA:
        combinacoes.append(solucao)
        total += 1

for i in range(int(pid*intervalos), int((pid+1)*intervalos)):
    x = bin(i)
    binario = x.split('b')[1].zfill(tam_lista)
    verificarBinario(binario)

if(pid != 0):
    comm.send(combinacoes,0)
else:
    for i in range(1, numProcs):
      combinacoes.append(comm.recv())