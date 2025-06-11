import pygame
pygame.init()
tela  = pygame.display.set_mode((300,300))



         
run = True         
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False
            pygame.quit()
    tela.fill('green') 
    pygame.draw.rect(tela,('red'),(150,150,70,70))
    pygame.draw.circle(tela,('red'),(90, 50),50)
    pygame.draw.ellipse(tela,('red'),(90,120,70,90))
    pygame.display.flip()

  
    

    
