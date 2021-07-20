import pygame as pg
import random
import time
#Initialization of pygame
pg.init()
"""
class Food():
    def __init__(self):
        self.x=screen_width/2 #Location of snake initially
        self.y=screen_height/2
        self.color=blue
        self.width=10   #snake dimensions
        self.height=10
    def draw_food(self,surface):
        self.food=pg.Rect(self.x,self.y,self.width,self.height) #Object for storing rectangular position
        pg.draw.rect(surface,self.color,self.food)
    #Checking if food if eaten?
    def is_eaten(self,head):
        return self.food.colliderect(head) #If the snake-head and food rectangle collide returns True
    #New location for food after being eaten
    def new_position(self):
        self.x=random.randint(0,screen_width-self.width) #Making sure the integer generated is within the screen width
        self.y=random.randint(0,screen_height-self.height)

class Snake():
    pass

"""

#defining colors (R,G,B)
red=pg.Color(255,0,0)
green=pg.Color(0,255,0)
blue=pg.Color(0,0,255)
black=pg.Color(0,0,0)
white=pg.Color(255,255,255)

#Screen variables
screen_width = 800
screen_height=800
#Making of screen window
window=pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Snake Game")


snake_block=10
snake_speed=10

#fonts
font_style=pg.font.SysFont("bahnschrift",30)
score_style=pg.font.SysFont("comicsansms",30)

def message(msg):
    mesg=font_style.render(msg,True,red)
    window.blit(mesg,[screen_width/4,screen_height/2])

def score(score):
    value=score_style.render("Your score:"+str(score),True,green)
    window.blit(value,[0,0])

def draw_snake(snake_list):
    for x in snake_list:
        pg.draw.rect(window, red, [x[0], x[1], snake_block, snake_block])


def draw_food(x,y):
    food_position=pg.Rect(x,y,snake_block,snake_block)
    pg.draw.rect(window,blue,food_position)

#Mainloop
clock=pg.time.Clock()
def main():
    game_over = False
    game_close = False

#Food positon
    food_position_width = round(random.randrange(0, screen_width - snake_block)/10.0)*10.0
    food_position_height = round(random.randrange(0, screen_height - snake_block)/10.0)*10.0
#Snake position
    snake_position_width = screen_width / 2
    snake_position_height = screen_height / 2

    x_change=0
    y_change=0

    snake_list=[]
    length_of_snake=1


    while not game_over:
        while game_close==True:
            window.fill(white)
            message("Game over!!!Press Q to quit and C to continue")
            #score(length_of_snake-1)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_c:
                        main()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over=True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pg.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pg.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pg.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        if snake_position_width>=screen_width or snake_position_width<0 or snake_position_height>=screen_height or snake_position_height<0:
            game_close=True
        snake_position_width += x_change
        snake_position_height += y_change

        window.fill(white)

        draw_food(food_position_width,food_position_height)

        snake_head = []
        snake_head.append(snake_position_width)
        snake_head.append(snake_position_height)
        snake_list.append(snake_head)
        #print(snake_list)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

#This loop is made to check if snake_Head position as occured in snake_List or not. This means the position has been added to the snake_List before and finding the same value again means that snake bites itself.

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close=True

        draw_snake(snake_list)
        score(length_of_snake-1)


        pg.display.update() #Updating the screen if any event occurs

        if snake_position_width==food_position_width and snake_position_height==food_position_height:
            food_position_width = round(random.randrange(0, screen_width - snake_block)/10.0)*10.0
            food_position_height = round(random.randrange(0, screen_height - snake_block)/10.0)*10.0
            length_of_snake += 1

        clock.tick(snake_speed)
    print("Length:",len(snake_list))
    pg.quit()
    quit()
main()

