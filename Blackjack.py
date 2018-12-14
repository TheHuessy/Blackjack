import random

##### Initial Load In #####
deck_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
wins = 0
loss = 0
play = 0
pl_money = 100
deal_money = 2000
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

while play == 0:
    game = 1
    print("Starting Game")
#show the random odds to the player

    while game == 1:
        odds_nu = random.randint(1,100)
        odds_de = random.randint(1,100)
        while odds_de > odds_nu:
            odds_de = random.randint(1,100)
        odds = str(odds_nu) + ":" + str(odds_de)
        print("Odds: " + odds)
        pl_bet = input('Place your bet:')
        pl_bet = int(float(pl_bet))    
        while pl_bet > pl_money:
            print("You don't have that much. You have to bet less than " + str(pl_money))
            pl_bet = input('Place your bet:')
            pl_bet = int(float(pl_bet))
        pl_money = pl_money-pl_bet


##### Player's Hand Deal #####


        hand = [deck_list[random.randint(0, 12)], deck_list[random.randint(0, 12)]]

        h_val = 0

        for i in range(len(hand)):
            d = hand[i]
            if d == '2':
                h_val = h_val+2
            if d == '3':
                h_val = h_val+3
            if d == '4':
                h_val = h_val+4
            if d == '5':
                h_val = h_val+5
            if d == '6':
                h_val = h_val+6
            if d == '7':
                h_val = h_val+7
            if d == '8':
                h_val = h_val+8
            if d == '9':
                h_val = h_val+9
            if d == '10':
                h_val = h_val+10
            if d == 'J':
                h_val = h_val+10
            if d == 'Q':
                h_val = h_val+10
            if d == 'K':
                h_val = h_val+10
            if d == 'A':
                h_val = h_val+11    

##### Dealer's Hand Deal #####
        
        deal_hand = [deck_list[random.randint(0, 12)], deck_list[random.randint(0, 12)]]
        deal_val = 0

        for i in range(len(deal_hand)):
            d_d = deal_hand[i]
            if d_d == '2':
                deal_val = deal_val+2
            if d_d == '3':
                deal_val = deal_val+3
            if d_d == '4':
                deal_val = deal_val+4
            if d_d == '5':
                deal_val = deal_val+5
            if d_d == '6':
                deal_val = deal_val+6
            if d_d == '7':
                deal_val = deal_val+7
            if d_d == '8':
                deal_val = deal_val+8
            if d_d == '9':
                deal_val = deal_val+9
            if d_d == '10':
                deal_val = deal_val+10
            if d_d == 'J':
                deal_val = deal_val+10
            if d_d == 'Q':
                deal_val = deal_val+10
            if d_d == 'K':
                deal_val = deal_val+10
            if d_d == 'A':
                deal_val = deal_val+11 
        
##### First Round Results #####

        print("You: " + str(hand) + " Total: " + str(h_val))
        print("Dealer: " + deal_hand[1])
        if h_val == 21:
                print('Blackjack!')
                pl_money = pl_money + int((pl_bet/odds_de)*odds_nu)
                wins = wins+1
                game = 0
                hit = 'N'

