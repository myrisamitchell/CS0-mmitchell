''''
Name: Myrisa Mitchell
Date: 2/23/2022

This program will take in the number of seconds and convert that
to HH:MM:SS

Step 1: Input number of seconds
Step 2: Convert seconds to minutes and hours
Step 2a: Convert seconds to hours
Step 2b: Convert remaining seconds to minutes
Step 3: Print out HH:MM:SS from inputted seconds
'''

#step 2a
def convert_seconds_to_hours(seconds):
    hours = seconds // 3600
    return hours

#step2b
def convert_seconds_to_minutes(seconds):
    minutes = seconds // 60 
    return minutes

def main():
    #Step 1
    seconds = int(input("Please enter the number of seconds: "))
    #Step 2
    hours = convert_seconds_to_hours(seconds)
    minutes = convert_seconds_to_minutes(seconds - (hours * 3600))

    print(f"The time format of {seconds} seconds is {hours}:{minutes}:{seconds%60}.")
    pass

main()