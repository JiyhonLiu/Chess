#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
from Chessman import *

class chess(object):
    pygame.init()
    font = pygame.font.Font("simsun.ttc",32)
    def __init__(self,SCREEN_SIZE=(560,630)):
        #pygame.init()
        self.SCREEN_SIZE=SCREEN_SIZE
        x=SCREEN_SIZE[0]+60
        y=SCREEN_SIZE[1]+60
        self.screen = pygame.display.set_mode((x,y),0,32)
        pygame.display.set_caption('Chess')
        #self.background = pygame.image.load('sushiplate.jpg').convert()
        self.grid_dict = {}
        for x in range(9):
            for y in range(10):
                self.grid_dict[(x,y)] = self.grid(x,y)
        self.red_list = maninit(red)
        self.green_list = maninit(green)
        #self.man_list = self.red_list + self.green_list
        self.select_point = (-1,-1)
        self.select_man = None
        self.current_color = red
        self.background = pygame.image.load('back2.jpg').convert()
        self.update()
        
        #print 'end'
    def over(self,color):
        text = ''
        if color == red:
            text = u'红方'
        if color == green:
            text = u'蓝方'
        text_surface = chess.font.render(text+u'输',True,color)
        self.screen.blit(text_surface,(305,345))
        
    def update(self):
        self.screen.blit(self.background,(0,0))
        self.drawbackground(self.screen)
        self.drawcross(self.screen)
        self.drawmans()
        self.select(self.select_point[0],self.select_point[1])
    def get_mans(self):
        return self.red_list + self.green_list
    def grid(self,x,y):
        gridX=self.SCREEN_SIZE[0] * x / 8.0 + 30
        gridY=self.SCREEN_SIZE[1] * y / 9.0 + 30
        return (gridX,gridY)
    def find_grid(self,Mouse_x,Mouse_y):
        longth = 10000
        points_list = self.grid_dict.values()
        tmp_point = (0,0)
        for point in points_list:
            tmp = (Mouse_x-point[0])**2+(Mouse_y-point[1])**2
            if longth>= tmp:
                longth = tmp
                tmp_point = point
        if longth >= 35**2:
            return None
        i = points_list.index(tmp_point)
        return self.grid_dict.keys()[i]
    
    def select(self,gridX,gridY):
        #self.drawcross(self.screen,(gridX,gridY))
        if (gridX,gridY)==(-1,-1):
            return
        x,y = self.grid(gridX,gridY)
        color = red
        pygame.draw.lines(self.screen,color,False,[(x-35,y-35),(x-10,y-35)],3)
        pygame.draw.lines(self.screen,color,False,[(x+35,y-35),(x+10,y-35)],3)
        pygame.draw.lines(self.screen,color,False,[(x-35,y+35),(x-10,y+35)],3)
        pygame.draw.lines(self.screen,color,False,[(x+35,y+35),(x+10,y+35)],3)
        pygame.draw.lines(self.screen,color,False,[(x-35,y-35),(x-35,y-10)],3)
        pygame.draw.lines(self.screen,color,False,[(x+35,y-35),(x+35,y-10)],3)
        pygame.draw.lines(self.screen,color,False,[(x-35,y+35),(x-35,y+10)],3)
        pygame.draw.lines(self.screen,color,False,[(x+35,y+35),(x+35,y+10)],3)
        
    def drawcross(self,screen,extra_point=None):
        if extra_point == None:
            points =[]
            x=0
            while x<=8:
                points += [(x,3),(x,6)]
                x+=2
            points+=[(1,2),(1,7),(7,2),(7,7)]
            color = (0,0,0)
        else:
            points = [extra_point]
            color = (200,0,0)
        #color = (0,0,0)
        for point in points:
            #print type(point)
            x,y = self.grid(point[0],point[1])
            pygame.draw.lines(screen,color,False,[(x-30,y-10),(x-10,y-10)],3)
            pygame.draw.lines(screen,color,False,[(x+30,y-10),(x+10,y-10)],3)
            pygame.draw.lines(screen,color,False,[(x-30,y+10),(x-10,y+10)],3)
            pygame.draw.lines(screen,color,False,[(x+30,y+10),(x+10,y+10)],3)
            pygame.draw.lines(screen,color,False,[(x-10,y-30),(x-10,y-10)],3)
            pygame.draw.lines(screen,color,False,[(x+10,y-30),(x+10,y-10)],3)
            pygame.draw.lines(screen,color,False,[(x-10,y+30),(x-10,y+10)],3)
            pygame.draw.lines(screen,color,False,[(x+10,y+30),(x+10,y+10)],3)
        pygame.display.update()
        
    def drawbackground(self,screen):
        color = (0,0,0)
        x=y=0
        for y in range(10):
            points=[]
            points.append(self.grid(0,y))
            points.append(self.grid(8,y))
            pygame.draw.lines(screen,color,False,points,3)
        '''while y<=SCREEN_SIZE[1]:
            pygame.draw.lines(screen,color,False,[(x,y),(x+560,y)],3)
            y+=SCREEN_SIZE[1] / 9.0'''
            
        pygame.draw.lines(screen,color,False,[self.grid(0,0),self.grid(0,9)],3)
        pygame.draw.lines(screen,color,False,[self.grid(8,0),self.grid(8,9)],3)

        x=self.SCREEN_SIZE[0] / 8.0
        for x in range(9):
            pygame.draw.lines(screen,color,False,[self.grid(x,0),self.grid(x,4)],3)
            pygame.draw.lines(screen,color,False,[self.grid(x,5),self.grid(x,9)],3)
        '''while x<SCREEN_SIZE[0]:
            pygame.draw.lines(screen,color,False,[(x,0),(x,280)],3)
            pygame.draw.lines(screen,color,False,[(x,350),(x,630)],3)
            x+=SCREEN_SIZE[0] / 8.0'''
        pygame.draw.lines(screen,color,False,[self.grid(3,0),self.grid(5,2)],3)
        pygame.draw.lines(screen,color,False,[self.grid(3,2),self.grid(5,0)],3)
        pygame.draw.lines(screen,color,False,[self.grid(3,7),self.grid(5,9)],3)
        pygame.draw.lines(screen,color,False,[self.grid(3,9),self.grid(5,7)],3)
        pygame.display.update()
    def drawman(self,chess_man):
        text_surface = chess.font.render(chess_man.name,True,chess_man.color)
        a,b = chess_man.position
        #print '(a,b)=',a,b
        x,y = self.grid(a-1,b-1)
        x1 = int(x - text_surface.get_width() / 2)
        y1 = int(y - text_surface.get_height() / 2)

        #print x1,y1
        pygame.draw.circle(self.screen,(150,150,0),(int(x),int(y)),32,0)
        pygame.draw.circle(self.screen,(255,0,0),(int(x),int(y)),32,3)
        self.screen.blit(text_surface,(x1,y1))
        #print 'drawman'
        pygame.display.update()
    def drawmans(self):
        #red_list = self.red_list
        for red_man in self.red_list:
            self.drawman(red_man)
        #green_list = maninit(green)
        for green_man in self.green_list:
            self.drawman(green_man)
            
