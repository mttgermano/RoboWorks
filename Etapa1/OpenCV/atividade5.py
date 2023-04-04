# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('ponte.jpg')

for y in range(0, imagem.shape[0], 10): # percorre linhas
    for x in range(0, imagem.shape[1], 10): # percorre colunas
        imagem[y:y+5, x: x+5] = (0,255,255) # cria um quadrado amarelo de 5x5 pixeis

# Mostra a imagem com a função imshow
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)  # espera pressionar qualquer tecla
