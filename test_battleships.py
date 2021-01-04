import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    s2 = (2, 3, True, 3, {(2,3)})
    s3 = (3,5, False, 5, {(3,5),(4,5),(5,5),(6,5),(7,5)})
    s4 = (3, 5, False, 5, {(3,5),(4,5),(5,5),(6,5)})
    s5 = (9, 9, False, 1, {(9,9)})
    
    
    assert is_sunk(s) == True
    assert is_sunk(s2) == False
    assert is_sunk(s3) == True
    assert is_sunk(s4) == False
    assert is_sunk(s5) == True

def test_is_sunk2():

    s2 = (2, 3, True, 3, {(2,3)})
    assert is_sunk(s2) == False

def test_is_sunk3():
    s3 = (3,5, False, 5, {(3,5),(4,5),(5,5),(6,5),(7,5)})

    assert is_sunk(s3) == True

def test_is_sunk4():

    s4 = (3, 5, False, 5, {(3,5),(4,5),(5,5),(6,5)})

    assert is_sunk(s4) == False


def test_is_sunk5():

    s5 = (9, 9, False, 1, {(9,9)})

    assert is_sunk(s5) == True


    


def test_ship_type1():
    #add at least one test for ship_type by the deadline of session 7 assignment
    #provide at least five tests in total for ship_type by the project submission deadline
    """
    This code inputs 4 different tuples that mimick a list that comproses of a ship (row, column, horizontal, length, hits)
    As the length of the ship dictates it's type only the length parameter will need to be populated.

    This test will fisrt check that the function returns the correct answer, then it will check that the function does
    not return the incorrect answer

    Tests 's5' and 's6' test to see what happens when the length value lies outside of the expected range.


    """
    s1= (0,0,0,1,0)
    s2= (0,0,0,2,0)
    s3= (0,0,0,3,0)
    s4= (0,0,0,4,0)
    s5= (0,0,0,0,0)
    s6 = (0,0,0,7,0)
    assert ship_type(s1)=="submarine"
    assert ship_type(s2)=="destroyer"
    assert ship_type(s3)=="cruiser"
    assert ship_type(s4)=="battleship"
    assert ship_type(s1)!="destroyer" or 'cruiser' or 'battleship'
    assert ship_type(s2)!="submarine" or 'cruiser' or 'battleship'
    assert ship_type(s3)!="submarine" or 'destroyer' or 'battleship'
    assert ship_type(s4)!="submarine" or 'destroyer' or 'cruiser'
    assert ship_type(s3)!="submarine" or 'destroyer'or 'cruiser' or 'battleship'
    assert ship_type(s4)!="submarine" or 'destroyer'or 'cruiser' or 'battleship'
    




def test_is_open_sea1():

    #add at least one test for open_sea by the deadline of session 7 assignment
    #provide at least five tests in total for open_sea by the project submission deadline
    """
        This function will use the list 'fleet' and check if the row and column is next to one of the ships
        in the list.

        The output of the function will be a boolean Value.

        Below is a visualisation of the fleet, where the test sites can be found as well as the fleet
         x = open sea, S = ship, T = test (If it is on a part of the Ship it will show T)

         0 1 2 3 4 5 6 7 8 9
       0 x x x x T x x x x x
       1 x S x x x x x x x x
       2 x x S T S x x x x x
       3 x x x x x x x x x x
       4 x T x x x S x x x x
       5 x x x x x S x x x x
       6 S S x x x S T x x x
       7 x T x x x S x x x x
       8 x x x x x x x x x x
       9 x x x x x x x x x T
       

    """
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]

    assert is_open_sea(4,1,fleet)==True

    return


def test_is_open_sea2():
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]

    assert is_open_sea(6,6,fleet)==False

    return


def test_is_open_sea3():

    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]

    assert is_open_sea(2,3,fleet)==False
    return

def test_is_open_sea4():
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    assert is_open_sea(9,9,fleet)==True
    #assert is_open_sea(7,1,fleet)==False
    #assert is_open_sea(0,4,fleet)==False
    return

def test_is_open_sea5():
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    assert is_open_sea(7,1,fleet)==False
    #assert is_open_sea(0,4,fleet)==False
    return

def test_is_open_sea6():
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    assert is_open_sea(0,4,fleet)==True
    return


