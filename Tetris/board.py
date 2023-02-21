class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def is_valid_position(self, piece):
        for i in range(4):
            x, y = piece.x + i % 2, piece.y + i // 2
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                return False
            if self.grid[y][x] is not None:
                return False
        return True

    def add_piece(self, piece):
        for i in range(4):
            x, y = piece.x + i % 2, piece.y + i // 2
            self.grid[y][x] = piece.blocks[i]

    def clear_lines(self):
        lines_cleared = 0
        for y in range(self.height):
            if all(self.grid[y]):
                self.grid.pop(y)
                self.grid.insert(0, [None for _ in range(self.width)])
                lines_cleared += 1
        return lines_cleared

    def is_game_over(self):
        return any(self.grid[0])
