import pygame

screen = pygame.display.set_mode((800, 800))
Width, Height = pygame.display.get_window_size()

Grid = []
size = 40
for y in range(-size, size+1):
    Grid.append([])
    for x in range(-size, size+1):
        Grid[y+size].append(0)

d = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            d = True
        elif event.type == pygame.MOUSEBUTTONUP:
            d = False
        pass

    mx, my = pygame.mouse.get_pos()

    screen.fill([0]*3)
    for y, row in enumerate(Grid):
        y -= size
        for x, tile in enumerate(row):
            x -= size
            if d:
                tile += max(15 - ((x-(mx-Width/2)/10)**2 + (y-(my-Height/2)/10)**2)**0.5, 0)
            tile = min(tile, 255)
            pygame.draw.rect(screen, [tile, tile, tile], (10*x+Width/2+5, 10*y+Height/2+5, 10, 10))

            Grid[y+size][x+size] = tile/1.01

    pygame.display.update()








# Poverty
# Treatment of criminals
# Child labour
# Inflation
# Segregation
# Food insecurity
# Immigration
# Police brutality
