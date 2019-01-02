import random
import datetime
import numpy as np

#### THERE IS A LOOP PROBLEM SOMEWHERE IN HERE~!
#### CHECK AROUND WHERE THE HANDS ARE DEALT/HIT
#### ALSO LOOK AT ANY REFERENCE TO H_VAL BEING 12 (IT'S ALMOST ALWAYS 12)
#### 

##### Initial Load In #####
deck_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
wins = 0
loss = 0
play = 0
pl_money = 100
pl_bet = 0
g_win = 1



#Add gambling section:
#Need running total of the pot and who contributed what
#Need to randomly generate odds for the player
#maybe build in card counting logic for the dealer to bet against you
##Will need to change for mat to show the player's hand and just one card from the dealer
##something like if c_count is above 1, then random number generator (1,(low number)), if less than 1 rng(1,(high number))
##for increasing bets. Making it so that they have a higher chance of up-betting if the card count is positive
###This won't be perfect logic by any means because there isn't a finite number of decks being used. Going to have
###it reset each game so we assume that there was only ever one deck. This will make sense in the RPG
ti = datetime.datetime.now()
while play == 0:
    game = 1
    hit = 'Y'
    print("Starting Game")
    print("Money: " + str(pl_money))

    #show the random odds to the player
    
    while game == 1:
        odds_nu = random.randint(1,100)
        odds_de = random.randint(1,100)
        while odds_de > odds_nu:
            odds_de = random.randint(1,100)
        odds = str(odds_nu) + ":" + str(odds_de)        
        print("Odds: " + odds)
        pl_bet = input('Place your bet: ')
        pl_bet = int(float(pl_bet))    
        while pl_bet > pl_money:
            print("You don't have that much. You have to bet less than " + str(pl_money))
            pl_bet = input('Place your bet: ')
            pl_bet = int(float(pl_bet))
        pl_money = pl_money-pl_bet
        ##### Player's Hand Deal #####
        hand = np.array([deck_list[random.randint(0, 12)], deck_list[random.randint(0, 12)]])
        h_val = 0
        for i in hand:
            if i not in ['A', 'K', 'Q', 'J']:
                h_val = h_val + int(i)
        for i in hand:
            if i in ['K', 'Q', 'J']:
                h_val = h_val + 10
        for i in hand:
            if i == 'A':
                if h_val <= 10:
                    h_val = h_val + 11
                else:
                    h_val = h_val + 1
        ##### Dealer's Hand Deal #####        
        deal_hand = np.array([deck_list[random.randint(0, 12)], deck_list[random.randint(0, 12)]])
        deal_val = 0
        for i in deal_hand:
            if i not in ['A', 'K', 'Q', 'J']:
                deal_val = deal_val + int(i)
        for i in deal_hand:
            if i in ['K', 'Q', 'J']:
                deal_val = deal_val + 10
        for i in deal_hand:
            if i == 'A':
                if deal_val <= 10:
                    deal_val = deal_val + 11
                else:
                    deal_val = deal_val + 1
        ##### First Round Results #####
        print("You: " + str(hand) + " Total: " + str(h_val))
        print("Dealer: " + deal_hand[0])
        #print("Dealer: " + str(deal_hand)
        if h_val == 21:
                print('Blackjack!')
                pl_money = pl_money + int((pl_bet/odds_de)*odds_nu)
                wins = wins+1
                game = 0
                hit = 'N'
        ##### Hitting #####
        hit = input("Hit?....(y/n)")
        if hit.upper() == 'Y':
            while hit.upper() == 'Y':
                #### Player ####
                #while hit.upper() == 'Y':
                d = deck_list[random.randint(0, 12)]
                hand = np.append(hand,d)    
                h_val = 0
                for i in hand:
                    if i not in ['A', 'K', 'Q', 'J']:
                        h_val = h_val + int(i)
                for i in hand:
                    if i in ['K', 'Q', 'J']:
                        h_val = h_val + 10
                for i in hand:
                    if i == 'A':
                        if h_val <= 10:
                            h_val = h_val + 11
                        else:
                            h_val = h_val + 1
                print("You: " + str(hand) + " Total: " + str(h_val))
                print("Dealer: " + deal_hand[0])
                #print("Dealer: " + str(deal_hand))
                if h_val == 21:
                    print('Blackjack!')
                    pl_money = pl_money + int((pl_bet/odds_de)*odds_nu)
                    #wins = wins+1
                    game = 0
                    hit = 'N'                
                if h_val > 21:
                    print("Bust!")                
                    #loss = loss+1
                    game = 0
                    hit = 'N'            
                if h_val < 21:  
                    hit = input("Hit again?....(y/n)")    
        else:
            if game != 0:
                while deal_val <= 21:
                    if h_val > deal_val:
                        while deal_val <= 16:
                            print("Dealer hits")
                            d_d = deck_list[random.randint(0, 12)]
                            deal_hand = np.append(deal_hand, d_d)
                            deal_val = 0
                            for i in deal_hand:
                                if i not in ['A', 'K', 'Q', 'J']:
                                    deal_val = deal_val + int(i)
                            for i in deal_hand:
                                if i in ['K', 'Q', 'J']:
                                    deal_val = deal_val + 10
                            for i in deal_hand:
                                if i == 'A':
                                    if deal_val <= 10:
                                        deal_val = deal_val + 11
                                    else:
                                        deal_val = deal_val + 1
                    else:
                        print("Dealer Stays")
                        game = 0
                        break
                        #break ########THIS IS THE PROBLEM, IT IS BREAKING THE WHOLE SET OF LOOPS!
                if deal_val > 21:
                    print("Dealer Busts!")                
                    #wins = wins+1
                    game = 0
        
        #### Dealer Hitting ####
        if game != 0:
            while deal_val <= 21:
                if h_val > deal_val:
                    while deal_val <= 16:
                        print("Dealer hits")
                        d_d = deck_list[random.randint(0, 12)]
                        deal_hand = np.append(deal_hand, d_d)
                        deal_val = 0
                        for i in deal_hand:
                            if i not in ['A', 'K', 'Q', 'J']:
                                deal_val = deal_val + int(i)
                        for i in deal_hand:
                            if i in ['K', 'Q', 'J']:
                                deal_val = deal_val + 10
                        for i in deal_hand:
                            if i == 'A':
                                if deal_val <= 10:
                                    deal_val = deal_val + 11
                                else:
                                    deal_val = deal_val + 1
                else:
                    print("Dealer Stays")
                    game = 0
                    break
                    #break ########THIS IS THE PROBLEM, IT IS BREAKING THE WHOLE SET OF LOOPS!
            if deal_val > 21:
                print("Dealer Busts!")                
                #wins = wins+1
                game = 0
    ##### Descision ####
    print("You: " + str(hand) + " Total: " + str(h_val))
    print("Dealer: " + str(deal_hand) + " Total: " + str(deal_val))
    if h_val > deal_val and h_val < 21 or deal_val > 21:
        print("You win!")
        pl_money = pl_money + int((pl_bet/odds_de)*odds_nu)
        wins = wins+1
    else:                
        print("Dealer wins!")                
        loss = loss+1

    print('-----------------------')
    print("Money: " + str(pl_money))
    print("Total wins: " + str(wins))
    print("Total losses: " + str(loss))
    print('-----------------------')
        
    kp = input("Keep playing?...(y/n)")
        
    if kp.upper() == 'N':
        to = datetime.datetime.now()
        tmm = to-ti
        td = to-ti
        tss = td.seconds
        fmon = pl_money - 100
        tsst = tss/60
        sect = (tsst % 1)*60
        mint = int(tsst)
        if tss/60 > 1 & fmon > 0:
            print("It took you " + str(mint) +  " minutes and " + str(int(sect)) + " seconds to win " + str(abs(int(fmon))) + " money!")
        if tss/60 > 1 & fmon < 0:
            print("It took you " + str(mint) +  " minutes and " + str(int(sect)) + " seconds to lose " + str(abs(int(fmon))) + " money!")
        if tss/60 < 1 & fmon > 0:
            print("It took you " + str(int(sect)) + " seconds to win " + str(abs(int(fmon))) + " money!")
        if tss/60 < 1 & fmon < 0:
            print("It took you " + str(int(sect)) + " seconds to lose " + str(abs(int(fmon))) + " money!")            
        print("Thanks for the money!")
        play = 1