def test_ok_to_place_ship_at1():
    #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline
    #This will return a Boolean value if it is ok to place the ship at a certain point.
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    row = 0
    column = 0
    horizontal = True
    length =1 
    
    assert ok_to_place_ship_at(row,column,horizontal,length,fleet) == False

def test_ok_to_place_ship_at2():
                            #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline
    #This will return a Boolean value if it is ok to place the ship at a certain point.
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    row = 3
    column = 1
    horizontal = True
    length =1 
    
    assert ok_to_place_ship_at(row,column,horizontal,length,fleet) == True

def test_ok_to_place_ship_at3():
                            #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline
    #This will return a Boolean value if it is ok to place the ship at a certain point.
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    row = 4
    column = 0
    horizontal = False
    length =4 
    
    assert ok_to_place_ship_at(row,column,horizontal,length,fleet) == False

def test_ok_to_place_ship_at4():
    #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline
    #This will return a Boolean value if it is ok to place the ship at a certain point.
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    row = 5
    column = 5
    horizontal = True
    length =4 
    
    assert ok_to_place_ship_at(row,column,horizontal,length,fleet) == False

def test_ok_to_place_ship_at5():

    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline
    #This will return a Boolean value if it is ok to place the ship at a certain point.
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    row = 2
    column = 3
    horizontal = False
    length =4 
    
    assert ok_to_place_ship_at(row,column,horizontal,length,fleet) == False

def test_place_ship_at1():
    #add at least one test for place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for place_ship_at by the project submission deadline
    fleet=[]
    row = 0
    column = 0
    horizontal = True
    length =1 
    testfleet=[((0,0,True,1,set()))]
    assert place_ship_at(row,column,horizontal,length,fleet)== testfleet

def test_place_ship_at2():

    #provide at least five tests in total for place_ship_at by the project submission deadline
    fleet=[((0,0,True,1,set())),]
    row = 5
    column = 5
    horizontal = False
    length =4 
    testfleet=[((0,0,True,1,set())),((5,5,False,4,set()))]
    assert place_ship_at(row,column,horizontal,length,fleet)== testfleet

def test_place_ship_at3():
                        
    #provide at least five tests in total for place_ship_at by the project submission deadline
    fleet=[((0,0,True,1,set())),((5,5,False,4,set()))]
    row = 9
    column = 0
    horizontal = True
    length =3 
    testfleet=[((0,0,True,1,set())),((5,5,False,4,set())),((9,0,True,3,set()))]
    assert place_ship_at(row,column,horizontal,length,fleet)== testfleet

def test_place_ship_at4():
                                                
    #provide at least five tests in total for place_ship_at by the project submission deadline
    fleet=[((0,0,True,1,set())),((5,5,False,4,set()))]
    row = 9
    column = 0
    horizontal = True
    length =3 
    testfleet=[((0,0,True,1,set())),((5,5,False,4,set()))]
    assert place_ship_at(row,column,horizontal,length,fleet) != testfleet

def test_place_ship_at5():
                        
    #provide at least five tests in total for place_ship_at by the project submission deadline
    fleet=[((0,0,True,1,set())),((5,5,False,4,set()))]
    row = 9
    column = 0
    horizontal = True
    length =3 
    testfleet=[((0,0,True,1,set()))]
    assert place_ship_at(row,column,horizontal,length,fleet)!= testfleet    

def test_check_if_hits1():
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    #provide at least five tests in total for check_if_hits by the project submission deadline
    row = 0
    column = 0
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    assert check_if_hits(row,column,fleet)==False

def test_check_if_hits2():
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    #provide at least five tests in total for check_if_hits by the project submission deadline
    row = 1
    column = 1
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    assert check_if_hits(row,column,fleet)==True

def test_check_if_hits3():
    #provide at least five tests in total for check_if_hits by the project submission deadline
    row = 2
    column = 6
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    assert check_if_hits(row,column,fleet)==False

def test_check_if_hits4():
    #provide at least five tests in total for check_if_hits by the project submission deadline
    row = 2
    column = 5
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    assert check_if_hits(row,column,fleet)==True

def test_check_if_hits5():
    #provide at least five tests in total for check_if_hits by the project submission deadline
    row = 7
    column = 5
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]
    assert check_if_hits(row,column,fleet)==True
    
