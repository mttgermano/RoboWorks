# Importação das bibliotecas
import cv2

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
