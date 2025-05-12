from itertools import permutations

def solve_cryptarithmetic(puzzle):
    """
    Solves the cryptarithmetic puzzle.
    puzzle: a string in the form "WORD + WORD = RESULT"
    Returns a dictionary mapping letters to digits, or None if no solution is found.
    """
    words = puzzle.replace('=', '+').split('+')
    words = [word.strip() for word in words]
    
    unique_letters = set(''.join(words))
    if len(unique_letters) > 10:
        return None  # Too many unique letters for digits 0-9

    first_letters = {word[0] for word in words}

    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))

        # No leading zeros
        if any(mapping[word[0]] == 0 for word in words):
            continue

        def word_to_number(word):
            return int(''.join(str(mapping[char]) for char in word))

        values = [word_to_number(word) for word in words]
        if sum(values[:-1]) == values[-1]:
            return mapping
    return None

# Example usage
puzzle = "SEND + MORE = MONEY"
mapping = solve_cryptarithmetic(puzzle)

if mapping:
    print("Solution mapping:", mapping)
    
    # Displaying the numeric values
    def word_to_number(word):
        return int(''.join(str(mapping[c]) for c in word))
    
    words = puzzle.replace('=', '+').split('+')
    words = [word.strip() for word in words]
    numeric_values = [word_to_number(word) for word in words]
    expression = " + ".join(str(num) for num in numeric_values[:-1]) + " = " + str(numeric_values[-1])
    
    print("Numeric substitution:", expression)
else:
    print("No solution found.")
