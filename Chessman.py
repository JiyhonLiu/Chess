#-*- conding:utf-8 -*-
import pygame

red = (255,0,0)
green = (0,255,0)
#font = pygame.font.Font("simsun.ttc", 36)
#SCREEN_SIZE=(560,630)
name_id_list = [u'车',u'马',u'相',u'士',u'帅',u'士',u'相',u'马',
                u'车',u'炮',u'炮',u'兵',u'兵',u'兵',u'兵',u'兵']
name_id_list2 = [u'車',u'马',u'象',u'仕',u'将',u'仕',u'象',u'马',
                 u'車',u'炮',u'炮',u'卒',u'卒',u'卒',u'卒',u'卒']
#list = 
class chessman(object):
    #id = 0
    SCREEN_SIZE=(560,630)
    def __init__(self,name,color,chess_id):
        self.name = name
        self.color = color
        self.id = chess_id
        self.position = (0,0)
        #self.picture = pygame.image.load('back2.jpg').convert()
    def grid(self,x,y):
        gridX = chessman.SCREEN_SIZE[0] * x / 8.0 + 10
        gridY = chessman.SCREEN_SIZE[1] * y / 9.0 + 10
        return (gridX,gridY)
    def move(self,gridX,gridY):
        pass
    def disappear(self,Chchess):
        self.position = (-1,-1)
    def eat(self,chess_man):
        del chess_man

class che(chessman):
    def __init__(self,color,chess_id):
        chessman.__init__(self,u'车',color,chess_id)
        #self.color = color
        if self.color == red:
            if self.id == 1:
                self.position = (1,10)
            if self.id == 9:
                self.position = (9,10)
        if self.color == green:
            self.name = name_id_list2[self.id-1]
            if self.id == 1:
                self.position = (1,1)
            if self.id == 9:
                self.position = (9,1)
    def move(self,gridX,gridY,Chchess):
        destination = (gridX+1,gridY+1)
        hinder = get_hinder(self.position,destination,Chchess.get_mans())
        if hinder == 0:
            #print 'hinder = 0'
            if self.color == red:
                for man in Chchess.red_list:
                    if destination == man.position:
                        return False
            if self.color == green:
                for man in Chchess.green_list:
                    if destination == man.position:
                        return False
            self.position = destination
            return True
        else:
            return False
            
class ma(chessman):
    def __init__(self,color,chess_id):
        chessman.__init__(self,u'马',color,chess_id)
        if self.color == red:
            if self.id == 2:
                self.position = (2,10)
            if self.id == 8:
                self.position = (8,10)
        if self.color == green:
            self.name = name_id_list2[self.id-1]
            if self.id == 2:
                self.position = (2,1)
            if self.id == 8:
                self.position = (8,1)
    def move(self,gridX,gridY,Chchess):
        flag = False
        X,Y = gridX+1,gridY+1
        if self.color == red:
            for man in Chchess.red_list:
                if man.position == (X,Y):
                    return False
        if self.color == green:
            for man in Chchess.green_list:
                if man.position == (X,Y):
                    return False
        #destination = (gridX+1,gridY+1)
        #X,Y = gridX+1,gridY+1
        a,b = self.position[0],self.position[1]
        if self.position[0]==(X-1) and self.position[1]==(Y-2):
            if not judge_position((a,b+1),Chchess):
                flag = True
        elif self.position[0]==(X+1) and self.position[1]==(Y-2):
            if not judge_position((a,b+1),Chchess):
                flag = True
        elif self.position[0]==(X-2) and self.position[1]==(Y-1):
            if not judge_position((a+1,b),Chchess):
                flag = True
        elif self.position[0]==(X-2) and self.position[1]==(Y+1):
            if not judge_position((a+1,b),Chchess):
                flag = True
        elif self.position[0]==(X+2) and self.position[1]==(Y+1):
            if not judge_position((a-1,b),Chchess):
                flag = True
        elif self.position[0]==(X+2) and self.position[1]==(Y-1):
            if not judge_position((a-1,b),Chchess):
                flag = True
        elif self.position[0]==(X+1) and self.position[1]==(Y+2):
            if not judge_position((a,b-1),Chchess):
                flag = True
        elif self.position[0]==(X-1) and self.position[1]==(Y+2):
            if not judge_position((a,b-1),Chchess):
                flag = True

        if flag:
            self.position = (X,Y)
        return flag

