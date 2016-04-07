#!/usr/bin/python3
"""
Template for new module
"""

from cocos.director import director
from cocos.scenes import transitions
from cocos import scene
from cocos import layer
from cocos import text
from cocos.actions.interval_actions import RotateBy, Delay
from cocos.actions.instant_actions import CallFunc

import menu

class IntroScene(scene.Scene):
    def __init__(self):
        super().__init__()
        self.add(Intro())

class Intro(layer.Layer):
    """ Intro, show for 5 seconds, then transit to Menu """
    
    def __init__(self):
        super().__init__()
        x, y = director.get_window_size()
        title = text.Label("Lazy Bomberman", (x/2, y/2), anchor_x="center", \
                           anchor_y="center", font_size=52)
        self.add(title)
        self.do(RotateBy(360,2)+Delay(1)+CallFunc(self.next_scene))
            
    def next_scene(self):
        director.replace( \
            transitions.JumpZoomTransition(menu.Menu(), 2.0))
    
def main():
    """ Test scene """
    director.init(width=800, height=600, autoscale=True)
    director.run(IntroScene())
    

if __name__ == "__main__":
    main()
