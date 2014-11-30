#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class RubikCubeGui:
    #controller
    control=None

    #widgets
    root = None
    
    frame_moves1 = None
    frame_moves2 = None
    frame_moves3 = None

    frame_top = None
    face_top = []
    
    frame_back = None            
    face_back = []

    frame_left = None
    face_left = []

    frame_front = None
    face_front = []

    frame_right = None
    face_right = []

    frame_bottom = None
    face_bottom = []

    bitmap1 = None
    bitmap2 = None

    bt1 = None
    bt2 = None 
    bt3 = None
    bt4 = None
    bt5 = None
    bt6 = None
    bt7 = None
    bt8 = None
    bt9 = None

    frame_buttons = None
    btNewGame = None
    btFreshCube = None
    btQuit = None

    def __init__(self, control):
        # controller
        self.control = control

        # initialize gui
        self.root = Tk()
        self.root.geometry("550x480")
        self.root.title("Rubik's cube")
        self.root.resizable(False, False)
        self.widgets()
        self.paintCube()
        self.root.mainloop()
        
    def movement(self, moveNumber):
        self.control.move(moveNumber)
        self.paintCube()

    def newGame(self):
        self.control.newGame()
        self.paintCube()

    def freshCube(self):
        self.control.freshCube()
        self.paintCube()

    def quit(self):
        if self.areYouSure():
            self.control.quit()

    def areYouSure(self):
        return True

    def widgets(self):
        self.frame_buttons = Frame(self.root)
        self.btNewGame = Button(master=self.frame_buttons, text="New game", command=self.newGame).grid(row=1, column=1)
        self.btFreshCube = Button(master=self.frame_buttons, text="Fresh cube", command=self.freshCube).grid(row=1, column=2)
        self.btFreshCube = Button(master=self.frame_buttons, text="Quit", command=self.quit).grid(row=1, column=3)     
        self.frame_buttons.grid(row=5, column=1, columnspan=5,  padx=5, pady=5)

        # move buttons
        self.frame_moves1 = Frame(self.root) 
        self.bitmap1 = BitmapImage(file="images/arrow_down.xbm")
        self.bt1 = Button(master=self.frame_moves1, image=self.bitmap1, command=lambda: self.movement(1)).grid(column=1, row=1)
        self.bt2 = Button(master=self.frame_moves1, image=self.bitmap1, command=lambda: self.movement(2)).grid(column=2, row=1)
        self.bt3 = Button(master=self.frame_moves1, image=self.bitmap1, command=lambda: self.movement(3)).grid(column=3, row=1)  
        self.frame_moves1.grid(row=1, column=3, padx=5, pady=5)       

        self.frame_moves2 = Frame(self.root)
        self.bitmap2 = BitmapImage(file="images/arrow_right.xbm")
        self.bt4 = Button(master=self.frame_moves2, image=self.bitmap2, command=lambda: self.movement(4)).grid(column=1, row=1, sticky="E")
        self.bt5 = Button(master=self.frame_moves2, image=self.bitmap2, command=lambda: self.movement(5)).grid(column=1, row=2, sticky="E")
        self.bt6 = Button(master=self.frame_moves2, image=self.bitmap2, command=lambda: self.movement(6)).grid(column=1, row=3, sticky="E")  
        self.frame_moves2.grid(row=2, column=2, padx=5, pady=5)       

        self.frame_moves3 = Frame(self.root)
        self.bt7 = Button(master=self.frame_moves3, image=self.bitmap2, command=lambda: self.movement(7)).grid(column=1, row=1, sticky="E")
        self.bt8 = Button(master=self.frame_moves3, image=self.bitmap2, command=lambda: self.movement(8)).grid(column=1, row=2, sticky="E")
        self.bt9 = Button(master=self.frame_moves3, image=self.bitmap2, command=lambda: self.movement(9)).grid(column=1, row=3, sticky="E")  
        self.frame_moves3.grid(row=3, column=1, padx=5, pady=5)       

        # row  top side of cube 
        self.frame_top = Frame(self.root)
        for i in range(0,9):
            self.face_top.append( Canvas(master=self.frame_top, height=32, width=32, bg="black"))
            self.face_top[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
        
        self.frame_top.grid(row=2, column=3, padx=5, pady=5)

        # row in the middle
        # left side
        self.frame_left = Frame(self.root)
        for i in range(0,9):
            self.face_left.append( Canvas(master=self.frame_left, height=32, width=32, bg="black"))
            self.face_left[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
        
        self.frame_left.grid(row=3, column=2, padx=5, pady=5)

        # front side
        self.frame_front = Frame(self.root)
        for i in range(0,9):
            self.face_front.append( Canvas(master=self.frame_front, height=32, width=32, bg="black"))
            self.face_front[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
        
        self.frame_front.grid(row=3, column=3, padx=5, pady=5)

        # right side
        self.frame_right = Frame(self.root)
        for i in range(0,9):
            self.face_right.append( Canvas(master=self.frame_right, height=32, width=32, bg="black"))
            self.face_right[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
        
        self.frame_right.grid(row=3, column=4, padx=5, pady=5)

        # back side
        self.frame_back = Frame(self.root)
        for i in range(0,9):
            self.face_back.append( Canvas(master=self.frame_back, height=32, width=32, bg="black"))
            self.face_back[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
        
        self.frame_back.grid(row=3, column=5, padx=5, pady=5)

      
        # row on bottom
        self.frame_bottom = Frame(self.root)
        for i in range(0,9):
            self.face_bottom.append( Canvas(master=self.frame_bottom, height=32, width=32, bg="black"))
            self.face_bottom[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
        
        self.frame_bottom.grid(row=4, column=3, padx=5, pady=5)

    def paintCube(self):
        i=0
        blockColorList=self.control.getBlockColorListTop()
        for blockColor in blockColorList:
            self.face_top[i].configure(background=blockColor)
            self.face_top[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
            i = i+1

        self.frame_top.grid(row=2, column=3, padx=5, pady=5)

        i=0
        blockColorList=self.control.getBlockColorListLeft()
        for blockColor in blockColorList:
            self.face_left[i].configure(background=blockColor)
            self.face_left[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
            i=i+1
  
        self.frame_left.grid(row=3, column=2, padx=5, pady=5)

        i=0
        blockColorList=self.control.getBlockColorListFront()
        for blockColor in blockColorList:
            self.face_front[i].configure(background=blockColor)
            self.face_front[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
            i=i+1

        self.frame_front.grid(row=3, column=3, padx=5, pady=5)

        i=0
        blockColorList=self.control.getBlockColorListRight()
        for blockColor in blockColorList:
            self.face_right[i].configure(background=blockColor)
            self.face_right[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
            i=i+1
            
        self.frame_right.grid(row=3, column=4, padx=5, pady=5)

        i=0
        blockColorList=self.control.getBlockColorListBack()
        for blockColor in blockColorList:
            self.face_back[i].configure(background=blockColor)
            self.face_back[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
            i=i+1
            
        self.frame_back.grid(row=3, column=5, padx=5, pady=5)

        i=0
        blockColorList=self.control.getBlockColorListBottom()
        for blockColor in blockColorList:
            self.face_bottom[i].configure(background=blockColor)
            self.face_bottom[i].grid(column = i % 3, row = i / 3, padx=1, pady=1)
            i=i+1
            
        self.frame_bottom.grid(row=4, column=3, padx=5, pady=5)
 
