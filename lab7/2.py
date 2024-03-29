import pygame  
import os   
  
path = r"C:\Users\Sanzhik\Desktop\2sempy\lab7\music"  
MUZ = sorted(os.listdir(path))  
  
pygame.init()  
    
pygame.display.set_caption("mp3 player")  
  
font = pygame.font.Font('freesansbold.ttf', 32)  
font1 = pygame.font.Font('freesansbold.ttf', 25)  
  
screen = pygame.display.set_mode((700,700))  
screen.fill((255, 255, 255))  
 
  
clock = pygame.time.Clock()  
listnum = 0  
play = True  
  
pygame.mixer.music.load(os.path.join('music', MUZ[0]))  
pygame.mixer.music.play(0)  
 
  
  
  
done = False  
while not done:  
    current = listnum  
    for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                    done = True  
  
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:  
                    play = not play  
                if event.key == pygame.K_RIGHT:  
                    if listnum < len(MUZ) - 1:  
                        listnum += 1  
                    else:  
                        listnum = 0  
                if event.key == pygame.K_LEFT:  
                    if listnum > 0:  
                        listnum -= 1  
                    else:  
                        listnum = len(MUZ) - 1  
    screen.fill((255,255,255))  
      
    music_text = font1.render(MUZ[listnum], True, (125, 125, 125))  
    screen.blit(music_text, (350 -music_text.get_width()//2, 350 -music_text.get_height()//2))  
    if play == False:  
        pygame.mixer.music.pause()  
        pause_text = font.render("PAUSED", False, (125, 125, 125))  
        screen.blit(pause_text, (350-pause_text.get_width()//2, 630 - pause_text.get_height()//2))  
 
    else:  
        pygame.mixer.music.unpause()  
        unpause_text = font.render("UNPAUSED", True, (125, 125, 125))  
        screen.blit(unpause_text, (350 - unpause_text.get_width()//2, 630 - unpause_text.get_height()//2))  
 
    if listnum != current:  
        pygame.mixer.music.load(os.path.join('music', MUZ[listnum]))  
        pygame.mixer.music.play(0)  
     
      
              
    pygame.display.flip()  
    clock.tick(30)