class xiang(chessman):
    def __init__(self,color,chess_id):
        chessman.__init__(self,u'相',color,chess_id)
        if self.color == red:
            if self.id == 3:
                self.position = (3,10)
            if self.id == 7:
                self.position = (7,10)
        if self.color == green:
            self.name = name_id_list2[self.id-1]
            if self.id == 3:
                self.position = (3,1)
            if self.id == 7:
                self.position = (7,1)
    def move(self,gridX,gridY,Chchess):
        flag = False
        X,Y = gridX+1,gridY+1
        if self.color == red:
            for man in Chchess.red_list:
                if man.position == (X,Y):
                    return False
        if self.color == green:
            for man in Chchess.green_list:
                if man.position == (X,Y):
                    return False
        a,b = self.position[0],self.position[1]
        if self.position[0]==(X+2) and self.position[1]==(Y+2):
            if not judge_position((a-1,b-1),Chchess):
                flag = True
        elif self.position[0]==(X+2) and self.position[1]==(Y-2):
            if not judge_position((a-1,b+1),Chchess):
                flag = True
        elif self.position[0]==(X-2) and self.position[1]==(Y+2):
            if not judge_position((a+1,b-1),Chchess):
                flag = True
        elif self.position[0]==(X-2) and self.position[1]==(Y-2):
            if not judge_position((a+1,b+1),Chchess):
                flag = True
        if flag:
            self.position = (X,Y)
        return flag

class shi(chessman):
    def __init__(self,color,chess_id):
        chessman.__init__(self,u'士',color,chess_id)
        if self.color == red:
            if self.id == 4:
                self.position = (4,10)
            if self.id == 6:
                self.position = (6,10)
        if self.color == green:
            self.name = name_id_list2[self.id-1]
            if self.id == 4:
                self.position = (4,1)
            if self.id == 6:
                self.position = (6,1)
    def move(self,gridX,gridY,Chchess):
        flag = False
        X,Y = gridX+1,gridY+1
        #
        if self.color == red:
            for man in Chchess.red_list:
                if man.position == (X,Y):
                    return False
        if self.color == green:
            for man in Chchess.green_list:
                if man.position == (X,Y):
                    return False
        #
        if X>6 or X<4:
            return False
        if self.color == red:
            if Y<8:
                return False
        if self.color == green:
            if Y>3:
                return False
        #
        if self.position[0]==(X+1) and self.position[1]==(Y+1):
            flag = True
        elif self.position[0]==(X-1) and self.position[1]==(Y+1):
            flag = True
        elif self.position[0]==(X+1) and self.position[1]==(Y-1):
            flag = True
        elif self.position[0]==(X-1) and self.position[1]==(Y-1):
            flag = True

        if flag:
            self.position = (X,Y)
        return flag

class jiang(chessman):
    def __init__(self,color,chess_id):
        chessman.__init__(self,u'帅',color,chess_id=5)
        if self.color == red:
            self.position = (5,10)
        if self.color == green:
            self.name = name_id_list2[self.id-1]
            self.position = (5,1)
    def disappear(self,Chchess):
        self.position = (-1,-1)
        #Chchess.over(self.color)
    def move(self,gridX,gridY,Chchess):
        flag = False
        X,Y = gridX+1,gridY+1
        #
        if self.color == red:
            for man in Chchess.red_list:
                if man.position == (X,Y):
                    return False
        if self.color == green:
            for man in Chchess.green_list:
                if man.position == (X,Y):
                    return False
        #
        if X>6 or X<4:
            return False
        if self.color == red:
            if Y<8:
                return False
        if self.color == green:
            if Y>3:
                return False
        #
        if self.position[0]==(X) and self.position[1]==(Y+1):
            flag = True
        elif self.position[0]==(X) and self.position[1]==(Y-1):
            flag = True
        elif self.position[0]==(X+1) and self.position[1]==(Y):
            flag = True
        elif self.position[0]==(X-1) and self.position[1]==(Y):
            flag = True

        if flag:
            self.position = (X,Y)
        return flag