def run():
    #SCREEN_SIZE=(560,630)
    Chchess = chess()
    clock = pygame.time.Clock()
    mainloop = True
    over = False
    while mainloop:
        #time_passed = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            '''if event.type == VIDEORESIZE:
                SCREEN_SIZE = event.size
                Chchess.screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)
                pygame.display.set_caption("Window resized to "+str(event.size))
            screen_width,screen_height = SCREEN_SIZE
            Chchess.SCREEN_SIZE = SCREEN_SIZE
            #print 'for y in'''
            '''for y in range(0, screen_height,Chchess.background.get_height()):
               for x in range(0, screen_width,Chchess.background.get_width()):
                    Chchess.screen.blit(Chchess.background,(x, y))'''
            if event.type == pygame.MOUSEBUTTONDOWN:
                #time_passed = clock.tick()
                Mouse_X,Mouse_Y = pygame.mouse.get_pos()
                #print '(Mouse_X,Mouse_Y)=',Mouse_X,Mouse_Y
                if Chchess.find_grid(Mouse_X,Mouse_Y)!=None:
                    x,y = Chchess.find_grid(Mouse_X,Mouse_Y)
                    if Chchess.select_man != None:
                        flag = Chchess.select_man.move(x,y,Chchess)
                        if flag == True:
                            if Chchess.current_color == red:
                                Chchess.current_color=green
                                #print 'green'
                            elif Chchess.current_color == green:
                                Chchess.current_color=red
                                #print 'red'
                            Chchess.select_point=(x,y)
                            for man in Chchess.get_mans():
                                if man.position == Chchess.select_man.position:
                                    if man.color != Chchess.select_man.color:
                                        man.disappear(Chchess)
                                        Chchess.update()
                                        if man.id == 5:
                                            Chchess.over(man.color)
                                            over = True
                            Chchess.select_man = None
                        else:
                            for man in Chchess.get_mans():
                                if (x+1,y+1)==man.position:
                                    if man.color == Chchess.current_color:
                                        Chchess.select_point=(x,y)
                                        Chchess.select_man = man
                    else:
                        for man in Chchess.get_mans():
                            if (x+1,y+1) == man.position:
                                if man.color == Chchess.current_color:
                                    Chchess.select_point = (x,y)
                                    Chchess.select_man = man
                    if not over:
                        Chchess.update()
            time_passed = clock.tick(100)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()
