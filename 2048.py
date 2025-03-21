import pygame
import random
import math

pygame.init()

FPS=60

WIDTH,HEIGHT=760,760
ROWS,COLS=4,4

BOX_HEIGHT=HEIGHT // ROWS
BOX_WIDTH=WIDTH // COLS

BACKGROUND_COLOR=(205,192,180)
OUTLINE_COLOR=(187,173,160)
OUTLINE_THICKNESS=10
FONT_COLOR=(119,110,101)

FONT=pygame.font.SysFont("comicsans",60,bold=True)

WINDOW= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")

class Tile:
    COLORS=[(237,229,218),(238,225,201),(243,178,122),(246,150,101),(247,124,95),(247,95,59),(237,208,115),(237,204,99),(236,202,80)]

    def __init__(self,value,row,col):
        self.value=value
        self.row=row
        self.col=col
        self.x=col*BOX_WIDTH
        self.y=row*BOX_HEIGHT

    def get_color(self):

        color_index=int(math.log2(self.value))-1
        color=self.COLORS[color_index]
        return color
        

    def draw(self,window):
        color=self.get_color()
        pygame.draw.rect(window,color,(self.x,self.y,BOX_WIDTH,BOX_HEIGHT))

        text=FONT.render(str(self.value),1,FONT_COLOR)
        window.blit(text,
                    (
                        self.x+(BOX_WIDTH/2-text.get_width()/2),
                        self.y+(BOX_HEIGHT/2-text.get_height()/2)
                    ) 
            
         )

    def set_pos(self):
        pass



def draw_grid(window):

    for row in range(1,ROWS):
        y=row*BOX_HEIGHT
        pygame.draw.line(window,OUTLINE_COLOR,(0,y),(WIDTH,y),OUTLINE_THICKNESS)


    for col in range(1,COLS):
        x=col*BOX_WIDTH   
        pygame.draw.line(window,OUTLINE_COLOR,(x,0),(x,HEIGHT),OUTLINE_THICKNESS)



    pygame.draw.rect(window,OUTLINE_COLOR,(0,0,WIDTH,HEIGHT),OUTLINE_THICKNESS)



def draw(window,tiles):
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)


    draw_grid(WINDOW)
    pygame.display.update()


def get_random_pos(tiles):

    row=None
    col=None
    while True:
        row=random.randrange(0,ROWS)
        col=random.randrange(0,COLS)

        if f"{row}{col}" not in tiles:
            break
    return row,col    





def generate_tiles():
    
    tiles={}
    for  _ in range(2):
        row,col=get_random_pos(tiles)
        tiles[f"{row}{col}"]=Tile(2,row,col)

    return tiles    

def main(WINDOW):
    clock=pygame.time.Clock()
    run=True

    tiles=generate_tiles()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if(event.type)==pygame.QUIT:
                run=False
                break
         
        draw(WINDOW,tiles)
        



    pygame.quit()
   


if(__name__ == "__main__"):
    main(WINDOW)




