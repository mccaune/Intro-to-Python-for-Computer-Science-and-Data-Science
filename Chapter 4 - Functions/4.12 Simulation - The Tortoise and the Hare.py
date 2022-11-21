"""
4.12 (Simulation: The Tortoise and the Hare) In this problem, you’ll re-create the clas-
sic race of the tortoise and the hare. You’ll use random-number generation to develop a
simulation of this memorable event.

Our contenders begin the race at square 1 of 70 squares. Each square represents a
position along the race course. The finish line is at square 70. The first contender to reach
or pass square 70 is rewarded with a pail of fresh carrots and lettuce. The course weaves its
way up the side of a slippery mountain, so occasionally the contenders lose ground.

A clock ticks once per second. With each tick of the clock, your application should
adjust the position of the animals according to the rules in the table below. Use variables
to keep track of the positions of the animals (i.e., position numbers are 1–70). Start each
animal at position 1 (the “starting gate”). If an animal slips left before square 1, move it
back to square 1.

Create two functions that generate the percentages in the table for the tortoise and
the hare, respectively, by producing a random integer i in the range 1 ≤ i ≤ 10. In the
function for the tortoise, perform a “fast plod” when 1 ≤ i ≤ 5, a “slip” when 6 ≤ i ≤ 7 or
a “slow plod” when 8 ≤ i ≤ 10. Use a similar technique in the function for the hare.
Begin the race by displaying

BANG !!!!!
AND THEY'RE OFF !!!!!

Then, for each tick of the clock (i.e., each iteration of a loop), display a 70-position line
showing the letter "T" in the position of the tortoise and the letter "H" in the position of
the hare. Occasionally, the contenders will land on the same square. In this case, the tor-
toise bites the hare, and your application should display "OUCH!!!" at that position. All
positions other than the "T", the "H" or the "OUCH!!!" (in case of a tie) should be blank.

After each line is displayed, test for whether either animal has reached or passed
square 70. If so, display the winner and terminate the simulation. If the tortoise wins, dis-
play TORTOISE WINS!!! YAY!!! If the hare wins, display Hare wins. Yuch. If both ani-
mals win on the same tick of the clock, you may want to favor the tortoise (the
“underdog”), or you may want to display "It's a tie". If neither animal wins, perform
the loop again to simulate the next tick of the clock. When you’re ready to run your
application, assemble a group of fans to watch the race. You’ll be amazed at how involved
your audience gets!
"""

#4.12
import random

def tortoise():
    i = random.randrange(1,11)
    if i >= 1 and i <= 5:
        t_move = 3
    elif i >= 6 and i <= 7:
        t_move = -6
    else:
        t_move = 1
    return t_move

def hare():
    i = random.randrange(1,11)
    if i >= 1 and i <= 2:
        h_move = 0
    elif i >= 3 and i <= 4:
        h_move = 9
    elif i == 5:
        h_move = -12
    elif i >= 6 and i <= 8:
        h_move = 1
    else:
        h_move = -2
    return h_move

def display_race(t, h):
    print(f'tortoise: {t}\thare: {h}')

road_tortoise = 0
road_hare = 0
game_status = 'CONTINUE'

while game_status == 'CONTINUE':
    road_tortoise += tortoise()
    road_hare += hare()
    display_race(road_tortoise, road_hare)
    if road_hare >= 70 and road_tortoise >= 70:
        game_status = 'TIE'
    elif road_tortoise >= 70:
        game_status = 'T_WON'
    elif road_hare >= 70:
        game_status = 'H_WON'
    

if game_status == 'T_WON':
    print('Tortoise Won!!!')
elif game_status == 'H_WON':
    print('Hare Won!!!')
elif game_status == 'TIE':
    print('It`s a Tie!!!')

