import pygame

# Number of frames per second
FPS = 10

# Set up Colors
Black = (0, 0, 0)
White = (255, 255, 255)
LightGray = (200, 200, 200)

# Set size of grid
WindowMultiplier = 15 # Change this number to change the window size
WindowSize = 90
WindowWidth = WindowSize * WindowMultiplier
WindowHeight = WindowSize * WindowMultiplier
SquareSize = (WindowSize * WindowMultiplier) // 3
CellSize = SquareSize // 3
NumberSize = CellSize // 3

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

def text_objects(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

def display_number(text, row, col):
    largeText = pygame.font.SysFont("comicsans", WindowWidth//9)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((row*CellSize)+NumberSize+(NumberSize//2), (col*CellSize)+NumberSize+((int(NumberSize//1.5))))
    screen.blit(TextSurf, TextRect)

    #pygame.display.update()

def initialize_board(board):
    for i in range(0, 9):
        for j in range (0, 9):
            if board[i][j] != 0:
                display_number(str(board[i][j]), i, j)

#Main
def main():
    global FPSCLOCK, screen
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((WindowWidth, WindowHeight))
    pygame.display.set_caption("Sudoku")
    screen.fill(White)
    initialize_board(board)
    drawGrid(screen)

    # Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.update()
        FPSCLOCK.tick(FPS)

main()
