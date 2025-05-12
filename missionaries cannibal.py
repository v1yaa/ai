def display_state(m_left, c_left, boat_position):
    left = 'M' * m_left + 'C' * c_left
    right = 'M' * (3 - m_left) + 'C' * (3 - c_left)
    if boat_position == 'left':
        print(f"{left} | ---     | {right}")
    else:
        print(f"{left} |     --- | {right}")

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left
    return (0 <= m_left <= 3 and 0 <= c_left <= 3 and
            (m_left == 0 or m_left >= c_left) and
            (m_right == 0 or m_right >= c_right))

def game():
    print("        Game Start")
    print("Now the task is to move all of them to right side of the river")
    print("rules:")
    print("1. The boat can carry at most two people")
    print("2. If cannibals num greater than missionaries then the cannibals would eat the missionaries")
    print("3. The boat cannot cross the river by itself with no people on board\n")

    m_left, c_left = 3, 3
    boat = 'left'

    while True:
        display_state(m_left, c_left, boat)

        if m_left == 0 and c_left == 0:
            print("\nCongratulations! All missionaries and cannibals are safely across.")
            break

        print("\nLeft side -> right side river travel" if boat == 'left' else "\nRight side -> left side river travel")

        try:
            m = int(input("Enter number of Missionaries travel => "))
            c = int(input("Enter number of Cannibals travel => "))

            if m + c == 0 or m + c > 2 or m < 0 or c < 0:
                print("Invalid input please retry !!\n")
                continue

            if boat == 'left':
                new_m_left = m_left - m
                new_c_left = c_left - c
            else:
                new_m_left = m_left + m
                new_c_left = c_left + c

            if not is_valid(new_m_left, new_c_left):
                print("Invalid move! Cannibals would eat the missionaries or invalid count. Try again.\n")
                continue

            m_left, c_left = new_m_left, new_c_left
            boat = 'right' if boat == 'left' else 'left'

        except ValueError:
            print("Invalid input please retry !!\n")

# Start the game
game()
