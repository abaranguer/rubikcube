#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os

class RubikCube:
    cube_front = ["R","R","R","R","R","R","R","R","R"]
    cube_left = ["W","W","W","W","W","W","W","W","W"]
    cube_top = ["B","B","B","B","B","B","B","B","B"]
    cube_back = ["O","O","O","O","O","O","O","O","O"]
    cube_bottom = ["G","G","G","G","G","G","G","G","G"]
    cube_right = ["Y","Y","Y","Y","Y","Y","Y","Y","Y"]

    solved_front = ["R","R","R","R","R","R","R","R","R"]
    solved_left = ["W","W","W","W","W","W","W","W","W"]
    solved_top = ["B","B","B","B","B","B","B","B","B"]
    solved_back = ["O","O","O","O","O","O","O","O","O"]
    solved_bottom = ["G","G","G","G","G","G","G","G","G"]
    solved_right = ["Y","Y","Y","Y","Y","Y","Y","Y","Y"]

    # debug
    #cube_front = ["1","2","3","4","5","6","7","8","9"]
    #cube_left = ["a","b","c","d","e","f","g","h","i"]
    #cube_top = ["j","k","l","m","n","o","p","q","r"]
    #cube_back = ["s","t","u","v","w","x","y","z","0"]
    #cube_bottom = ["A","B","C","D","E","F","G","H","I"]
    #cube_right = ["J","K","L","M","N","O","P","Q","R"]

    #solved_front = ["1","2","3","4","5","6","7","8","9"]
    #solved_left = ["a","b","c","d","e","f","g","h","i"]
    #solved_top = ["j","k","l","m","n","o","p","q","r"]
    #solved_back = ["s","t","u","v","w","x","y","z","0"]
    #solved_bottom = ["A","B","C","D","E","F","G","H","I"]
    #solved_right = ["J","K","L","M","N","O","P","Q","R"]

    spcs1 = "    "  # four white spaces
    spcs2 = "       "  # seven white spaces

    def getFront(self):
        return self.cube_front

    def getBack(self):
        return self.cube_back

    def getLeft(self):
        return self.cube_left
     
    def getTop(self):
        return self.cube_top 
    
    def getBottom(self):
        return self.cube_bottom
    
    def getRight(self):
        return self.cube_right

    def setFront(self, values):
        self.cube_front = list(values)

    def setBack(self, values):
        self.cube_back = list(values)
    
    def setTop(self, values):
        self.cube_top = list(values)
    
    def setBottom(self, values):
        self.cube_bottom = list(values)
    
    def setRight(self, values):
        self.cube_right = list(values)
    
    def setLeft(self, values):
        self.cube_left = list(values)
    
    def show(self):
        top = "%s123" % (self.spcs2)
        top = "%s\n%s4  %s%s%s" % (top, self.spcs1, self.cube_top[0], self.cube_top[1], self.cube_top[2])
        top = "%s\n%s5  %s%s%s" % (top, self.spcs1, self.cube_top[3], self.cube_top[4], self.cube_top[5])
        top = "%s\n%s6  %s%s%s\n" % (top, self.spcs1, self.cube_top[6], self.cube_top[7], self.cube_top[8])    
        middle = "7 %s%s%s" % (self.cube_left[0], self.cube_left[1], self.cube_left[2])
        middle = "%s  %s%s%s" % (middle, self.cube_front[0], self.cube_front[1], self.cube_front[2])
        middle = "%s  %s%s%s" % (middle, self.cube_right[0], self.cube_right[1], self.cube_right[2])
        middle = "%s  %s%s%s" % (middle, self.cube_back[0], self.cube_back[1], self.cube_back[2])
        middle = "%s\n8 %s%s%s" % (middle, self.cube_left[3], self.cube_left[4], self.cube_left[5])
        middle = "%s  %s%s%s" % (middle, self.cube_front[3], self.cube_front[4], self.cube_front[5])
        middle = "%s  %s%s%s" % (middle, self.cube_right[3], self.cube_right[4], self.cube_right[5])
        middle = "%s  %s%s%s" % (middle, self.cube_back[3], self.cube_back[4], self.cube_back[5])
        middle = "%s\n9 %s%s%s" % (middle, self.cube_left[6], self.cube_left[7], self.cube_left[8])
        middle = "%s  %s%s%s" % (middle, self.cube_front[6], self.cube_front[7], self.cube_front[8])
        middle = "%s  %s%s%s" % (middle, self.cube_right[6], self.cube_right[7], self.cube_right[8])
        middle = "%s  %s%s%s\n" % (middle, self.cube_back[6], self.cube_back[7], self.cube_back[8])
        bottom = "%s%s%s%s" % (self.spcs2, self.cube_bottom[0], self.cube_bottom[1], self.cube_bottom[2])
        bottom = "%s\n%s%s%s%s" % (bottom, self.spcs2, self.cube_bottom[3], self.cube_bottom[4], self.cube_bottom[5])
        bottom = "%s\n%s%s%s%s" % (bottom, self.spcs2, self.cube_bottom[6], self.cube_bottom[7], self.cube_bottom[8])
        print " \n\nRubik's cube\n------------\n"
        print "%s\n%s\n%s\n" % (top, middle, bottom)

    def movement1(self):
        cube_aux = [self.cube_back[2], self.cube_back[5], self.cube_back[8]]
        self.cube_back[2] = self.cube_bottom[6]
        self.cube_back[5] = self.cube_bottom[3]
        self.cube_back[8] = self.cube_bottom[0]   
        self.cube_bottom[0] = self.cube_front[0]
        self.cube_bottom[3] = self.cube_front[3]
        self.cube_bottom[6] = self.cube_front[6]
        self.cube_front[0] = self.cube_top[0]
        self.cube_front[3] = self.cube_top[3]
        self.cube_front[6] = self.cube_top[6]
        self.cube_top[0] = cube_aux[2]
        self.cube_top[3] = cube_aux[1]
        self.cube_top[6] = cube_aux[0]
        cube_aux_left = self.cube_left[0]
        self.cube_left[0] = self.cube_left[6]
        self.cube_left[6] = self.cube_left[8]
        self.cube_left[8] = self.cube_left[2]
        self.cube_left[2] = cube_aux_left
        cube_aux_left = self.cube_left[1]
        self.cube_left[1] = self.cube_left[3]
        self.cube_left[3] = self.cube_left[7]
        self.cube_left[7] = self.cube_left[5]
        self.cube_left[5] = cube_aux_left

    def movement2(self):
        cube_aux = [self.cube_back[1], self.cube_back[4], self.cube_back[7]]
        self.cube_back[1] = self.cube_bottom[7]
        self.cube_back[4] = self.cube_bottom[4]
        self.cube_back[7] = self.cube_bottom[1]
        self.cube_bottom[1] = self.cube_front[1]
        self.cube_bottom[4] = self.cube_front[4]
        self.cube_bottom[7] = self.cube_front[7]
        self.cube_front[1] = self.cube_top[1]
        self.cube_front[4] = self.cube_top[4]
        self.cube_front[7] = self.cube_top[7]
        self.cube_top[1] = cube_aux[2]
        self.cube_top[4] = cube_aux[1]
        self.cube_top[7] = cube_aux[0]

    def movement3(self):
        cube_aux = [self.cube_top[2], self.cube_top[5], self.cube_top[8]]
        self.cube_top[2] = self.cube_back[6]
        self.cube_top[5] = self.cube_back[3]
        self.cube_top[8] = self.cube_back[0]
        self.cube_back[0] = self.cube_bottom[8]
        self.cube_back[3] = self.cube_bottom[5]
        self.cube_back[6] = self.cube_bottom[2]
        self.cube_bottom[2] = self.cube_front[2]
        self.cube_bottom[5] = self.cube_front[5]
        self.cube_bottom[8] = self.cube_front[8]
        self.cube_front[2] = cube_aux[0]
        self.cube_front[5] = cube_aux[1]
        self.cube_front[8] = cube_aux[2]
        cube_aux_right = self.cube_right[0]
        self.cube_right[0] = self.cube_right[2]
        self.cube_right[2] = self.cube_right[8]    
        self.cube_right[8] = self.cube_right[6]
        self.cube_right[6] = cube_aux_right
        cube_aux_right = self.cube_right[1]
        self.cube_right[1] = self.cube_right[5]
        self.cube_right[5] = self.cube_right[7]
        self.cube_right[7] = self.cube_right[3]
        self.cube_right[3] = cube_aux_right

    def movement4(self):
        cube_aux = [self.cube_top[0], self.cube_top[1], self.cube_top[2]]
        self.cube_top[0] = self.cube_left[6]
        self.cube_top[1] = self.cube_left[3]
        self.cube_top[2] = self.cube_left[0]
        self.cube_left[0] = self.cube_bottom[6]
        self.cube_left[3] = self.cube_bottom[7]
        self.cube_left[6] = self.cube_bottom[8]
        self.cube_bottom[6] = self.cube_right[8]
        self.cube_bottom[7] = self.cube_right[5]
        self.cube_bottom[8] = self.cube_right[2]
        self.cube_right[2] = cube_aux[0]
        self.cube_right[5] = cube_aux[1]
        self.cube_right[8] = cube_aux[2]
        cube_aux_back = self.cube_back[0]
        self.cube_back[0] = self.cube_back[2]
        self.cube_back[2] = self.cube_back[8]
        self.cube_back[8] = self.cube_back[6]
        self.cube_back[6] = cube_aux_back
        cube_aux_back = self.cube_back[1]
        self.cube_back[1] = self.cube_back[5]
        self.cube_back[5] = self.cube_back[7]
        self.cube_back[7] = self.cube_back[3]
        self.cube_back[3] = cube_aux_back
    
    def movement5(self):
        cube_aux = [self.cube_top[3], self.cube_top[4], self.cube_top[5]]
        self.cube_top[5] = self.cube_left[1]
        self.cube_top[4] = self.cube_left[4]
        self.cube_top[3] = self.cube_left[7]
        self.cube_left[1] = self.cube_bottom[3]
        self.cube_left[4] = self.cube_bottom[4]
        self.cube_left[7] = self.cube_bottom[5]
        self.cube_bottom[5] = self.cube_right[1]
        self.cube_bottom[4] = self.cube_right[4]
        self.cube_bottom[3] = self.cube_right[7]
        self.cube_right[1] = cube_aux[0]
        self.cube_right[4] = cube_aux[1]
        self.cube_right[7] = cube_aux[2]

    def movement6(self):
        cube_aux = [self.cube_top[6], self.cube_top[7], self.cube_top[8]]
        self.cube_top[6] = self.cube_left[8]
        self.cube_top[7] = self.cube_left[5]
        self.cube_top[8] = self.cube_left[2]
        self.cube_left[2] = self.cube_bottom[0]
        self.cube_left[5] = self.cube_bottom[1]
        self.cube_left[8] = self.cube_bottom[2]
        self.cube_bottom[0] = self.cube_right[6]
        self.cube_bottom[1] = self.cube_right[3]
        self.cube_bottom[2] = self.cube_right[0]
        self.cube_right[0] = cube_aux[0]
        self.cube_right[3] = cube_aux[1]
        self.cube_right[6] = cube_aux[2]
        cube_aux_front = self.cube_front[0]
        self.cube_front[0] = self.cube_front[6]
        self.cube_front[6] = self.cube_front[8]
        self.cube_front[8] = self.cube_front[2]
        self.cube_front[2] = cube_aux_front
        cube_aux_front = self.cube_front[1]
        self.cube_front[1] = self.cube_front[3]
        self.cube_front[3] = self.cube_front[7]
        self.cube_front[7] = self.cube_front[5]
        self.cube_front[5] = cube_aux_front

    def movement7(self):
        cube_aux = [self.cube_back[0], self.cube_back[1], self.cube_back[2]]
        self.cube_back[0] = self.cube_right[0]
        self.cube_back[1] = self.cube_right[1]
        self.cube_back[2] = self.cube_right[2]
        self.cube_right[0] = self.cube_front[0] 
        self.cube_right[1] = self.cube_front[1] 
        self.cube_right[2] = self.cube_front[2] 
        self.cube_front[0] = self.cube_left[0]
        self.cube_front[1] = self.cube_left[1]
        self.cube_front[2] = self.cube_left[2]
        self.cube_left[0] = cube_aux[0]
        self.cube_left[1] = cube_aux[1]
        self.cube_left[2] = cube_aux[2]
        cube_aux_top = self.cube_top[0]
        self.cube_top[0] = self.cube_top[2]
        self.cube_top[2] = self.cube_top[8]
        self.cube_top[8] = self.cube_top[6]
        self.cube_top[6] = cube_aux_top
        cube_aux_top = self.cube_top[3]
        self.cube_top[3] = self.cube_top[1]
        self.cube_top[1] = self.cube_top[5]
        self.cube_top[5] = self.cube_top[7]
        self.cube_top[7] = cube_aux_top

    def movement8(self):
        cube_aux = [self.cube_back[3], self.cube_back[4], self.cube_back[5]]
        self.cube_back[3] = self.cube_right[3]
        self.cube_back[4] = self.cube_right[4]
        self.cube_back[5] = self.cube_right[5]
        self.cube_right[3] = self.cube_front[3]
        self.cube_right[4] = self.cube_front[4]
        self.cube_right[5] = self.cube_front[5]
        self.cube_front[3] = self.cube_left[3]
        self.cube_front[4] = self.cube_left[4]
        self.cube_front[5] = self.cube_left[5]
        self.cube_left[3] = cube_aux[0]
        self.cube_left[4] = cube_aux[1]
        self.cube_left[5] = cube_aux[2]

    def movement9(self):
        cube_aux = [self.cube_back[6], self.cube_back[7], self.cube_back[8]]
        self.cube_back[6] = self.cube_right[6]
        self.cube_back[7] = self.cube_right[7]
        self.cube_back[8] = self.cube_right[8]
        self.cube_right[6] = self.cube_front[6] 
        self.cube_right[7] = self.cube_front[7] 
        self.cube_right[8] = self.cube_front[8] 
        self.cube_front[6] = self.cube_left[6]
        self.cube_front[7] = self.cube_left[7]
        self.cube_front[8] = self.cube_left[8]
        self.cube_left[6] = cube_aux[0]
        self.cube_left[7] = cube_aux[1]
        self.cube_left[8] = cube_aux[2]
        cube_aux_bottom = self.cube_bottom[0]
        self.cube_bottom[0] = self.cube_bottom[6]
        self.cube_bottom[6] = self.cube_bottom[8]
        self.cube_bottom[8] = self.cube_bottom[2]
        self.cube_bottom[2] = cube_aux_bottom
        cube_aux_bottom = self.cube_bottom[3]
        self.cube_bottom[3] = self.cube_bottom[7]
        self.cube_bottom[7] = self.cube_bottom[5]
        self.cube_bottom[5] = self.cube_bottom[1]
        self.cube_bottom[1] = cube_aux_bottom

    def freshCube(self):
        self.cube_front = list(self.solved_front)
        self.cube_left = list(self.solved_left)
        self.cube_top = list(self.solved_top)
        self.cube_back = list(self.solved_back)
        self.cube_bottom = list(self.solved_bottom)
        self.cube_right = list(self.solved_right)

    def newGame(self):    
        for i in range(0,25):
            n = random.randint(1,9)
            if n==1:
                self.movement1()
            elif n==2:
                self.movement2()
            elif n==3:
                self.movement3()
            elif n==4:
                self.movement4()
            elif n==5:
                self.movement5()
            elif n==6:
                self.movement6()
            elif n==7:
                self.movement7()
            elif n==8:
                self.movement8()              
            elif n==9:
                self.movement9()

    
