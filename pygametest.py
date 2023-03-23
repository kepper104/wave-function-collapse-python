import pygame
from random import randint
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]


class GridWindow:
    def __init__(self, grid_size, cell_size):
        self.grid_size = grid_size
        self.cell_size = cell_size

        self.WIDTH = self.grid_size * self.cell_size
        self.HEIGHT = self.grid_size * self.cell_size

        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Grid")

        self.grid = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                row.append({'lit': False, 'values': None, 'color': WHITE})
            self.grid.append(row)

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell_color = self.grid[i][j]['color']
                cell_rect = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, cell_color, cell_rect)
                if self.grid[i][j]['values'] is not None:
                    font = pygame.font.SysFont(None, int(self.cell_size * 0.5))
                    values = self.grid[i][j]['values']
                    if len(values) > 0:
                        text1 = font.render(str(values[0]), True, (0, 0, 0))
                        self.screen.blit(text1, (j * self.cell_size + self.cell_size // 2 - text1.get_width() // 2,
                                       i * self.cell_size + self.cell_size // 2 - text1.get_height() // 2))
                    if len(values) > 1:
                        text2 = font.render(str(values[1]), True, (0, 0, 0))
                        self.screen.blit(text2, (j * self.cell_size + self.cell_size // 2 - text1.get_width() // 2 + 15,
                                       i * self.cell_size + self.cell_size // 2 - text1.get_height() // 2))
                    if len(values) > 2:
                        text3 = font.render(str(values[2]), True, (0, 0, 0))
                        self.screen.blit(text3, (j * self.cell_size + self.cell_size // 2 - text1.get_width() // 2,
                                       i * self.cell_size + self.cell_size // 2 - text1.get_height() // 2 + 15))
                    if len(values) > 3:
                        text4 = font.render(str(values[3]), True, (0, 0, 0))
                        self.screen.blit(text4, (j * self.cell_size + self.cell_size // 2 - text1.get_width() // 2 + 15,
                                       i * self.cell_size + self.cell_size // 2 - text1.get_height() // 2 + 15))

                    # self.screen.blit(text, (j * self.cell_size + self.cell_size // 2 - text.get_width() // 2 + 10,
                    #                         i * self.cell_size + self.cell_size // 2 - text.get_height() // 2 + 10))

    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    print("change")
                    self.change_color(2, 2, GRAY)
                    # self.change_values(2, 2, 5)
                    self.update_screen()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // self.cell_size
                    col = pos[0] // self.cell_size
                    self.grid[row][col]['lit'] = not self.grid[row][col]['lit']
                    if self.grid[row][col]['lit']:
                        self.change_color(row, col, GRAY)
                    else:
                        self.change_color(row, col, WHITE)
                    self.update_screen()

    def external_update(self):
        self.update_screen()

    def update_screen(self):
        self.screen.fill(WHITE)
        self.draw_grid()
        pygame.display.update()
        # print("updated")

    def change_color(self, row, col, color):
        self.grid[row][col]['color'] = color

    def change_values(self, row, col, values):
        self.grid[row][col]['values'] = values

    def cycle_color(self, row, col, color):
        self.grid[row][col]['color'] = color
        # prev_color = self.grid[row][col]['color']
        # self.grid[row][col]['color']  = colors[colors.index(prev_color) + 1]

#
# window = GridWindow(5, 40)
# window.change_color(3, 3, GRAY)
# window.external_update()
# input()
# window.change_color(1, 1, GRAY)
# window.external_update()
