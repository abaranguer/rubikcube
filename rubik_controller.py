#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rubik_model import RubikCube
from rubik_view import RubikCubeGui
from rubik_archiver import RubikArchiver

class RubikController:
    model = None
    gui = None
    archiver = None

    translator={'R':'red', 'G':'green', 'B':'blue',  'W':'white', 'Y':'yellow', 'P':'pink', 'O':'orange'}

    def __init__(self):
        self.model = RubikCube()
        self.archiver = RubikArchiver()
        self.archiver.loadCube(self.model)
        self.gui = RubikCubeGui(self) 
            
    def translateList(self, colorList):
        ret = []
        for element in colorList:
            ret.append(self.translator[element])

        return ret

    def newGame(self):
        self.model.newGame()

    def freshCube(self):
        self.model.freshCube()

    def quit(self):
        self.archiver.saveCube(self.model)
        exit(0)

    def getBlockColorListBottom(self):
        blockColorList = self.model.getBottom()
        return self.translateList(blockColorList) 

    def getBlockColorListTop(self):
        blockColorList = self.model.getTop()
        return self.translateList(blockColorList) 

    def getBlockColorListFront(self):
        blockColorList = self.model.getFront()
        return self.translateList(blockColorList) 

    def getBlockColorListBack(self):
        blockColorList = self.model.getBack()
        return self.translateList(blockColorList) 

    def getBlockColorListLeft(self):
        blockColorList = self.model.getLeft()
        return self.translateList(blockColorList) 

    def getBlockColorListRight(self):
        blockColorList = self.model.getRight()
        return self.translateList(blockColorList) 

    def move(self, movement):
        if movement==1:
            self.model.movement1()
        elif movement==2:
            self.model.movement2()
        elif movement==3:
            self.model.movement3()
        elif movement==4:
            self.model.movement4()
        elif movement==5:
            self.model.movement5()
        elif movement==6:
            self.model.movement6()
        elif movement==7:
            self.model.movement7()
        elif movement==8:
            self.model.movement8()
        elif movement==9:
            self.model.movement9()
        
