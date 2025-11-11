#classes module
import pygame
import sys


pygame.init()

font_size = 64
font = pygame.font.SysFont(None, font_size)
menu_font = pygame.font.SysFont("Calibri",40) #sets the style of the menu font
font_colour = (0,0,0) #sets the font to black

SCREEN_WIDTH = 1600 #sets the width of the screen
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6) #sets the screen height
screen = pygame.display.set_mode(((SCREEN_WIDTH), (SCREEN_HEIGHT)))

p1turn = True#for now is used for turn distinction

#colour palette declaration - default
RED = (150,6,18)
BLUE = (6,11,150)
BISQUE = (154,255,199)
BLACK = (0,0,0)

#Card mechanics variables
slot_size = 5 #the size of the individual slots
num_slots_main = 15 #number of slots in the main queue
num_slots_priority = 3 #number of slots in the priority queue
queue_position = (50, 300) #the main position of the queue
priority_queue_position = (500, 50)
capacity_indicator_position = (1100, 550) #position of the recording stuffs
capacity_font_size = 24
capacity_font = pygame.font.SysFont('Arial', capacity_font_size)


class MenuButton():#creates the menu buttons
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))#co-ordinates to draw the location of the detection rect
		#change self.rect and self.text_rect co-ordinates to maintain positional consistency
		self.text_input = text_input #allows me to input the text
		self.text = menu_font.render(self.text_input, True, "Black")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True

	def HighlightByMouseHover(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = menu_font.render(self.text_input, True, RED) #allows the user to know whether the cursor is by the text
		else:
			self.text = menu_font.render(self.text_input, True, "black")#resets back to black

class GameButtonClass(MenuButton):#creates the new button instance for the Game buttons ie Back button etc
	def ___init__(self,image,x_pos,y_pos,text_input):
		super().__init__(image, x_pos, y_pos, text_input)
		self.image = image #image for this
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.circle = self.image.get_rect(center=(self.x_pos,self.y_pos))
		self.text_input = text_input
		self.text = menu_font.render(self.text_input,True,"Black")

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True

	def HighlightByMouseHover(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = menu_font.render(self.text_input, True, RED) #allows the user to know whether the cursor is by the text
		else:
			self.text = menu_font.render(self.text_input, True, "black")#resets back to black

#	def HighlightStats(self, position):
#		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
#			self.text = str(likelihood)
#			text_surface = font.render(self.text,True,BLACK)
#			pygame.draw.rect(text_surface,BISQUE,[self.x_pos, self.y_pos + 20])


class Territory(MenuButton):
	def __init__(self, image, y_pos,x_pos,text_input,troopval,name):
		super().__init__(image, x_pos, y_pos, text_input)
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		#self.circle = self.image.get_rect()
		self.text_input = text_input
		self.text = menu_font.render(self.text_input,True,"Black")
		self.troopval = int(troopval)
		self.trooptext = menu_font.render(str(self.troopval),True,"Black")
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.name = name
		self.Neighbours = []
		
	def update_troop_text(self):
		self.trooptext = menu_font.render(str(self.troopval),True,"Black")

	def update(self):
		screen.blit(self.image,self.rect)
		screen.blit(self.text, self.text_rect)
			
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True

	def HighlightByMouseHover(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.trooptext = menu_font.render(self.troopval, True, RED) #allows the user to know whether the cursor is by the text
		else:
			self.text = menu_font.render(self.troopval, True, "black")#resets back to black

	def ChangeAllegience(self):
		if self.image == 'ally.png' and self.troopval <= 0: #if this is the image it occupies but the troops have been expended
			self.image = 'enemy.png' #change to enemy
			self.troopval = 1 #increment to 1 so it avoids the 0 error
		elif self.image == 'neutral.png' and self.troopval <= 0:
			if p1turn == True:
				self.image = 'ally.png'
				self.troopval = 1
			elif not p1turn:
				self.image = 'enemy.png'
				self.troopval = 1
		if self.image == 'protan_test.png' and self.troopval <= 0: #if this is the image it occupies but the troops have been expended
			self.image = 'protan_enemy.png' #change to enemy
			self.troopval = 1 #then add 1 so that it doesn't loop in diff colours
		elif self.image == 'neutral.png' and self.troopval <= 0:
			if p1turn == True:
				self.image = 'protan_test.png'
				self.troopval = 1
			elif not p1turn:
				self.image = 'protan_enemy.png'
				self.troopval = 1
		if self.image == 'deutro_test.png' and self.troopval <= 0: #if this is the image it occupies but the troops have been expended
			self.image = 'deutro_enemy.png' #change to enemy
			self.troopval = 1 #then add 1 so that it doesn't loop in diff colours
		elif self.image == 'neutral.png' and self.troopval <= 0:
			if p1turn == True:
				self.image = 'deutro_test.png'
				self.troopval = 1
			elif not p1turn:
				self.image = 'deutro_enemy.png'
				self.troopval = 1
		if self.image == 'trit_ally.png' and self.troopval <= 0: #if this is the image it occupies but the troops have been expended
			self.image = 'trit_enemy.png' #change to enemy
			self.troopval = 1 #then add 1 so that it doesn't loop in diff colours
		elif self.image == 'neutral.png' and self.troopval <= 0:
			if p1turn == True:
				self.image = 'trit_ally.png'
				self.troopval = 1
			elif not p1turn:
				self.image = 'trit_enemy.png'
				self.troopval = 1

	def add_neighbour(self,territory):
		self.Neighbours.append(territory)

	def is_neighbour(self,territory):
		return territory in self.Neighbours



class Cards():
	def __init__(self, image, type, titlename):
		self.image = image #the image
		self.rect = self.image.get_rect() #the clickbox
		self.type = type
		self.titlename = titlename #this is to identify if the title matches self.territoryname later on in development

	def draw(self, screen, x, y): #draws the object onto the screen
		self.rect.x = x
		self.rect.y = y
		#puts the image onto the screen
		screen.blit(self.image, self.rect)

	def check_for_input(self, GAMEBUTTON_MOUSE_POS):  #checks to see if object clicked by mouse
		return self.rect.collidepoint(GAMEBUTTON_MOUSE_POS) 

class Queue:
    def __init__(self, num_slots, position):
        self.num_slots = num_slots #defines the number of available slots
        self.position = position
        self.slots = [] #defines the slots themselves as an empty list
        self.capacity_indicator = capacity_font.render(f"{len(self.slots)}/{self.num_slots}", True, (0,0,0)) 
		#creates a surface, for testing purposes, so that i may see if the cards fulfil its capacity limits

    def add(self, obj): #defines the adding mechanics between queues
        if len(self.slots) < self.num_slots: #checks to see if the slot number is less than the number of available slots
            self.slots.append(obj) #if there are sufficient slots available, append the object
            self.capacity_indicator = capacity_font.render(f"{len(self.slots)}/{self.num_slots}", True, (0,0,0)) #records the capacity
            return True
        else:
            return False #if it exceeds capacity, do nothing

    def remove(self, obj): #defines the removal mechanics between queues
        if obj in self.slots: #if the object is to be found in the slot position
            self.slots.remove(obj) #remove the object
            self.capacity_indicator = capacity_font.render(f"{len(self.slots)}/{self.num_slots}", True, (0,0,0))

    def draw(self, screen):
        for i, obj in enumerate(self.slots):
            x = self.position[0] + (i % 5) * (slot_size + 200) #draw each card 200 x co-ordinates away from one another
            y = self.position[1] + (i // 5) * (slot_size + 300) #for each new line in the queues, add 200 y co-ords of space
            obj.draw(screen, x, y) #draw the objects onto the screen in their assigned places
        screen.blit(self.capacity_indicator, capacity_indicator_position) #put the objects onto the screen
