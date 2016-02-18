#!/usr/bin/python3
"""
Template for new module
"""

from cocos.director import director
from cocos import scene
from cocos import tiles
from cocos.layer import scrolling


class Gamescene(scene.Scene):
    
    def __init__(self):
        super().__init__()
        level_map = tiles.load('test-field.tmx')
        bg_layer = level_map['bg']
        walls_layer = level_map['walls']
        scroller = scrolling.ScrollingManager()
        scroller.add(bg_layer)
        scroller.add(walls_layer)
        self.add(scroller)



def main():
    """ Test scene """
    director.init(width=800, height=600, autoscale=True)
    director.run(Intro())
    

if __name__ == "__main__":
    main()
