import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director

class Me(actions.Move):
  def step(self, dt):
    super(Me, self).step(dt)
    velocity_x = 100 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
    velocity_y = 100 * (keyboard[key.UP] - keyboard[key.DOWN])
    self.target.velocity = (velocity_x, velocity_y)
    

def main():
  global keyboard
  director.init(width=500, height=300, do_not_scale=True, resizable=True)
  player_layer = layer.Layer()
  me = sprite.Sprite('circle6.png')
  player_layer.add(me)
  me.position = (100, 100)
  me.velocity = (0, 0)
  me.do(Me())
  main_scene = scene.Scene(player_layer)
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)
  director.run(main_scene)

main()
