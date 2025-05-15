from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Sky()
AmbientLight(color=color.rgba(255, 255, 255, 0.4))

player = FirstPersonController()
player.gravity = 0
player.cursor.visible = False

ground = Entity(
    model='plane',
    scale=(50, 1, 50),
    texture='white_cube',
    texture_scale=(20, 20),
    color=color.gray,
    collider='box'
)

rack = Entity(
    model='cube',
    position=(5, 0.5, 5),
    scale=(1, 1, 1),
    color=color.black,
    collider='box'
)

diamond = Entity(
    model='sphere',
    color=color.cyan,
    position=(5, 1.3, 5),
    scale=0.4,
    collider='box'
)
diamond.stolen = False

crosshair = Entity(parent=camera.ui, model='quad', color=color.red, scale=(0.01, 0.01), position=(0, 0))

car = Entity(
    model='cube',
    color=color.red,
    position=(15, 0.5, 15),
    scale=(2, 1, 4),
    collider='box'
)
car.active = False

message = Text('', origin=(0, 0), scale=2, color=color.lime)

def update():
    hit_info = raycast(camera.world_position, camera.forward, distance=3, ignore=[player])

    if hit_info.hit:
        target = hit_info.entity

        if target == diamond and held_keys['e'] and not diamond.stolen:
            diamond.stolen = True
            destroy(diamond)
            message.text = "💎 Now get to the getaway car!"
            car.active = True

        elif target == car and held_keys['e'] and diamond.stolen:
            message.text = "🚗 YOU ESCAPED! HEIST COMPLETE!"

app.run()
