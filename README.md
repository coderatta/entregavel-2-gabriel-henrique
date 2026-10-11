# entregavel-2-gabriel-henrique

>Segundo entregável do processo seletivo da UFRJ Harpia

**Autor:** Gabriel Henrique Freitas Ribeiro

## Descrição:

Um programa que lê um arquivo CSV contendo as informações sobre as posições das caixas vindas de um software de reconhecimento de imagem, mostra as imagens com as caixas já posicionadas e as salva em uma pasta separada.

A leitura dos arquivos CSV é feita usando a biblioteca csv já presente no Python, para o posicionamento das caixas é utilizada a, biblioteca OpenCV.

## Descrição das classes:

### Deteccao
Armazena as informações de uma das caixas, como a posição dela na imagem delimitadora e a classe do objeto detectado.
O método desenhar() recebe o objeto externo imagem lido pelo OpenCV e desenha a caixa na posicao e cor especificadas.

### ImagemAnotada
Recebe o nome da imagem e uma lista com as caixas a serem desenhadas. O método adicionar_deteccao() lê a imagem e em um loop para cada imagem, chama a funcao desenhar() de cada caixa, mostrando ao final a imagem com todas as caixas. Outro loop verifica a tecla pressionada para avançar ou parar o programa

## Instalação

Para iniciar o ambiente virtual, siga os seguintes passos:

1. Garanta que possua o Python instalado em sua máquina.
2. Clone o repositório do projeto com o comando(aqui usando SSH):
```bash
git clone git@github.com:coderatta/entregavel-2-gabriel-henrique.git
cd entregavel-2-gabriel-henrique
```
4. Crie e ative o ambiente virtual:
- No Windows:
```bash
python -m venv venv 
venv\Scripts\activate
```
- No Linux ou MacOS:
```bash
python3 -m venv venv 
source venv/bin/activate
```
6. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
7. Execute o programa:
```bash
python src/main.py
```
## Interação

Ao executar o programa ele mostrará as imagens com as caixas, aperte "espaco" para avançar e salvar a imagem com as caixas na pasta resultados, ou aperte "q" para sair do programa salvando a imagem atual