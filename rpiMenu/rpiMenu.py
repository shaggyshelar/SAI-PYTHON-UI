import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = 240 / 2, 240 / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('$', self.cursor_rect.x, self.cursor_rect.y)

    # def blit_screen(self):
    #     self.game.window.blit(self.game.display, (0, 0))
    #     pygame.display.update()
    #     self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        print(" Main run_display = {}".format(self.run_display))
        while self.run_display:
            # self.game.check_events()
            # self.check_input()
            self.game.draw.rectangle((0, 0, self.game.disp.width, self.game.disp.height), (0, 0, 0))
            self.game.draw_text('SAI', 0, 0)
            self.game.draw_text("Start Game", 0, self.game.title_size_y)
            self.game.draw_text("Options", 0, self.game.title_size_y * 2)
            self.game.draw_text("Credits", 0, self.game.title_size_y * 3)
            self.draw_cursor()
            self.game.display(self.game.img)
            # self.blit_screen()
        print(" Main run_display completed")
        


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        print(" OptionsMenu run_display = {}".format(self.run_display))
        while self.run_display:
            # self.game.check_events()
            # self.check_input()
            self.game.draw.rectangle((0, 0, self.game.disp.width, self.game.disp.height), (0, 0, 0))
            self.game.draw_text('Options', 0, 0)
            self.game.draw_text("Volume", 0, self.game.title_size_y)
            self.game.draw_text("Controls", 0, self.game.title_size_y * 2)
            self.draw_cursor()
            # self.blit_screen()
        print(" OptionsMenu run_display completed")

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        print(" CreditsMenu run_display = {}".format(self.run_display))
        while self.run_display:
            # self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.draw.rectangle((0, 0, self.game.disp.width, self.game.disp.height), (0, 0, 0))
            self.game.draw_text('Credits', 0, 0)
            self.game.draw_text('Made by me', 0, self.game.title_size_y)
            # self.blit_screen()
        print(" CreditsMenu run_display completed")
        