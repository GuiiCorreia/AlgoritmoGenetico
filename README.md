# AlgoritmoGenetico
O código apresenta um exemplo de como utilizar algoritmos genéticos para gerar senhas aleatórias e encontrar a mais apta dentre elas, utilizando funções específicas para reprodução, mutação e avaliação de aptidão.

A população inicial é gerada e o algoritmo é executado por 50 gerações, imprimindo a avaliação de cada indivíduo em cada geração. Ao final, a melhor senha encontrada é selecionada e impressa na tela.


A função **gerar_senha()** é responsável por criar uma senha aleatória com base na lista de caracteres definida.  
A função **avaliar_aptidao()** recebe um indivíduo e retorna o número de caracteres corretos na posição correta em relação à senha correta.  
A função **selecionar_pais()** utiliza uma roleta viciada para selecionar dois indivíduos para a reprodução.   
A função **reproduzir()** realiza o crossover entre dois pais para gerar um filho.  
A função **mutar()** realiza a mutação em um indivíduo, trocando um caractere aleatório por outro. 

E, por fim, a função **gerar_proxima_geracao()** gera uma nova população com base nos indivíduos selecionados, reproduzidos e mutados.
