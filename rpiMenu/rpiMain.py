#!/usr/bin/env python3
from rpiGame import Game

g = Game()

while g.running:
    # g.curr_menu.display_menu()
    g.game_loop()