#NEA main project file
#started 14.11.22 - finished 28.04.23

#imported modules
import random
import pygame
import sys
from classes import *
import time

pygame.init()

#general game variable setup
menu = True
Timer = False
attackphase = True
deployphase = False
fortifyphase = False
finished = False
dist_done = False
p_start_troops = 40
e_start_troops = 40
n_start_troops = 39
troop_minimum = 1
p1_startup = False
timer_active = True
troopval = int()
cards_done = False
feedback = False
card_handin = False
turn_count = 0

#troopcounts for deploy phase
default = 4
NorthAmericaBonus = 5
SouthAmericaBonus = 3
troop_done = False
n_done = False
first_iteration = 0 
p1_turn = True
ai_turn = False
ai_done = False
#likelihood = 0

#variables for attack phase
second_selection = False
selection = False
transfer = True
clicked_territory = None

font_size = 24
font = pygame.font.SysFont('Arial', font_size)
menu_font = pygame.font.SysFont("Calibri",40) #sets the style of the menu font
font_colour = (0,0,0) #sets the font to black
attacker_text = font.render("Attacker is: None", True, (BLACK))
defender_text = font.render("Defender is: None", True, (BLACK))
output = font.render("", True, (BLACK))
attacker_surface = font.render("", True, (0, 0, 0))
defender_surface = font.render("", True, (0, 0, 0))


SCREEN_WIDTH = 1600 #sets the width of the screen
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6) #sets the screen height
screen = pygame.display.set_mode(((SCREEN_WIDTH), (SCREEN_HEIGHT)))

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1000) #Fires every 1000 milliseconds/ 1 second
time_remaining = 70
fortify_time_remaining = 30
fortify_timer_active = False
attack_timer_active = True

#fortify text
transfer_between = font.render(f"Troop transfer between:",True,BLACK)
element_zero = font.render(f"None",True,BLACK)
element_one = font.render(f"None",True,BLACK)
#not_valid = font.render("Not valid: territories are not neighbours",True,BLACK)
fortifying = False

#colour palette declaration - default
RED = (150,6,18)
BLUE = (6,11,150)
BISQUE = (154,255,199)
BLACK = (0,0,0)

#setting a timeframe
clock = pygame.time.Clock()
FPS = 60

#sets the gui size & caption
screen = pygame.display.set_mode(((SCREEN_WIDTH), (SCREEN_HEIGHT)))
pygame.display.set_caption('Control')

menu_button = pygame.image.load("Images/button.png") #associates the button image with the class button
menu_button = pygame.transform.scale(menu_button, (400, 150))

adjustment_button = pygame.transform.scale(menu_button,(50,50))

troop_button = pygame.image.load("Images/neutral.png")
troop_button = pygame.transform.scale(troop_button, (40,40))#scales the image size down of the troop button to fit the image 

game_button = pygame.image.load("Images/button.png")#associates with the same button image as menu_button
game_button = pygame.transform.scale(game_button, (200,75))

elongated_game_buttonv1 = pygame.transform.scale(game_button, (300,75))
elongated_game_buttonv2 = pygame.transform.scale(game_button, (400,75))

title_button = pygame.image.load("Images/Title.svg")
title_button = pygame.transform.scale(title_button,(600,200))

ally_button = pygame.image.load("Images/ally.png")
ally_button = pygame.transform.scale(ally_button,(60,60))

enemy_button = pygame.image.load("Images/enemy.png")
enemy_button = pygame.transform.scale(enemy_button, (40,40))

#map loading
map = pygame.image.load("Images/riskmap.svg")
map = pygame.transform.scale(map,(1600,960))
#loads all the buttons onto the screen, defining their location and text
GameButton = MenuButton(menu_button, 800, 300, "Game")#assigns the MenuButton class to the image, position and Text values specific to this instance
SettingsButton = MenuButton(menu_button,800, 500, "Settings")
QuitButton = MenuButton(menu_button,800,700,"Quit")
TitleButton = MenuButton(title_button,800,100,"Control")
#Settings Buttons
ColourBlind = MenuButton(menu_button,800,400,"ColourBlind Mode")
Rules = MenuButton(menu_button,800,400,"Rules")
#loads all adjustment buttons - for transferrence
PLUS = MenuButton(adjustment_button, 10,300,"+")
REMOVE = MenuButton(adjustment_button, 10,400,"-")
END_TURN = GameButtonClass(elongated_game_buttonv1, 500, 900, "END TURN") 

#defining the territories
#North America
Alaska = Territory(troop_button,125,115,"x",troopval,"Alaska")
NWTerritory = Territory(troop_button,125,240,"x",troopval,"North West Territory")
Alberta = Territory(troop_button,200,230,"x",troopval,"Alberta")
Ontario = Territory(troop_button,210,330,"x",troopval,"Ontario")#format y,x
Greenland = Territory(troop_button,100,540,"x",troopval,"Greenland")
WUS = Territory(troop_button,300,240,"x",troopval,"Western US")
Quebec = Territory(troop_button,210,450,"x",troopval,"Quebec")
EUS = Territory(troop_button,340,360,"x",troopval,"Eastern US")
Central_America = Territory(troop_button,430,260,"x",troopval,"Central America")

#South America
Venezuela = Territory(troop_button,495,360,"x",troopval,"Venezuela")
Peru = Territory(troop_button,610,370,"x",troopval,"Peru")
Brazil = Territory(troop_button,600,500,"x",troopval,"Brazil")
Argentina = Territory(troop_button,720,390,"x",troopval,"Argentina")

#Europe
Iceland = Territory(troop_button,160,650,"x",troopval,"Iceland")
GB = Territory(troop_button,290,650,"x",troopval,"Great Britain")
North_Europe = Territory(troop_button,300,760,"x",troopval,"North Europe")
West_Europe = Territory(troop_button,380,680,"x",troopval,"West Europe")
Scandinavia = Territory(troop_button,170,790,"x",troopval,"Scandinavia")
South_Europe = Territory(troop_button,380,790,"x",troopval,"Southern Europe")
East_Europe = Territory(troop_button,260,910,"x",troopval,"East Europe")

#Africa
N_Africa = Territory(troop_button,555,710,"x",troopval,"North Africa")
Egypt = Territory(troop_button,505,850,"x",troopval,"Egypt")
Congo = Territory(troop_button,660,850,"x",troopval,"Congo")
South_Africa = Territory(troop_button,780,850,"x",troopval,"South Africa")
East_Africa = Territory(troop_button,600,910,"x",troopval,"East Africa")
Madagascar = Territory(troop_button,780,1000,"x",troopval,"Madagascar")

#This is for the cards
NW_card_image = pygame.image.load('Images/NWTerritory_Card.png') #creates a surface for this type of card
NWTerritory_Card = Cards(NW_card_image,'Cannon','NW')

Ontario_card_image = pygame.image.load('Images/OntarioTerritory_Card.png')
Ontario_Card = Cards(Ontario_card_image,'Cannon','Ontario')

