#see the readme.md file for description and data 
import random as rand


def is_sunk(ship):
    """
    Expected Input: tuple

    Functionality: 
        Will return true if the length of the hits set is the same as the length of the ship.

    Expected Output: Boolean
    """
    if len(ship[4]) == ship[3]:
        return True
    
    else:
        return False

    

def ship_type(ship):
    """
    Input: The List of the Hit Ship
    Function: Select the Ship[3], to return the length. Use this length to find out what the ship type is.
    Output:

    This will return what type of ship the inputed ship value is.
    Ship Types are:
        - battleship (4)
        - cruiser(3)
        - destroyer(2)
        - Submarine(1)
    
    """
    
    ship_list = ('submarine','destroyer','cruiser','battleship')
    return ship_list[ship[3]-1]

def ship_box(top_left,orient,input_length,width= 0):
    # This function returns the ship hit box, the width defaults to 0 so 
    # that it can be used to check if the ship is hit or not( This is in effect a hit box)
    if orient:
        bottom_right = [top_left[0]+ width,top_left[1]+input_length]
    else:
        bottom_right = [top_left[0]+input_length,top_left[1]+width]

    ship_area = [top_left,bottom_right]

    return ship_area



def is_open_sea(row, column, fleet):
    #remove pass and add your implementation
    """
    
    Checks if the square given is neither a ship nor adjacent to a ship.
    need to check if the ship is vertical or Horizontal.  There is effectively a rectangle around the ship that is not open sea.

                X X X X X
                X S S S X
                X X X X X
    I will need to +- the ship row and column 

    Expected output: boolean
    """

    for x in fleet:
    # This will return the left most corner of the non open sea area and then increase the length of the ship
        new_col = x[1]-1
        new_row = x[0]-1
        new_len = x[3]+1

        box = ship_box([new_row,new_col],x[2],new_len,width=2)

        if (box[0][0]<= row <= box[1][0]) and (box[0][1]<= column <= box[1][1]):
            # If the row + column lies within the ship_box then the function will return False.
            return False

    return True


    
def generate_ship_body(row,column,horizontal,length):
    """ 
    This function returns all of the squares in the ships body so that it can be checked to see if the ship has been hit.
    """
    body=[[row,column]]
    for x in range(1,length):
        if horizontal:
            body.append([row,column+x])
        else:
            body.append([row+x,column])
    
    return body




def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """
    This will return if the placement of the ship is ok by checking the previously placed ships placed ships in the fleet.

    This function will first generate the coordinates for each section of the ship and then test to see if any of them interact with the rest of the fleet.

    Expected output: Boolean
    """
    ship = generate_ship_body(row,column,horizontal,length)
    

    for x in ship:
        if not is_open_sea(x[0],x[1],fleet):
            return False

        elif (x[0] > 9 ) or (x[1]>9):
            return False 
    return True


def place_ship_at(row, column, horizontal, length, fleet):
    """
    Expected Input: row (int), column (int), horizontal(bool), length(int), fleet(list)
    
    function: add a new ship to the list fleet.

    """
    x = set()
    ship = (row,column,horizontal,length,set())
    fleet.append(ship)
    return fleet



def randomly_place_all_ships():
    """
    This will run through the different lengths of the ship that need to be added to the battleships battleground.
    This moves from largest to smallst in order to make it easierr to fit the ships in.
    Expected output: List that contains all 
    """
    ships = [4,3,3,2,2,2,1,1,1,1]
    fleet = []

    for x in range(0,10):
        row = rand.randrange(0,9)
        column = rand.randrange(0,9)
        horizontal = bool(rand.getrandbits(1))
        length = ships[x]
        while not ok_to_place_ship_at(row,column,horizontal,length,fleet) :
            row = rand.randrange(0,9)
            column = rand.randrange(0,9)
            horizontal = bool(rand.getrandbits(1))
            pass
    
        fleet = place_ship_at(row,column,horizontal,length,fleet)
    return fleet


def check_if_hits(row, column, fleet):
    """
    This will check to see if the value input is open ocean.
    This will take the row and column of the shot and utilise the fleet data structure in order to check if a ship has been hit.
    """

    for x in fleet:
        box = ship_box([x[0],x[1]],x[2],x[3]-1)
        if (box[0][0]<= row <= box[1][0]) and (box[0][1]<= column <= box[1][1]):
            # If the row + column lies within the ship_box then the function will return False.
            return True

    return False


def hit(row, column, fleet):
    """
    This will return the ship and the new fleet that contains the updated hit ship.
    """
    fleet1 = fleet.copy()
    for x in range(0,len(fleet)):
        ship = fleet1[x]
        if check_if_hits(row,column,[ship]):
            
            ship_body = generate_ship_body(ship[0],ship[1],ship[2],ship[3])
            
            
            for i in ship_body:
                
                if row == i[0] and column == i[1]:
                    print("hit")
                    ship[4].add((row,column))
                    return (fleet1, ship)

                
    return (fleet1, ship)








    

def are_unsunk_ships_left(fleet):
    """
    This will check to see if the value input is open ocean.
    Maybe a good way to do this would be to remove the sunk ship from the fleet so that
    this function will simply need to check if the length if greater than 0.
    """
    for x in fleet:
        if not is_sunk(x):
            return True
    
    return False

    

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    """
        Data structure of ship is:(
            ROW(This is the positional row of the ship. This is an integer between 0 and 9),
            COLUMN (This is the positional column of the ship. This is an integer between 0 and 9),
            HORIZONTAL ( This is a BOOLEAN value True REpresentes horizontal and False represents a vertical ship),
            LENGTH ,(This can be a length of between 1-4 depending on the type of the ship)
            HITS(This is a set of tuples (row,col) of each hit that occurs for the ship),

        )



    """
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1 
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_ships_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
