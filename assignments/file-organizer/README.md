# 📘 Assignment: Organizador de Arquivos com Python

## 🎯 Objetivo

Pratique automação de arquivos com `pathlib` e `shutil`, organizando arquivos por extensão. O exercício usa uma pasta de demonstração criada pelo código inicial para manter a atividade isolada dos demais arquivos.

## 📝 Tarefas

### 🛠️ Inspecionar os arquivos de entrada

#### Descrição
Execute `python starter-code.py` a partir desta pasta. O código inicial prepara exemplos em `organizer-demo/incoming`; implemente a leitura dessa pasta usando `pathlib`.

#### Requisitos
O programa concluído deve:

- Listar somente os arquivos diretamente dentro de `organizer-demo/incoming`.
- Exibir o nome e a extensão de cada arquivo.
- Não alterar nem acessar arquivos fora de `organizer-demo`.

### 🛠️ Agrupar arquivos por extensão

#### Descrição
Crie uma estrutura que associe cada extensão aos arquivos correspondentes e mostre uma prévia da organização antes de mover qualquer arquivo.

#### Requisitos
O programa concluído deve:

- Agrupar os arquivos pela extensão em letras minúsculas e sem o ponto inicial.
- Usar a categoria `sem-extensao` para arquivos sem extensão.
- Mostrar cada categoria e os nomes dos arquivos que serão organizados nela.
- Manter os arquivos na pasta de entrada durante a prévia.

### 🛠️ Organizar os arquivos

#### Descrição
Use `pathlib` para criar uma pasta de destino para cada categoria e `shutil` para mover os arquivos para essas pastas.

#### Requisitos
O programa concluído deve:

- Criar as pastas de categoria dentro de `organizer-demo/organized`.
- Mover cada arquivo para a pasta correspondente à sua extensão.
- Ignorar um destino que já contenha um arquivo com o mesmo nome, sem sobrescrevê-lo.
- Exibir uma mensagem com a quantidade de arquivos organizados.

O exercício usa apenas a biblioteca padrão do Python. Para reiniciar a demonstração, remova somente a pasta `organizer-demo` e execute o programa novamente.