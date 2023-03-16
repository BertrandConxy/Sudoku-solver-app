# import pygame
from module.check_valid import valid
from module.board_drawing import draw, draw_box

def solve(pygame, screen, grid, i, j, dif, font):
	
	while grid[i][j]!= 0:
		if i<8:
			i+= 1
		elif i == 8 and j<8:
			i = 0
			j+= 1
		elif i == 8 and j == 8:
			return True
	pygame.event.pump()
	for it in range(1, 10):
		if valid(grid, i, j, it)== True:
			grid[i][j]= it
			global x, y
			x = i
			y = j
			# white color background\
			screen.fill((255, 255, 255))
			draw(pygame, screen, dif, font, grid)
			draw_box(pygame, screen, i, j, dif)
			pygame.display.update()
			pygame.time.delay(20)
			if solve(grid, i, j)== 1:
				return True
			else:
				grid[i][j]= 0
			# white color background\
			screen.fill((255, 255, 255))
		
			draw(pygame, screen, dif, font, grid)
			draw_box(pygame, screen, i, j, dif)
			pygame.display.update()
			pygame.time.delay(50)
	return False