Alberta_card_image = pygame.image.load('Images/AlbertaTerritory_Card.png')
Alberta_Card = Cards(Alberta_card_image,'Soldier','Alberta')

Alaska_card_image = pygame.image.load('Images/AlaskaTerritory_Card.png')
Alaska_Card = Cards(Alaska_card_image,'Cavalry','Alaska')

Quebec_card_image = pygame.image.load('Images/QuebecTerritory_Card.png')
Quebec_Card = Cards(Quebec_card_image,'Cannon','Quebec')

EUS_card_image = pygame.image.load('Images/EasternUSTerritory_Card.png')
EUS_Card = Cards(EUS_card_image,'Cavalry','EUS')

#neighbouring defining - North America
Alaska.add_neighbour(NWTerritory)
Alaska.add_neighbour(Alberta)
NWTerritory.add_neighbour(Alaska)
NWTerritory.add_neighbour(Alberta)
NWTerritory.add_neighbour(Greenland)
NWTerritory.add_neighbour(Ontario)
Greenland.add_neighbour(NWTerritory)
Greenland.add_neighbour(Ontario)
Greenland.add_neighbour(Quebec)
Alberta.add_neighbour(Alaska)
Alberta.add_neighbour(NWTerritory)
Alberta.add_neighbour(Ontario)
Alberta.add_neighbour(WUS)
Ontario.add_neighbour(NWTerritory)
Ontario.add_neighbour(Greenland)
Ontario.add_neighbour(Alberta)
Ontario.add_neighbour(Quebec)
Ontario.add_neighbour(EUS)
Ontario.add_neighbour(WUS)
Quebec.add_neighbour(Greenland)
Quebec.add_neighbour(Ontario)
Quebec.add_neighbour(EUS)
WUS.add_neighbour(Alberta)
WUS.add_neighbour(Ontario)
WUS.add_neighbour(EUS)
WUS.add_neighbour(Central_America)
EUS.add_neighbour(Quebec)
EUS.add_neighbour(Ontario)
EUS.add_neighbour(WUS)
EUS.add_neighbour(Central_America)
Central_America.add_neighbour(EUS)
Central_America.add_neighbour(WUS)
Central_America.add_neighbour(Venezuela)
Venezuela.add_neighbour(Central_America)
Venezuela.add_neighbour(Peru)
Venezuela.add_neighbour(Brazil)
Peru.add_neighbour(Venezuela)
Peru.add_neighbour(Brazil)
Peru.add_neighbour(Argentina)
Argentina.add_neighbour(Peru)
Argentina.add_neighbour(Brazil)
Brazil.add_neighbour(Peru)
Brazil.add_neighbour(Venezuela)
Brazil.add_neighbour(Argentina)
Brazil.add_neighbour(N_Africa)
N_Africa.add_neighbour(Egypt)
N_Africa.add_neighbour(Congo)
N_Africa.add_neighbour(West_Europe)
N_Africa.add_neighbour(East_Africa)
Congo.add_neighbour(N_Africa)
Congo.add_neighbour(East_Africa)
Congo.add_neighbour(South_Africa)
South_Africa.add_neighbour(Congo)
South_Africa.add_neighbour(Madagascar)
Madagascar.add_neighbour(South_Africa)
Madagascar.add_neighbour(East_Africa)
East_Africa.add_neighbour(Madagascar)
East_Africa.add_neighbour(Congo)
East_Africa.add_neighbour(Egypt)
East_Africa.add_neighbour(N_Africa)
Egypt.add_neighbour(East_Africa)
Egypt.add_neighbour(N_Africa)
Egypt.add_neighbour(South_Europe)
South_Europe.add_neighbour(Egypt)
South_Europe.add_neighbour(East_Europe)
South_Europe.add_neighbour(North_Europe)
South_Europe.add_neighbour(West_Europe)
West_Europe.add_neighbour(East_Europe)
West_Europe.add_neighbour(GB)
West_Europe.add_neighbour(N_Africa)
West_Europe.add_neighbour(North_Europe)
GB.add_neighbour(Iceland)
GB.add_neighbour(West_Europe)
GB.add_neighbour(Scandinavia)
GB.add_neighbour(North_Europe)
Iceland.add_neighbour(GB)
Iceland.add_neighbour(Scandinavia)
Iceland.add_neighbour(Greenland)
North_Europe.add_neighbour(Scandinavia)
North_Europe.add_neighbour(GB)
North_Europe.add_neighbour(East_Europe)
North_Europe.add_neighbour(South_Europe)
Scandinavia.add_neighbour(GB)
Scandinavia.add_neighbour(Iceland)
Scandinavia.add_neighbour(North_Europe)
Scandinavia.add_neighbour(East_Europe)
East_Europe.add_neighbour(Scandinavia)
East_Europe.add_neighbour(North_Europe)
East_Europe.add_neighbour(South_Europe)

