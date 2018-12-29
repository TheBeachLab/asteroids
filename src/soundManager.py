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
import random
from pygame.locals import *

sounds = {}  # create empty dictionary of sounds


def initSoundManager():
    pygame.mixer.init()
    sounds["fire"] = pygame.mixer.Sound("../res/FIRE.WAV")
    sounds["explode1"] = pygame.mixer.Sound("../res/EXPLODE1.WAV")
    sounds["explode2"] = pygame.mixer.Sound("../res/EXPLODE2.WAV")
    sounds["explode3"] = pygame.mixer.Sound("../res/EXPLODE3.WAV")
    sounds["lsaucer"] = pygame.mixer.Sound("../res/LSAUCER.WAV")
    sounds["ssaucer"] = pygame.mixer.Sound("../res/SSAUCER.WAV")
    sounds["thrust"] = pygame.mixer.Sound("../res/THRUST.WAV")
    sounds["sfire"] = pygame.mixer.Sound("../res/SFIRE.WAV")
    sounds["extralife"] = pygame.mixer.Sound("../res/LIFE.WAV")


def playSound(soundName):
    channel = sounds[soundName].play()


def playSoundContinuous(soundName):
    channel = sounds[soundName].play(-1)


def stopSound(soundName):
    channel = sounds[soundName].stop()
