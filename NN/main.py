
# Credit to https://github.com/tecladocode/tkinter-snake
# Thank you for the game source code


import tkinter as tk
from random import randint
from PIL import Image, ImageTk

# set constants
MOVE_INCREMENT = 50
MOVES_PER_SECOND = 25
GAME_SPEED = 1000 #moves per second


# create gem class

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height = 620, 
                    background="black", highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.target_position = self.set_new_target_position()
        self.direction = "Right"

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

    def create_objects(self):
        self.create_text(
            35, 12, text=f"Score: {self.score}", tag="score",
                        fill="#fff", font=10
            )

        for x_pos, y_pos in self.snake_positions:
            self.create_image(
                x_pos, y_pos, image=self.snake_body, tag="snake"
            )

        self.create_image(*self.target_position, image=self.target, tag="target")
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    def check_collision(self):
        head_x_pos, head_y_pos = self.snake_positions[0]

        return (
            head_x_pos in (0, 600)
            or head_y_pos in (20, 620)
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

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game Over! You scored: {self.score}!",
            fill="#fff",
            font=14
        )

    def move_snake(self):
        head_x_pos, head_y_pos = self.snake_positions[0]

        if self.direction == "Left":
            new_head_pos = (head_x_pos - MOVE_INCREMENT, head_y_pos)

        elif self.direction == "Right":
            new_head_pos = (head_x_pos + MOVE_INCREMENT, head_y_pos)

        elif self.direction == "Down":
            new_head_pos = (head_x_pos, head_y_pos + MOVE_INCREMENT)

        elif self.direction == "Up":
            new_head_pos = (head_x_pos, head_y_pos - MOVE_INCREMENT)

        self.snake_positions = [new_head_pos] + self.snake_positions[:-1]

        for segment, pos in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, pos)

    def on_key_press(self, e):
        new_direction = e.keysym

        all_directions = ("Up", "Down", "Left", "Right")
        opposites = ({"Up", "Down"}, {"Left", "Right"})

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction

    def perform_actions(self):
        if self.check_collision():
            self.end_game()

        self.check_target_collision()
        self.move_snake()

        self.after(GAME_SPEED, self.perform_actions)

    def set_new_target_position(self):
        while True:
            x_pos = randint(1, 29) * MOVE_INCREMENT
            y_pos = randint(3, 30) * MOVE_INCREMENT
            food_position = (x_pos, y_pos)

            if food_position not in self.snake_positions:
                return food_position

root = tk.Tk()
root.title("snek")
root.resizable(False, False)
root.tk.call("tk", "scaling", 4.0)

board = Snake()

root.mainloop()

