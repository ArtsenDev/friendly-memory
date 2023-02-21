class Piece:
    def __init__(self, x, y, blocks):
        self.x = x
        self.y = y
        self.blocks = blocks

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        # implement rotation logic here
        pass
