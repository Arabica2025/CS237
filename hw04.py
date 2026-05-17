def answer(a,b,c,d):
    #Fix this function and return the correct probabilities
    """
    N and T plays dart
    
    probability of N shoots target = a/b
    probability of T shoots target = c/d
    
    probability of N doesn't shoot target = 1-a/b
    probability of T doesn't shoot target = 1-c/d

    The one who shoots in the target first should be the winner.
    
    Return
    the probability that Nathan will win the match
    """
    # need probability of N winning
    # prob of N winning = probability of N winning / total sample space (probability of N winning + prob of N lost AND prob of T winning)
    # ans = a/b
    n_winning = a/b
    t_winning = c/d
    
    total_sample_space = a/b + (1-(a/b))*c/d
    
    return n_winning / total_sample_space
    
    # # calculate total probability of N winning
    # for i in range(10):
    #     ans+= (a/b)*((1-c/d)*(1-a/b))**i
        
    # return ans

print(answer(1,2,1,2))
