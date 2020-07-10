
# Credit to https://github.com/tecladocode/tkinter-snake for source code
# Thank you for the game!!


import tkinter as tk
from random import randint
from PIL import Image, ImageTk
import random

# set constants
MOVE_INCREMENT = 20
MOVES_PER_SECOND = 15
GAME_SPEED = 1000 // MOVES_PER_SECOND
SCREEN_WIDTH = 1160
SCREEN_HEIGHT = 840

# create gem class
class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, 
                    background="black", highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.target_position = self.set_new_target_position()
        self.event = "Right"

        self.score = 0
        
        self.load_assets()
        self.create_objects()

        self.bind_all("<Key>", self.on_key_press)

        self.pack()

        self.after(GAME_SPEED, self.perform_actions)

    def load_assets(self):
        try:
            #load snek
            self.snake_body_image = Image.open("./Assets/snek.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)
            #load target
            self.target_image = Image.open("./Assets/target.png")
            self.target = ImageTk.PhotoImage(self.target_image)
        except IOError as error:
            print("error")
            root.destroy()
            raise
    # create objects for tk window
    def create_objects(self):
        # score text
        self.create_text(
            75, 30, text=f"Score: {self.score}", tag="score",
                        fill="#fff", font=8
            )

        # snake pos
        for x_pos, y_pos in self.snake_positions:
            self.create_image(
                x_pos, y_pos, image=self.snake_body, tag="snake"
            )

        self.create_image(*self.target_position, image=self.target, tag="target")
        self.create_rectangle(40, 80, 1120, 800, outline="#525d69")

        '''# Data Output
        self.create_rectangle(1140, 80, 1480, 800, outline="#525d69")
        self.create_text(
            1200, 120, text=f"Data:", tag=None, fill="#fff", font=8
        )'''
    # check for collisions
    def check_collision(self):
        head_x_pos, head_y_pos = self.snake_positions[0]
        
        return (
            head_x_pos in (40, 1120)
            or head_y_pos in (80, 800)
            or (head_x_pos, head_y_pos) in self.snake_positions[1:]
        )

    def check_target_collision(self):
        if self.snake_positions[0] == self.target_position:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])

            self.create_image(
                *self.snake_positions[-1], image=self.snake_body, tag="snake"
            )
            self.target_position = self.set_new_target_position()
            self.coords(self.find_withtag("target"), *self.target_position)
            
            score = self.find_withtag("score")
            self.itemconfigure(score, text=f"Score: {self.score}", tag="score")

    #Character movement
    def move_snake(self):
        head_x_pos, head_y_pos = self.snake_positions[0]
        # random movement
        actions = ["Right", "Left", "Up", "Down"]
        outcome = random.choice(actions)

        if self.event == "Right":
            new_head_pos = (head_x_pos + MOVE_INCREMENT, head_y_pos)

        elif self.event == "Left":
            new_head_pos = (head_x_pos - MOVE_INCREMENT, head_y_pos)

        elif self.event == "Down":
            new_head_pos = (head_x_pos, head_y_pos + MOVE_INCREMENT)

        elif self.event == "Up":
            new_head_pos = (head_x_pos, head_y_pos - MOVE_INCREMENT)

        self.snake_positions = [new_head_pos] + self.snake_positions[:-1]

        for segment, pos in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, pos)

    def on_key_press(self, e):
        new_event = e.keysym

        all_events = ("Up", "Down", "Left", "Right")
        opposites = ({"Up", "Down"}, {"Left", "Right"})

        if (new_event in all_events and {new_event, self.event} not in opposites):
            self.event = new_event

    # run functions to check for events'
    def perform_actions(self):
        if self.check_collision():
            self.end_game()

        self.check_target_collision()
        self.move_snake()

        self.after(GAME_SPEED, self.perform_actions)
    # random target location
    def set_new_target_position(self):
        while True:
            x_pos = randint(3, 55) * MOVE_INCREMENT
            y_pos = randint(5, 39) * MOVE_INCREMENT
            food_position = (x_pos, y_pos)

            if food_position not in self.snake_positions:
                return food_position

    #Check endgame
    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game Over! You scored: {self.score}!",
            fill="#fff",
            font=14
        )

root = tk.Tk()
root.title("NN-Snake")
root.resizable(False, False)
root.tk.call("tk", "scaling", 4.0)

board = Snake()

root.mainloop()

