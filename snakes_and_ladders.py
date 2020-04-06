# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:48:01 2020

@author: Kevin Li
"""

class SnakesLadders():

    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.player1turn = True
        self.ladders = {2:38, 7:14, 8:31, 15:26, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}
        self.snakes = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}

    def play(self, die1, die2):
        moves = die1 + die2
        if die1 != die2:
            if self.player1turn:
                self.player1 += moves
                self.player1turn = self.player1turn and False
                if self.player1 in self.ladders.keys():
                    self.player1 = self.ladders[self.player1]
                if self.player1 in self.snakes.keys():
                    self.player1 = self.snakes[self.player1]
                
            elif not self.player1turn:
                self.player2 += moves
                self.player1turn = self.player1turn and False
                if self.player2 in self.ladders.keys():
                    self.player2 = self.ladders[self.player2]
                if self.player2 in self.snakes.keys():
                    self.player2 = self.snakes[self.player2]
        else:
            if self.player1turn:
                self.player1 += moves
                self.player1turn = self.player1turn and True
                if self.player1 in self.ladders.keys():
                    self.player1 = self.ladders[self.player1]
                if self.player1 in self.snakes.keys():
                    self.player1 = self.snakes[self.player1]
            elif not self.player1turn:
                self.player2 += moves
                self.player1turn = self.player1turn and True
                if self.player2 in self.ladders.keys():
                    self.player2 = self.ladders[self.player2]
                if self.player2 in self.snakes.keys():
                    self.player2 = self.snakes[self.player2]
        print(self.player1, self.player2, self.player1turn)
                
if __name__ == "__main__":
    game = SnakesLadders()
    game.play(1, 1)
    game.play(1, 5)
    game.play(6, 2)
    game.play(1, 1)