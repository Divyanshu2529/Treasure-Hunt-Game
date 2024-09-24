#Treasure Hunt Game 
#Description: A treasure hunting game where the player moves on a 7x7 grid in search
#of treasures while avoiding traps. The player can look around for hints, and the game
#ends when all treasures are found or if the player steps on a trap.


def read_map(filename='map.txt'):
    
    #Reads the map from a file and stores each character in a 2D list.
    
    #Parameters:
    #filename (str): The name of the file containing the map.
    
    #Returns:
    #list: A 2D list representing the map without spaces and new lines.
    
    with open(filename, 'r') as file:
        maze = [list(line.strip().replace(' ', '')) for line in file]
    return maze

def display_map(game_map, player):
    
    #Displays the map with the player's location marked by 'P'.
    
    #Parameters:
    #game_map (list): The 2D list representing the game map.
    #player (list): A two-item list storing the player's current position [row, col].
    
    #Returns:
    #None
    
    for row in range(len(game_map)):
        for col in range(len(game_map[row])):
            if [row, col] == player:
                print('P', end=' ')
            else:
                print(game_map[row][col], end=' ')
        print()  # New line at the end of each row.

def move_player(player, direction, upper_bound):
    
    #Moves the player in the specified direction, checking boundaries.
    
    #Parameters:
    #player (list): The current player's location [row, col].
    #direction (str): The direction of movement ('W', 'A', 'S', 'D').
    #upper_bound (int): The maximum index allowed on the grid.
    
    #Returns:
    #bool: True if the movement is successful, False otherwise.
    
    row, col = player
    if direction == 'W' and row > 0:
        player[0] -= 1
    elif direction == 'S' and row < upper_bound:
        player[0] += 1
    elif direction == 'A' and col > 0:
        player[1] -= 1
    elif direction == 'D' and col < upper_bound:
        player[1] += 1
    else:
        print("You cannot move that direction")
        return False
    return True

def count_treasures_traps(game_map, player, upper_bound):
    
    #Counts the number of treasures ('T') and traps ('X') in the surrounding cells.
    
    #Parameters:
    #game_map (list): The 2D list representing the game map.
    #player (list): The current player's location [row, col].
    #upper_bound (int): The maximum index allowed on the grid.
    
    #Returns:
    #tuple: A tuple containing (number_of_treasures, number_of_traps).
    
    row, col = player
    treasures = 0
    traps = 0
    
    for i in range(max(0, row-1), min(row+2, upper_bound+1)):
        for j in range(max(0, col-1), min(col+2, upper_bound+1)):
            if game_map[i][j] == 'T':
                treasures += 1
            elif game_map[i][j] == 'X':
                traps += 1
    
    return treasures, traps

def main():
    
    #Main function to run the Treasure Hunter game.
    
    #Returns:
    #None
    
    game_map = read_map('map.txt')  # Read the solution map from file.
    player_map = [['.' for _ in range(7)] for _ in range(7)]  # Player's visible map.
    player = [0, 0]  # Player starts at the top left corner (0,0).
    treasures_found = 0
    total_treasures = 7
    upper_bound = 6  # 7x7 grid has boundaries from 0 to 6.
    
    print("Treasure Hunt!\nFind the 7 treasures without getting caught in a trap.\nLook around to spot nearby trap and treasure.")
    
    while True:
        display_map(player_map, player)  # Show the player's visible map.
        choice = input("Enter Direction (WASD or L to Look around or Q to quit): ").upper()
        
        if choice == 'Q':
            print(f"You quit the game. Treasures found: {treasures_found}")
            break
        
        if choice in ['W', 'A', 'S', 'D']:
            moved = move_player(player, choice, upper_bound)
            if moved:
                current_row, current_col = player
                if game_map[current_row][current_col] == 'T':
                    print("You found a treasure!")
                    treasures_found += 1
                    player_map[current_row][current_col] = 'T'
                    print(f"There are {total_treasures - treasures_found} treasures remaining.")
                    if treasures_found == total_treasures:
                        print("You found all the treasures. You win!")
                        break
                elif game_map[current_row][current_col] == 'X':
                    print("You were caught in a trap!")
                    print(f"You found {treasures_found} treasures.")
                    player_map[current_row][current_col] = 'X'
                    display_map(player_map, player)  # Show the final map state with the trap.
                    print("Game Over!")
                    break
        
        elif choice == 'L':
            treasures, traps = count_treasures_traps(game_map, player, upper_bound)
            print(f"You detect {treasures} treasures nearby.")
            print(f"You detect {traps} traps nearby.")
            current_row, current_col = player
            if player_map[current_row][current_col] != 'T':
                player_map[current_row][current_col] = str(traps)  # Display the number of traps.
        else:
            print("Invalid input.")

if __name__ == '__main__':
    main()
