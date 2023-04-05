# INACABADO

<h2 align="center">
    <img src="https://avatars.githubusercontent.com/u/5009934?s=200&v=4" alt="arduino logo" height="200" width="200"></br>
    <br> Missão OpenCV </br>
</h2>

<h2 align="center">
    <img src="./output.jpg" alt="output main.py"></igm>
</h2>

>A biblioteca OpenCV é uma biblioteca em cóigo aberto voltada à visão computacional. 
Ela pode ser utilizada para análise de imagens, detecção de objetos, reconhecimento de rostos, rastreamento de objetos, entre outras.

### 🎯 Desafio da Missão
- Ler e executar os exemplos dos capítulos 1 e 2 da apostila "Introdução a Visão Computacional com Python e OpenCV".

### 📒 Steps
1. De início, criei uma [venv](https://docs.python.org/3/library/venv.html) para conteinerizar a biblioteca instalada, permitindo a portabilidade dos codigos a seguir;
2. Partindo para as atividades, o intuito da [atividade1.py](./atividade1.py) é demonstrar como acessar os pixéis de uma imagem qualquer utilizando a respectiva biblioteca;
usando
```py
imagem = cv2.imread('entrada.jpg')
imagem.shape[1] #largura da imagem
imagem.shape[0] #altura da imagem
```

2. A seguir, a [atividade2.py](./funcoes_cap2.py) ensina como alterar o valor de um pixel, no trecho:
```py
imagem = cv2.imread('ponte.jpg')

for y in range(0, imagem.shape[0]): # percorre linhas
    for x in range(0, imagem.shape[1]): # percorre colunas
        imagem[y, x] = (255,0,0)    # muda a cor do pixel para azul
```

3. Já a [atividade3.py](./funcoes_cap2.py) dialoga acerca de como manter o valor dos pixéis da imagem dentro do intervalo [0, 256[  e que tal transformacao
resulta na crição de um gradiente verde e roxo por meio do código:
```py
imagem = cv2.imread('ponte.jpg')

for y in range(0, imagem.shape[0]): # percorre linhas
    for x in range(0, imagem.shape[1]): # percorre colunas
        imagem[y, x] = (x%256,y%256,x%256)  # mantem o valor do pixel entre 0 e 255
                                            # uma vez que valores RGB assumem esse intevalo
```

4. Continuamente, o exercício da [atividade4.py](./funcoes_cap2.py) mostra um padrão curioso, formado quando se retira as componentes vermelhas e azuis de 
uma imagem e se limita a componente verde para valores no intervalo [0, 256[ , escrito na parte:
```py
imagem = cv2.imread('ponte.jpg')

for y in range(0, imagem.shape[0], 1): # percorre as linhas
    for x in range(0, imagem.shape[1], 1): # percorre as colunas
        imagem[y, x] = (0,(x*y)%256,0)  # altera o valor dos pixeis, tirando matrizes 
                                        # de cores Azuis e Vermelhas além de modificar
                                        # a matriz Verde
```

5. Por fim, a [atividade5.py](./funcoes_cap2.py) gera quadrados da cor amarela a cada 10 pixeis percorridos na imagem. Os quadrados possuem tamanho 5x5 pixéis, como mostra a passagem:
```py
imagem = cv2.imread('ponte.jpg')

for y in range(0, imagem.shape[0], 10): # percorre linhas
    for x in range(0, imagem.shape[1], 10): # percorre colunas, pulando de 10 em 10
        imagem[y:y+5, x: x+5] = (0,255,255) # cria um quadrado amarelo de 5x5 pixeis
```
