import MalmoPython
import os
import json
import logging
import math
import sys
import time
import random


class PuzzleGenerator:
    """"
        Class that generates mazes for our jumping agent to solve.
        Therefore the maps that are generated require the maze
        runner to jump in order to solve the puzzle.

        Format of the mazes:
            Start block: 'emeral_block'     (default location ((0, 26, 0))
            End block: 'redstone_block'

        """
    def __init__(self, x=24, y=24, z=2):
        """Constructor
           Args
                x:  <int>   map width   (default = 24)
                y:  <int>   map height   (default = 24)
                z:  <int>   map length   (default = 24)
         """
        self.SIZE_X = x
        self.SIZE_y = y
        self.SIZE_Z = z

    def createStructure(self, method='relative'):
        """Constructor
            Args
                method:  <string>   sets the method used to generate maps   (default = 'absolute')
                    relative:   Blocks are generated relative to one another starting with the start block.
                                This generates a valid map every iteration.
                    random:     Blocks are randomly generated then tested to determine whether the map is valid

        """