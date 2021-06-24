import pygame
import math 
import random

#initialising the pygame
pygame.init()

#creating the screen
# in pygame the screen is known as the surface
screen=pygame.display.set_mode((800,600))

#background image
background=pygame.image.load("space.png")

# title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo_logo.png")
pygame.display.set_icon(icon)

#player
player_img=pygame.image.load("player.png")
playerX=370
playerY=480
playerX_change=0

# creating enemy
enemy_img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
enemies_number = 6

for i in range(enemies_number):
    enemy_img.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
# dormant --> the bullet is ready to shoot but you can't see it right now
# active --> the bullet is shooting and is currently moving
bullet_img=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

# creating a variable to track the score
score=0
font = pygame.font.Font("freesansbold.ttf",28)

fontX = 10
fontY = 10



def player(x,y):
    screen.blit(player_img,(x,y))   # the "blit" command is used to draw the image on the surface # 2 parameters 1)Image 2)Co-ordinates

def enemy(x,y):
    screen.blit(enemy_img,(x,y))

def bullet_active(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(16+x,10+y))

def collision(enemyX,enemyY,bulletX,bulletY):
    dist = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if dist < 27:
        return True
    else:
        return False 

def score_visible(x,y):
    print_score = font.render(f"Score : {score}", True, (255,255,255))
    screen.blit(print_score,(x,y))

#keeping the creen on display till we click the cross button
# game loop which keeps the game running
# if we write pass in a while true loop, the computer system will hang
running = True
while running:
    # to change the background colour 
    # the 3 values stand for RGB 
    screen.fill((0,0,0))

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


        # check whether right keystroke is pressed or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change=-5

            if event.key == pygame.K_RIGHT:
                playerX_change=5

            if event.key == pygame.K_SPACE:
                # We can fire the second bullet only after the first bullet has reached the top of the screen 
                if bullet_state == "ready":
                    # saving the current value of the y-cordinate of the spaceship inside the bulletX variable
                    bulletX=playerX
                    bullet_active(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                playerX_change=0


        

         
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736   

    # to change the direction of the enemy
    for i in range (enemies_number):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

    # motion of the bullet

        collide = collision(enemyX[i],enemyY[i],bulletX[i],bulletY[i])
        if collide:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i])
    
    # this is to shoot multiple bullets
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    
    # solving the bullet following the direction of space ship by saving the value of current playerX only once in the bulletX command
    if bullet_state == "fire":
        bullet_active(bulletX,bulletY)
        bulletY -= bulletY_change 

    # collision of he bullet and the enemy
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet_active(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX,playerY) # always call this unctions after the screen.fill otherwise the image would not appear
    score_visible(fontX,fontY)
    pygame.display.update()

