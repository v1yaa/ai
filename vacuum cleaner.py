import random

def generate_room(rows, cols):
    return [[1 for _ in range(cols)] for _ in range(rows)]

def randomly_clean_some_cells(room):
    for i in range(len(room)):
        for j in range(len(room[0])):
            if random.random() < 0.3:  # 30% chance to start as clean
                room[i][j] = 0
    return room

def display_room(room):
    for row in room:
        print(row)

def vacuum_cleaner(room):
    total_cells = len(room) * len(room[0])
    dirty_cells = sum(cell == 1 for row in room for cell in row)
    cleaned = 0

    print("All the rooom are dirty")
    print(generate_room(len(room), len(room[0])))
    
    print("Before cleaning the room I detect all of these random dirts")
    display_room(room)

    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j] == 1:
                print(f"\nVaccum in this location now, {i} {j}")
                print(f"cleaned {i} {j}")
                room[i][j] = 0
                cleaned += 1

    print("\nRoom is clean now, Thanks for using : A.SAFARJI CLEANER")
    display_room(room)

    performance = (cleaned / total_cells) * 100
    print(f"performance= {performance:.2f} %")

if __name__ == '__main__':
    room = generate_room(4, 4)
    room = randomly_clean_some_cells(room)
    vacuum_cleaner(room)

