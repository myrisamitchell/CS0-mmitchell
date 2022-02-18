'''
Myrisa Mitchell
Date: 02/18/22

This program will prompt for the users name, then print out
the various stages of a hangman game.

Step 1: Prompt for player's name.
Step 1a: Greet player with their name.
Step 2: Print out gallows. 
Step 3: Print hangman's head. 
Step 4: Print hangman's body.
Step 5: Print hangman's left arm.
Step 6: Print hangman's right arm.
Step 7: Print hangman's left leg.
Step 8: Print hangmans' right leg.
'''

#step 1
name1 = input("Hey there, what's your name? ")

#step 1a
print(f'Hey, {name1}!')
print("The hangman game is under construction,"
     " maybe you'll get to play it in a few weeks...")
print("This is what various stages of the hangman game will look like...")

#step 2
print("Stage 0")
print("     |__________") 						
print("     |/     |") 
print("     |") 	
print("     |")
print("     |") 	
print("     |")
print("     |") 				              
print("-------------") 	

#step 3
print("Stage 1")
print("     |__________") 						
print("     |/     |") 
print("     |     (_)") 	
print("     |")
print("     |") 	
print("     |")
print("     |") 				              
print("-------------") 	

#step 4
print("Stage 2")
print("     |__________") 						
print("     |/     |") 
print("     |     (_)") 	
print("     |      |")
print("     |      |") 	
print("     |")
print("     |") 				              
print("-------------") 	

#step 5
print("Stage 3")
print("     |__________") 						
print("     |/     |") 
print("     |     (_)") 	
print("     |     \|")
print("     |      |") 	
print("     |")
print("     |") 				              
print("-------------") 	

#step 6
print("Stage 4")
print("     |__________") 						
print("     |/     |") 
print("     |     (_)") 	
print("     |     \|/")
print("     |      |") 	
print("     |")
print("     |") 				              
print("-------------") 	

#step 7
print("Stage 5")
print("     |__________") 						
print("     |/     |") 
print("     |     (_)") 	
print("     |     \|/")
print("     |      |") 	
print("     |     /")
print("     |") 				              
print("-------------") 	

#step 8
print("Stage 6")
print("     |__________") 						
print("     |/     |") 
print("     |     (_)") 	
print("     |     \|/")
print("     |      |") 	
print("     |     / \\")
print("     |") 				              
print("-------------") 