class pao(chessman):
    def __init__(self,color,chess_id):
        chessman.__init__(self,u'炮',color,chess_id)
        if self.color == red:
            if self.id == 10:
                self.position = (2,8)
            if self.id == 11:
                self.position = (8,8)
        if self.color == green:
            self.name = name_id_list2[self.id-1]
            if self.id == 10:
                self.position = (2,3)
            if self.id == 11:
                self.position = (8,3)
    def move(self,gridX,gridY,Chchess):
        destination = (gridX+1,gridY+1)
        hinder = get_hinder(self.position,destination,Chchess.get_mans())
        if hinder == 0:
            #print 'hinder = 0'
            if judge_position(destination,Chchess):
                return False
            self.position = destination
            return True
        elif hinder == 1:
            if judge_position(destination,Chchess):
                color = judge_position(destination,Chchess)
                if color != self.color:
                    self.position = destination
                    return True
        else:
            return False

class bing(chessman):
    def __init__(self,color,chess_id):
        chessman.__init__(self,u'兵',color,chess_id)
        if self.color == red:
            if self.id == 12:
                self.position = (1,7)
            if self.id == 13:
                self.position = (3,7)
            if self.id == 14:
                self.position = (5,7)
            if self.id == 15:
                self.position = (7,7)
            if self.id == 16:
                self.position = (9,7)
        if self.color == green:
            self.name = name_id_list2[self.id-1]
            if self.id == 12:
                self.position = (1,4)
            if self.id == 13:
                self.position = (3,4)
            if self.id == 14:
                self.position = (5,4)
            if self.id == 15:
                self.position = (7,4)
            if self.id == 16:
                self.position = (9,4)
    def move(self,gridX,gridY,Chchess):
        flag = False
        if self.color == red:
            if self.position[0]==(gridX+1):
                if self.position[1]==(gridY+2):
                    self.position = (gridX+1,gridY+1)
                    flag = True
            if self.position[1]<=5:
                if self.position[1]==(gridY+1):
                    if self.position[0]==gridX or self.position[0]==(gridX+2):
                        self.position = (gridX+1,gridY+1)
                        flag = True
        if self.color == green:
            if self.position[0]==(gridX+1):
                if self.position[1]==gridY:
                    self.position = (gridX+1,gridY+1)
                    flag = True
            if self.position[1]>=6:
                if self.position[1]==(gridY+1):
                    if self.position[0]==gridX or self.position[0]==(gridX+2):
                        self.position = (gridX+1,gridY+1)
                        flag = True
        #if flag:
            #print self.position
        return flag

def maninit(color):
    man_list = []
    man_list.append(che(color,1))
    man_list.append(che(color,9))
    man_list.append(ma(color,2))
    man_list.append(ma(color,8))
    man_list.append(xiang(color,3))
    man_list.append(xiang(color,7))
    man_list.append(shi(color,4))
    man_list.append(shi(color,6))
    man_list.append(jiang(color,5))
    man_list.append(pao(color,10))
    man_list.append(pao(color,11))
    man_list.append(bing(color,12))
    man_list.append(bing(color,13))
    man_list.append(bing(color,14))
    man_list.append(bing(color,15))
    man_list.append(bing(color,16))
    return man_list
def get_hinder(position1,position2,man_list):
    hinder = 0
    if position1[0]==position2[0]:
        for man in man_list:
            position_ = man.position
            if man.position[0]==position1[0]:
                if position1[1]<position_[1]<position2[1]:
                    hinder += 1
                    #print position1,position_,position2
                if position2[1]<position_[1]<position1[1]:
                    hinder += 1
                    #print position1,position_,position2
        return hinder
    elif position1[1]==position2[1]:
        for man in man_list:
            position_ = man.position
            if man.position[1]==position1[1]:
                if position1[0]<position_[0]<position2[0]:
                    hinder += 1
                    #print position1,position_,position2
                if position2[0]<position_[0]<position1[0]:
                    hinder += 1
                    #print position1,position_,position2
        return hinder
    else:
        return -1
        
def judge_position(position,Chchess):
    #print 'judge'
    for man in Chchess.get_mans():
        if man.position == position:
            return man.color
    return False





    
    
