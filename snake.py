from variables import CELL_SIZE, WIDTH, HEIGHT

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)  # (x, y)

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % (WIDTH // CELL_SIZE), (head_y + dir_y) % (HEIGHT // CELL_SIZE))
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        if not (self.direction[0] + new_direction[0] == 0 and self.direction[1] + new_direction[1] == 0):
            self.direction = new_direction

    def collides_with_itself(self):
        return self.body[0] in self.body[1:]

    def get_head_position(self):
        return self.body[0]