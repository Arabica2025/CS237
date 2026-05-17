# n cities and n-1 roads in the Tree Kingdom, each connects
# two cities; we can reach any city from any other by the roads

# traveling with horse; when horse reaches a city, it goes
# to one of the cities connected to the current city.

# it only goes to cities they weren't before
# in each city, horse moves uniformly at random to one unvisited
# neighbor city, and stops if no unvisited neighbor city exists

# length of each road = 1. journey starts in the city 1.

# expected length of the journey?

# input = dictionary g = {c: [n_1, n_2, ...]}
# c = one of the cities
# [n_1, n_2, ...] = list of its neighbor cities connected by direct road.


# must return the expected length of the journey.
# it starts in the city 1.

# Don't change the function name
def expected_length(g: dict) -> float:   
    
    def l_helper(city: int, visited: set) -> float:
        # find unvisited neighbors in current city
        unvisited = [n for n in g[city] if n not in visited] # e.g. city 1: unvisited = [2,3]
        
        # if there is no unvisited city left, return 0
        if not unvisited:
            return 0
        
        # total number of expected length for the next move
        total_expected_length: int = 0
        # in neighboring unvisited cities,
        for neighbor in unvisited:
            # total expected length += 1 and recursive call as I add the visited city of neighboring to visited '|'-> union
            # recursion until there is no unvisited city left
            total_expected_length += 1 + l_helper(neighbor, visited | {neighbor})
        
        # after the sum, devide the total by the number of unvisited cities
        return total_expected_length / len(unvisited)
        
    
    # Complete the following code
    
    return l_helper(1, {1}) # start from city 1; include city 1 in visited list as default
