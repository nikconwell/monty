#
# Experiment with the Monty Hall problem.
# Nik Conwell
#

from colorama import Fore, Style


# 3 doors, Empty, Empty ,Winner
# Parallel universes, a stay universe, a switch1 universe, and a switch2 universe (switch depending on which way they switch)

stages = [ [' ',' ','W'],
           [' ','W',' '],
           ['W',' ',' ']]

# Number of games and counts of winners
games = 0                 # Number of games attempted.  Same in all universes.

stay_validgame = True            # Set to false if stupid Monty messed up.
stay_validgames = 0       # Number that are valid after Monty opened a door.
switch1_validgame = True
switch1_validgames = 0
switch2_validgame = True
switch2_validgames = 0

stay_won = False
switch1_won = False
switch2_won = False
stay_wins = 0
switch1_wins = 0
switch2_wins = 0

def showplayers():
    player = "X"
    monty = "O"
    
    # Print out the initial choice by all players.
    playerstring = "{}    {}    {}"
    if (staychoice == 0):
        staystring = playerstring.format(player,'','')
    elif (staychoice == 1):
        staystring = playerstring.format('',player,'')
    elif (staychoice == 2):
        staystring = playerstring.format('','',player)
    if (stay_won == True):
        staystring = Fore.GREEN + staystring + Fore.RESET


    if (switch_firstchoice == 0):
        switchstring = playerstring.format(player,'','')
    elif (switch_firstchoice == 1):
        switchstring = playerstring.format('',player,'')
    elif (switch_firstchoice == 2):
        switchstring = playerstring.format('','',player)

    playertemplate = " {}                                          {}                                          {}"
    print (playertemplate.format(staystring,switchstring,switchstring))

    # Print out monty choice.
    if (montychoice == 0):
        staystring = playerstring.format(monty,'','')
        switch1string = playerstring.format(monty,'','')
        switch2string = playerstring.format(monty,'','')
    elif (montychoice == 1):
        staystring = playerstring.format('',monty,'')
        switch1string = playerstring.format('',monty,'')
        switch2string = playerstring.format('',monty,'')
    elif (montychoice == 2):
        staystring = playerstring.format('','',monty)
        switch1string = playerstring.format('','',monty)
        switch2string = playerstring.format('','',monty)
    if (stay_validgame == False):
        staystring = Fore.RED + staystring + Fore.RESET
    if (switch1_validgame == False):
        switch1string = Fore.RED + switch1string + Fore.RESET
    if (switch2_validgame == False):
        switch2string = Fore.RED + switch2string + Fore.RESET
    print (playertemplate.format(staystring,switch1string,switch2string))

    # Print out second choice for the switchers.
    if (switch1_secondchoice == 0):
        switch1string = playerstring.format(player,'','')
    elif (switch1_secondchoice == 1):
        switch1string = playerstring.format('',player,'')
    elif (switch1_secondchoice == 2):
        switch1string = playerstring.format('','',player)
    if (switch2_secondchoice == 0):
        switch2string = playerstring.format(player,'','')
    elif (switch2_secondchoice == 1):
        switch2string = playerstring.format('',player,'')
    elif (switch2_secondchoice == 2):
        switch2string = playerstring.format('','',player)
    if (switch1_validgame == False):
        switch1string = Fore.RED + switch1string + Fore.RESET
    if (switch1_won == True):
        switch1string = Fore.GREEN + switch1string + Fore.RESET
    if (switch2_validgame == False):
        switch2string = Fore.RED + switch2string + Fore.RESET
    if (switch2_won == True):
        switch2string = Fore.GREEN + switch2string + Fore.RESET
    
    print (playertemplate.format('         ',switch1string,switch2string))


#
# Count up the winners.
#
def tally_winners():
    global games,stay_wins,switch1_wins,switch2_wins,stay_validgame,switch1_validgame,switch2_validgame
    global stay_validgames,switch1_validgames,switch2_validgames,stay_won,switch1_won,switch2_won

    games += 1

    # If same door choice between Monty and the stay person or Monty and the switching choices, it is not a valid game.
    if (montychoice == staychoice):
        stay_validgame = False
    if ((montychoice == switch_firstchoice) or (montychoice == switch1_secondchoice)):
        switch1_validgame = False
    if ((montychoice == switch_firstchoice) or (montychoice == switch2_secondchoice)):
        switch2_validgame = False

    # Figure out the winner of the games
    if (stay_validgame == True):
        stay_validgames += 1
        if (stage[staychoice] == 'W'):
            stay_wins += 1
            stay_won = True

    if (switch1_validgame == True):
        switch1_validgames += 1
        if (stage[switch1_secondchoice] == 'W'):
            switch1_wins += 1
            switch1_won = True
    if (switch2_validgame == True):
        switch2_validgames += 1
        if (stage[switch2_secondchoice] == 'W'):
            switch2_wins += 1
            switch2_won = True

    # Show doors of the three universes and current count of games
    stagestring = "[{}] [{}] [{}] (game: {:3d} wins: {:3d} validgame: {:3d})"
    print()
    print(stagestring.format(stage[0],stage[1],stage[2],games,stay_wins,stay_validgames),end='')
    print("   ",end='')
    print(stagestring.format(stage[0],stage[1],stage[2],games,switch1_wins,switch1_validgames),end='')
    print("   ",end='')
    print(stagestring.format(stage[0],stage[1],stage[2],games,switch2_wins,switch2_validgames))

    showplayers()


    stay_validgame = True             # Reset for the next iteration
    switch1_validgame = True
    switch2_validgame = True
    stay_won = False
    switch1_won = False
    switch2_won = False

    
    
#
# Run the game, run through all possible choices.  In some universes the game will be invalid (monty opens door we picked, etc.)
#
print ("\n             STAY                                            SWITCH1                                            SWITCH2")

for stage in stages:
    for staychoice in range(3):

        for switch_firstchoice in range(3):

            for montychoice in range(3):
            
                # Go through all the switching choices of the switcher.
                if (switch_firstchoice == 0):
                    switch1_secondchoice = 1
                    switch2_secondchoice = 2
                    tally_winners()
                elif (switch_firstchoice == 1):
                    switch1_secondchoice = 0
                    switch2_secondchoice = 2
                    tally_winners()
                elif (switch_firstchoice == 2):
                    switch1_secondchoice = 0
                    switch2_secondchoice = 1
                    tally_winners()
            
    
print()

print("attempted games = {}".format(games))
validgames_format = "valid games = {}                                   valid games = {}                                   valid games = {}"
print(validgames_format.format(stay_validgames,switch1_validgames,switch2_validgames))
wins_format = "staywins = {} ({:.0f}% all, {:.0f}% valid)                 switchwins = {} ({:.0f}% all, {:.0f}% valid)                switchwins = {} ({:.0f}% all, {:.0f}% valid)"
if (switch1_validgames > 0):
    switch1_wins_percent_valid = (switch1_wins/switch1_validgames)*100
else:
    switch1_wins_percent_valid = 0
if (switch2_validgames > 0):
    switch2_wins_percent_valid = (switch2_wins/switch2_validgames)*100
else:
    switch2_wins_percent_valid = 0
print(wins_format.format(stay_wins,(stay_wins/games)*100,(stay_wins/stay_validgames)*100,
                        switch1_wins,(switch1_wins/games)*100,switch1_wins_percent_valid,
                        switch2_wins,(switch2_wins/games)*100,switch2_wins_percent_valid))
                         
