import random


def randomSolution(tsp):
    """
    Generates a random solution for the TSP.
    """
    cities = list(range(len(tsp)))
    solution = []

    while cities:
        randomCity = random.choice(cities)
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution


def routeLength(tsp, solution):
    """
    Calculates the total route length for a given solution.
    """
    length = 0
    for i in range(len(solution)):
        length += tsp[solution[i - 1]][solution[i]]  # Wraps around using i-1
    return length


def getNeighbours(solution):
    """
    Generates all neighbors of the current solution by swapping two cities.
    """
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbours.append(neighbour)
    return neighbours


def getBestNeighbour(tsp, neighbours):
    """
    Finds the best neighbor with the shortest route length.
    """
    bestNeighbour = neighbours[0]
    bestRouteLength = routeLength(tsp, bestNeighbour)

    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestNeighbour = neighbour
            bestRouteLength = currentRouteLength

    return bestNeighbour, bestRouteLength


def hillClimbing(tsp):
    """
    Performs the Hill Climbing algorithm for the TSP.
    """
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)

    while True:
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

        if bestNeighbourRouteLength >= currentRouteLength:
            # If no improvement, terminate
            break

        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength

    return currentSolution, currentRouteLength


def main():
    tsp = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]

    solution, route_length = hillClimbing(tsp)
    print(f"Solution: {solution}, Route Length: {route_length}")


if __name__ == "__main__":
    main()
