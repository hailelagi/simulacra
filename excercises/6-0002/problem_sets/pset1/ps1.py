###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    import copy
    consider_cows = copy.deepcopy(cows)
    transport_cows = []

    # O(n) + O(n) + O(n) + O(n) + O(1) = O(n)
    def get_cow_trip(trip_cows, limit):
        trip_limit = limit
        trip_transport = []
        # O(n)
        pick_cow = max(consider_cows.values())
        smallest_cow = min(consider_cows.values())

        # O(n) + O(1)
        for cow in trip_cows:
            if (pick_cow == cow[1] and trip_limit >= pick_cow) or (trip_limit >= cow[1]):
                trip_limit -= cow[1]
                trip_transport.append(cow[0])
                consider_cows.pop(cow[0])

            elif smallest_cow > trip_limit:
                break
        return trip_transport

    while consider_cows:
        # O(log(n)) + (nlog(n)) = O(nlog(n))
        trip = get_cow_trip(sorted(consider_cows.items(), key=lambda x: -x[1]), limit)
        transport_cows.append(trip)

    # O(nlog(n))
    return transport_cows

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    import copy
    from functools import reduce

    all_cows = copy.deepcopy(cows)

    # O(n2^n)
    possible_partitions = []

    for partition in get_partitions(all_cows.keys()):
        part_weights = []

        for part in partition:
            part_weights.append(list(map(lambda cow: all_cows[cow], part)))

        constraint = map(lambda trip: sum(trip) <= limit, part_weights)
        is_trip = reduce(lambda x, y: x and y, constraint)

        if is_trip:
            possible_partitions.append(partition)
    
    optimal = min(map(lambda pos: len(pos), possible_partitions))
    
    for possibility in possible_partitions:
        if len(possibility) == optimal:
            return possibility


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
    start_greedy = time.time()
    greedy_cow_transport(cows, limit)
    end_greedy = time.time()
    print(f"It took greedy cow transport {end_greedy - start_greedy}s")

    start_brute = time.time()
    brute_force_cow_transport(cows, limit)
    end_brute = time.time()
    print(f"It took brute force cow transport {end_brute - start_brute}s")
"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))