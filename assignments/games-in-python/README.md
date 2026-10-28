
# 📘 Assignment: Jogo da Forca

## 🎯 Objetivo

Pratique strings, listas, seleção aleatória, loops e condicionais em Python construindo um jogo da Forca. O programa deve permitir que a pessoa descubra uma palavra antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Preparar a palavra e o estado do jogo

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher uma palavra secreta e preparar as informações necessárias para acompanhar a partida.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente da lista `words`.
- Inicializar uma estrutura para registrar as letras já tentadas e definir o limite de palpites incorretos.
- Exibir o progresso da palavra com letras ainda não descobertas representadas por `_`, separadas por espaços.

### 🛠️ Processar palpites e encerrar a partida

#### Descrição
Implemente o loop principal para receber palpites, atualizar o progresso e terminar a partida quando a palavra for descoberta ou o limite de erros for atingido.

#### Requisitos
O programa concluído deve:

- Solicitar um palpite de letra e comparar a entrada com a palavra secreta sem diferenciar maiúsculas de minúsculas.
- Revelar todas as posições de uma letra correta e contabilizar palpites incorretos.
- Atualizar e exibir o progresso e o número de tentativas incorretas restantes após cada palpite.
- Encerrar quando todas as letras forem descobertas ou quando não houver mais tentativas incorretas.
- Exibir uma mensagem indicando vitória ou derrota; em caso de derrota, revelar a palavra secreta.