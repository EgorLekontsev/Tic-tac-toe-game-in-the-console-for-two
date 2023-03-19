# Определяем размер поля
size = 3

# Создаем пустое поле
board = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(".")
    board.append(row)

# Определяем функцию для отображения поля
def display_board():
    for row in board:
        print(" ".join(row))

# Определяем функцию для проверки выигрышной комбинации
def check_win():
    # Проверяем по горизонтали
    for i in range(size):
        if board[i][0] != "." and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return True
    # Проверяем по вертикали
    for j in range(size):
        if board[0][j] != "." and board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            return True
    # Проверяем по диагоналям
    if board[0][0] != "." and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    if board[0][2] != "." and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True
    return False

# Цикл игры
players = ["X", "O"]
current_player = players[0]
while True:
    # Отображаем поле и запрашиваем ход
    display_board()
    row = int(input("Выберите строку (от 1 до 3): ")) - 1
    col = int(input("Выберите столбец (от 1 до 3): ")) - 1
    # Проверяем, что выбранные координаты находятся в пределах поля и клетка свободна
    if row >= 0 and row < size and col >= 0 and col < size and board[row][col] == ".":
        board[row][col] = current_player
        # Проверяем, есть ли победитель или ничья
        if check_win():
            display_board()
            print("Игрок", current_player, "выиграл!")
            break
        elif "." not in [cell for row in board for cell in row]:
            display_board()
            print("Ничья!")
            break
        # Передаем ход следующему игроку
        current_player = players[(players.index(current_player) + 1) % len(players)]
    else:
        print("Выберите правильные координаты и клетку должна быть свободна!")
