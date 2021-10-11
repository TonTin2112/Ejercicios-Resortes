import pygame  
import numpy as np
import sys

clock = pygame.time.Clock()


pygame.init() 
screenSize = 680
win = pygame.display.set_mode((screenSize, screenSize)) #display 640x640
pygame.display.set_caption("Resorte") #Nombre de la ventana 
timeInSimulation = 0 #segundos
x1_eq = screenSize/2 -100 #Les da la posición inicial a las partículas 
y1_eq = screenSize/2      
x2_eq = screenSize/2 + 100
y2_eq = screenSize/2
x1 = x1_eq 
y1 = y1_eq
x2 = x2_eq
y2 = y2_eq

E1 = 0
E2 = 0
 
Radius = 20 #Radio de las partículas
w_1 = 1 
w_2 = 5/3
start = False

 #Para animar, lo que sucede es que entra en este while loop y no sale hasta que alguien cierre la ventana. 
while True:

    mx, my = pygame.mouse.get_pos() #Devuelve la posición del mouse en coordenadas x e y.

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #Esto le dice al loop que pare de correr cuando se aprieta la X roja.
                pygame.quit()
                sys.exit()
            

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #Apretar el Espacio para empezar la simulación
        #Esto básicamente son las condiciones iniciales. 4 Grados de libertad.
            AmplitudeX1, AmplitudeY1 = x1, y1 
            AmplitudeX2, AmplitudeY2 = x2, y2

            k1 = (AmplitudeX1 - x1_eq)*1/2 + (AmplitudeX2 - x2_eq)*1/2
            k2 = (AmplitudeX1 - x1_eq)*1/2 - (AmplitudeX2 - x2_eq)*1/2
            k3 = (AmplitudeY1 - y1_eq)*1/2 + (AmplitudeY2 - y2_eq)*1/2
            k4 = (AmplitudeY1 - y1_eq)*1/2 - (AmplitudeY2 - y2_eq)*1/2
            start = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r: #Si se pulsa la R se reinicia con las ultimas
            x1, y1 = AmplitudeX1, AmplitudeY1                        #CI simuladas.
            x2, y2 = AmplitudeX2, AmplitudeY2
            start = False 
            timeInSimulation = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Si se pulsa el ESC se reinicia la simulación.
            start = False
            x1 = x1_eq
            y1 = y1_eq
            x2 = x2_eq
            y2 = y2_eq
            timeInSimulation = 0    
    
    if start == True:
        x1 = k1*np.cos(w_1*timeInSimulation) + k2*np.cos(w_2*timeInSimulation) + x1_eq 
        x2 = k1*np.cos(w_1*timeInSimulation) - k2*np.cos(w_2*timeInSimulation) + x2_eq        
        y1 = k3*np.cos(w_1*timeInSimulation) + k4*np.cos(w_2*timeInSimulation) + y1_eq
        y2 = k3*np.cos(w_1*timeInSimulation) - k4*np.cos(w_2*timeInSimulation) + y2_eq
        
        #Energía
        E1 = 1/2*1/20*((-k1*w_1*np.sin(w_1*timeInSimulation) - k2*w_2*np.sin(w_2*timeInSimulation))**2 + (-k3*w_1*np.sin(w_1*timeInSimulation) - k4*w_2*np.sin(w_2*timeInSimulation))**2)
        E2 = 1/2*1/20*((-k1*w_1*np.sin(w_1*timeInSimulation) + k2*w_2*np.sin(w_2*timeInSimulation))**2 + (-k3*w_1*np.sin(w_1*timeInSimulation) + k4*w_2*np.sin(w_2*timeInSimulation))**2)
        
        timeInSimulation += 0.01 





    left, middle, right = pygame.mouse.get_pressed()
    if left and  x1+40>mx>x1-40 and y1+40>my>y1-40: #Esto le indica al programa que al tocar en una determinada área, la 
        x1 = mx                                     #Partícula siga el mouse.
        y1 = my
    if left and  x2+40>mx>x2-40 and y2+40>my>y2-40:
        x2 = mx
        y2 = my


    win.fill((0,0,0)) #Le da el fondo negro
    pygame.draw.circle(win, (255, 233, 0), (x1, y1), Radius, 0) #Dibuja los círculos
    pygame.draw.circle(win, (255, 0, 0), (x2, y2), Radius, 0)
    #Dibuja un rectangulo que representa la energía
    pygame.draw.rect(win, (255, 233, 0), (y1_eq -250, y1_eq + 250, E1, 30))
    pygame.draw.rect(win, (255, 0, 0), (y1_eq -250, y1_eq + 290, E2, 30))
    #Dibuja el rectangulo dándole los vetices.
    pygame.draw.polygon(win, (0, 255, 0), [(y1_eq -250, y1_eq - 150), (y1_eq - 250, y1_eq + 150), (y1_eq + 250, y1_eq + 150), (y1_eq + 250, y1_eq - 150)], 10) #draws the square
    #Dibuja los "resortes" dándole las coordenadas de los extremos, se podría meter en un for loop pero bueno quedó asi.
    pygame.draw.line(win, (0, 160, 160), (y1_eq - 250, y1_eq), (x1 - Radius,y1), width = 3)
    pygame.draw.line(win, (0, 160, 160), (x1_eq, y1_eq + 150), (x1,y1 + Radius), width = 3)
    pygame.draw.line(win, (0, 160, 160), (x1_eq, y1_eq - 150), (x1,y1 - Radius), width = 3)
    pygame.draw.line(win, (0, 160, 160), (x2 - Radius, y2), (x1 + Radius,y1), width = 3)
    pygame.draw.line(win, (0, 160, 160), (y2_eq + 250, y2_eq), (x2 + Radius,y2), width = 3)
    pygame.draw.line(win, (0, 160, 160), (x2_eq, y2_eq + 150), (x2,y2 + Radius), width = 3)
    pygame.draw.line(win, (0, 160, 160), (x2_eq, y2_eq - 150), (x2,y2 - Radius), width = 3)    
    pygame.display.update()
    clock.tick(60) #60 FPS