#this function's purpose is to flip between the Game screen and menu screen once this function is activated from the button associated being pressed
def Game():
	
	if dist_done == False:
		territorydistribution()
	if p1_startup == False:
		troopdistribution()
	while True:
		global GAMEBUTTON_MOUSE_POS, time_remaining, attackphase, fortifyphase, deployphase, timer_active, fortify_time_remaining, fortify_timer_active, DeployTroops, attack_timer_active
		global timer_rect, available_troops, troop_done, first_iteration, turn_count, territory_a, territory_b, territory_a_name, territory_b_name,  second_selection, selection, attacker_text
		global defender_text, output, territorya, territoryb, transfer, clicked_territory, element_one, element_zero, fortifying, p1_turn, ai_turn, n_done, ai_done, likelihood
		GAMEBUTTON_MOUSE_POS = pygame.mouse.get_pos()#location of the mouse pointer is assigned to this variable, that is only valid whilst Game() has been activated
		

		screen.fill(BISQUE)#the screen of the background is filled with bg colour default

		if attack_timer_active == True:
			# Substract time since last frame from remaining time
			time_remaining -= clock.tick(FPS) / 1000
		# Split the remaining time into minutes and seconds. divmod function returns the result of the integer
		# division (minutes) and the modulus of two inputs (seconds). 
  		# max function ensures timer does not go negative
			minutes, seconds = divmod(max(0, time_remaining), 120)
			timer_font = pygame.font.SysFont('Consolas',32) #defines the font type to be used
			timer_text = timer_font.render(f"Time Left: {seconds:.2f}", True, (BLACK))

			timer_rect = pygame.Rect((650, 50), (1, 1))
			screen.blit(timer_text, timer_rect)

		elif fortify_timer_active == True:
			fortify_time_remaining -= clock.tick(FPS) / 1000

			minutes, seconds = divmod(max(0, fortify_time_remaining), 120)
			timer_font = pygame.font.SysFont('Consolas',32) #defines the font type to be used
			timer_text = timer_font.render(f"Time Left: {seconds:.2f}", True, (BLACK))

			timer_rect = pygame.Rect((650, 50), (1, 1))
			screen.blit(timer_text, timer_rect)


		elif fortify_timer_active == False and attack_timer_active == False and deployphase == True: #if the conditions are in place...
			deploy_font = pygame.font.SysFont('Consolas',24)
			deploy_text = deploy_font.render(f"You have {available_troops} troops remaining",True,(BLACK)) #formats the troops available
			screen.blit(deploy_text,timer_rect)#outputs the troops available

		if attackphase == True and transfer == True:
			screen.blit(attacker_text, (10, 10))
			screen.blit(defender_text, (10,40))
			screen.blit(output,(10,70))
			screen.blit(attacker_surface,(10,600))
			screen.blit(defender_surface,(10,650))


		screen.blit(map,(0,0))#puts the map onto the screen
		GAME_BACK = GameButtonClass(game_button, 200, 900, "BACK")#in format image, y,x,text


		GAME_BACK.HighlightByMouseHover(GAMEBUTTON_MOUSE_POS)
		GAME_BACK.update()

		END_TURN.HighlightByMouseHover(GAMEBUTTON_MOUSE_POS)
		END_TURN.update()
		
		TRADE_IN = GameButtonClass(elongated_game_buttonv2, 900, 900, "CARD TRADE IN")

		TRADE_IN.HighlightByMouseHover(GAMEBUTTON_MOUSE_POS)
		TRADE_IN.update()

		CONFIRM_SELECTION = GameButtonClass(elongated_game_buttonv2, 1350,900, "CONFIRM ATTACK")

		CONFIRM_SELECTION.HighlightByMouseHover(GAMEBUTTON_MOUSE_POS)
		CONFIRM_SELECTION.update()

		if ai_turn == True and attackphase == True:#if it is the ai's turn and the attack phase has commenced
			if time_remaining != 0:#as long as the time is not 0
				random_territory = random.choice(enemy_territories)#picks a random territory
				territorya = random_territory#assigning it to territorya
				if territorya.troopval == 1:
					territorya = None
					random_territory = None
					random_territory = random.choice(enemy_territories)#picks a random territory
					territorya = random_territory
					print(territorya.name, territorya.troopval)
				elif territorya.troopval <= 0:
					territorya.troopval = 1
				else:	
					print(territorya.name,territorya.troopval)#prints out the name (for test purposes) - to keep track of terminal responses
				random_territory = None#resets to None, so will not endlessly iterate
				random_territory = random.choice(p1_territories+neutral_territories) #picks a new territory
				territoryb = random_territory#assigns this to territory b
				print(territoryb.name, territoryb.troopval)#print this for testing purposes
				random_territory = None
				if territorya.is_neighbour(territoryb):#if they are neighbours
					win_probability()#calculate the win probability
					print(likelihood)
					if likelihood > 30 and territorya.troopval != 1:#if the win probility is greater tha 30%
						#print(likelihood)
						diceroll()#make the move
					else:
						time.sleep(0.05) #time.sleep in place to put limitations on ai
				else:
					time.sleep(0.05)

		if transfer == False: #setting all the text values...
			transfer_font = pygame.font.SysFont('Arial',12)
			transfer_text = transfer_font.render(f"{territory_a_name}:{territorya.troopval}",True,BLACK)
			instruction_text = transfer_font.render("Press '.' to confirm choice",True,BLACK)
			instruction_text_2 = transfer_font.render(f"Press '+' to transfer troops to {territory_b_name}",True,BLACK)
			instruction_text_3 = transfer_font.render(f"Press '-' to transfer troops to {territory_a_name}",True,BLACK)
			transfer_text_2 = transfer_font.render(f"{territory_b_name}:{territoryb.troopval}",True,BLACK)

		if attackphase == True and transfer == False:
			screen.blit(attacker_text, (10, 10))
			screen.blit(defender_text, (10,40))
			screen.blit(transfer_text,(10,750))
			screen.blit(instruction_text,(10,600))
			screen.blit(instruction_text_2,(10,650))
			screen.blit(instruction_text_3,(10,700))
			screen.blit(transfer_text_2,(10,800))
		PLUS = MenuButton(adjustment_button, 30,450,"+")
		REMOVE = MenuButton(adjustment_button, 30,500,"-")
		TRANSFER_FINALIZE = MenuButton(adjustment_button, 30,550,".")

		REMOVE.HighlightByMouseHover(GAMEBUTTON_MOUSE_POS)
		REMOVE.update()
		PLUS.HighlightByMouseHover(GAMEBUTTON_MOUSE_POS)
		PLUS.update()
		TRANSFER_FINALIZE.HighlightByMouseHover(GAMEBUTTON_MOUSE_POS)
		TRANSFER_FINALIZE.update()

		if fortifyphase and fortifying == True:
			transfer_font = pygame.font.SysFont('Arial',12)
			if len(chosen_list) != 0:
				instruction_text_setb = transfer_font.render("Press '.' to confirm/reset",True,BLACK)
				instruction_text_set_b_2 = transfer_font.render(f"Press '+' to transfer troops to {chosen_list[0].name}",True,BLACK)
				instruction_text_set_b_3 = transfer_font.render(f"Press '-' to transfer troops to {chosen_list[1].name}",True,BLACK)
			else:
				instruction_text_setb = transfer_font.render("Press '.' to confirm/reset",True,BLACK)
				instruction_text_set_b_2 = transfer_font.render(f"Press '+' to transfer troops to Not selected",True,BLACK)
				instruction_text_set_b_3 = transfer_font.render(f"Press '-' to transfer troops to Not selected",True,BLACK)

			screen.blit(instruction_text_setb,(10,600))
			screen.blit(instruction_text_set_b_2,(10,650))
			screen.blit(instruction_text_set_b_3,(10,700))


		if fortifyphase == True:
			screen.blit(transfer_between,(10,10))
			screen.blit(element_zero,(10,40))
			screen.blit(element_one,(10,70))
			#screen.blit(not_valid(10,100))

		for territory in territories:
			if territory in p1_territories:
				screen.blit(ally_button, (territory.x_pos, territory.y_pos))
			elif territory in enemy_territories:
				screen.blit(enemy_button, (territory.x_pos, territory.y_pos))
			elif territory in neutral_territories:
				screen.blit(troop_button, (territory.x_pos, territory.y_pos))
			screen.blit(territory.trooptext, (territory.x_pos, territory.y_pos))

		for event in pygame.event.get():
			if len(p1_territories) == 0 or len(enemy_territories) == 0:
				win_screen()
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if GAME_BACK.checkForInput(GAMEBUTTON_MOUSE_POS):
					main_menu()
				elif END_TURN.checkForInput(GAMEBUTTON_MOUSE_POS) and p1_turn == True:
					if attack_timer_active == True:
						time_remaining = 0
					elif fortify_timer_active == True:
						fortify_time_remaining = 0
				if deployphase == True:
					if TRADE_IN.checkForInput(GAMEBUTTON_MOUSE_POS):
						trade_in()
					for territory in territories:
						if territory.rect.collidepoint(GAMEBUTTON_MOUSE_POS): #if the territory is clicked by the mouse
							chosen_list.append(territory) #append it to a new list
							for territory in chosen_list: #for that one territory
								if territory in p1_territories and available_troops!=0: #validates which territory the player can add to
									territory.troopval += 1
									available_troops -= 1
									territory.update_troop_text()
									chosen_list.remove(territory)
								else:
									print("You cannot access this at this time")
				if attackphase == True:#if the attack phase in in progress
					if p1_turn == True:
						if CONFIRM_SELECTION.checkForInput(GAMEBUTTON_MOUSE_POS): #if the confirm selection has been clicked
							if selection == True and second_selection == True and transfer == True: #as long as both values have been submitted
								if territorya.is_neighbour(territoryb): #if the territory a is neighbours with the selected enemy territory...
									output = font.render("Attack Confirmed",True,(BLACK)) #change the text to attack confirmed
									diceroll()
								else:
									output = font.render("Error: Territories aren't neighbours.",True,(BLACK)) #otherwise tell the user that they cannot do this
									#resets the territories selected
									territory_a.remove(territorya)
									territory_b.remove(territoryb)
									#updates the text to notify the user
									attacker_text = font.render("Attacker is: None", True, (BLACK))
									defender_text = font.render("Defender is: None", True, (BLACK))
									#prevents the cycle from erroring
									selection = False
									second_selection = False
						if TRANSFER_FINALIZE.checkForInput(GAMEBUTTON_MOUSE_POS): #if the user wishes to finalize movement...
							if transfer == False: #if transfer is active
								territorya = None#set territory a to none, so that it cannot be altered now
								selection = False #set selection to False, so as to not error the confirm attack button if pressed
								territoryb = None #set territory b to none
								second_selection = False #same as selection
								transfer = True #set to true, so that these buttons can no longer be used until next transfer
						if PLUS.checkForInput(GAMEBUTTON_MOUSE_POS): #if the '+' is pressed...
							if transfer == False: #if the troops are in the prcess of being moved..
								if territoryb.troopval >= 1 and territorya.troopval > 1: #as long as at least 1 troop on territory being moved from..
									territoryb.troopval += 1#add 1 to the other
									territoryb.update_troop_text()#update to screen
									territorya.troopval -= 1 #remove from current
									territorya.update_troop_text()
						elif REMOVE.checkForInput(GAMEBUTTON_MOUSE_POS): #if the '-' is pressed...
							if transfer == False: #if the troops are in the process of being moved
								if territorya.troopval >= 1 and territoryb.troopval > 1: #as long as there is at least 1 troop on the territory it is being moved from...
									territoryb.troopval -= 1 #remove one
									territoryb.update_troop_text() #update the value
									territorya.troopval += 1 #add to the other territory
									territorya.update_troop_text()
						for territory in p1_territories:#if the territory is player 1's
							if territory.rect.collidepoint(GAMEBUTTON_MOUSE_POS): #and gets clicked....
								if len(territory_a) != 1: #if the length of the territory is not 1
									territory_a.append(territory) #add it to the list
									for territory in territory_a: #for the listed territory
										territory_a_name = territory.name #log the name (for testing purposes)
										territorya = territory #logs the territory (for comparison values)
										territoryatroops = territory.troopval #logs the troop value
										if territoryatroops >= 2:
											attacker_text = font.render(f"Attacker is: {territory_a_name}", True, (BLACK))
											selection = True
										else:
											attacker_text = font.render(f"Attacker is: None, please select another, as {territory_a_name} does not have enough troops", True, (BLACK))
											territory_a.remove(territorya)
											selection = False
								else:
									attacker_text = font.render("Attacker is: None", True, (BLACK))
									territory_a.remove(territorya) #if it gets to larger than 1, deselect
									selection = False

						for territory in enemy_territories+neutral_territories: #if the territory is not te player's
							if territory.rect.collidepoint(GAMEBUTTON_MOUSE_POS): #and it gets clicked
								if len(territory_b) != 1: #check if empty
									territory_b.append(territory) #add to the list
									for territory in territory_b:
										territory_b_name = territory.name #log the name (for test purposes)
										territoryb = territory #logs the name
										defender_text = font.render(f"Defender is: {territory_b_name}", True, (BLACK))
										second_selection = True
								else:
									defender_text = font.render("Defender is: None", True, (BLACK))
									territory_b.remove(territoryb)#if it is 1 then remove it - so deselects
									second_selection = False						
				if fortifyphase == True:
					for territory in p1_territories:
						if territory.rect.collidepoint(GAMEBUTTON_MOUSE_POS):
							clicked_territory = territory #the collided territory becomes selected
							if len(chosen_list) == 0: #if the list is empty
								chosen_list.append(clicked_territory) #add the selected territoriy to the list
								#print(chosen_list[0].name) #print the name of the first indexed object
								#transfer_between = font.render(f"Troop transfer between:",True,BLACK)
								element_zero = font.render(f"{chosen_list[0].name}",True,BLACK)
							elif len(chosen_list) == 1: #if the list already has an object
								chosen_list.append(clicked_territory) #add the next
								if chosen_list[1] == chosen_list[0]: #if both indexed elements are the same
									#print(f"Not valid:{chosen_list[1].name} must be different to {chosen_list[0].name}")
									chosen_list.remove(clicked_territory) #remove from the list
								elif chosen_list[0].is_neighbour(chosen_list[1]): #validate if they are neighbours
									#print(f"They match {chosen_list[0].name} is neighbours with {chosen_list[1].name}")
									element_one = font.render(f"{chosen_list[1].name}",True,BLACK)
								else: #if they aren't neighbours, remove them
									chosen_list.remove(clicked_territory)
									#not_valid = font.render("Not valid: territories are not neighbours",True,BLACK)
									#print(f"{chosen_list[0].name}")#show the only remaining element in the list
							elif len(chosen_list) == 2:#if the list is already full
								chosen_list[0] = chosen_list[1] #element 0 is now element 1
								#chosen_list[1] = None
								chosen_list.remove(chosen_list[1]) #remove element 1, so that the length is now 1
								element_one = font.render(f"None",True,BLACK)
								#print(f"first element in list reset {chosen_list[0].name}")
						if len(chosen_list) == 2:
							fortifying = True
					if TRANSFER_FINALIZE.checkForInput(GAMEBUTTON_MOUSE_POS): #if the user wishes to finalize movement...
						if fortifying == True: #if transfer is active
							chosen_list.remove(chosen_list[1])#set first selected none, so no alteration
							chosen_list.remove(chosen_list[0]) #set territory b to none
							fortifying = False
							element_zero = font.render(f"None",True,BLACK)
							element_one = font.render(f"None",True,BLACK)
					if PLUS.checkForInput(GAMEBUTTON_MOUSE_POS): #if the '+' is pressed...
						if fortifying == True: #if the troops are in the prcess of being moved..
							if chosen_list[0].troopval >= 1 and chosen_list[1].troopval > 1: #as long as at least 1 troop on territory being moved from..
								chosen_list[1].troopval -= 1#add 1 to the other
								chosen_list[1].update_troop_text()#update to screen
								chosen_list[0].troopval += 1 #remove from current
								chosen_list[0].update_troop_text()
					elif REMOVE.checkForInput(GAMEBUTTON_MOUSE_POS): #if the '-' is pressed...
						if fortifying == True: #if the troops are in the prcess of being moved..
							if chosen_list[1].troopval >= 1 and chosen_list[0].troopval > 1: #as long as there is at least 1 troop on the territory it is being moved from...
								chosen_list[0].troopval -= 1 #remove one
								chosen_list[0].update_troop_text() #update the value
								chosen_list[1].troopval += 1 #add to the other territory
								chosen_list[1].update_troop_text()

		if attackphase == True and first_iteration<1 and p1_turn == True:
			attack_timer_active = True
			deployphase = False
			#time_remaining = 10
			if time_remaining <= 0:
				fortifyphase = True
				timer_active = False
				attackphase = False 
				attack_timer_active = False
				fortify_time_remaining = 30
		if attackphase == True and first_iteration>=1 and p1_turn == True:
			attack_timer_active = True
			deployphase = False
			if time_remaining <= 0:
				fortifyphase = True
				timer_active = False
				attackphase = False 
				attack_timer_active = False
				fortify_time_remaining = 30
		if attackphase == True and first_iteration>=1 and ai_turn == True:
			attack_timer_active = True
			deployphase = False
			if time_remaining <= 0:
				fortifyphase = True
				timer_active = False
				attackphase = False 
				attack_timer_active = False
				fortify_time_remaining = 30
		elif fortifyphase == True and first_iteration<1 and p1_turn == True: #continue as normal
			fortify_timer_active = True
			if fortify_time_remaining <= 0:
				fortifyphase = False
				fortify_timer_active = False
				deployphase = True
		elif fortifyphase == True and first_iteration>=1 and p1_turn == True: #this will allow to end the turn
			fortify_timer_active = True
			if fortify_time_remaining <= 0:
				fortifyphase = False
				fortify_timer_active = False
				deployphase = True
				troop_done = False
				n_done = False
				turn_count+=1
		elif fortifyphase == True and first_iteration>=1 and ai_turn == True: #this will allow to end the turn
			fortify_timer_active = True
			if fortify_time_remaining <= 0:
				fortifyphase = False
				fortify_timer_active = False
				deployphase = True
				troop_done = False
				ai_done = False
				turn_count +=1 #change turns once this is over.
		elif deployphase == True and p1_turn == True:
			DeployTroops()#calls the function to calculate p1's troops
			NeutralDeploy()#calls the function for the neutral deployment
			if available_troops == 0 and first_iteration == 0:
				first_iteration += 1 #the first iteration is used to create a unique set of events from the rest of the game
				attackphase = True
				deployphase = False
				time_remaining = 70
			if available_troops == 0 and first_iteration > 0:#this will be followed for the rest of the game
				#so that phase system goes deploy < attack < fortify < end turn
				attackphase = True
				deployphase = False
				time_remaining = 70
		elif deployphase == True and ai_turn == True:
			DeployTroops()#calls function for troop calc
			NeutralDeploy()#calls function for neutral deployment
			AIDeploy()#calls the function to deploy ai's troops based off this calc

		if turn_count % 2 == 0: #if the turn count(automatically set to 0) is divisible by 2, and the remainder is 0, then it is
			#player 1's turn, if not, it is ai turn
			p1_turn = True
			ai_turn = False
		else: #if there is 1 left over, it is ai's turn
			p1_turn = False
			ai_turn = True
		
		pygame.display.update()

