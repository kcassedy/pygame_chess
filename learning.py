
import pygame
from pygame import *


pygame.init()

white = (255, 255, 255)
black = (0,0,0)
red = (255, 0,0)
blue = [0, 0, 225]
lead_x = 300
lead_y = 300
lead_x_change = 0
clock = pygame.time.Clock()



gameDisplay = pygame.display.set_mode((805, 805))
pygame.display.set_caption('Chess')






gameExit = False # GAME EXIT

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True



    gameDisplay.fill(white)







    pygame.draw.rect(gameDisplay, black, [0, 0, 5, 800]) # X COR, Y Cor,
    pygame.draw.rect(gameDisplay, black, [100,0, 5, 800])
    pygame.draw.rect(gameDisplay, black, [200, 0, 5, 800])
    pygame.draw.rect(gameDisplay, black, [300, 0, 5, 800])
    pygame.draw.rect(gameDisplay, black, [400, 0, 5, 800])
    pygame.draw.rect(gameDisplay, black, [500, 0, 5, 800])
    pygame.draw.rect(gameDisplay, black, [600, 0, 5, 800])
    pygame.draw.rect(gameDisplay, black, [700, 0, 5, 800])
    pygame.draw.rect(gameDisplay, black, [800, 0, 5, 800])


    #LEFT TO RIGHT LINES
    pygame.draw.rect(gameDisplay, black, [0, 0, 800, 5])
    pygame.draw.rect(gameDisplay, black, [0, 100, 800, 5])
    pygame.draw.rect(gameDisplay, black, [0, 200, 800, 5])
    pygame.draw.rect(gameDisplay, black, [0, 300, 800, 5])
    pygame.draw.rect(gameDisplay, black, [0, 400, 800, 5])
    pygame.draw.rect(gameDisplay, black, [0, 500, 800, 5])
    pygame.draw.rect(gameDisplay, black, [0, 600, 800, 5])
    pygame.draw.rect(gameDisplay, black, [0, 700, 800, 5])
    pygame.draw.rect(gameDisplay, black, [0, 800, 800, 5])


    #row 1 black
    Black_Square_8A = gameDisplay.fill(black, rect=[0,0,100,100])
    Black_Square_8C = gameDisplay.fill(black, rect=[200,0, 100, 100])
    Black_Square_8E = gameDisplay.fill(black, rect=[400, 0, 100, 100])
    Black_Square_8G = gameDisplay.fill(black, rect=[600, 0, 100, 100])
     #row 1 white
    White_Square_8B = gameDisplay.fill(white, rect=[100, 0, 100, 100])
    White_Square_8D = gameDisplay.fill(white, rect=[300, 0, 100, 100])
    White_Square_8F = gameDisplay.fill(white, rect=[500, 0, 100, 100])
    White_Square_8H = gameDisplay.fill(white, rect=[700, 0, 100, 100])

    # row 2 black
    Black_Square_7B = gameDisplay.fill(black, rect=[100, 100, 100, 100])
    Black_Square_7D = gameDisplay.fill(black, rect=[300, 100, 100, 100])
    Black_Square_7F = gameDisplay.fill(black, rect=[500, 100, 100, 100])
    Black_Square_7H = gameDisplay.fill(black, rect=[700, 100, 100, 100])
    # row 2 white
    White_Square_7A = gameDisplay.fill(white, rect=[0, 100, 100, 100])
    White_Square_7C = gameDisplay.fill(white, rect=[200, 100, 100, 100])
    White_Square_7E = gameDisplay.fill(white, rect=[400, 100, 100, 100])
    White_Square_7G = gameDisplay.fill(white, rect=[600, 100, 100, 100])

    #row 3
    Black_Square_6A = gameDisplay.fill(black, rect=[0, 200, 100, 100])
    Black_Square_6C = gameDisplay.fill(black, rect=[200, 200, 100, 100])
    Black_Square_6E = gameDisplay.fill(black, rect=[400, 200, 100, 100])
    Black_Square_6G = gameDisplay.fill(black, rect=[600, 200, 100, 100])

    # row 4

    White_Square_6B = gameDisplay.fill(black, rect=[100, 300, 100, 100])
    White_Square_6D = gameDisplay.fill(black, rect=[300, 300, 100, 100])
    White_Square_6F = gameDisplay.fill(black, rect=[500, 300, 100, 100])
    White_Square_6H = gameDisplay.fill(black, rect=[700, 300, 100, 100])

    #row 5

    Black_Square_5A = gameDisplay.fill(black, rect=[0, 400, 100, 100])
    Black_Square_5C = gameDisplay.fill(black, rect=[200, 400, 100, 100])
    Black_Square_5E = gameDisplay.fill(black, rect=[400, 400, 100, 100])
    Black_Square_5G = gameDisplay.fill(black, rect=[600, 400, 100, 100])

    White_Square_5B = gameDisplay.fill(white, rect=[100, 400, 100, 100])
    White_Square_5D = gameDisplay.fill(white, rect=[300, 400, 100, 100])
    White_Square_5F = gameDisplay.fill(white, rect=[500, 400, 100, 100])
    White_Square_5H = gameDisplay.fill(white, rect=[700, 400, 100, 100])

    # row 6
    Black_Square_4B = gameDisplay.fill(black, rect=[100, 500, 100, 100])
    Black_Square_4D = gameDisplay.fill(black, rect=[300, 500, 100, 100])
    Black_Square_4F = gameDisplay.fill(black, rect=[500, 500, 100, 100])
    Black_Square_4H = gameDisplay.fill(black, rect=[700, 500, 100, 100])

    White_Square_4A = gameDisplay.fill(white, rect=[0, 500, 100, 100])
    White_Square_4C = gameDisplay.fill(white, rect=[200, 500, 100, 100])
    White_Square_4E = gameDisplay.fill(white, rect=[400, 500, 100, 100])
    White_Square_4G = gameDisplay.fill(white, rect=[600, 500, 100, 100])
    # row 7
    Black_Square_3A = gameDisplay.fill(black, rect=[0, 600, 100, 100])
    Black_Square_3C = gameDisplay.fill(black, rect=[200, 600, 100, 100])
    Black_Square_3E = gameDisplay.fill(black, rect=[400, 600, 100, 100])
    Black_Square_3G = gameDisplay.fill(black, rect=[600, 600, 100, 100])

    White_Square_3B = gameDisplay.fill(white, rect=[100, 600, 100, 100])
    White_Square_3D = gameDisplay.fill(white, rect=[300, 600, 100, 100])
    White_Square_3F = gameDisplay.fill(white, rect=[500, 600, 100, 100])
    White_Square_3G = gameDisplay.fill(white, rect=[700, 600, 100, 100])
    # row 8
    Black_Square_2A = gameDisplay.fill(black, rect=[100, 700, 100, 100])
    Black_Square_2C = gameDisplay.fill(black, rect=[300, 700, 100, 100])
    Black_Square_2E = gameDisplay.fill(black, rect=[500, 700, 100, 100])
    Black_Square_2G = gameDisplay.fill(black, rect=[700, 700, 100, 100])

    White_Square_2B = gameDisplay.fill(white, rect=[0, 700, 100, 100])
    White_Square_2D = gameDisplay.fill(white, rect=[200, 700, 100, 100])
    White_Square_2F = gameDisplay.fill(white, rect=[400, 700, 100, 100])
    White_Square_2H = gameDisplay.fill(white, rect=[600, 700, 100, 100])


    """piece location and movement"""




    """RED PIECES"""


    """7A"""
    Red_Pawn7A = [
                pygame.draw.line(gameDisplay, red, (25, 110), (25, 190), 10),
                pygame.draw.line(gameDisplay, red, (25, 110), (80, 110), 10),
                pygame.draw.line(gameDisplay, red, (25, 150), (80, 150), 10),
                pygame.draw.line(gameDisplay, red, (80, 150), (80, 110), 10)
                  ]

    """7B"""
    Red_Pawn7B = [
                pygame.draw.line(gameDisplay, red, (125, 110), (125, 190), 10),
                pygame.draw.line(gameDisplay, red, (125, 110), (180, 110), 10),
                pygame.draw.line(gameDisplay, red, (125, 150), (180, 150), 10),
                pygame.draw.line(gameDisplay, red, (180, 150), (180, 110), 10)
                ]
    """7C"""
    Red_Pawn7C = [
        pygame.draw.line(gameDisplay, red, (225, 110), (225, 190), 10),
        pygame.draw.line(gameDisplay, red, (225, 110), (280, 110), 10),
        pygame.draw.line(gameDisplay, red, (225, 150), (280, 150), 10),
        pygame.draw.line(gameDisplay, red, (280, 150), (280, 110), 10)
    ]
    """7D"""
    Red_Pawn7D = [
        pygame.draw.line(gameDisplay, red, (325, 110), (325, 190), 10),
        pygame.draw.line(gameDisplay, red, (325, 110), (380, 110), 10),
        pygame.draw.line(gameDisplay, red, (325, 150), (380, 150), 10),
        pygame.draw.line(gameDisplay, red, (380, 150), (380, 110), 10)
    ]
    """7E"""
    Red_Pawn7E = [
        pygame.draw.line(gameDisplay, red, (425, 110), (425, 190), 10),
        pygame.draw.line(gameDisplay, red, (425, 110), (480, 110), 10),
        pygame.draw.line(gameDisplay, red, (425, 150), (480, 150), 10),
        pygame.draw.line(gameDisplay, red, (480, 150), (480, 110), 10)
    ]
    """7F"""
    Red_Pawn7F = [
        pygame.draw.line(gameDisplay, red, (525, 110), (525, 190), 10),
        pygame.draw.line(gameDisplay, red, (525, 110), (580, 110), 10),
        pygame.draw.line(gameDisplay, red, (525, 150), (580, 150), 10),
        pygame.draw.line(gameDisplay, red, (580, 150), (580, 110), 10)
    ]
    """7G"""
    Red_Pawn7G = [
        pygame.draw.line(gameDisplay, red, (625, 110), (625, 190), 10),
        pygame.draw.line(gameDisplay, red, (625, 110), (680, 110), 10),
        pygame.draw.line(gameDisplay, red, (625, 150), (680, 150), 10),
        pygame.draw.line(gameDisplay, red, (680, 150), (680, 110), 10)
    ]

    """7H"""
    Red_Pawn7H = [
            pygame.draw.line(gameDisplay, red, (725, 110), (725, 190), 10),
            pygame.draw.line(gameDisplay, red, (725, 110), (780, 110), 10),
            pygame.draw.line(gameDisplay, red, (725, 150), (780, 150), 10),
            pygame.draw.line(gameDisplay, red, (780, 150), (780, 110), 10)
        ]

    """8A"""
    Red_Rook_Left = [
                    pygame.draw.line(gameDisplay, red, (25, 10), (25, 90), 10),
                     pygame.draw.line(gameDisplay, red, (25, 10), (80, 10), 10),
                     pygame.draw.line(gameDisplay, red, (80, 10), (80, 50), 10),
                     pygame.draw.line(gameDisplay, red, (80, 50), (25, 50), 10),
                     pygame.draw.line(gameDisplay, red, (40, 50), (80, 90), 10)
                    ]
    """8H"""
    Red_Rook_Right = [
                      pygame.draw.line(gameDisplay, red, (725, 10), (725, 90), 10),
                      pygame.draw.line(gameDisplay, red, (725, 10), (780, 10), 10),
                      pygame.draw.line(gameDisplay, red, (780, 10), (780, 50), 10),
                      pygame.draw.line(gameDisplay, red, (725, 50), (780, 50), 10),
                      pygame.draw.line(gameDisplay, red, (725, 50), (780, 90), 10)
                    ]
    """8B"""
    Red_Knight_Left = [
                       pygame.draw.line(gameDisplay, red, (125, 10), (125, 90), 10),
                       pygame.draw.line(gameDisplay, red, (125, 50), (180, 10), 10),
                       pygame.draw.line(gameDisplay, red, (125, 50), (180, 90), 10)
                    ]
    """8G"""
    Red_Knight_Right = [
                        pygame.draw.line(gameDisplay, red, (625, 10), (625, 90), 10),
                        pygame.draw.line(gameDisplay, red, (625, 50), (680, 10), 10),
                        pygame.draw.line(gameDisplay, red, (625, 50), (680, 90), 10)
                        ]
    """8C"""
    Red_Bishop_Left = [
                       pygame.draw.line(gameDisplay, red, (225, 10), (225, 90), 10),
                       pygame.draw.line(gameDisplay, red, (225, 10), (280, 10), 10),
                       pygame.draw.line(gameDisplay, red, (225, 50), (280, 50), 10),
                       pygame.draw.line(gameDisplay, red, (225, 90), (280, 90), 10),
                       pygame.draw.line(gameDisplay, red, (280, 10), (280, 90), 10)
                    ]
    """8F"""
    Red_Bishop_Right = [
                        pygame.draw.line(gameDisplay, red, (525, 10), (525, 90), 10),
                        pygame.draw.line(gameDisplay, red, (525, 10), (580, 10), 10),
                        pygame.draw.line(gameDisplay, red, (525, 50), (580, 50), 10),
                        pygame.draw.line(gameDisplay, red, (525, 90), (580, 90), 10),
                        pygame.draw.line(gameDisplay, red, (580, 10), (580, 90), 10)
                    ]
    """8D"""
    Red_Queen = [
                 pygame.draw.line(gameDisplay, red, (325, 10), (325, 90), 10),
                 pygame.draw.line(gameDisplay, red, (325, 10), (380, 10), 10),
                 pygame.draw.line(gameDisplay, red, (325, 90), (380, 90), 10),
                 pygame.draw.line(gameDisplay, red, (380, 10), (380, 90), 10),
                 pygame.draw.line(gameDisplay, red, (345, 55), (375, 95), 10)
                ]
    """8E"""
    Red_King = [
                pygame.draw.line(gameDisplay, red, (450, 10), (450, 90), 10),
                pygame.draw.line(gameDisplay, red, (425, 30), (475, 30), 10)
                ]


    """BLUE PIECES"""


    """2A"""
    Blue_Pawn2A = [
                pygame.draw.line(gameDisplay, blue, (25, 610), (25, 690), 10),
                pygame.draw.line(gameDisplay, blue, (25, 610), (80, 610), 10),
                pygame.draw.line(gameDisplay, blue, (25, 650), (80, 650), 10),
                pygame.draw.line(gameDisplay, blue, (80, 650), (80, 610), 10)
                ]
    """2B"""
    Blue_Pawn2B = [
        pygame.draw.line(gameDisplay, blue, (125, 610), (125, 690), 10),
        pygame.draw.line(gameDisplay, blue, (125, 610), (180, 610), 10),
        pygame.draw.line(gameDisplay, blue, (125, 650), (180, 650), 10),
        pygame.draw.line(gameDisplay, blue, (180, 650), (180, 610), 10)
    ]

    """2C"""
    Blue_Pawn2C = [
        pygame.draw.line(gameDisplay, blue, (225, 610), (225, 690), 10),
        pygame.draw.line(gameDisplay, blue, (225, 610), (280, 610), 10),
        pygame.draw.line(gameDisplay, blue, (225, 650), (280, 650), 10),
        pygame.draw.line(gameDisplay, blue, (280, 650), (280, 610), 10)
    ]

    """2D"""
    Blue_Pawn2D = [
        pygame.draw.line(gameDisplay, blue, (325, 610), (325, 690), 10),
        pygame.draw.line(gameDisplay, blue, (325, 610), (380, 610), 10),
        pygame.draw.line(gameDisplay, blue, (325, 650), (380, 650), 10),
        pygame.draw.line(gameDisplay, blue, (380, 650), (380, 610), 10)
    ]

    """2E"""
    Blue_Pawn2E = [
        pygame.draw.line(gameDisplay, blue, (425, 610), (425, 690), 10),
        pygame.draw.line(gameDisplay, blue, (425, 610), (480, 610), 10),
        pygame.draw.line(gameDisplay, blue, (425, 650), (480, 650), 10),
        pygame.draw.line(gameDisplay, blue, (480, 650), (480, 610), 10)
    ]

    """2F"""
    Blue_Pawn2F = [
        pygame.draw.line(gameDisplay, blue, (525, 610), (525, 690), 10),
        pygame.draw.line(gameDisplay, blue, (525, 610), (580, 610), 10),
        pygame.draw.line(gameDisplay, blue, (525, 650), (580, 650), 10),
        pygame.draw.line(gameDisplay, blue, (580, 650), (580, 610), 10)
    ]

    """2G"""
    Blue_Pawn2G = [
        pygame.draw.line(gameDisplay, blue, (625, 610), (625, 690), 10),
        pygame.draw.line(gameDisplay, blue, (625, 610), (680, 610), 10),
        pygame.draw.line(gameDisplay, blue, (625, 650), (680, 650), 10),
        pygame.draw.line(gameDisplay, blue, (680, 650), (680, 610), 10)
    ]

    """2H"""
    Blue_Pawn2H = [
        pygame.draw.line(gameDisplay, blue, (725, 610), (725, 690), 10),
        pygame.draw.line(gameDisplay, blue, (725, 610), (780, 610), 10),
        pygame.draw.line(gameDisplay, blue, (725, 650), (780, 650), 10),
        pygame.draw.line(gameDisplay, blue, (780, 650), (780, 610), 10)
    ]

    """1A"""
    Blue_Rook_Left = [
        pygame.draw.line(gameDisplay, blue, (25, 710), (25, 790), 10),
        pygame.draw.line(gameDisplay, blue, (25, 710), (80, 710), 10),
        pygame.draw.line(gameDisplay, blue, (80, 710), (80, 750), 10),
        pygame.draw.line(gameDisplay, blue, (80, 750), (25, 750), 10),
        pygame.draw.line(gameDisplay, blue, (40, 750), (80, 790), 10)
    ]
    """1H"""
    Blue_Rook_Right = [
        pygame.draw.line(gameDisplay, blue, (725, 710), (725, 790), 10),
        pygame.draw.line(gameDisplay, blue, (725, 710), (780, 710), 10),
        pygame.draw.line(gameDisplay, blue, (780, 710), (780, 750), 10),
        pygame.draw.line(gameDisplay, blue, (725, 750), (780, 750), 10),
        pygame.draw.line(gameDisplay, blue, (725, 750), (780, 790), 10)
        ]

    """1B"""
    Blue_Knight_Left = [
        pygame.draw.line(gameDisplay, blue, (125, 710), (125, 790), 10),
        pygame.draw.line(gameDisplay, blue, (125, 750), (180, 710), 10),
        pygame.draw.line(gameDisplay, blue, (125, 750), (180, 790), 10)
    ]
    """1G"""
    Blue_Knight_Right = [
        pygame.draw.line(gameDisplay, blue, (625, 710), (625, 790), 10),
        pygame.draw.line(gameDisplay, blue, (625, 750), (680, 710), 10),
        pygame.draw.line(gameDisplay, blue, (625, 750), (680, 790), 10)
    ]

    """8C"""
    Blue_Bishop_Left = [
        pygame.draw.line(gameDisplay, blue, (225, 710), (225, 790), 10),
        pygame.draw.line(gameDisplay, blue, (225, 710), (280, 710), 10),
        pygame.draw.line(gameDisplay, blue, (225, 750), (280, 750), 10),
        pygame.draw.line(gameDisplay, blue, (225, 790), (280, 790), 10),
        pygame.draw.line(gameDisplay, blue, (280, 710), (280, 790), 10)
    ]
    """8F"""
    Blue_Bishop_Right = [
        pygame.draw.line(gameDisplay, blue, (525, 710), (525, 790), 10),
        pygame.draw.line(gameDisplay, blue, (525, 710), (580, 710), 10),
        pygame.draw.line(gameDisplay, blue, (525, 750), (580, 750), 10),
        pygame.draw.line(gameDisplay, blue, (525, 790), (580, 790), 10),
        pygame.draw.line(gameDisplay, blue, (580, 710), (580, 790), 10)
    ]

    """8D"""
    Blue_Queen = [
        pygame.draw.line(gameDisplay, blue, (325, 710), (325, 790), 10),
        pygame.draw.line(gameDisplay, blue, (325, 710), (380, 710), 10),
        pygame.draw.line(gameDisplay, blue, (325, 790), (380, 790), 10),
        pygame.draw.line(gameDisplay, blue, (380, 710), (380, 790), 10),
        pygame.draw.line(gameDisplay, blue, (345, 755), (375, 795), 10)
    ]
    """8E"""
    Blue_King = [
        pygame.draw.line(gameDisplay, blue, (450, 710), (450, 790), 10),
        pygame.draw.line(gameDisplay, blue, (425, 730), (475, 730), 10)
    ]





    blue_pieces = [ Blue_Pawn2B,
                   Blue_Pawn2C,
                   Blue_Pawn2D,
                   Blue_Pawn2E,
                   Blue_Pawn2F,
                   Blue_Pawn2G,
                   Blue_Pawn2H,
                   Blue_Rook_Left,
                   Blue_Rook_Right,
                   Blue_Knight_Left,
                   Blue_Knight_Right,
                   Blue_Bishop_Left,
                   Blue_Bishop_Right,
                   Blue_Queen,
                   Blue_King]

    red_pieces = [
                  Red_Pawn7A,
                  Red_Pawn7B,
                  Red_Pawn7C,
                  Red_Pawn7D,
                  Red_Pawn7E,
                  Red_Pawn7F,
                  Red_Pawn7G,
                  Red_Pawn7H,
                  Red_Rook_Left,
                  Red_Rook_Right,
                  Red_Knight_Left,
                  Red_Knight_Right,
                  Red_Bishop_Left,
                  Red_Bishop_Right,
                  Red_Queen,
                  Red_King
                  ]




    pygame.display.update() #AFTER GRAPHICS

    #FPS
    clock.tick(30)



pygame.quit()
quit()