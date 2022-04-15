'''
Name: Myrisa Mitchell
Date: April 15, 2022

This program will search through rows of commands and do what simon says in strings that 
contain "Simon says"

Step 1: Take in input of strings
Step 2: Search strings for "Simon says"
Step 3: Print out end of strings that contain "Simon says"
Step 4: Write test function that contains three test cases
'''

#Step 4
def tests():
    commands1 = ["Simon says raise your hand.", "Sit down.", "Simon says lift your left foot."]
    assert search_string(commands1) == ["raise your hand.", "lift your left foot."]
    commands2 = ["Touch your nose.", "Simon says blink twice.", "Simon says touch your elbow."]
    assert search_string(commands2) == ["blink twice.", "touch your elbow."]
    commands3 = ["Lick your lips.", "Clap three times.", "Simon says snap your fingers."]
    assert search_string(commands3) == ["snap your fingers."]

#Step 1
def build_commands():
    simonSays = []
    n = int(input())
    for i in range(0, n):
        command = input()
        simonSays.append(command)
    return simonSays

#Step 2
def search_string(commands):
    simon_says = []
    for i in (commands):
        if ("Simon says" in i):
            simon_says.append(i[11:])
    return simon_says

def main():
    tests()
    commands = build_commands()
    simonSays = search_string(commands)
    
    #Step 3
    print(*simonSays, sep = '\n')

if __name__ == "__main__":
    main()