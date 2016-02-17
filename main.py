#!/usr/bin/python3
"""
==============
Lazy Bomberman
==============

- Load scenes
  - Menu
  - Game
- Set up director
"""
#### DEBUG ####
no_intro = False
#####################

from cocos.director import director

import intro
import menu

def main():
    """ Run Intro or Menu"""
    director.init(width=800, height=600)
    if no_intro :
        director.run(menu.Menu())
    else:
        director.run(intro.Intro())
    

if __name__ == "__main__":
    main()
