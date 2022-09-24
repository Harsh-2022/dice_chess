from cmath import rect
from turtle import pos
import pygame  


FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
pygame.init()  
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)  

  
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('comicsansms',35)

sq_size=(height-60)/8
p_size=sq_size-17

b_k=pygame.image.load('images/black_k.png')
b_n=pygame.image.load('images/black_n.png')
b_p=pygame.image.load('images/black_p.png')
b_b=pygame.image.load('images/black_b.png')
b_q=pygame.image.load('images/black_q.png')
b_r=pygame.image.load('images/black_r.png')

w_b=pygame.image.load('images/white_b.png')
w_k=pygame.image.load('images/white_k.png')
w_n=pygame.image.load('images/white_n.png')
w_p=pygame.image.load('images/white_p.png')
w_q=pygame.image.load('images/white_q.png')
w_r=pygame.image.load('images/white_r.png')

b_p=pygame.transform.scale(b_p,(p_size,p_size))
b_k=pygame.transform.scale(b_k,(p_size,p_size))
b_n=pygame.transform.scale(b_n,(p_size,p_size))
b_b=pygame.transform.scale(b_b,(p_size,p_size))
b_q=pygame.transform.scale(b_q,(p_size,p_size))
b_r=pygame.transform.scale(b_r,(p_size,p_size))

w_p=pygame.transform.scale(w_p,(p_size,p_size))
w_k=pygame.transform.scale(w_k,(p_size,p_size))
w_n=pygame.transform.scale(w_n,(p_size,p_size))
w_b=pygame.transform.scale(w_b,(p_size,p_size))
w_q=pygame.transform.scale(w_q,(p_size,p_size))
w_r=pygame.transform.scale(w_r,(p_size,p_size))

class Piece:
 
    def __init__(self, chess_colour):
        self._chess_colour = chess_colour
        self._is_active = True
 
    # chess_colour getter
    @property
    def chess_colour(self):
        return self._chess_colour
 
    # is_active setter/getter
    @property
    def is_active(self):
        return self._is_active
 
    @is_active.setter
    def is_active(self, value):
        self._is_active = value

def set_peice(x,y,isWhite,pos):
    x=x+8
    y=y+7
    if (pos[1]=='2'):
        screen.blit(w_p,(x,y))

    if (pos[1]=='7'):
        screen.blit(b_p,(x,y))
    
    if pos[1]=='1' and (pos[0]=='A' or pos[0]=='H'):
        screen.blit(w_r,(x,y))
    
    if pos[1]=='1' and (pos[0]=='B' or pos[0]=='G'):
        screen.blit(w_n,(x,y))

    if pos[1]=='1' and (pos[0]=='C' or pos[0]=='F'):
        screen.blit(w_b,(x,y))

    if (pos[1]=='1' and pos[0]=='D'):
        screen.blit(w_q,(x,y))
    
    if (pos[1]=='1' and pos[0]=='E'):
        screen.blit(w_k,(x,y))

    if pos[1]=='8' and (pos[0]=='A' or pos[0]=='H'):
        screen.blit(b_r,(x,y))
    
    if pos[1]=='8' and (pos[0]=='B' or pos[0]=='G'):
        screen.blit(b_n,(x,y))

    if pos[1]=='8' and (pos[0]=='C' or pos[0]=='F'):
        screen.blit(b_b,(x,y))

    if (pos[1]=='8' and pos[0]=='D'):
        screen.blit(b_q,(x,y))
    
    if (pos[1]=='8' and pos[0]=='E'):
        screen.blit(b_k,(x,y))

    
    
    

    

    


    

def calculate_coordinates(x,y,is_white,square_size,position):
    
    x_coordinate=x*square_size+30
    y_coordinate=y*square_size+30
    tuple=[x_coordinate,y_coordinate,is_white,position]
    return tuple



def board_square(board_size,board_start_pt):
    chess_board=[]
    is_white=False
    square_size=board_size/8
    for y in range(8):
        chess_row=[]
        is_white=not is_white
        for x in range(8):
            position = chr(x+65) + str(8-y)
            chess_row.append(calculate_coordinates(x,y,is_white,square_size,position))
            is_white= not is_white
        chess_board.append(chess_row)
    
    count=0
    for row in chess_board:                             #[x_coordinate,y_coordinate,is_white,position]
        for square in row:
            count =count+1
            # print(square[3][1])
            surf=pygame.Surface((square_size,square_size))

            if square[2]:
                surf.fill((255,255,255))
            else:
                surf.fill((100,100,100))
            
            rect = surf.get_rect()
            screen.blit(surf,(square[0],square[1]))
            # pygame.display.flip()
            set_peice(square[0],square[1],square[2],square[3])

def chesscanvas():
    board_size=height-60
    board_start_pt=30 
    player1=smallfont.render('Player 1',True,"white")
    player2=smallfont.render('Player 2',True,"white")
    screen.blit(player1,(board_size+50, 30))
    pygame.draw.rect(screen, "white", pygame.Rect(board_start_pt,board_start_pt, board_size, board_size))
    board_square(board_size,board_start_pt)
    screen.blit(player2,(board_size+50,board_size-20))


def show_score(score):
    Scoring=smallfont.render(str(score),True,"white")
    screen.blit(Scoring, (925,500))

def main():
    score=0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if width-85 <= mouse[0] <= width-5 and 7 <= mouse[1] <= 60:
                    running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
                if width-285<= mouse[0] <= width-90 and 7 <= mouse[1] <= 60:
                    running=False
                    main()

            # elif event.type == pygame.MOUSEBUTTONDOWN:
                if 900<=mouse[0]<=920 and 500 <=mouse[1]<=550:
                    score=score+1
    
               

            
            mouse = pygame.mouse.get_pos()


            global Quit 
            global rematch
            if width-85 <= mouse[0] <= width-5 and 7 <= mouse[1] <= 60:
                Quit = smallfont.render('Exit' , True , "yellow")
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                Quit = smallfont.render('Exit' , True , "white")
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if width-285<= mouse[0] <= width-90 and 7 <= mouse[1] <= 60:
                rematch=smallfont.render('Play Again',True,"yellow")
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                rematch=smallfont.render('Play Again',True,"white")

        # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(Quit , (width-80,10))
        screen.blit(rematch , (width-280,10))
        show_score(score)
                           
        
        chesscanvas()
        
        
        pygame.draw.rect(screen, "red", pygame.Rect(900,500,20,50))




        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    main()