def saveCube(rubik):
    fd = open("cube.data","w")

    for value in rubik.getFront():
        fd.write(value)
    
    for value in rubik.getBack():
        fd.write(value)
    
    for value in rubik.getTop():
        fd.write(value)

    for value in rubik.getBottom():
        fd.write(value)

    for value in rubik.getLeft():
        fd.write(value)

    for value in rubik.getRight():
        fd.write(value)
    
    fd.close()

def loadCube(rubik):
    if os.path.isfile("cube.data"):
        loadCubeFromFile(rubik)
    else:
        rubik.freshCube()
        saveCube()

def loadCubeFromFile(rubik):
    fd = open("cube.data","r")
    data = fd.read()
    rubik.setFront([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]])
    rubik.setBack([data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17]])
    rubik.setTop([data[18],data[19],data[20],data[21],data[22],data[23],data[24],data[25],data[26]])
    rubik.setBottom([data[27],data[28],data[29],data[30],data[31],data[32],data[33],data[34],data[35]])
    rubik.setLeft([data[36],data[37],data[38],data[39],data[40],data[41],data[42],data[43],data[44]])
    rubik.setRight([data[45],data[46],data[47],data[48],data[49],data[50],data[51],data[52],data[53]])
    fd.close()

if __name__ == "__main__":
    rubik = RubikCube()
     
    while(True):
        rubik.show()
        order = raw_input("(1-9)-movements; 'n','N'-new game; 'f','F'-fresh cube; 'e','E'-exit game; 'l','L'-load cube. ")

        if order=="e" or order=="E":
            saveCube(rubik)
            exit(0)
        elif order=="l" or order=="L":
            loadCube(rubik)
        elif order=="n" or order=="N":
            rubik.newGame()
        elif order=="f" or order=="F":
            rubik.freshCube()
        elif order=="1":
            rubik.movement1() 
        elif order=="2":
            rubik.movement2() 
        elif order=="3":
            rubik.movement3() 
        elif order=="4":
            rubik.movement4() 
        elif order=="5":
            rubik.movement5() 
        elif order=="6":
            rubik.movement6() 
        elif order=="7":
            rubik.movement7() 
        elif order=="8":
            rubik.movement8() 
        elif order=="9":
            rubik.movement9()
