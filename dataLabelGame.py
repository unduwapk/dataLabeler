# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Data Labeler")

# def main():
#     run=True

#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 break
#     pygame.quit()

# if __name__ == "__main__":
#     main()



clock = pygame.time.Clock()
running = True
dt = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")

    pygame.draw.rect(screen, "black", pygame.Rect( screen.get_width()//2 -375, 100, 750, 300), 3, 3)

    doggoImg = pygame.image.load("doggo.jpg")
    iwidth, iheight = doggoImg.get_size()
    imgScale = 300 // iheight
    doggoImg = pygame.transform.scale(doggoImg, (700, 250))

    screen.blit(doggoImg, (screen.get_width()//2 -350 , 125))


    # label options
    pygame.draw.rect(screen, "black", pygame.Rect( screen.get_width()//2 -375, 500, 200, 100), 3, 3)
    pygame.draw.rect(screen, "black", pygame.Rect( screen.get_width()//2 -100, 500, 200, 100), 3, 3)
    pygame.draw.rect(screen, "black", pygame.Rect( screen.get_width()//2 +175, 500, 200, 100), 3, 3)


    # Define and render the text
    font = pygame.font.SysFont("Comic Sans", 48,  bold=True)
    text_color = (255, 255, 255)  # White
    text_surface_dog = font.render("Dog", True, text_color)
    text_surface_cat = font.render("Cat", True, text_color)
    text_surface_other = font.render("Other", True, text_color)

    # Position and blit the text
    text_rect_dog = text_surface_dog.get_rect()
    text_rect_dog.center = (200 + ( screen.get_width()//2 -375) // 2, 300 + 500 // 2)
    screen.blit(text_surface_dog, text_rect_dog)

    text_rect_cat = text_surface_cat.get_rect()
    text_rect_cat.center = (350 + ( screen.get_width()//2 -100) // 2, 300 + 500 // 2)
    screen.blit(text_surface_cat, text_rect_cat)

    text_rect_other = text_surface_other.get_rect()
    text_rect_other.center = (500 + ( screen.get_width()//2 +175) // 2, 300 + 500 // 2)
    screen.blit(text_surface_other, text_rect_other)    



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()