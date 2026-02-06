#import random
def answer(r,b):
    #print("Don't change the function name")
    """
    answer(r: int[],b: int[]) -> str:
    Parameters:
        r: an array of n digits r_1,..., r_n red digits on cards 1,..., n, respectively
        b: an array of n digits b_1,..., b_n blue digits on cards 1,..., n, respectively
        
    Return value:
        "RED" if RED has a strictly higher chance to win
        "BLUE" if BLUE has a strictly higher chance to win
        "EQUAL" if both players are equally likely to win
        
    
    n cards numbers 1,...,n. the card i has a red digit r_i and a blue digit b_i.
    arrange all n cards in random order from left to right, with permutations of 1,...n. have same probability
    
    
    after shuffle,
    read all red digits left to right and obtain an int R
    read all blue digits left to right and obtain an in B
    
    leading zeros can be ignored
    if all digits in a number are zeros: return 0
    
    Red bets after shuffle: R > B
    Blue bets after shuffle: B > R
    
    if Red has strictly higher chance to win: return "RED"
    if Blue has strictly higher change to win: return "BLUE"
    if both are equally likely to win: return "EQUAL"
    """
    ## in the given array, the one who gets higher number on the leftmost index probably wins..?
    ## but since we shuffle the deck, we don't know what int will be on which digit
    ## so the more we have greater number of digits on the left side has higher chance of winning?
    
    r_winning = 0
    b_winning = 0
    
    # we don't need to shuffle? the hw2.pdf example looks like we do not actually shuffle inside the function so i'll just remove this
    # random.shuffle(r)
    # random.shuffle(b)
    
    # I thought I have to use the R and B value as exactly shown in hw2.pdf
    # I guess it is unnecessary task and i guess it just simply make things difficult?
    # reduces efficiency... 
    # R_str = ""
    # B_str = ""
    
    ## remove leading zeros of red
    r_non_leading_zero_index = 0
    b_non_leading_zero_index = 0

    for i in range(len(r)):
        if r[i] == 0:
            r_non_leading_zero_index += 1
        else:
            break
        
    # for i in range(r_non_leading_zero_index, len(r)):
    #     R_str += str(r[i])

    ## remove leading zeros of blue
    for j in range(len(b)):
        if b[j] == 0:
            b_non_leading_zero_index += 1
        else:
            break
    
    # reassign the array after removing leading zeros    
    r = r[r_non_leading_zero_index:]
    b = b[b_non_leading_zero_index:]
    print(r)
    print(b)
    
    # if any array that has less number of digits compared to the other, then 
    # the one that has more digits always wins
    if len(r) > len(b):
        return "RED"
    elif len(r) < len(b):
        return "BLUE"
    else:
        # since len(r) == len(b), it does not matter if i use red array or blue array?
        for i, j in zip(r, b):
            if i > j:
                r_winning+=1
            elif i < j:
                b_winning+=1
            else:
                continue
            

    
    if r_winning > b_winning:
        return "RED"
    elif r_winning < b_winning:
        return "BLUE"
    else:
        return "EQUAL"
            

    # for j in range(b_non_leading_zero_index, len(b)):
    #     B_str += str(b[j])
        
    # R = int(R_str)
    # B = int(B_str)
    
    
    # if R > B:
    #     return "RED"
    # elif R < B:
    #     return "BLUE"
    # else:
    #     return "EQUAL"
    
# r1 = [7,7,7]
# b1 = [1,1,1]
# print(answer(r1,b1))

# r2 = [3,1,4]
# b2 = [1,5,9]
# print(answer(r2,b2))

# r3 = [0,9,2,8,1]
# b3 = [0,9,2,8,1]
# print(answer(r3,b3))

# r = [0,0,2,8,1]
# b = [4,3,2,1,0]
# print(answer(r,b))

    # return("RED")
    # return("BLUE")
    # return("EQUAL")