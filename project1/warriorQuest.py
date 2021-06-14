print("What kind of warrior are you?")

score = 0

keepGoing = True
q1Loop = True
q2Loop = True
q3Loop = True

 
while q1Loop:
    q1 = input("""
                What do you drink? (Enter the letter that represents your choice.)
                A. Monster 
                B. Rockstar 
                C. IPA
                D. JP8
                """).upper()
    if q1 == "A":
        score += 2
        q1Loop = False
    elif q1 == "B":
        score += 0
        q1Loop = False
    elif q1 == "C":
        score += 1
        q1Loop = False
    elif q1 == "D":
        score += 3
        q1Loop = False
    else:
        print("Invalid input, try again!")

while q2Loop: 
    q2 = input("""
                What's your favorite MRE? (Enter the letter that represents your choice.)
                A. Beef Stew
                B. Creamy Spinach Fettuccine
                C. Pizza
                D. Copenhagen
                """).upper()
    if q2 == "A":
        score += 3
        q2Loop = False
    elif q2 == "B":
        score += 1
        q2Loop = False
    elif q2 == "C":
        score += 0
        q2Loop = False
    elif q2 == "D":
        score += 2
        q2Loop = False
    else:
        print("Invalid input, try again!")

while q3Loop:
    q3 = input("""
                Why is the sky blue? (Enter the letter that represents your choice.)
                A. God's love
                B. Science
                C. Because
                D. What?
                """).upper()
    if q3 == "A":
        score += 3
        q3Loop = False
    elif q3 == "B":
        score += 1
        q3Loop = False
    elif q3 == "C":
        score += 2
        q3Loop = False
    elif q3 == "D":
        score += 0
        q3Loop = False
    else:
        print("Invalid input, try again!")



if score == 9:
    print("Jason Bourne, thank you for your service.")
elif score == 8 or score == 7:
    print("Deplorable grunt, what's your ASVAB score?")
elif score == 6 or score == 5:
    print("Paint-ballerz, don't forget your face-shield.")
elif score == 4: 
    print("Airsoft milsim, keep trying.")
else :
    print("Keyboard warrior, keep typing.")
