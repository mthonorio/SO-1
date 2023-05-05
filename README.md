# Projeto da disciplina de Sistemas Operacionais 1

Este projeto foi desenvolvido para a disciplina de Sistemas Operacionais 1 no semestre 2022.1 ministrada pelo professor Fernando.

## Especificação do Projeto

Implementar um conjunto de algoritmos de escalonamento de CPU e escrever um programa que calcula uma série de estatísticas baseado nestes algoritmos.

Os algoritmos de escalonamento a serem implementados são os seguintes:

- FCFS: First-Come, First-Served
- SJF: Shortest Job First
- RR: Round Robin (com quantum = 2)

Deverá ler de um arquivo uma lista de processos com seus respectivos tempos de chegada e de duração e deverá imprimir na tela uma tabela contendo os valores para as seguintes métricas:

- Tempo de retorno médio
- Tempo de resposta médio
- Tempo de espera médio

### Input

A entrada é composta por uma série de pares de números inteiros separados por um espaço em branco indicando o tempo de chegada e a duração de cada processo. A entrada termina com o fim do arquivo.

### Output

A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e os valores das três métricas solicitadas.

Cada linha apresenta a sigla do algoritmo e os valores médios (com uma casa decimal) para tempo de retorno, tempo de resposta e tempo de espera, exatamente nesta ordem, separados por um espaço em branco.

## Requisitos

## Execução

Para rodar o programa é necessário passar os argumentos:

- Operação
- Número do Quantum
- Arquivo de teste para a execução

Como exemplo:

```
python main.py -rr 2 unorganized.txt
```
