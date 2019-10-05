#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: Sep 2019
# This program changes the background of the Pybadge

import ugame
import stage

# an image bank of CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# the list of the sprites that will be on the device
sprites = []


def main():
    # this functionm is a scene

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # creating the sprites
    alien = stage.Sprite(image_bank_1, 7, 64, 56)
    sprites.append(alien)
    ship = stage.sprites(image_bank_1, 8, 75, 56)
    sprites.insert(0, ship)

    # create a stage for the background to show up
    # setting the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # setting the layers to show them in order
    game.layers = sprites + [background]
    # rendering the background and the locations of the sprites
    game.render_block()

    # repeat forever game loop
    while True:

        # redraw sprites
        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    main()
