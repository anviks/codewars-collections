"""https://www.codewars.com/kata/52423db9add6f6fc39000354"""


class GameOfLife:
    def __init__(self, cells: list[list[int]]):
        self.grid = {i + j * 1j
                     for i in range(len(cells))
                     for j in range(len(cells[i]))
                     if cells[i][j] == 1}

    def progress_generations(self, generations: int):
        for _ in range(generations):
            locations_to_check = set()
            for ij in self.grid:
                locations_to_check.add(ij)
                locations_to_check.update(self.get_neighbours(ij))

            new_grid = self.grid.copy()

            for ij in locations_to_check:
                live_neighbours = len(list(self.get_live_neighbours(ij)))
                if not (2 <= live_neighbours <= 3):
                    new_grid.discard(ij)
                elif live_neighbours == 3:
                    new_grid.add(ij)

            self.grid = new_grid

    def get_live_neighbours(self, location: complex):
        return (neighbour for neighbour in self.get_neighbours(location) if neighbour in self.grid)

    @staticmethod
    def get_neighbours(location: complex):
        x, y = location.real, location.imag
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    yield complex(x + dx, y + dy)

    def grid_to_list(self) -> list[list[int]]:
        x_coords, y_coords = zip(*((coord.real, coord.imag) for coord in self.grid))
        min_x, max_x = int(min(x_coords)), int(max(x_coords))
        min_y, max_y = int(min(y_coords)), int(max(y_coords))

        return [
            [1 if complex(x, y) in self.grid else 0 for y in range(min_y, max_y + 1)]
            for x in range(min_x, max_x + 1)
        ]


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    game = GameOfLife(cells)
    game.progress_generations(generations)
    return game.grid_to_list()
