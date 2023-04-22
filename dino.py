import pygame
import random

##### Classes #####

class OBJ(object):
    def __init__(self,x,y,image):
       self.x = x
       self.y = y
       self.xs = 0
       self.ys = 0
       self.image =  image
       
    def bl(self):
       dis.blit(self.image,(self.x,self.y))
 
    def rise(self):
      self.x+=self.xs
      self.y+=self.ys

    def SET_SPEED(self,xs,ys):
        self.xs = xs
        self.ys = ys
    
    def SET_X(self,x):
        self.x = x

    def SET_Y(self,y):
        self.y = y    
        
    def GET_X(self):
        return self.x
    
    def GET_Y(self):
        return self.y

class Background(OBJ):
    def isInEnd(self,size):
        if self.x+size <= 0:
            self.x = w
        
        
class Player(OBJ):
    def __init__(self,x,y,image):
       self.x = x
       self.y = y
       self.xs = 0
       self.ys = 0
       self.image =  image
       self.num = 0
       
    def SET_IMAGE(self,img):
        self.image = img
        
    def Animation(self,img1,img2):
        if(self.num%24 == 0):
          self.SET_IMAGE(pygame.image.load(img1))
        elif(self.num%12 == 0):
          self.SET_IMAGE(pygame.image.load(img2))
        self.num+=1
        if self.num == 25:
            self.num = 0

            
    def controll(self,step):
      keys = pygame.key.get_pressed()

      if self.y >= 226:
       if keys[pygame.K_SPACE]:
             self.ys = -step
             
      if self.y <= 50:
          
          self.ys = step+1
          
      if self.y >= 226 and self.ys > 0:
          self.ys = 0
          
      self.rise() 
      
class enemy(Background):

    def isTaching(self,obj,numx,numy):
      if self.x <= obj.x+numx and self.x >= obj.x:
         if self.y <= obj.y:
             return True
    
        
##### Create Pygame Object #####
pygame.init()
h = 450
w = 769
c = pygame.time.Clock()
dis = pygame.display.set_mode([w,h])


##### Create Background Objects #####
bg = [Background(0,200,pygame.image.load("sprite_data/bgdino.png")),
      Background(769,200,pygame.image.load("sprite_data/bgdino.png"))]

clouds = [Background(400,30,pygame.image.load("sprite_data/cloud.png")),
          Background(50,60,pygame.image.load("sprite_data/cloud.png"))]


clouds[0].SET_SPEED(-1,0)
clouds[1].SET_SPEED(-1,0)

bg[0].SET_SPEED(-3,0)
bg[1].SET_SPEED(-3,0)

##### Create Enemy Objects #####
cactus = [enemy(390,207,pygame.image.load("sprite_data/kaktos.png")),
          enemy(100,207,pygame.image.load("sprite_data/kaktos.png"))]

cactus[0].SET_SPEED(-3,0)
cactus[1].SET_SPEED(-3,0)


##### Create Player Object #####

dino = Player(30,226,pygame.image.load("sprite_data/dino.png"))


##### Fonts #####
txt = ""
score = 0
fontns =[
    pygame.font.Font("fonts_data/ARCADECLASSIC.ttf", 71),
    pygame.font.Font("fonts_data/ARCADECLASSIC.ttf", 18),
    ]




##### Main Game Loop #####
fl = True
while fl:
   
   for ev in pygame.event.get():
       if ev.type == pygame.QUIT:
         fl = False
       if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_r:
                   txt = ""
   ##### Text format and methods #####
        
   scoretxt = fontns[1].render("score "+str(score), True, (0,0,0))
   if txt == "":
    score+=1
   overtxt = fontns[0].render(txt, True, (0,0,0))

   ##### Background methods calls #####
   for i in range(len(bg)):
    bg[i].rise()
    bg[i].isInEnd(769)

   for i in range(len(clouds)):
    clouds[i].isInEnd(82)
    clouds[i].rise()
   
   ##### Player methods calls #####

   dino.controll(4) 
   dino.Animation("sprite_data/dino.png","sprite_data/dino1.png")


   ##### Enemy methods calls #####

   for i in range(len(cactus)):
     cactus[i].rise()
     cactus[i].isInEnd(40)

     if(cactus[i].isTaching(dino,50,50)):
       score = 0
       txt = "YOU LOUSE"

    
   ##### Display On Screen #####

   dis.fill((247,247,247))

   for i in range(len(bg)):
    bg[i].bl()

   for i in range(len(clouds)): 
    clouds[i].bl()

   for i in range(len(cactus)):
    cactus[i].bl()

   dino.bl()

   dis.blit(scoretxt,(10,10))
   dis.blit(overtxt,(w//2-160,h//2-100))
   pygame.display.update()
   c.tick(150)
pygame.quit() 
quit()
