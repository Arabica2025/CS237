# Input
# The input consists of two parameters:
# - n: an integer representing the total number of distinct cards;
# - game: a list of pairs following the format $(integer, string)$ with at least $n$ pairs. The integer number in each pair represents the card value in the range from 1 to $n$. The string represents whether the card is discarded, \texttt{"discard"}, or returned to the deck, \texttt{"keep"}, after each draw.
# Output
# Your output must be a list of strings. Each string can be one of the possible values:
# - "higher": if the next card is more likely to have a higher value.
# - "lower": if the next card is more likely to have a lower value.
# - "impossible": when the previous cases don't apply.
# n = 3
# game  = [(1,"keep"),(2,"discard"),(3,"keep"),(3,"discard"),(1,"keep"),(1,"discard")]
# OUTPUT:
# ["higher", "impossible", "impossible", "lower", "impossible", "impossible"]

def answer(n, game):
    # write your code solution here
    
    cardList = [i for i in range(1,n+1)] # [1,2, .... n] deck
    output = [] # initialize output list
    
    # conditional prob P(A|B) = P(A and B) / P(B)
    # P(A) = probability of the next card being higher or lower
    # P(B) = probability of drawing the current card from the deck
    # P(A and B) = probability that the next card is higher or lower given the current card

    for i in range(len(game)):
        
        card_values, todo = game[i] # key: integer card values # value: string value that tells us what dealer does (discard, keep)
        num_cards = len(cardList) # number of cards in the deck

        print(i, "th iteration. card list:", cardList, "card values drawn:", card_values, "todo:", todo)

        if todo == "keep": # 1st case: keeping the card in the deck
            if num_cards == 0: # if there are no cards left in the deck, it's impossible to draw a card
                output.append("impossible")
                continue # escape the check for todo and go to the next iteration
            
            # Pr(B) stays the same; does not matter whether keep or discard
            Prob_b = 1/num_cards 
            print("Prob_b:", Prob_b)
            
            # we have to check if probability of the next value is higher or lower than the drawn value
            higher_count = sum(1 for eachCard in cardList if eachCard > card_values) # count the number of values in the deck that have higher values than the one that I drew in current iteration
            high_Prob_a = higher_count/num_cards # prob of being higher
            print("high Prob_a:", high_Prob_a)

            # count the number of values in the deck that have lower values than the one that I drew in current iteration
            lower_count = sum(1 for eachCard in cardList if eachCard < card_values)
            low_Prob_a = lower_count/num_cards # prob of being lower
            print("low Prob_a:", low_Prob_a)

            # calcualte the conditional probability
            # prob of drawing higher values given the value drawn 
            high_conditional_prob = (high_Prob_a * Prob_b) / Prob_b
            print("high conditional_prob:", high_conditional_prob)
            
            # prob of drawing lower values given the value drawn
            low_conditional_prob = (low_Prob_a * Prob_b) / Prob_b
            print("low conditional_prob:", low_conditional_prob)
            print()

            if high_conditional_prob > 0.5: # if prob of being higher > 0.5
                output.append("higher")
            elif low_conditional_prob > 0.5: # if prob of being lower > 0.5
                output.append("lower")
            else:
                output.append("impossible")
                
        elif todo == "discard": # 2nd case: discard the drawn value from the deck
            # remove the value out of the value first to calculate probabilities with minimal change in codes
            print("card_list before discard:", cardList)
            cardList.remove(card_values)
            print("card_list after discard:", cardList)
            
            # update the number of values in the deck after the discard
            num_cards = len(cardList)
            
            
            if num_cards < 1: # if there are no cards left in the deck, it's impossible to draw a card
                output.append("impossible")
                continue

            # Pr(B) stays the same; does not matter whether keep or discard
            Prob_b = 1/num_cards
            print("Prob_b:", Prob_b)
            
            
            # same process with case 1(keep the value in the deck)
            higher_count = sum(1 for eachCard in cardList if eachCard > card_values)
            high_Prob_a = higher_count/num_cards
            print("higher Prob_a:", high_Prob_a)
            high_conditional_prob = (high_Prob_a * Prob_b) / Prob_b
            print("higher conditional_prob:", high_conditional_prob)

            low_count = sum(1 for eachCard in cardList if eachCard < card_values)
            low_Prob_a = low_count/num_cards
            print("lower Prob A:", low_Prob_a)
            
            low_conditional_prob = (low_Prob_a * Prob_b) / Prob_b
            print("low conditional prob:",low_conditional_prob)
            if high_conditional_prob > 0.5:
                output.append("higher")
            elif low_conditional_prob > 0.5:
                output.append("lower")
            else:
                output.append("impossible")

            print()

    return output

n = 3
game = [(1,"keep"),(2,"discard"),(3,"keep"),(3,"discard"),(1,"keep"),(1,"discard")]

print("1st test of answer(n, game)",answer(n, game))

print()
n1 = 10
game1 = [(1, "keep"), (2, "discard"), (9, "keep"), (8, "discard"), (9, "discard"), (7, "keep"),(7,"discard"), (10, "discard")]
print("2nd test of answer(n1, game1)", answer(n1, game1))
# cardList = [i for i in range(1,3)]
# print(cardList)

