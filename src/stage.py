#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Copyright (C) 2008  Nick Redshaw
#    Copyright (C) 2018  Francisco Sanchez Arroyo
#

import pygame
import sys
import os
from pygame.locals import *


class Stage:

    # Set up the PyGame surface
    def __init__(self, caption, dimensions=None):
        pygame.init()

        # If no screen size is provided pick the first available mode
        if dimensions == None:
            dimensions = pygame.display.list_modes()[0]

        pygame.display.set_mode(dimensions, FULLSCREEN)
        pygame.mouse.set_visible(False)

        # pygame.display.set_mode(dimensions)

        pygame.display.set_caption(caption)
        self.screen = pygame.display.get_surface()
        self.spriteList = []
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.showBoundingBoxes = False

    # Add sprite to list then draw it as a easy way to get the bounding rect
    def addSprite(self, sprite):
        self.spriteList.append(sprite)
        sprite.boundingRect = pygame.draw.aalines(
            self.screen, sprite.color, True, sprite.draw())

    def removeSprite(self, sprite):
        self.spriteList.remove(sprite)

    def drawSprites(self):
        for sprite in self.spriteList:
            sprite.boundingRect = pygame.draw.aalines(
                self.screen, sprite.color, True, sprite.draw())
            if self.showBoundingBoxes == True:
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 sprite.boundingRect, 1)

    def moveSprites(self):
        for sprite in self.spriteList:
            sprite.move()

            if sprite.position.x < 0:
                sprite.position.x = self.width

            if sprite.position.x > self.width:
                sprite.position.x = 0

            if sprite.position.y < 0:
                sprite.position.y = self.height

            if sprite.position.y > self.height:
                sprite.position.y = 0
