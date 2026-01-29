from numpy.random import uniform
# input: Two natural numbers B and C — the results of Bob's and Charlie's die rolls.
def answer(B: int, C: int) -> str:
    # output: A string with the probability of Alice winning in the form of an 
    # irreducible fraction in format A/B, where A — the numerator, and B — the 
    # denominator.

    ## If she ties with either of them, they will let her win.
    ## If the required probability equals zero, output 0/1. If the required probability equals one, output 1/1.
    
    #sample_Size = 6 * 6 * 6 ## total possible outcomes when rolling dice three times (Bob -> Charlie -> Alice)
    
    count = 0
    for A in range(1,7):
        if 6 < B or 6 < C: # Because by the time Alice rolls, both Bob and Charlie already has rolled their dices.
            return "0/1" ## So if the required possibility equals 0, then there should be no chance that Alice wins even if Bob and Charlie let Alice win if she ties with either of them.
        if B == 1 and C == 1:
            return "1/1" ## if the required probability is 1, then Alice wins in all cases. meaning both B and C must be the minimum value of 1.
        elif A >= B and A >= C:
            count += 1
            
    if count == 2 or count == 4:
        return f"{count//2}/{6//2}"
    if count == 3:
        return f"{count//3}/{6//3}"
    return f"{count}/{6}"

if __name__ == "__main__":
    print(answer(1,2))