territories = [
	Alaska, NWTerritory, Alberta, Ontario, Quebec, Greenland, WUS, EUS, Central_America, Venezuela, Peru, Brazil, 
	Argentina, Iceland, GB, North_Europe, West_Europe, Scandinavia, South_Europe, East_Europe, N_Africa, Egypt, Congo
	,South_Africa, East_Africa, Madagascar]
neutral_territories = [
	Alaska, NWTerritory, Alberta, Ontario, Quebec, Greenland, WUS, EUS, Central_America, Venezuela, Peru, Brazil, 
	Argentina, Iceland, GB, North_Europe, West_Europe, Scandinavia, South_Europe, East_Europe, N_Africa, Egypt, Congo
	,South_Africa, East_Africa, Madagascar]
p1_territories = []
enemy_territories = []

chosen_list = []
territory_a = []
territory_b = []

troops = []

#defining the north american countries
NAterritories = [Alaska, NWTerritory, Alberta, Ontario, Quebec, Greenland, WUS, EUS, Central_America]
SAterritories = [Venezuela, Peru, Brazil, Argentina, ]
Europe = [Iceland, GB, North_Europe, West_Europe, Scandinavia, South_Europe, East_Europe]
Africa = [N_Africa, Egypt, Congo,South_Africa, East_Africa, Madagascar]

