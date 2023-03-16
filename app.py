# import pygame library
import pygame

from module.check_valid import valid
from module.raise_error import raise_error1, raise_error2
from module.instructions import instruction, result
from module.board_drawing import draw, draw_box, draw_val
from module.track_cord import get_cord

# from module.auto_solve import solve

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((500, 600))

# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
img = pygame.image.load('sudoku.png')
pygame.display.set_icon(img)

x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.
grid =[
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

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 25)
font2 = pygame.font.SysFont("comicsans", 15)

# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
	
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
			draw(pygame, screen, dif, font1, grid) # Draw required lines for making Sudoku grid
			draw_box(pygame, screen, x, y, dif) # Highlight the cell selected
			pygame.display.update()
			pygame.time.delay(20)
			if solve(grid, i, j)== 1:
				return True
			else:
				grid[i][j]= 0
			# white color background\
			screen.fill((255, 255, 255))
		
			draw(pygame, screen, dif, font1, grid) # Draw required lines for making Sudoku grid
			draw_box(pygame, screen, x, y, dif) # Highlight the cell selected
			pygame.display.update()
			pygame.time.delay(50)
	return False

run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop thats keep the window running
while run:	
	# White color background
	screen.fill((255, 255, 255))
	# Loop through the events stored in event.get()
	for event in pygame.event.get():
		# Quit the game window
		if event.type == pygame.QUIT:
			run = False
		# Get the mouse position to insert number
		if event.type == pygame.MOUSEBUTTONDOWN:
			flag1 = 1
			pos = pygame.mouse.get_pos()
			get_cord(pos, dif)
		# Get the number to be inserted if key pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x-= 1
				flag1 = 1
			if event.key == pygame.K_RIGHT:
				x+= 1
				flag1 = 1
			if event.key == pygame.K_UP:
				y-= 1
				flag1 = 1
			if event.key == pygame.K_DOWN:
				y+= 1
				flag1 = 1
			if event.key == pygame.K_1:
				val = 1
			if event.key == pygame.K_2:
				val = 2
			if event.key == pygame.K_3:
				val = 3
			if event.key == pygame.K_4:
				val = 4
			if event.key == pygame.K_5:
				val = 5
			if event.key == pygame.K_6:
				val = 6
			if event.key == pygame.K_7:
				val = 7
			if event.key == pygame.K_8:
				val = 8
			if event.key == pygame.K_9:
				val = 9
			if event.key == pygame.K_RETURN:
				flag2 = 1
			# If R pressed clear the sudoku board
			if event.key == pygame.K_r:
				rs = 0
				error = 0
				flag2 = 0
				grid =[
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0]
				]
			# If D is pressed reset the board to default
			if event.key == pygame.K_d:
				rs = 0
				error = 0
				flag2 = 0
				grid =[
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
	if flag2 == 1:
		if solve(grid, 0, 0)== False:
			error = 1
		else:
			rs = 1
		flag2 = 0
	if val != 0:		
		draw_val(val, font1, screen, x , y, dif) # Fill value entered in cell
		if valid(grid, int(x), int(y), val)== True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2(screen, font1) # Raise error when wrong value entered
		val = 0
	
	if error == 1:
		raise_error1(screen, font1) # Raise error when wrong value entered
	if rs == 1:
		result(screen, font1) # Display options when solved
	draw(pygame, screen, dif, font1, grid) # Draw required lines for making Sudoku grid
	if flag1 == 1:
		draw_box(pygame, screen, x, y, dif)	# Highlight the cell selected
	instruction(screen, font2) # Display instructions for the game

	# Update window
	pygame.display.update()

# Quit pygame window
pygame.quit()	
	
