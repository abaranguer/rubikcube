#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class RubikArchiver:
    def saveCube(self, rubik):
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

    def loadCube(self, rubik):
        if os.path.isfile("cube.data"):
            self.loadCubeFromFile(rubik)
        else:
            rubik.freshCube()
            self.saveCube(rubik)

    def loadCubeFromFile(self, rubik):
        fd = open("cube.data","r")
        data = fd.read()
        rubik.setFront([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]])
        rubik.setBack([data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17]])
        rubik.setTop([data[18],data[19],data[20],data[21],data[22],data[23],data[24],data[25],data[26]])
        rubik.setBottom([data[27],data[28],data[29],data[30],data[31],data[32],data[33],data[34],data[35]])
        rubik.setLeft([data[36],data[37],data[38],data[39],data[40],data[41],data[42],data[43],data[44]])
        rubik.setRight([data[45],data[46],data[47],data[48],data[49],data[50],data[51],data[52],data[53]])
        fd.close()