def win_screen():
	if len(p1_territories) > len(enemy_territories):
		winningalias = "Player"
	else:
		winningalias = "AI Player"
	while True:
		screen.fill(BISQUE)

		winner_font = pygame.font.SysFont('Arial',72)
		win_text = winner_font.render(f"{winningalias} Wins!", True,BLACK)
		win_subtext= winner_font.render("Close screen to exit",True,BLACK)

		screen.blit(win_text,(550,400))
		screen.blit(win_subtext,(450,800))

	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		
#creating the territory randomiser
def territorydistribution():
	global dist_done
	dist_done = True
	territorycount = 0
	if len(neutral_territories) > 0:
		while territorycount !=8:
			random_territory = random.choice(neutral_territories) #for the random territories of the ally
			neutral_territories.remove(random_territory)
			p1_territories.append(random_territory)
			random_enemy = random.choice(neutral_territories) #for the random territories of the enemy
			neutral_territories.remove(random_enemy)
			enemy_territories.append(random_enemy)
			territorycount += 1

def troopdistribution():
	#this will be used to distibute the troops randomly
	global p1_startup
	p1_startup = True
	global p_start_troops, e_start_troops, n_start_troops #Defines the variables for the number of starting troops per player

	p1_territory_troop_vals = [0] * len(p1_territories) #Creates a list of the troopvals foe each territory owned by p1
	enemy_territory_troop_vals = [0] * len(enemy_territories)

	while sum(p1_territory_troop_vals) != p_start_troops: #loop until total troopval is equal to starting number (p1)
		for idx in range(len(p1_territory_troop_vals)): #loops through each p1 territory, randomly assinging troopvals
			p1_territory_troop_vals[idx] = random.randint(1, p_start_troops-len(p1_territories)+1)
	
	for idx, territory in enumerate(p1_territories):#Assign troopval to p1, update text on screen
		territory.troopval = p1_territory_troop_vals[idx]
		territory.update_troop_text()

	while sum(enemy_territory_troop_vals) != e_start_troops:#loop until total troopval is equal to starting number (enemy)
		for idx in range(len(enemy_territory_troop_vals)):#loops through each enemy territory, randomly assinging troopvals
			enemy_territory_troop_vals[idx] = random.randint(1, e_start_troops-len(enemy_territories)+1)
	
	for idx, territory in enumerate(enemy_territories):#Assign troopval to enemy, update text on screen
		territory.troopval = enemy_territory_troop_vals[idx]
		territory.update_troop_text()

	neutral_territory_troop_vals = [n_start_troops // len(neutral_territories)] * len(neutral_territories)
	#the line above creates a troop value list for each neutral territory where troops are equally distributed

	for idx, territory in enumerate(neutral_territories):#Assign troopval to neutral territories, updating the text on screen
			territory.troopval = neutral_territory_troop_vals[idx]
			territory.update_troop_text()
			
def Settings():
	global BISQUE, ally_button, enemy_button
	while True:
		SETTINGS_MOUSE_POS = pygame.mouse.get_pos()

		screen.fill(BISQUE) #overlays the screen

		TitleButton = MenuButton(title_button,800,100,"Control") #title button

		TitleButton.update()#ensures that it appears on the screen

		SETTINGS_BACK = GameButtonClass(game_button, 100, 800, "BACK") #so the user can jump back and forth between screens
		SETTINGS_BACK.HighlightByMouseHover(SETTINGS_MOUSE_POS)
		SETTINGS_BACK.update()

		Tritanopia = MenuButton(menu_button,800,300,"Tritanopia") #tritanopia button
		Tritanopia.HighlightByMouseHover(SETTINGS_MOUSE_POS)
		Tritanopia.update()

		Deuteranopia = MenuButton(menu_button,300,300,"Deuteranopia") #deuteranopia button
		Deuteranopia.HighlightByMouseHover(SETTINGS_MOUSE_POS)
		Deuteranopia.update()

		Protanopia = MenuButton(menu_button,1300,300,"Protanopia") #protanopia button
		Protanopia.HighlightByMouseHover(SETTINGS_MOUSE_POS)
		Protanopia.update()

		Default = MenuButton(menu_button,800,500,"Default") #default colour settings
		Default.HighlightByMouseHover(SETTINGS_MOUSE_POS)
		Default.update()

		Rules = MenuButton(menu_button,800,700,"Rules") #rules button
		Rules.HighlightByMouseHover(SETTINGS_MOUSE_POS)
		Rules.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if SETTINGS_BACK.checkForInput(SETTINGS_MOUSE_POS):
					main_menu()
				if Tritanopia.checkForInput(SETTINGS_MOUSE_POS): #if the tritanopia button is clicked..
					BISQUE = (159,223,225) #change the background colour
					ally_button = pygame.image.load("Images/trit_ally.png")
					ally_button = pygame.transform.scale(ally_button,(60,60)) #change the colour scheme for the ally
					enemy_button = pygame.image.load("Images/trit_enemy.png")
					enemy_button = pygame.transform.scale(enemy_button, (40,40)) #change the colour scheme for ai
				if Deuteranopia.checkForInput(SETTINGS_MOUSE_POS):#if the deuteranopia button is clicked..
					BISQUE = (191,184,215)#change the background colour
					ally_button = pygame.image.load("Images/deutro_test.png")
					ally_button = pygame.transform.scale(ally_button,(60,60))#change the colour scheme for the ally
					enemy_button = pygame.image.load("Images/deutro_enemy.png")
					enemy_button = pygame.transform.scale(enemy_button, (40,40))#change the colour scheme for ai
				if Protanopia.checkForInput(SETTINGS_MOUSE_POS):
					BISQUE = (197,198,212)#change the background colour
					ally_button = pygame.image.load("Images/protan_test.png")
					ally_button = pygame.transform.scale(ally_button,(60,60))#change the colour scheme for the ally
					enemy_button = pygame.image.load("Images/protan_enemy.png")
					enemy_button = pygame.transform.scale(enemy_button, (40,40))#change the colour scheme for ai
				if Default.checkForInput(SETTINGS_MOUSE_POS):
					BISQUE = (154,255,199)#change the background colour
					ally_button = pygame.image.load("Images/ally.png")
					ally_button = pygame.transform.scale(ally_button,(60,60))#change the colour scheme for the ally
					enemy_button = pygame.image.load("Images/enemy.png")
					enemy_button = pygame.transform.scale(enemy_button, (40,40))#change the colour scheme for ai
				if Rules.checkForInput(SETTINGS_MOUSE_POS):
					pass

		pygame.display.update()

def main_menu():#main menu function
	while menu == True:#when the menu is active
		screen.fill(BISQUE)#set background

		MENU_MOUSE_POS = pygame.mouse.get_pos()#the menu pointer is now the mouse pointer

		GameButton = MenuButton(menu_button, 800, 300, "Game")
		
		SettingsButton = MenuButton(menu_button, 800, 500, "Settings")
		
		QuitButton = MenuButton(menu_button, 800, 700, "Exit")
		TitleButton = MenuButton(title_button,800,100,"Control") #sets the title button out onto the screen

		for button in [GameButton, SettingsButton, QuitButton, TitleButton]:
			button.HighlightByMouseHover(MENU_MOUSE_POS)
			button.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if GameButton.checkForInput(MENU_MOUSE_POS):
					Game()
				if SettingsButton.checkForInput(MENU_MOUSE_POS):
					Settings()
				if QuitButton.checkForInput(MENU_MOUSE_POS):
					pygame.quit()
					sys.exit()

		pygame.display.update()

def DeployTroops():
	global default, NorthAmericaBonus, available_troops,deployphase,attackphase,attack_timer_active,card_handin,troop_done,ai_available_troops
	#for territories in NAterritories:
	if p1_turn == True:
		if troop_done == False: #if it not unactivated
			if card_handin == False: #and there is no additionals
				if  p1_territories in NAterritories:#if the 1st player's territories cannot be found in the NA list as a whole
					#if generate == True:
					available_troops = default + NorthAmericaBonus #make the total 8
					troop_done = True#make done
					return available_troops
				if p1_territories in SAterritories:
					available_troops = default + SouthAmericaBonus
				else:
					NorthAmericaBonus = 0
					SouthAmericaBonus = 0
					available_troops = default + NorthAmericaBonus + SouthAmericaBonus#make total 3
					troop_done = True
					return available_troops
			else:
				available_troops = available_troops + 10 #add 10 to the total once.
				troop_done = True
				return available_troops
	elif ai_turn == True:
		if troop_done == False: #if it not unactivated
			if  enemy_territories in NAterritories:#if the 1st player's territories cannot be found in the NA list as a whole
				#if generate == True:
				ai_available_troops = default + NorthAmericaBonus #make the total 8
				troop_done = True#make done
				return ai_available_troops
			if enemy_territories in SAterritories:
				ai_available_troops = default + SouthAmericaBonus
				return ai_available_troops
			else:
				NorthAmericaBonus = 0
				SouthAmericaBonus = 0
				ai_available_troops = default + NorthAmericaBonus + SouthAmericaBonus#make total 3
				troop_done = True
				return ai_available_troops

available_troops = DeployTroops()
ai_available_troops = DeployTroops()

def trade_in():
	global GAMEBUTTON_MOUSE_POS, main_queue,feedback,available_troops,troop_done, card_handin, first_obj
	if cards_done == False:
		CardDistribution()
	while True:
		GAMEBUTTON_MOUSE_POS = pygame.mouse.get_pos()

		screen.fill (BISQUE)
		main_queue.draw(screen)
		priority_queue.draw(screen)
		GAME_BACK = GameButtonClass(game_button, 200, 900, "BACK")#in format image, y,x,text


		GAME_BACK.HighlightByMouseHover(GAMEBUTTON_MOUSE_POS)
		GAME_BACK.update()

		if feedback == True:#if something not valid triggered...
			response_rect = pygame.Rect((650, 50), (1, 1))
			response_font = pygame.font.SysFont('Sans Serif',32)
			response_text = response_font.render("That is not valid",True,(125,125,125))#create the text surface
			#print("not valid") #if the type's don't match then not valid
			screen.blit(response_text,response_rect)#put onto the screen
			time.sleep(1)
			feedback = False
			if len(priority_queue.slots) == 0:#if the queue is reset
				feedback = False#message disappears
		else:
			feedback = False

		if len(priority_queue.slots) == 3:#if it has reached capacity
			priority_queue.type = None
			for obj in priority_queue.slots.copy():#all the objects in the priority queue...
				#print(len(priority_queue.slots))
				if obj in priority_queue.slots:
				#while len(priority_queue.slots) !=0:
					priority_queue.remove(obj)#are individually deleted...
					cards.append(obj)#these cards are then added back to the list for later randomisation
					card_handin = True
					troop_done = False


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if GAME_BACK.checkForInput(GAMEBUTTON_MOUSE_POS):
					Game()
				#GAMEBUTTON_MOUSE_POS = pygame.mouse.get_pos()
			# Check if an object in the main queue was clicked
				#mouse_pos = pygame.mouse.get_pos()
				clicked_obj = None
				# Check if an object in the main queue was clicked
				for obj in main_queue.slots:
					if obj.check_for_input(GAMEBUTTON_MOUSE_POS):
						clicked_obj = obj
						break
				# Check if an object in the priority queue was clicked
				for obj in priority_queue.slots:
					if obj.check_for_input(GAMEBUTTON_MOUSE_POS):
						clicked_obj = obj
						break
				if clicked_obj:
					if clicked_obj in main_queue.slots:
						if len (priority_queue.slots)!=3 and len(priority_queue.slots)>=1: #if the length ranges from 1-3..
							if clicked_obj.type == first_obj.type:#if the type is the same
								main_queue.remove(clicked_obj) #remove from the main queue
								priority_queue.add(clicked_obj)#add to priority
							else:
								feedback = True
						#this is the setup statement, as it always starts with 0 in.
						elif len(priority_queue.slots) == 0:#if there is nothing in the priority queue, reset
							priority_queue.type = None
							first_obj = clicked_obj#starts off the priority list type
							main_queue.remove(clicked_obj)
							priority_queue.add(clicked_obj)
							priority_queue.type = first_obj.type
					elif clicked_obj in priority_queue.slots:#can remove anything from priority queue
						priority_queue.remove(clicked_obj)
						main_queue.add(clicked_obj)





			pygame.display.flip()
		pygame.display.update()

main_queue = Queue(num_slots_main, queue_position) #defines the queue with 15 slots, and their positions
priority_queue = Queue(num_slots_priority, priority_queue_position) #3 slots and their location

def CardDistribution():
	global cards
	cards = [NWTerritory_Card,Ontario_Card,Alberta_Card,Alaska_Card, Quebec_Card,EUS_Card]
	p1cards = []
	global cards_done, main_queue
	cards_done = True
	cardcount = 0
	if len(cards) > 0:
		while cardcount !=6: #set this to 1, then every time the turn begins again, 
			#set the cardcount back down to 0, so that it can enact this loop again
			random_card = random.choice(cards) #for the random cards of the ally
			cards.remove(random_card)
			p1cards.append(random_card)
			main_queue.add(random_card)
			cardcount += 1

def NeutralDeploy(): #adds half of what the player recieves, randomly adding it
	global available_troops, n_done
	neutral_available_troops = available_troops // 2
	while neutral_available_troops > 0 and n_done == False:#while the requirements arent met...
		random_territory = random.choice(neutral_territories) #pick a random territory
		chosen_list.append(random_territory)#add it to the current edited territory
		random_territory.troopval += 1 #add to the troopvalue
		neutral_available_troops -= 1#decrement the available troops by 1
		random_territory.update_troop_text() #update the text on screen
		chosen_list.remove(random_territory)#remove it from the list
		random_territory = None#set to none, so it wont duplicate itself in the list
		#print(neutral_available_troops)
		if neutral_available_troops == 0:#if it reaches 0, disable the while loop
			n_done = True

def AIDeploy(): #adds half of what the player recieves, randomly adding it
	global ai_available_troops, ai_done,attackphase,deployphase,time_remaining
	while ai_available_troops > 0 and ai_done == False:#while the requirements arent met...
		random_territory = random.choice(enemy_territories) #pick a random territory
		chosen_list.append(random_territory)#add it to the current edited territory
		random_territory.troopval += 1 #add to the troopvalue
		ai_available_troops -= 1#decrement the available troops by 1
		random_territory.update_troop_text() #update the text on screen
		chosen_list.remove(random_territory)#remove it from the list
		random_territory = None#set to none, so it wont duplicate itself in the list
		if ai_available_troops == 0:#if it reaches 0, disable the while loop
			attackphase = True
			deployphase = False
			time_remaining = 35 #shortens the time - makes it fair for the player
			ai_done = True

def diceroll(): #function for the start of the troop decrements
	global attacker_surface, defender_surface, attacker_text, defender_text, territoryb, selection, second_selection, territorya, transfer
	# Determine how many dice to roll for the attacker and defender

	min = 1

	if territorya.troopval == 2: #if the player has only 2 troops available
		attacker_dice_count = 1 #they only get one attack dice
	elif territorya.troopval == 3: #if there are 3 troops, give them 2 dice
		attacker_dice_count = 2
	else:
		attacker_dice_count = 3#otherwise they get 3 dice
		
	if territoryb.troopval == 1:#if the defender has only 1 troop, they are entitled to 1 dice
		defender_dice_count = 1
	else:
		defender_dice_count = 2#whereas anything more than 1 allows them to have 2

	#picks a random value from 1 to 6, for every time each playr have a dice
	attacker_rolls = sorted([random.randint(1, 6) for i in range(attacker_dice_count)],reverse=True)
	#reverse = True ensures that it is sorted into descending order so that its first element is the highest
	defender_rolls = sorted([random.randint(1, 6) for j in range(defender_dice_count)],reverse=True)

	# Render the results as text
	attacker_dice = f"Attacker: {attacker_rolls}"
	defender_dice = f"Defender: {defender_rolls}"
	
	#print(attacker_dice,defender_dice) #print statement used for testing purposes
	attacker_surface = font.render(attacker_dice, True, (0, 0, 0))
	defender_surface = font.render(defender_dice, True, (0, 0, 0))

	if attacker_rolls[0]>defender_rolls[0]:#if the attacker rolls more than the defender
		territoryb.troopval -=1 #attacker wins, so defender loses a troop
		territoryb.update_troop_text()
	elif attacker_rolls[0] == defender_rolls[0]: #if they are equal, only the attacker loses a troop
		territorya.troopval -= 1
		territorya.update_troop_text()
	else:
		territorya.troopval -= 1 #if the defender is higher, attacker loses a troop
		territorya.update_troop_text()

	if attacker_dice_count >= 2 and defender_dice_count == 2:
		if attacker_rolls[1]>defender_rolls[1]:#if the attacker's 2nd highest is greater than defender's 2nd highest
			territoryb.troopval -=1 #attacker wins, so defender loses a troop
			territoryb.update_troop_text()
		elif attacker_rolls[1] == defender_rolls[1]: #if they are equal, only the attacker loses a troop
			territorya.troopval -= 1
			territorya.update_troop_text()
		else:
			territorya.troopval -= 1 #if the defender is higher, attacker loses a troop
			territorya.update_troop_text()

	if p1_turn == True:
		if territorya.troopval == 1: #if the attacker only has 1 troop left, do not let them attack
			territory_a.remove(territorya) #thus remove it from the selected
			attacker_text = font.render("Attacker is: None", True, (BLACK)) #update the display to show this
			territorya = None
			selection = False
			defender_text = font.render("Defender is: None", True, (BLACK)) #update the text on the display
			territory_b.remove(territoryb) #deselect the territory so thar it can no longer be attacked by player
			territoryb = None
			second_selection = False#so that territories can be reselected
		elif territoryb.troopval == 0:#if the defender runs out of troops
			territoryb.ChangeAllegience() #change the allegience
			territoryb.troopval += 1 #ensures that there is never 0 on that territory - will later be changed on the input mechanics
			territoryb.update_troop_text()
		#####
			p1_territories.append(territoryb) #ensures that now the player owns this
			if territoryb in enemy_territories:
				enemy_territories.remove(territoryb) #ensures that the enemy no longer owns this
				territory_b.remove(territoryb) #deselect the territory so thar it can no longer be attacked by player
				defender_text = font.render("Defender is: None", True, (BLACK)) #update the text on the display
				territory_a.remove(territorya)
				attacker_text = font.render("Attacker is: None", True, (BLACK))
				transfer = False
			else:
				neutral_territories.remove(territoryb)
				territory_b.remove(territoryb) #deselect the territory so thar it can no longer be attacked by player
				defender_text = font.render("Defender is: None", True, (BLACK)) #update the text on the display
				territory_a.remove(territorya)
				attacker_text = font.render("Attacker is: None", True, (BLACK))
				transfer = False
	elif ai_turn == True:
		if territorya.troopval == 1: #if the attacker only has 1 troop left, do not let them attack
			attacker_text = font.render("Attacker is: None", True, (BLACK)) #update the display to show this
			territorya = None
			selection = False
			defender_text = font.render("Defender is: None", True, (BLACK)) #update the text on the display
			territoryb = None
			second_selection = False#so that territories can be reselected
		elif territoryb.troopval == 0:#if the defender runs out of troops
			territoryb.ChangeAllegience() #change the allegience
			territoryb.troopval += 1 #ensures that there is never 0 on that territory - will later be changed on the input mechanics
			territoryb.update_troop_text()
			enemy_territories.append(territoryb)
			if territoryb in p1_territories:
				p1_territories.remove(territoryb)
				defender_text = font.render("Defender is: None", True, (BLACK)) #update the text on the display
				attacker_text = font.render("Attacker is: None", True, (BLACK))
				#transfer would go here - decide what to do before this though...
			else:
				neutral_territories.remove(territoryb)
				defender_text = font.render("Defender is: None", True, (BLACK)) #update the text on the display
				attacker_text = font.render("Attacker is: None", True, (BLACK))
				#transfer boolean goes here
			
def win_probability():
	global territorya, territoryb, likelihood
	#Reusing the dice mechanics for the dice roll
	if territorya.troopval == 3:
		attacker_dice_count = 2
	elif territorya.troopval == 2:
		attacker_dice_count = 1
	else:
		attacker_dice_count = territorya.troopval - 1
	
	if territoryb.troopval == 1:
		defender_dice_count = 1
	else:
		defender_dice_count = 2
	
	# Roll the dice for each side - a simulation
	attacker_rolls = sorted([random.choice(range(1, 7)) for x in range(attacker_dice_count)], reverse=True)
	defender_rolls = sorted([random.choice(range(1, 7)) for y in range(defender_dice_count)], reverse=True)
	
	attacker_troops = territorya.troopval #creates a copy - preventing erroring
	defender_troops = territoryb.troopval #copy

	# Compare the dice rolls and remove the appropriate number of troops (the simulated results)
	for i in range(min(attacker_dice_count, defender_dice_count)):
		print(attacker_rolls,defender_rolls)
		if attacker_rolls[i] > defender_rolls[i]:#if attacker's result is highest
			attacker_troops -= 1#remove from defender
		else:
			defender_troops -= 1 #otherwise -1 from attacker
	
	# Return the win probability for the attacker
	#likelihood = f"{(territorya.troopval / ((territorya.troopval) + territoryb.troopval) * 100)}%"
	#print (f"chances of attacker winning is:{likelihood}")
	likelihood = (territorya.troopval / ((territorya.troopval) + territoryb.troopval) * 100)
	return likelihood

while menu == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:#this bit ensures that the buttons themselves respond to the given input
			if GameButton.checkForInput(pygame.mouse.get_pos()):#GameButton will check if it is clicked, if so, will output checkforinput value test
				Game()
			if SettingsButton.checkForInput(pygame.mouse.get_pos()):
				Settings()
			if QuitButton.checkForInput(pygame.mouse.get_pos()):
				pygame.quit()
				sys.exit()

	screen.fill(BISQUE)

	#ensures all update with highlight animation
	GameButton.update()
	GameButton.HighlightByMouseHover(pygame.mouse.get_pos())

	SettingsButton.update()
	SettingsButton.HighlightByMouseHover(pygame.mouse.get_pos())

	QuitButton.update()
	QuitButton.HighlightByMouseHover(pygame.mouse.get_pos())

	TitleButton.update()

	pygame.display.update() #updates with feedback

