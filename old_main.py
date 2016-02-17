from __future__ import division, print_function, unicode_literals

import pyglet
from pyglet.window import key

pyglet.resource.path.append(pyglet.resource.get_script_home())
pyglet.resource.reindex()

import cocos
from cocos import tiles, actions, layer
from cocos.director import director
"""
class DriveCar(actions.Driver):
    def step(self, dt):
        # handle input and move the car
        self.target.rotation += (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 150 * dt
        self.target.acceleration = (keyboard[key.UP] - keyboard[key.DOWN]) * 400
        if keyboard[key.SPACE]: self.target.speed = 0
        super(DriveCar, self).step(dt)
        scroller.set_focus(self.target.x, self.target.y)
"""
def main():
    global keyboard, scroller
    director.init(width=800, height=600, autoscale=False, resizable=True)
    """
    car_layer = layer.ScrollableLayer()
    car = cocos.sprite.Sprite('car.png')
    car_layer.add(car)
    car.position = (200, 100)
    car.max_forward_speed = 200
    car.max_reverse_speed = -100
    car.do(DriveCar())
    """
#   scroller.add(car_layer)
    level_map = tiles.load('test-field.tmx')
    bg_layer = level_map['bg']
    walls_layer = level_map['walls']
    scroller = layer.ScrollingManager()
    scroller.add(bg_layer)
    scroller.add(walls_layer)
    main_scene = cocos.scene.Scene(scroller)

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)
    """
    def on_key_press(key, modifier):
        if key == pyglet.window.key.Z:
            if scroller.scale == .75:
                scroller.do(actions.ScaleTo(1, 2))
            else:
                scroller.do(actions.ScaleTo(.75, 2))
        elif key == pyglet.window.key.D:
            bg_layer.set_debug(True)
    director.window.push_handlers(on_key_press)
    """
    director.run(main_scene)

if __name__ == '__main__':
    main()
    