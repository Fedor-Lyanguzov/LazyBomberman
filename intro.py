#!/usr/bin/python3
"""
Template for new module
"""

from cocos.director import director
from cocos.scenes import transitions
from cocos import scene
from cocos import text

import menu

class Intro(scene.Scene):
    """ Intro, show for 5 seconds, then transit to Menu """
    
    def __init__(self):
        super().__init__()
        x, y = director.get_window_size()
        title = text.Label("Lazy Bomberman", (x/2, y/2), anchor_x="center", \
                           anchor_y="center", font_size=52)
        self.add(title)
        
    def on_enter(self):       
        director.replace( \
            transitions.JumpZoomTransition(menu.Menu(), 2.0))
        
def main():
    """ Test scene """
    director.init(width=800, height=600, autoscale=True)
    director.run(Intro())
    

if __name__ == "__main__":
    main()
