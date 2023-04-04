# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('ponte.jpg')

for y in range(0, imagem.shape[0]): # percorre linhas
    for x in range(0, imagem.shape[1]): # percorre colunas
        imagem[y, x] = (255,0,0)    # muda a cor do pixel para azul

# Mostra a imagem com a função imshow
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)  # espera pressionar qualquer tecla
