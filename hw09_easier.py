# Don't change the function name
def expected_length(g):   
    # Stack stores tuples of: (current_node, parent_node, probability, depth)
    # The journey starts at city 1 with a probability of 1.0 (100%) and a depth of 0
    stack = [(1, None, 1.0, 0)]
    total_length = 0.0
    lenghts = []
    while stack:
        node, parent, prob, depth = stack.pop()
        
        # Find all unvisited children
        children = [n for n in g[node] if n != parent]
        
        if not children:
            # We hit a leaf. 
            lenghts += [depth]
        else:
            # The probability is split equally among all unvisited children
            next_prob = prob / len(children)
            
            # Add all children to the stack to be processed
            for child in children:
                stack.append((child, node, next_prob, depth + 1))

    total_length = sum(lenghts)  
    return total_length
