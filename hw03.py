import random
import matplotlib.pyplot as plt

# --- HELPER FUNCTION FOR PLOTTING ---
def plot_distribution(x_values, pmf, cdf, title):
    """
    Plots the PMF and CDF side-by-side.
    Args:
        x_values (list): The possible outcomes (sorted).
        pmf (list): Probability of each outcome.
        cdf (list): Cumulative probability of each outcome.
        title (str): Title for the charts.
    """
    plt.figure(figsize=(12, 5))
    
    # PMF Plot (Bar Chart)
    plt.subplot(1, 2, 1)
    plt.bar(x_values, pmf, color='skyblue', edgecolor='black')
    plt.title(f"PMF: {title}")
    plt.xlabel("Count")
    plt.ylabel("Probability")
    
    # CDF Plot (Step Function)
    plt.subplot(1, 2, 2)
    plt.step(x_values, cdf, where='post', color='orange', linewidth=2)
    plt.title(f"CDF: {title}")
    plt.xlabel("Count")
    plt.ylabel("Cumulative Probability")
    plt.ylim(0, 1.05)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# --- EXAMPLE: DICE SIMULATION ---
def simulate_dice_until_six():
    """
    Simulates rolling a die until a 6 is rolled.
    Returns: x_values, pmf, cdf
    """
    n_simulations = 10000
    counts = {}

    # 1. Run Simulation
    for _ in range(n_simulations):
        rolls = 0
        while True:
            rolls += 1
            roll = random.randint(1, 6)
            if roll == 6:
                break
        
        # Record the result
        if rolls in counts:
            counts[rolls] += 1
        else:
            counts[rolls] = 1

    # 2. Process Results into Lists
    x_values = sorted(counts.keys())
    pmf = []
    cdf = []
    cumulative_sum = 0

    for x in x_values:
        # Calculate Probability
        prob = counts[x] / n_simulations
        pmf.append(prob)
        
        # Calculate Cumulative Probability
        cumulative_sum += prob
        cdf.append(cumulative_sum)
        
    return x_values, pmf, cdf

# --- YOUR TASK: CARD SIMULATION ---
def simulate_card_bust():
    """
    Simulates drawing cards until the total > 21.
    Returns: x_values, pmf, cdf
    
    Face Cards(J,Q,K): 10
    Aces: 11; 
        if the hand total exceeds 21, Ace: 1
    
    deck shuffled for every single simulation
    
    the number of simulation: 10,000
    count how many cards were drawn to exceed 21
    
    Calculate PMF and CDF manually without using any statistical libraries (e.g. numpy)
    """
    n_simulations = 10000
    counts = {}

    # TODO: Implement the simulation loop
    # 1. Create a deck: 4 suits of values 2-11 (J,Q,K=10, A=11).
    # 2. Shuffle.
    # 3. Draw cards until sum > 21. (Handle Ace 11->1 constraint).
    # 4. Count cards drawn and update 'counts'.
    
    for _ in range(n_simulations):
        # initialize variables
        drawNum: int = 0
        sum: int = 0
        deck  = [2,3,4,5,6,7,8,9,10,11]
        threshold: int = 21
        
        # loop unless we reached to the threshold
        while(sum < threshold):
            # draw random values from 2-11
            rand_draw: int = random.randint(1, len(deck)-1)
            ## if the hand total exceeds 21 and we drew aces, then ace becomes 1 instead of 11
            if (sum + rand_draw >= threshold and rand_draw == 11):
                rand_draw = 1
            # we add the drawn values after checking for aces threshold
            sum += rand_draw
            # update the number of cards drawn in drawNum
            drawNum+=1
        
        
        if drawNum in counts:
            # Record the result
            counts[drawNum] += 1
        else:
            counts[drawNum] = 1

    # TODO: Convert 'counts' dictionary to x_values, pmf, and cdf lists.
    x_values = sorted(counts.keys())
    pmf = []
    cdf = []
    cumulative_sum = 0
    
    for x in x_values:
        # Calculate Probability
        prob = counts[x] / n_simulations
        pmf.append(prob)
        
        # Calculate Cumulative Probability
        cumulative_sum += prob
        cdf.append(cumulative_sum)
    
    return x_values, pmf, cdf

if __name__ == "__main__":
    # # 1. Run and Plot Dice Simulation
    # print("Running Dice Simulation...")
    # d_x, d_pmf, d_cdf = simulate_dice_until_six()
    # plot_distribution(d_x, d_pmf, d_cdf, "Rolls until 6")
    
    # 2. Run and Plot Card Simulation
    print("Running Card Simulation (Your Work)...")
    c_x, c_pmf, c_cdf = simulate_card_bust()
    
    # Only plot if it has beeb implemented
    if len(c_x) > 0:
        plot_distribution(c_x, c_pmf, c_cdf, "Cards to Exceed 21")
    else:
        print("... Card simulation not implemented yet.")