##### Hitting #####


        hit = input("Hit?....(y/n)")
        while hit.upper() == 'Y':
        #### Player ####
            d = deck_list[random.randint(0, 12)]
            hand.append(d)    
            if d == '2':
                h_val = h_val+2
            if d == '3':
                h_val = h_val+3
            if d == '4':
                h_val = h_val+4
            if d == '5':
                h_val = h_val+5
            if d == '6':
                h_val = h_val+6
            if d == '7':
                h_val = h_val+7
            if d == '8':
                h_val = h_val+8
            if d == '9':
                h_val = h_val+9
            if d == '10':
                h_val = h_val+10
            if d == 'J':
                h_val = h_val+10
            if d == 'Q':
                h_val = h_val+10
            if d == 'K':
                h_val = h_val+10
            if d == 'A':
                if 'A' in hand:
                    t_val = 0
                    for i, j in enumerate(hand):
                        if j == 'A':
                            A_loc = i
                    w_hand = hand[:A_loc]+hand[A_loc:]
                    for i in w_hand:
                        if i == '2':
                            t_val = t_val + 2
                        if i == '3':
                            t_val = t_val + 3
                        if i == '4':
                            t_val = t_val + 4
                        if i == '5':
                            t_val = t_val + 5
                        if i == '6':
                            t_val = t_val + 6
                        if i == '7':
                            t_val = t_val + 7
                        if i == '8':
                            t_val = t_val + 8
                        if i == '9':
                            t_val = t_val + 9
                        if i == '10':
                            t_val = t_val + 10
                        if i == 'J':
                            t_val = t_val + 10
                        if i == 'Q':
                            t_val = t_val + 10
                        if i == 'K':
                            t_val = t_val + 10
                    if t_val <= 10:
                        t_val = t_val + 11
                    else:
                        t_val = t_val + 1
                    h_val = t_val
    

                else:
                    if h_val < 10:
                        h_val = h_val+11
                    else:
                        h_val = h_val+1
            print("You: " + str(hand) + " Total: " + str(h_val))
            print("Dealer: " + deal_hand[1])
            if h_val == 21:
                print('Blackjack!')
                pl_money = pl_money + int((pl_bet/odds_de)*odds_nu)
                wins = wins+1
                game = 0
                hit = 'N'
                
            if h_val > 21:
                print("Bust!")                
                loss = loss+1
                game = 0
                hit = 'N'
            
            if h_val < 21:  
                hit = input("Hit again?....(y/n)")
    
    #### Dealer Hitting ####
        if game != 0:
            while deal_val <= 21:
                if h_val > deal_val:
                    while deal_val < 17:
                        print("Dealer hits")
                        d_d = deck_list[random.randint(0, 12)]
                        deal_hand.append(d_d)
                        if d_d == '2':
                            deal_val = deal_val+2
                        if d_d == '3':
                            deal_val = deal_val+3
                        if d_d == '4':
                            deal_val = deal_val+4
                        if d_d == '5':
                            deal_val = deal_val+5
                        if d_d == '6':
                            deal_val = deal_val+6
                        if d_d == '7':
                            deal_val = deal_val+7
                        if d_d == '8':
                            deal_val = deal_val+8
                        if d_d == '9':
                            deal_val = deal_val+9
                        if d_d == '10':
                            deal_val = deal_val+10
                        if d_d == 'J':
                            deal_val = deal_val+10
                        if d_d == 'Q':
                            deal_val = deal_val+10
                        if d_d == 'K':
                            deal_val = deal_val+10
                        if d_d == 'A':
                            if 'A' in deal_hand:
                                td_val = 0
                                for i, j in enumerate(deal_hand):
                                    if j == 'A':
                                        AD_loc = i
                                wd_hand = deal_hand[:AD_loc]+deal_hand[AD_loc:]
                                for i in wd_hand:
                                    if i == '2':
                                        td_val = td_val + 2
                                    if i == '3':
                                        td_val = td_val + 3
                                    if i == '4':
                                        td_val = td_val + 4
                                    if i == '5':
                                        td_val = td_val + 5
                                    if i == '6':
                                        td_val = td_val + 6
                                    if i == '7':
                                        td_val = td_val + 7
                                    if i == '8':
                                        td_val = td_val + 8
                                    if i == '9':
                                        td_val = td_val + 9
                                    if i == '10':
                                        td_val = td_val + 10
                                    if i == 'J':
                                        td_val = td_val + 10
                                    if i == 'Q':
                                        td_val = td_val + 10
                                    if i == 'K':
                                        td_val = td_val + 10
                                if td_val <= 10:
                                    td_val = td_val + 11
                                else:
                                    td_val = td_val + 1
                                deal_val = td_val
    

                            else:
                                if deal_val <= 10:
                                    deal_val = deal_val+11
                                else:
                                    deal_val = deal_val+1
            
                else:
                    print("Dealer Stays")
                    break
            if deal_val > 21:
                print("Dealer Busts!")
                
                wins = wins+1
                game = 0

##### Descision ####
            print("You: " + str(hand) + " Total: " + str(h_val))
            print("Dealer: " + str(deal_hand) + " Total: " + str(deal_val))

            if h_val > deal_val or deal_val > 21:
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
            print("Thanks for the money!")
            play = 1
    
    



