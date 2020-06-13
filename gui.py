import pygame
from solver import solve, valid, print_board

# Number of frames per second
FPS = 10

# Set up Colors
Black = (0, 0, 0)
White = (255, 255, 255)
LightGray = (200, 200, 200)

# Set size of grid
WindowMultiplier = 5 # Change this number to change the window size
WindowSize = 90
WindowWidth = WindowSize * WindowMultiplier
WindowHeight = WindowSize * WindowMultiplier
SquareSize = (WindowSize * WindowMultiplier) // 3
CellSize = SquareSize // 3
NumberSize = CellSize // 3

# Keep track of the solved and unsolved numbers
Solved = {}
Unsolved = set()

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

# Draw the Sudoku Board
def drawGrid(screen):
    
    # Draw the cells
    for x in range(0, WindowWidth, CellSize): 
        pygame.draw.line(screen, LightGray, (x,0),(x,WindowHeight))
    for y in range (0, WindowHeight, CellSize):
        pygame.draw.line(screen, LightGray, (0,y), (WindowWidth, y))

    # Draw the the Square
    for x in range(0, WindowWidth, SquareSize): 
        pygame.draw.line(screen, Black, (x,0), (x, WindowHeight), 3)
    for y in range(0, WindowHeight, SquareSize):
        pygame.draw.line(screen, Black, (0, y), (WindowWidth, y), 3)

    return None

# Set up the Numbers text
def text_objects(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

# Set up the position of the Numbers
def display_number(text, pos):
    largeText = pygame.font.SysFont("comicsans", WindowWidth//9)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((pos[1]*CellSize)+NumberSize+(NumberSize//2), (pos[0]*CellSize)+NumberSize+((int(NumberSize//1.5))))
    screen.blit(TextSurf, TextRect)

# Initialize the board with the starting board
def initialize_board(board):
    for i in range(0, 9):
        for j in range (0, 9):
            if board[i][j] != 0:
                display_number(str(board[i][j]), (i, j))
            else:
                Unsolved.add((i,j))

# Draw Box when clicked
def drawBox(mousex, mousey):
    mousex = mousex//CellSize
    mousey = mousey//CellSize
    pygame.draw.rect(screen, (0, 0, 255), (mousex*CellSize, mousey*CellSize, CellSize, CellSize), 2)
    return (mousey, mousex)
    

#Main
def main():
    global FPSCLOCK, screen, solved_board
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((WindowWidth, WindowHeight))
    pygame.display.set_caption("Sudoku")
    screen.fill(White)
    initialize_board(board)
    drawGrid(screen)
    solve(board)
    board_selected = None
    Key = None

    # Save solution in a Dictionary
    for i in range(0, 9):
        for j in range(0, 9):
            Solved[(i,j)] = board[i][j]

    # Game Loop
    running = True
    while running:
        MouseClicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Mouse movement commands
            elif event.type == pygame.MOUSEMOTION:
                MouseX, MouseY = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                MouseX, MouseY = event.pos
                MouseClicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

        if MouseClicked == True:
            board_selected = drawBox(MouseX, MouseY)
            key = None

        if board_selected != None and key != None:
            display_number(str(key), board_selected)


        pygame.display.update()
        FPSCLOCK.tick(FPS)

main()
