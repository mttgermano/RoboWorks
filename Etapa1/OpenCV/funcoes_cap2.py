# Importação das bibliotecas
import cv2

def atividade2():
    # Leitura da imagem com a função imread()
    imagem = cv2.imread('ponte.jpg')
    
    for y in range(0, imagem.shape[0]): # percorre linhas
        for x in range(0, imagem.shape[1]): # percorre colunas
            imagem[y, x] = (255,0,0)    # muda a cor do pixel para azul
    
    # Mostra a imagem com a função imshow
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)  # espera pressionar qualquer tecla


def atividade3():
    # Leitura da imagem com a função imread()
    imagem = cv2.imread('ponte.jpg')
    
    for y in range(0, imagem.shape[0]): # percorre linhas
        for x in range(0, imagem.shape[1]): # percorre colunas
            imagem[y, x] = (x%256,y%256,x%256)  # mantem o valor do pixel entre 0 e 255
                                                # uma vez que valores RGB assumem esse intevalo
    
    # Mostra a imagem com a função imshow
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)  # espera pressionar qualquer tecla


def atividade4():
    # Leitura da imagem com a função imread()
    imagem = cv2.imread('ponte.jpg')
    
    for y in range(0, imagem.shape[0], 1): # percorre as linhas
        for x in range(0, imagem.shape[1], 1): # percorre as colunas
            imagem[y, x] = (0,(x*y)%256,0)  # altera o valor dos pixeis, tirando matrizes 
                                            # de cores Azuis e Vermelhas além de modificar
                                            # a matriz Verde
    
    # Mostra a imagem com a função imshow
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)  # espera pressionar qualquer tecla


def atividade5():
    # Leitura da imagem com a função imread()
    imagem = cv2.imread('ponte.jpg')
    
    for y in range(0, imagem.shape[0], 10): # percorre linhas
        for x in range(0, imagem.shape[1], 10): # percorre colunas, pulando de 10 em 10
            imagem[y:y+5, x: x+5] = (0,255,255) # cria um quadrado amarelo de 5x5 pixeis
    
    # Mostra a imagem com a função imshow
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)  # espera pressionar qualquer tecla
