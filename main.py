import random
import math

def create_data_model():
    data = {}
    data['matriz_distancia'] = [
      [0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],
      [548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],
      [776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754],
      [696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],
      [582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],
      [274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],
      [502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],
      [194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856],
      [308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514],
      [194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468],
      [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354],
      [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844],
      [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730],
      [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536],
      [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194],
      [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798],
      [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730,536, 194, 798, 0]
    ]
    data['num_vehicles'] = 4
    data['depot'] = 0
    return data

# hiperparâmetros
tamanho_populacao = 100
tx_mutacao = 0.10
tx_crossover = 0.15
tx_tragedia = 0.05
geracoes_max = 20_000
geracoes_tragedia = 1000
matriz = create_data_model()

# utilidade
# se está aumentando, está melhorando o resultado
def fitness(individuo):
  score = 0
  caminho = individuo

  lista_unica = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  for x in lista_unica:
    if caminho.count(x) > 1:
      return score
  
  # print(caminho)
  peso_caminho = []
  # print(peso_caminho)
  ponto_atual = 0
  for destino in caminho:
    peso_caminho.append(matriz['matriz_distancia'][ponto_atual][destino])
    ponto_atual = destino
  
  fitness_1 = peso_caminho[0] + peso_caminho[1] + peso_caminho[2] + peso_caminho[3]
  fitness_2 = peso_caminho[4] + peso_caminho[5] + peso_caminho[6] + peso_caminho[7]
  fitness_3 = peso_caminho[8] + peso_caminho[9] + peso_caminho[10] + peso_caminho[11]
  fitness_4 = peso_caminho[12] + peso_caminho[13] + peso_caminho[14] + peso_caminho[15]

  score += 1

  # if fitness_1 == fitness_2 or fitness_1 == fitness_3 or fitness_1 == fitness_4:
  #   score += 1
  # if fitness_2 == fitness_3 or fitness_2 == fitness_4:
  #   score += 1
  # if fitness_3 == fitness_4:
  #   score += 1

  if abs(abs(fitness_1 - fitness_2) - abs(fitness_3 - fitness_4)) < 50:
    score += 1

  if abs(abs(fitness_1 - fitness_3) - abs(fitness_2 - fitness_4)) < 50:
    score += 1

  if abs(abs(fitness_1 - fitness_4) - abs(fitness_2 - fitness_3)) < 50:
    score += 1

  if abs(fitness_1 - fitness_2) < 150:
    score += 1
  if abs(fitness_1 - fitness_3) < 150:
    score += 1
  if abs(fitness_1 - fitness_4) < 150:
    score += 1
  if abs(fitness_2 - fitness_3) < 150:
    score += 1
  if abs(fitness_2 - fitness_4) < 150:
    score += 1
  if abs(fitness_3 - fitness_4) < 150:
    score += 1
    
  if abs(fitness_1 - fitness_2) < 100:
    score += 1
  if abs(fitness_1 - fitness_3) < 100:
    score += 1
  if abs(fitness_1 - fitness_4) < 100:
    score += 1
  if abs(fitness_2 - fitness_3) < 100:
    score += 1
  if abs(fitness_2 - fitness_4) < 100:
    score += 1
  if abs(fitness_3 - fitness_4) < 100:
    score += 1

  if abs(fitness_1 - fitness_2) < 80:
    score += 1
  if abs(fitness_1 - fitness_3) < 80:
    score += 1
  if abs(fitness_1 - fitness_4) < 80:
    score += 1
  if abs(fitness_2 - fitness_3) < 80:
    score += 1
  if abs(fitness_2 - fitness_4) < 80:
    score += 1
  if abs(fitness_3 - fitness_4) < 80:
    score += 1
    

  if abs(fitness_1 - fitness_2) < 50:
    score += 1
  if abs(fitness_1 - fitness_3) < 50:
    score += 1
  if abs(fitness_1 - fitness_4) < 50:
    score += 1
  if abs(fitness_2 - fitness_3) < 50:
    score += 1
  if abs(fitness_2 - fitness_4) < 50:
    score += 1
  if abs(fitness_3 - fitness_4) < 50:
    score += 1

  if abs(fitness_1 - fitness_2) < 30:
    score += 1
  if abs(fitness_1 - fitness_3) < 30:
    score += 1
  if abs(fitness_1 - fitness_4) < 30:
    score += 1
  if abs(fitness_2 - fitness_3) < 30:
    score += 1
  if abs(fitness_2 - fitness_4) < 30:
    score += 1
  if abs(fitness_3 - fitness_4) < 30:
    score += 1

  if abs(fitness_1 - fitness_2) < 10:
    score += 1
  if abs(fitness_1 - fitness_3) < 10:
    score += 1
  if abs(fitness_1 - fitness_4) < 10:
    score += 1
  if abs(fitness_2 - fitness_3) < 10:
    score += 1
  if abs(fitness_2 - fitness_4) < 10:
    score += 1
  if abs(fitness_3 - fitness_4) < 10:
    score += 1

  # if fitness_1 < 1550:
  #   score += 1 
  # if fitness_2 < 1550:
  #   score += 1
  # if fitness_3 < 1550:
  #   score += 1
  # if fitness_4 < 1550:
  #   score += 1

  return score
  
def gerar_individuo():
  # peso_caminho = []
  # ponto_atual = 0
  randomico = random.sample(range(1,17), 16)
  # for destino in randomico:
  #   peso_caminho.append(matriz['matriz_distancia'][ponto_atual][destino])
  #   ponto_atual = destino
  return randomico

