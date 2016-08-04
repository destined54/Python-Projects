import pygame
#initalize all modules in pygame
pygame.init()

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#set width and height of the screen (x,y)
size = (700, 500)

screen = pygame.display.set_mode(size)

#include a caption on screen
pygame.display.set_caption("My Game")

#loop until user clicks "close button"
done = False 

#clock function to manage how fast screen updates
clock = pygame.time.Clock()

#-------- Main loop ---------#
while not done:
	#---Main event loop---#
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True 
			
		#game logic(everything you need for game play) goes here#
		
		
		
		#screen-clearing code goes here#
		
		#here, we clear the screen to white. Don't put the 
		#drawing above this or they will be erased by this command
		
		#if you want a background image, replace this clear with 
		#blit'ing the background image using pygame.blit()
		screen.fill(WHITE)
		
		
		
		
		#-------- drwaing code ---------#
		pygame.draw.rect(screen, RED, (0,0, 700, 500), 0)
		#draw this 
		
		
		
		#--- Update screen with drawing
		pygame.display.flip()
		#pygame.display.update()
		
		#--limit to 60 frames per second
		clock.tick(60)

pygame.quit()
exit()
