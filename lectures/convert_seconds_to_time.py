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

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    rem_seconds = seconds - (hours * 3600)
    minutes = rem_seconds // 60 
    rem_seconds = seconds%60
    return hours, minutes, rem_seconds

def tests():
    assert convert_seconds_to_time(3661) == (1, 1, 1)
    assert convert_seconds_to_time(5280) == (1, 28, 0)
    print("All test cases passed.")

def main():
    tests()
    #Step 1
    seconds = int(input("Please enter the number of seconds: "))
    #Step 2
    #hours = convert_seconds_to_hours(seconds)
    #minutes = convert_seconds_to_minutes(seconds - (hours * 3600))
    hours, minutes, rem_seconds = convert_seconds_to_time(seconds)

    print(f"The time format of {seconds} seconds is {hours}:{minutes}:{rem_seconds}.")
    pass

main()