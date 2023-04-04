# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('ponte.jpg')

for y in range(0, imagem.shape[0]): # percorre linhas
    for x in range(0, imagem.shape[1]): # percorre colunas
        imagem[y, x] = (x%256,y%256,x%256)  # mantem o valor do pixel entre 0 e 255
                                            # uma vez que valores RGB assumem esse intevalo

# Mostra a imagem com a função imshow
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)  # espera pressionar qualquer tecla
