def solutions():
    """
    Solves the SEND + MORE = MONEY cryptarithm using brute force.
    """
    all_solutions = []

    # Iterate over all possible values for the letters
    for s in range(1, 10):  # 'S' must not be 0 as SEND is a 4-digit number
        for e in range(10):
            for n in range(10):
                for d in range(10):
                    for m in range(1, 10):  # 'M' must not be 0 as MONEY is a 5-digit number
                        for o in range(10):
                            for r in range(10):
                                for y in range(10):
                                    # Ensure all letters are unique
                                    if len(set([s, e, n, d, m, o, r, y])) == 8:
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

                                        # Check if the cryptarithm equation is satisfied
                                        if send + more == money:
                                            all_solutions.append((send, more, money))

    return all_solutions


# Output the solutions
print(solutions())
