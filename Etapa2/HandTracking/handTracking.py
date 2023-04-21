"""
==================== Hand Tracking Code =========================
@author:    https://github.com/mttgermano
@date  :    20/04/2023    
=================================================================
"""

# Bibliotecas ###################################################
import mediapipe as mp
import cv2 as cv
import time


 
# Funções auxiliares ############################################
# conta os frames por segundo do video #
def countFPS(t0: float,t1: float) -> tuple[int, float, float]:
    t1 = time.time()        # obtém o tempo atual 

    fps = int(1//(t1-t0))   # divide-se 1 pela subtração do tempo 
                            # atual com o tempo passado, obtendo 
                            # o número de frames 

    t0 = t1                 # atualiza o tempo passado 

    return (fps, t0, t1)

# soma o número de dedos levantados #
def countDedos(pontos: list,dedos: list) -> int:
    numero_dedos = 0
    if pontos:
        # para o dedão #
        # se o ponto superior do dedao estiver a direita do 
        # proximo ponto
        if pontos[4][0] < pontos[3][0]:
            # numer de dedos abaixados e aumentado em 1
            numero_dedos += 1
    
        # para cada ponto dos outros dedos #
        for x in dedos:     
            # se o ponto superior estiver abaixo de dois outros
            # pontos
            if pontos[x][1] < pontos[x-2][1]:
                # número de dedos abaixados é aumentado em 1
                numero_dedos += 1
    return numero_dedos



# MAIN ##########################################################
def main():

    # Variaveis Globais #########################################
    t0,t1 = 0,0                 # variáveis de tempo inicial e 
                                # final usadas para calcular FPS
                                # do vídeo
                                    
    
    frame = cv.VideoCapture(0)  # cria um objeto que receberá o 
                                # vídeo obtido da primeira câmera 
                                # disponível no computador 
                                # (por isso o '0').
    
    color_text = (85,85,255)        # cor do texto 
    color_background = (40,50,42)   # cor do quadrado
    
    # Shortcuts para métodos das bibliotecas ####################
    hands = mp.solutions.hands      # configura a biblioteca do
                                    # mediapiepe para usar 
                                    # funções relacionadas  mãos

    Hands = hands.Hands(max_num_hands=2)    # quantidade máxima 
                                            # de mãos que serão 
                                            # detectadas

    mpDwaw = mp.solutions.drawing_utils # configuração da
                                        # biblioteca do mediapipe
                                        # para funções
                                        # relacionadas à desenhos
    

    
    # Main Loop #################################################
    while(True):
        ret,video = frame.read()   # captura cada frame do vídeo
        video = cv.flip(video,1)    # inverte o vídeo
    
    
        # cria o retângulo de display que mostrara o número de
        # dedos levantados
        cv.rectangle(video,(20,20),(170,170),color_background,cv.FILLED)
    
    
        # FPS ###################################################
        fps,t0,t1 = countFPS(t0,t1)     # conta quantos frames 
                                        # por segundo o vídeo 
                                        # esta conseguindo 
                                        # capturar
    
        # printa o resultado do fps
        cv.putText(video, f"FPS: {fps}",(200,50),cv.FONT_HERSHEY_PLAIN,2,color_text,3)
    

        # Número Dedos ##########################################
        results = Hands.process(video)  # faz o processamento do
                                        # vídeo visando encontrar 
                                        # padroes similares aos  
                                        # de uma mo

        # obtém as coordenadas dos pontos das mãos
        handPoints = results.multi_hand_landmarks   

        # extrai as dimensões do vídeo: sua altura e sua largura
        altura, largura, _ = video.shape    

        # lista contendo os pontos
        pontos = []
    
        # se existem coordenadas da mão, isto é, se um objeto 
        # parecido com uma mão foi encontrado no vídeo
        if handPoints:

            # para cada ponto obtida a partir da mão
            for points in handPoints:

                # desenhe no vídeo os pontos e suas conexões
                mpDwaw.draw_landmarks(video, points,hands.HAND_CONNECTIONS)

                # para cada ponto, obtemos seu id e suas
                # coordenadas (x,y)
                for id, cord in enumerate(points.landmark):

                    # obtém as coordenadas corretas dos pontos ao
                    # se multiplicar pela dimensão da imagem
                    cx, cy = int(cord.x * largura), int(cord.y * altura)

                    # mostra no vídeo o id dos pontos nas mãos
                    # (a implementação da biblioteca enumera um 
                    # id à certos pontos cruciais das mãos)
                    cv.putText(video,str(id),(cx,cy+10),cv.FONT_HERSHEY_PLAIN,1,color_text,2)

                    pontos.append((cx,cy))  # coloca as 
                                            # coordenadas dentro
                                            # da lista de
                                            # pontos atuais
        
                # lista com o id dos pontos superiores dos dedos
                dedos = [8,12,16,20]

                # conta o número de dedos levantados
                numero_dedos = countDedos(pontos,dedos)
        
                # printa o resultado do número de dedos
                # dentro do retângulo de display
                cv.putText(video, f"{numero_dedos}",(48,153),cv.FONT_HERSHEY_PLAIN,10,color_text,3)

        #########################################################
    
    
        # exibe os vídeos obtidos à partir da camera #
        cv.imshow("video",video) 
    
        # waitKey retorna o código ascii do caractere pressionado   
        # ord(q) retorna o código ascii do caractere 'q'            
        if cv.waitKey(1) == ord('q'): break
    
    #############################################################
    
    # Fecha o acesso à camera e tambem s janeas #
    frame.release()
    cv.destroyAllWindows()