def test_hit1():
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline
    row =1
    column = 1
    s=set()
    fleet = [
        (1,1,True,1,set()),
        (2, 3, True, 3,set()),
        (4,5, False, 4,set() ),
        (6,0, True, 2, set())
    ]
    fleet1 = [
        (1,1,True,1,{(1,1)}),
        (2, 3, True, 3,set()),
        (4,5, False, 4, set()),
        (6,0, True, 2, set())
    ]
    ship = (1,1,True,1,{(1,1)})

    assert hit(row,column,fleet) == (fleet1,ship)



def test_hit2():
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline
    row =5
    column = 5 
    fleet = [
        (1,1,True,1,set()),
        (2, 3, True, 3, set()),
        (4,5, False, 4, set()),
        (6,0, True, 2, set())
    ]
    fleet1 = [
        (1,1,True,1,set()),
        (2, 3, True, 3,set()),
        (4,5, False, 4, {(5,5)}),
        (6,0, True, 2, set())
    ]
    ship = (4,5, False, 4,{(5,5)} )

    assert hit(row,column,fleet) == (fleet1,ship)

def test_hit3():
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline
    row =6
    column = 1
    fleet = [
        (1,1,True,1,set()),
        (2, 3, True, 3, set()),
        (4,5, False, 4, set()),
        (6,0, True, 2, set())
    ]

    fleet1 = [
        (1,1,True,1,set()),
        (2, 3, True, 3,set()),
        (4,5, False, 4, set()),
        (6,0, True, 2, {(6,1)})
    ]

    ship = (6,0, True, 2, {(6,1)})

    assert hit(row,column,fleet) == (fleet1,ship)


def test_hit4():
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline
    row =2
    column = 3
    fleet = [
        (1,1,True,1,set()),
        (2, 3, True, 3, {(2,4)}),
        (4,5, False, 4, set()),
        (6,0, True, 2, set())
    ]

    fleet1 = [
        (1,1,True,1,set()),
        (2, 3, True, 3,{(2,4),(2,3)}),
        (4,5, False, 4, set()),
        (6,0, True, 2, set())
    ]

    ship = (2, 3, True, 3,{(2,4),(2,3)})

    assert hit(row,column,fleet) == (fleet1,ship)


def test_hit5():
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline
    row =1
    column = 1
    fleet = [
        (1,1,True,1,{(1,1)}),
        (2, 3, True, 3, set()),
        (4,5, False, 4, set()),
        (6,0, True, 2, set())
    ]

    fleet1 = [
        (1,1,True,1,{(1,1)}),
        (2, 3, True, 3,set()),
        (4,5, False, 4, set()),
        (6,0, True, 2, set())
    ]

    ship = (1,1,True,1,{(1,1)})

    assert hit(row,column,fleet) == (fleet1,ship)


def test_are_unsunk_ships_left1():
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    fleet = [
        (1,1,True,1,{}),
        (2, 3, True, 3, {}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]

    assert are_unsunk_ships_left(fleet) == True

     
def test_are_unsunk_ships_left2():
    fleet = [
        (1,1,True,1,{(1,1)})
    ]

    assert are_unsunk_ships_left(fleet) == False
                            
def test_are_unsunk_ships_left3():
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    fleet = [
        (1,1,True,1,{(1,1)}),
        (2, 3, True, 3, {(2,3),(3,3),(4,3)}),
        (4,5, False, 4, {}),
        (6,0, True, 2, {})
    ]

    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left4():
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    fleet = [
        (1,1,True,1,{(1,1)}),
        (2, 3, True, 3, {(2,3),(3,3),(4,3)}),
        (4,5, False, 4, {(4,5),(4,6),(4,7),(4,8)}),
        (6,0, True, 2, {(6,0),(6,1)})
    ]

    assert are_unsunk_ships_left(fleet) == False

def test_are_unsunk_ships_left5():
                            #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    fleet = [
        (1,1,True,1,{(1,1)}),
        (2, 3, True, 3, {(2,3),(3,3),(4,3)}),
        (4,5, False, 4, {(4,5),(4,6),(4,7),(4,8)}),
        (6,0, True, 2, {(6,0),})
    ]

    assert are_unsunk_ships_left(fleet) == True
