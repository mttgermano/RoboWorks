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


 
# Funcoes auxiliares ############################################
# conta os frames por segundo do video #
def countFPS(t0: float,t1: float) -> tuple[int, float, float]:
    t1 = time.time()        # obtem o tempo atual 

    fps = int(1//(t1-t0))   # divide-se 1 pela subtracao do tempo 
                            # atual com o tempo passado, obtend o 
                            # numero de frames 

    t0 = t1                 # atualiza o tempo passado 

    return (fps, t0, t1)

# soma o numero de dedos levantados #
def countDedos(pontos: list,dedos: list) -> int:
    numero_dedos = 0
    if pontos:
        # para o dedao #
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
                # numer de dedos abaixados e aumentado em 1
                numero_dedos += 1
    return numero_dedos



# MAIN ##########################################################
def main():

    # Variaveis Globais #########################################
    t0,t1 = 0,0                 # variaveis de tempo inicial e 
                                # final usadas para calcular fps
                                # do video
                                    
    
    frame = cv.VideoCapture(0)  # cria um objeto que receberá o 
                                # video obtido da primeira camera 
                                # disponivel no computador 
                                # (por isso o '0').
    
    color_text = (85,85,255)        # cor do texto 
    color_background = (40,50,42)   # cor do quadrado
    
    # Shortcuts para metodos das bibliotecas ####################
    hands = mp.solutions.hands      # configura a biblioteca do
                                    # mediapiepe para usar 
                                    # funcoes relacionadas a maos

    Hands = hands.Hands(max_num_hands=2)    # quantidade maxima 
                                            # de maos que serao 
                                            # detectadas

    mpDwaw = mp.solutions.drawing_utils # configuracao da
                                        # biblioteca do mediapipe
                                        # para funcoes
                                        # relacionadas a desenhos
    

    
    # Main Loop #################################################
    while(True):
        ret,video = frame.read()    # captura cada frame do video
        video = cv.flip(video,1)    # inverte o video
    
    
        # cria o retangulo de display que mostrara o numero de
        # dedos levantados
        cv.rectangle(video,(20,20),(170,170),color_background,cv.FILLED)
    
    
        # FPS section ###########################################
        fps,t0,t1 = countFPS(t0,t1)     # conta quantos frames 
                                        # por segundo o video 
                                        # esta conseguindo 
                                        # capturar
    
        # printa o resultado do fps dentro do retangulo display
        cv.putText(video, f"FPS: {fps}",(200,50),cv.FONT_HERSHEY_PLAIN,2,color_text,3)
    

        # Finger Numbers ########################################

        results = Hands.process(video)  # faz o processamento do
                                        # video visando encontrar 
                                        # padroes similares a 
                                        # uma mao

        # obtem as coordenadas dos pontos das maos
        handPoints = results.multi_hand_landmarks   

        # extrai as dimensoes do video: sua altura e sua largura
        altura, largura, _ = video.shape    

        # lista contendo os pontos
        pontos = []
    
        # se existem coordenadas da mao, isto e, um objeto 
        # parecido com uma mao foi encontrado no video
        if handPoints:

            # para cada ponto obtida a partir da mao
            for points in handPoints:

                # desenhe no video os pontos e suas conexoes
                mpDwaw.draw_landmarks(video, points,hands.HAND_CONNECTIONS)

                # podemos enumerar esses pontos da seguinte 
                # forma:
                #
                # para cada ponto, obtemos seu id e suas
                # coordenadas (x,y)
                for id, cord in enumerate(points.landmark):

                    # obtem as coordenadas corretas dos pontos ao
                    # se multiplicar pela dimensao da imagem
                    cx, cy = int(cord.x * largura), int(cord.y * altura)

                    # mostra no video o id dos pontos nas maos
                    # (a implementacao da biblioteca da um id 
                    # a certos pontos cruciais das maos)
                    cv.putText(video,str(id),(cx,cy+10),cv.FONT_HERSHEY_PLAIN,1,color_text,2)

                    pontos.append((cx,cy))  # coloca as 
                                            # coordenadas dentro
                                            # da lista de
                                            # pontos atuais
        
                # lista com o id dos pontos superiores dos dedos
                dedos = [8,12,16,20]

                # conta o numero de dedos levantados
                numero_dedos = countDedos(pontos,dedos)
        
                # printa o resultado do numero de dedos
                # dentro do retangulo de display
                cv.putText(video, f"{numero_dedos}",(48,153),cv.FONT_HERSHEY_PLAIN,10,color_text,3)

        #########################################################
    
    
        # exibe os videos obtidos a partir da camera #
        cv.imshow("video",video) 
    
        # waitKey retorna o código ascii do caractere pressionado   
        # ord(q) retorna o código ascii do caractere 'q'            
        if cv.waitKey(1) == ord('q'): break
    
    #############################################################
    
    # Fecha o acesso a camera e tambem as janeas #
    frame.release()
    cv.destroyAllWindows()
