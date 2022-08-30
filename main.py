import os
import subprocess
import time as t
import matplotlib.pyplot as plt


def runCode(qtdProcess,soma):
  tempo_exec=[]
  tempo_teorico=[]
  for i in range(15, 26):
    tempo_inicial = t.time()
    os.system("mpirun --allow-run-as-root -np "+str(qtdProcess)+" python3 paralela.py "+str(i)+" "+str(soma))
    tempo_final = t.time()
    tempo_final -= tempo_inicial
    tempo_exec.append((i,tempo_final))
    tempo_teorico.append((i+1, tempo_final*2))
  return[tempo_exec,tempo_teorico]



SOMA=10
[exec_single,teoric_single] = runCode(1,SOMA)
[exec_multi,teoric_multi] = runCode(2,SOMA)  

os.system('clear')
print('Single')
print(exec_single)

print('Multi')
print(exec_multi)

# graficoSingle
plt.figure(figsize=(10,7))
plt.plot([exec_single[i][0] for i in range(len(exec_single))], [exec_single[i][1] for i in range(len(exec_single))], marker='o', label='Alg.Single')
plt.plot([teoric_single[i][0] for i in range(len(teoric_single)-1)], [teoric_single[i][1] for i in range(len(teoric_single)-1)],  marker='o', label='Previsto')
plt.title('Tempo de execução')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Segundos')
plt.legend()
plt.grid()
plt.savefig('graficoSingle.png', format='png')


# graficoMulti
plt.figure(figsize=(10,7))
plt.plot([exec_multi[i][0] for i in range(len(exec_multi))], [exec_multi[i][1] for i in range(len(exec_multi))], marker='o', label='Alg.Multi')
plt.plot([teoric_multi[i][0] for i in range(len(teoric_multi)-1)], [teoric_multi[i][1] for i in range(len(teoric_multi)-1)], marker='o', label='Previsto')
plt.title('Tempo de execução')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Segundos')
plt.legend()
plt.grid()
plt.savefig('graficoMulti.png', format='png')

# Gráfico para comparação dos dois modelos (single e multi)
plt.figure(figsize=(10,7))
plt.plot([exec_multi[i][0] for i in range(len(exec_multi))], [exec_multi[i][1] for i in range(len(exec_multi))], marker='o', label='Alg.Multi')
plt.plot([exec_single[i][0] for i in range(len(exec_single))], [exec_single[i][1] for i in range(len(exec_single))], marker='o', label='Alg.Single')
plt.title('Tempo de execução')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Segundos')
plt.legend()
plt.grid()
plt.savefig('graficoComparacao.png', format='png')

# plt.show()
