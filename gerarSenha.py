# o código apresenta um exemplo de como utilizar algoritmos genéticos para gerar senhas 
# aleatórias e encontrar a mais apta dentre elas, utilizando funções específicas para reprodução,
# mutação e avaliação de aptidão.


import random

# Definindo o tamanho da senha e a população inicial
tamanho_senha = 8
tamanho_populacao = 100

# Definindo a lista de caracteres possíveis para a senha
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+"

# Função para gerar uma senha aleatória
def gerar_senha():
    senha = ""
    for i in range(tamanho_senha):
        senha += random.choice(caracteres)
    return senha

# Função para avaliar a aptidão de cada indivíduo na população (quanto mais caracteres corretos na 
# posição correta, maior a aptidão)
def avaliar_aptidao(individuo):
    aptidao = 0
    senha_correta = "password1"
    for i in range(tamanho_senha):  
        if individuo[i] == senha_correta[i]:
            aptidao += 1
    return aptidao

# Função para selecionar os pais para reprodução (roleta viciada)
def selecionar_pais(populacao):
    soma_aptidoes = sum([avaliar_aptidao(individuo) for individuo in populacao])
    roleta = []
    for individuo in populacao:
        probabilidade = avaliar_aptidao(individuo) / soma_aptidoes
        roleta.append((individuo, probabilidade))
    pais = []
    for i in range(2):
        pai = None
        while pai is None:
            sorteio = random.random()
            for individuo, probabilidade in roleta:
                if sorteio <= probabilidade:
                    pai = individuo
                    break
                else:
                    sorteio -= probabilidade
        pais.append(pai)
    return pais

# Função para realizar a reprodução (crossover) entre dois pais e gerar um filho
def reproduzir(pai1, mae):
    ponto_crossover = random.randint(1, tamanho_senha - 1)
    filho = pai1[:ponto_crossover] + mae[ponto_crossover:]
    return filho

# Função para realizar a mutação em um indivíduo (trocar um caracter aleatório por outro aleatório)
def mutar(individuo):
    indice_mutacao = random.randint(0, tamanho_senha - 1)
    novo_caracter = random.choice(caracteres)
    novo_individuo = individuo[:indice_mutacao] + novo_caracter + individuo[indice_mutacao+1:]
    return novo_individuo

# Função para gerar a próxima geração de indivíduos
def gerar_proxima_geracao(populacao):
    nova_populacao = []
    while len(nova_populacao) < tamanho_populacao:
        pais = selecionar_pais(populacao)
        filho = reproduzir(pais[0], pais[1])
        if random.random() <= 0.1:
            filho = mutar(filho)
        nova_populacao.append(filho)
    return nova_populacao

# Gerando a população inicial
populacao = [gerar_senha() for i in range(tamanho_populacao)]

# Executando o algoritmo por 50 gerações

              
for i in range(50):
    print(f"Geração {i+1}:")
    for individuo in populacao:
        print(f"{individuo}: {avaliar_aptidao(individuo)}")
    populacao = gerar_proxima_geracao(populacao)


melhor_senha = max(populacao, key=avaliar_aptidao)
print(f"\nMelhor senha encontrada: {melhor_senha}")
