import pygame

#initialising the pygame
pygame.init()

#creating the screen
screen=pygame.display.set_mode((800,600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo_logo.png")
pygame.display.set_icon(icon)

#keeping the creen on display till we click the cross button
# game loop which keeps the game running
# if we write pass in a while true loop, the computer system will hang
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