# retorna populuacao mutada com uma taxa
def mutacao(populacao):
  populacao_escolhida = random.choices(populacao, k=math.ceil(tx_mutacao*len(populacao)))
  return [mutacao_flip(individuo) for individuo in populacao_escolhida]

# flip de valor de gene de um gene aleatório
def mutacao_flip(individuo):
  novo_individuo = individuo
  index = random.randint(0, 15)
  novo_valor = random.randint(1, 16)
  novo_individuo[index] = novo_valor # mutando gene
  novo_individuo[novo_valor-1] = index + 1
  return novo_individuo

# def mutacao_flip(individuo):
#   novo_individuo = individuo
#   index = random.randint(0,16)
  
#   if index > 0:
#     index_anterior = index - 1
#     ponto_anterior = individuo[1][index_anterior]      
#     novo_caminho = random.randint(1,16)
    
#     while novo_caminho == individuo[1][index]:
#       novo_caminho = random.randint(1,16)
      
#     novo_peso_atual = matriz['matriz_distancia'][ponto_anterior][novo_caminho]
#   else:      
#     novo_caminho = random.randint(1,16)
#     while novo_caminho == individuo[1][index]:
#       novo_caminho = random.randint(1,16)

#     novo_peso_atual = matriz['matriz_distancia'][0][novo_caminho]

#   if index < 16:
#     index_seguinte = index + 1
#     ponto_seguinte = individuo[1][index_seguinte]
#     novo_peso_seguinte = matriz['matriz_distancia'][novo_caminho][ponto_seguinte]
#     novo_individuo[0][index_seguinte] = novo_peso_seguinte

#   novo_individuo[1][index] = novo_caminho 
#   novo_individuo[0][index] = novo_peso_atual
  
#   return novo_individuo

def crossover(populacao, geracao):
  funcao_decaimento_crossover = 1 #math.exp(-geracao/200)
  qtd = funcao_decaimento_crossover*tx_crossover*len(populacao)
  populacao_crossover = []
  populacao_escolhida = random.choices(populacao, k=math.ceil(qtd))
  [1, 2, 3, 4]
  for i in range(len(populacao_escolhida) - 1):
    for j in range(i+1, len(populacao_escolhida)):
      ind1 = populacao_escolhida[i]
      ind2 = populacao_escolhida[j]

      index = random.randint(0, 17 - 1)
      populacao_crossover.append(ind1[0:index] + ind2[index:])
      populacao_crossover.append(ind2[0:index] + ind1[index:])

  return populacao_crossover

# escolhe os indivíduos mais aptos
def selecao_com_tragedia(populacao, geracao):
  nova_populacao = sorted(populacao, key=fitness, reverse=True)
  if (geracao % geracoes_tragedia == 0):
    tamanho_tragedia = math.ceil(tamanho_populacao*tx_tragedia)
    novos_individuos = [gerar_individuo() for _ in range(0, tamanho_populacao - tamanho_tragedia)]
    return nova_populacao[0:tamanho_tragedia] + novos_individuos
  else:
    return nova_populacao[0:tamanho_populacao]

def selecao(populacao, geracao):
  nova_populacao = sorted(populacao, key=fitness, reverse=True)
  return nova_populacao[0:tamanho_populacao]

populacao = [gerar_individuo() for _ in range(0, tamanho_populacao)]
# ordernar lista
populacao = sorted(populacao, key=fitness, reverse=True)
geracao = 0

while fitness(populacao[0]) < 39 and geracao < geracoes_max:
  geracao += 1
  populacao_mutada = mutacao(populacao)
  populacao_crossover = crossover(populacao, geracao)
  populacao = selecao_com_tragedia(populacao_mutada + populacao + populacao_crossover, geracao)
  if geracao % 100 == 0 or (geracao % 10 == 0 and geracao < 100):
    print("\n---------------- Intermediário: " + str(geracao) + " ----------------\n")
    caminho = populacao[0]
    print("Van 1:")
    print(str(caminho[0]) + " → " + str(caminho[1]) + " → " + str(caminho[2]) + " → " + str(caminho[3]))
    print("\nVan 2:")
    print(str(caminho[4]) + " → " + str(caminho[5]) + " → " + str(caminho[6]) + " → " + str(caminho[7]))
    print("\nVan 3:")
    print(str(caminho[8]) + " → " + str(caminho[9]) + " → " + str(caminho[10]) + " → " + str(caminho[11]))
    print("\nVan 4:")
    print(str(caminho[12]) + " → " + str(caminho[13]) + " → " + str(caminho[14]) + " → " + str(caminho[15]))
    print("\nTx Acerto: " + str(fitness(populacao[0])))

print("---------------- Final " + str(geracao) + " ----------------")
caminho = populacao[0]
print("Van 1:")
print(str(caminho[0]) + " → " + str(caminho[1]) + " → " + str(caminho[2]) + " → " + str(caminho[3]))
print("\nVan 2:")
print(str(caminho[4]) + " → " + str(caminho[5]) + " → " + str(caminho[6]) + " → " + str(caminho[7]))
print("\nVan 3:")
print(str(caminho[8]) + " → " + str(caminho[9]) + " → " + str(caminho[10]) + " → " + str(caminho[11]))
print("\nVan 4:")
print(str(caminho[12]) + " → " + str(caminho[13]) + " → " + str(caminho[14]) + " → " + str(caminho[15]))