#!/usr/bin/env python
# -*- coding: utf-8 -*-

EMPTY = "?"
BOMB = "*"

class Board(object):
    def __init__(self,size=8):
        self.size = size;
        self.board = [[EMPTY]*self.size for i in range(self.size)]

    def draw_board(self):
        x = 0
        y = 0
        print ""
        print "{:<4}|".format(""),
        for a in range(self.size):
            print " {}".format(a),
        print ""
        print "     "," - "*self.size
        for line in self.board:
            print "{:<4}|".format(x),
            x += 1
            for elemet in line:
                print " {}".format(elemet),
            print ""
        print ""

    def add_bomb(self,x,y):
        self.board[x][y] = BOMB

    def count_sourondings_bombs(self,x,y):
        print "do it for",x,y
        bom = 0
        for a in range(x-1,x+2):
            if a-1 >= -1 and a < self.size:
                for b in range(y-1,y+2):
                    if b - 1 >= -1 and b + 1 < self.size:
                        print "{},{} - {}".format(a,b,self.board[a][b])
                        if self.board[a][b] == BOMB:
                            print "bomb found"
                            bom += 1
        self.board[x][y] = bom


    def count_bobmbs_for_all(self):
        for a in range(self.size):
            for b in range(self.size):
                if self.board[a][b] != BOMB:
                    self.count_sourondings_bombs(a,b)


