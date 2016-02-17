#!/usr/bin/python3
"""
Menu scene
"""

from cocos.director import director
from cocos import scene
from cocos import menu

class Menu(scene.Scene):
    """ 
    Menu scene
    
    Consists of menu layer
    """
    def __init__(self):
        """ Collect layers into scene """
        super().__init__()
        self.add(MenuLayer())
    
class MenuLayer(menu.Menu):
    """ Menu layer """
    
    def __init__(self):
        """ Set style and caption. Add items. Generate menu """
        super().__init__("Lazy Bomberman")
        """
        self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['font_size'] = 72
        self.font_title['color'] = (204,164,164,255)

        self.font_item['font_name'] = 'Edit Undo Line BRK',
        self.font_item['color'] = (32,16,32,255)
        self.font_item['font_size'] = 32
        self.font_item_selected['font_name'] = 'Edit Undo Line BRK'
        self.font_item_selected['color'] = (32,16,32,255)
        self.font_item_selected['font_size'] = 46
        """
        items = []
        items.append(menu.MenuItem("New game", self.on_new_game))
        items.append(menu.MenuItem("Exit", self.on_exit))
        self.create_menu(items, menu.zoom_in(), menu.zoom_out())

    def on_new_game(self):
        """ Start new game """
    
    def on_exit(self):
        """ Exit game """
    
def main():
    """ Test menu scene """
    director.init(width=800, height=600, autoscale=True)
    director.run(Menu())
    

if __name__ == "__main__":
    main()
