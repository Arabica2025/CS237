import math

# an airline overbooks
# sell n tickets; has exactly m seats => n ≥ m
# independent probability that individual passenger will show up = p
# if the number of passengers showed up exceeds the number of seats m,
# kick the exceeding number of passengers 
# kicked passengers get compensation of c dollars
# return expected total compensation penalty the airline has to pay

# n = the number of tickets
# m = the number of seats
# p = independent probability that individual passenger shows up 
# c = the amount of compensation each individual kicked passenger receives

# X = random variable that indicates total compensation penalty the airline has to pay
# X_i = random variable that indicates compensation penalty the airline has to pay to kicked passenger n-m-i
# X ~ Binomial
def answer(n: int, m: int, c: int, p: float) -> float:
        # case 0: if less passenger than the seat(quite impressive!), then just return 0
        # obsolete because always n≥m
        # if n<m:
        #         return 0 
        
        # # given that this airline always overbook
        # bumped: int = n-m # the number of bumped passengers; 
        # # case 1: probability that all passenger shows up
        # if n==m:
        #         p_all_show: float = math.comb(m, n)*(p**n)*((1-p)**(m-n))
        #         expected_penalty : float = p_all_show * bumped * c
        #         return expected_penalty

        
        

        # below that range of line: don't care; it is 0 anyways so why bother computing it
        # binomial distribution probability 
        # (n choose k) * p^k * (1-p)^{n-k}
        # declare expected_penalty
        expected_penalty: float = 0.0
        for k in range(m+1, n+1):
                p_show: float = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
                bumped: int = k - m # we need to decrement the number of people to be compensated as we narrow the range
                expected_penalty += p_show * (bumped * c)

        
        
        
        return expected_penalty
print(answer(3, 2,  500,  0.5))