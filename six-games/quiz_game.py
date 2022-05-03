print('Welcome to my computer Quiz!')

playing = input ("Do you want to play? ")

if playing.lower() != "yes" :
    quit()
    
print('OK, let\'s play :)')
score = 0

awnser = input('What does CPU stand for? ')
if awnser.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect!')

awnser = input('What does GPU stand for? ')
if awnser.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    
awnser = input('What does RAM stand for? ')
if awnser.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    
awnser = input('What does PSU stand for? ')
if awnser.lower() == "power supply":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    
print("You got " + str(score) + " question correct!")
print("You got " + str((score / 4)* 100 ) + "%.")