import random
from queue import PriorityQueue

import pygame

# я ненавижу длинные названия переменных, но тут прога огромная - букв не хватит
# Инициализация Pygame
pygame.init()

# Константы
WIDTH = 600
GRID_SIZE = 30  # Размер поля NxN
CELL_SIZE = WIDTH // GRID_SIZE
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A*")

# Цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Типы ячеек
EMPTY = 0
OBSTACLE = 1
START = 2
END = 3
PATH = 4
VISITED = 5

# Словарь цветов для типов ячеек
CELL_COLORS = {
    START: ORANGE,
    END: TURQUOISE,
    OBSTACLE: BLACK,
    PATH: PURPLE,
    VISITED: RED,
    EMPTY: WHITE
}


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = EMPTY
        self.g = float('inf')  # Стоимость пути от старта
        self.h = 0  # Эвристическая оценка
        self.f = float('inf')  # Общая стоимость (g + h)
        self.parent = None  # Родительская ячейка для восстановления пути
        self.neighbors = []  # Соседние ячейки

    def get_position(self):
        return (self.row, self.col)

    def is_barrier(self):
        return self.type == OBSTACLE

    def is_start(self):
        return self.type == START

    def is_end(self):
        return self.type == END

    def reset(self):
        self.type = EMPTY
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.parent = None
        self.neighbors = []

    def make_start(self):
        self.type = START

    def make_end(self):
        self.type = END

    def make_barrier(self):
        self.type = OBSTACLE

    def make_path(self):
        if not self.is_start() and not self.is_end():
            self.type = PATH

    def make_visited(self):
        if not self.is_start() and not self.is_end():
            self.type = VISITED

    def update_neighbors(self, grid):
        self.neighbors = []
        # Проверяем четыре направления: вверх, вниз, влево, вправо
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = self.row + dr, self.col + dc
            # Проверяем, что сосед в пределах сетки
            if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
                neighbor = grid[new_row][new_col]
                if not neighbor.is_barrier():
                    self.neighbors.append(neighbor)

    def draw(self, surface):
        color = CELL_COLORS[self.type]
        pygame.draw.rect(
            surface,
            color,
            (self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )


def make_grid():
    grid = []
    for row in range(GRID_SIZE):
        grid.append([])
        for col in range(GRID_SIZE):
            cell = Cell(row, col)
            grid[row].append(cell)
    return grid


def draw_grid(win, grid):
    # Очищаем экран
    win.fill(WHITE)

    # Рисуем все ячейки
    for row in grid:
        for cell in row:
            cell.draw(win)

    # Рисуем сетку
    for i in range(GRID_SIZE + 1):
        # Горизонтальные линии
        pygame.draw.line(win, GREY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
        # Вертикальные линии
        pygame.draw.line(win, GREY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))

    pygame.display.update()


def generate_random_grid(grid):
    # Очищаем сетку
    for row in grid:
        for cell in row:
            cell.reset()

    # Выбираем случайные начальную и конечную точки
    start_row, start_col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    end_row, end_col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

    # Убедимся, что начальная и конечная точки разные
    while (start_row, start_col) == (end_row, end_col):
        end_row, end_col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

    start = grid[start_row][start_col]
    end = grid[end_row][end_col]

    start.make_start()
    end.make_end()

    # Добавляем случайные препятствия (20% ячеек)
    obstacle_count = int(GRID_SIZE * GRID_SIZE * 0.2)
    for _ in range(obstacle_count):
        row, col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        cell = grid[row][col]
        if not cell.is_start() and not cell.is_end():
            cell.make_barrier()

    return start, end


# Манхэттенское расстояние между ячейками
def manhattan(c1, c2):
    return abs(c1.row - c2.row) + abs(c1.col - c2.col)


# Восстановление пути от конечной точки
def rec_path(ec):
    p = []
    t = ec
    while t:
        p.append(t)
        t = t.parent
    # Переворачиваем путь, чтобы он шел от начала к концу
    return p[::-1]


# Алгоритм поиска пути A*
def a_star(gd, s, e):
    # Инициализация очереди с приоритетом
    oo = PriorityQueue()
    # Множество для отслеживания ячеек в очереди
    os = set()

    # Сбрасываем значения ячеек
    for row in gd:
        for cell in row:
            cell.g = float('inf')
            cell.f = float('inf')
            cell.parent = None

    # Инициализация стартовой ячейки
    s.g = 0
    s.h = manhattan(s, e)
    s.f = s.h

    # Добавляем стартовую ячейку в очередь
    # Используем id(cell) как второй элемент для сравнения при одинаковых f
    oo.put((s.f, id(s), s))
    os.add(s)

    # Основной цикл алгоритма
    while not oo.empty():
        # Извлекаем ячейку с наименьшей f-стоимостью
        cr = oo.get()[2]
        os.remove(cr)

        # Если достигли цели
        if cr == e:
            return rec_path(e)

        # Обновляем соседей текущей ячейки нейгхбор
        cr.update_neighbors(gd)

        # Обрабатываем всех соседей
        for neighbor in cr.neighbors:
            # Предварительная стоимость пути
            tg = cr.g + 1

            # Если нашли лучший путь
            if tg < neighbor.g:
                neighbor.parent = cr
                neighbor.g = tg
                neighbor.h = manhattan(neighbor, e)
                neighbor.f = neighbor.g + neighbor.h

                # Добавляем соседа в очередь, если его там еще нет
                if neighbor not in os:
                    os.add(neighbor)
                    oo.put((neighbor.f, id(neighbor), neighbor))
                    if not neighbor.is_end() and not neighbor.is_start():
                        neighbor.make_visited()

        # Визуализация процесса
        draw_grid(WIN, gd)
        pygame.time.delay(20)

    # Путь не найден
    return None


# Загрузка предопределенной карты из варианта
def load_pres():
    preset = [
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [2, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 3]
    ]

    # Создаем новую сетку
    grid = make_grid()
    start = None
    end = None

    # Заполняем сетку на основе предопределенной карты
    for row_idx, row_data in enumerate(preset):
        for col_idx, cell_type in enumerate(row_data):
            cell = grid[row_idx][col_idx]
            cell.type = cell_type
            if cell_type == START:
                start = cell
            elif cell_type == END:
                end = cell

    # Обновляем соседей для всех ячеек
    for row in grid:
        for cell in row:
            cell.update_neighbors(grid)

    return grid, start, end


# Основная функция программы
def main():
    # Инициализация
    grid = make_grid()
    start, end = generate_random_grid(grid)
    algorithm_done = False  # я не знала, что в этом слове есть эйч

    # Главный цикл
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                # Загрузка предопределенной карты
                if event.key == pygame.K_e:
                    grid, start, end = load_pres()
                    algorithm_done = False

                # Генерация новой случайной карты
                elif event.key == pygame.K_r:
                    grid = make_grid()
                    start, end = generate_random_grid(grid)
                    algorithm_done = False

                # Запуск алгоритма поиска пути
                elif event.key == pygame.K_SPACE and not algorithm_done:
                    # Обновляем соседей для всех ячеек
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    # Запускаем A* поиск
                    path = a_star(grid, start, end)

                    # Визуализация найденного пути
                    if path:
                        for cell in path[1:-1]:  # Пропускаем start и end
                            cell.make_path()
                        algorithm_done = True

        # Отрисовка текущего состояния
        draw_grid(WIN, grid)

    # Завершение работы
    pygame.quit()


if __name__ == "__main__":
    main()
