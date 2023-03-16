def instruction(screen, font):
	text1 = font.render("PRESS D TO RESET TO DEFAULT | R TO EMPTY", 1, (0, 0, 0))
	text2 = font.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
	screen.blit(text1, (20, 520))	
	screen.blit(text2, (20, 540))
	
def result(screen, font):
	text1 = font.render("FINISHED PRESS R or D", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))