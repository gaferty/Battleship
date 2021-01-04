"""
To run this game you will need to make sure that:

- pygame is installed
- battleships.py is in the same folder

To note this will take a couple of seconds to initialise
"""

import pygame as pg
import battleships as bt
import random



class Rectangle():
  
  def __init__(self,screen,x,y,length,border,color,height = 0):
    """ 
    This class will initialse rectangles that can then be drawn on the screen.
    X,Y = the coordinates the top left hand corner
    length = the length of the rectangle based on the X axis
    border = the width of the border around the square
    color= the color of the inner rectangle
    height = will manipulate the height og the rectangle ( change the value on the Y axis) 
    """
    # if the height = 0 then the 
    if height ==0:
      height = length

    # initialise the dimensions of the rectangle
    self.screen = screen
    self.internal_X = x + border
    self.internal_Y = y + border
    self.internal_color = color
    
    self.internal_length = length - (border*2)
    self.internal_height = height - (border*2)
    
    self.dimensions = self.rectangle_dimensions(x,y,length,height)

    # if the border is not 0 then the outer rectangle will be drawn.
    if border !=0:
      pg.draw.rect(screen, (0,0,0), pg.Rect(x,y,length,height),0)
    self.innerRect()
  
      
  def innerRect(self):
    #This function will set up the inner rectangle for the rectangle
    pg.draw.rect(self.screen, self.internal_color, pg.Rect(self.internal_X, self.internal_Y, self.internal_length,self.internal_height),0)
  
  def updateColor(self,color):
    # This will update the internal color of the rectangel
    self.internal_color = color
    self.innerRect()
  
  def rectangle_dimensions(self,x,y,length,height):
    #This will create a tuple of two lists that will contain the top right and the topleft of a Rectangle
    bottom_right_x = x+length
    bottom_right_y = y + height
    return([x,y],[bottom_right_x,bottom_right_y])
  
  def in_rectangle_area(self,x,y):
    #This function will return if the x and y values exist in the function
    if (self.dimensions[0][0]<=x<=self.dimensions[1][0]) and (self.dimensions[0][1] <= y <= self.dimensions[1][1]):
      return True

    return False


    
      


class Button(Rectangle):
  def __init__(self,screen,top_left,padding,message,font,color = (0,0,0),background_color=(255,255,255),border=0):
    """
    This Class will initialise the button by inheriting the functions from the Rectangle class. It will be able to return the grid dimensions and the text value within it.

    These can be used used for click detection.

    The action functions will allow a function to be run when the button is clicked.
    """
    # First Render the Text
    self.text=0
    self.text = self.init_text(font,message,color)
    # Second Calculate the Size of the Text
    (message_length,message_height)= self.text_dimensions(font,message)
    
    # Use this size with padding the input the width and length
    height = message_height + (padding*2)
    length = message_length + (padding*2)

    #This will initialise the button
    

    super().__init__(screen,top_left[0],top_left[1],length,border,background_color,height=height)


    screen.blit(self.text,(top_left[0]+padding,top_left[1]+padding))

  
  def init_text(self,font,message,color):
    # this function will initialise the text
    text=font.render(message,True,color)
    return text
  

  
  def define_action(self,func):
    # This function will allow the button to perform the action presented to it.
    self.action = func
    
    

  def action(self):
    # This action button simply runs the function that is passed in define_action
    self.action()

  def text_dimensions(self,font,text):
      # This function will return the height and length of the text
      return font.size(text)
  
  def return_text(self):
  # This will return the text value in the button
      return self.text
                                       
    

        
class Grid():
  def __init__(self,screen,topleft,length,border=1,color=(255,255,255)):
    #This will contain the Grid class in the future, which will be used by the Battlefield class.
    self.grid = {}
    for x in range(0,10):
      for y in range(0,10):
        rectX = (x*length) + topleft[0]
        rectY = (y*length) + topleft[1]
        new = Rectangle(screen,rectX,rectY,length,border,color)
        self.grid[x,y] = new

  
  def update_square(self,x,y,color):
    #This will update the color in the square
    self.grid[x,y].updateColor(color)  
        
    

                                
                            


class BattleField():
  
  def __init__(self):
    # This will initialise the grid for battleships and then start the game.
    
    instructions = "Click on a white square in the grid. It will turn Red if you hit and blue if you miss."


    # This creates the general parameters for colors and the grid sizes of the game
    self.colors = { 'red':(255,0,0),'blue':(0,0,255),'white':(255,255,255),'black':(0,0,0)}
    self.window = (800, 800)

    self.gridX = 60
    self.gridY = 60
    self.length = 50
    self.border = 1


    
    # This sets the topleft part of the grid
    self.topleft = [self.gridX,self.gridY]
    self.bottomright =[self.gridX+(self.length*10),self.gridY+(self.length*10)]
    self.game_over = False

    self.initialise_game()
  
      
    pg.init()
    # This will initialise the fonts for the System
    
    self.initialise_fonts()

    # This will initialise the different parts of the window
    self.screen = pg.display.set_mode(self.window)
    self.screen.fill(self.colors['white'])
    self.grid = Grid(self.screen,[self.gridX,self.gridY],self.length)
    pg.display.set_caption('Battleships')

    self.ships_left=[4,3,2,1]


    self.Restartbutton = Button(self.screen,[600,50],10,'Restart',self.labelFont,background_color=(125,125,125))
    self.Restartbutton.define_action(self.restart)


    # Need to initialise the different labels for battleships
    self.initialise_text(instructions)
    
    
    
    
    pg.display.flip()
    # Once the initialisations of the game are completed then the game enters into the main loop for updating the game
    self.loop()
  

      
  
  def initialise_fonts(self):
    #This function will initialise the different fonts that can be used in the game. The main font will be labelFont
    self.labelFont = pg.font.SysFont(None, 20)
    self.textFont = pg.font.SysFont(None,10)
    self.AnnounceFont = pg.font.SysFont(None,100)
  

  def restart(self):
    #This function will be used to restart the game by reseting the ships and the grid
    self.initialise_game()
    for i in range(0,10):
      for j in range(0,10):
        self.grid.update_square(i,j,self.colors['white'])
    
    if self.game_over:
      self.victory.clear_text(self.screen,[100,700])
    # This resets the game over to be true so the check functions will continue to run. also it resets the numbers for different ships
    self.ships_left=[4,3,2,1]
    self.ship_numbers=self.init_ship_numbers([660,200],25)
    self.game_over=False
    pg.display.flip()


  def add_labels_to_axis(self,axis=1,offset=20):
    """
    This function will add labels to the X and Y axis
    if Axis is 1 then the value will be be set on the X axis
    any other number will add it to the Y axis
    """
    
    if axis == 1:
      # This handles the X axis labels for numbering
      starting_position_X = self.topleft[0] + (self.length/2)
      starting_position_Y = self.topleft[1] - offset

      for i in range(0,10):
        img = self.labelFont.render(str(i),True,self.colors['black'])
        self.screen.blit(img,(starting_position_X + (i*self.length),starting_position_Y))


    else:
      # This handles the Y axis for numbering
      starting_position_Y = self.topleft[1] + (self.length/2)
      starting_position_X = self.topleft[0] - offset
      for i in range(0,10):
        img = self.labelFont.render(str(i),True,self.colors['black'])
        self.screen.blit(img,(starting_position_X,starting_position_Y+ (i*self.length)))
      pass
      
      
        

  def loop(self):
    # This will be the main loop that will be used when running the UI
    running = True
    while running:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          running = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
          x,y = pg.mouse.get_pos()
          #Will need to add in the ability to check that the retry button is hit
          if self.Restartbutton.in_rectangle_area(x,y):
            self.Restartbutton.action()
     
          else:                    
            self.click_in_grid(x,y)


  def click_in_grid(self,x,y):
    #This checks to see if the click occured in battleships grid
    if (self.topleft[0]<=x<=self.bottomright[0]) and (self.topleft[1]<=y<=self.bottomright[1]):
  
        clickX,clickY = self.return_grid_pos(x,y)
        #print(clickX,clickY)

        if self.run_check(clickX,clickY):
          self.grid.update_square(clickX,clickY,self.colors['red'])
        else:
          self.grid.update_square(clickX,clickY,self.colors['blue']) 
        pg.display.flip()


  
  def return_grid_pos(self,x,y):
    # This will return the integer values for the click on the grid.
    gridX = int((x-self.topleft[0])/50)
    gridY = int((y-self.topleft[1])/50)
    
    return gridX,gridY

  def initialise_game(self):
    # This function initialises the game of battleships abd creates the fleet.
    self.current_fleet = bt.randomly_place_all_ships()
    



  def run_check(self,x,y):
    # This section will run a check to see if the ship has been hit or not.
    current_column = x
    current_row = y
    
    while not self.game_over:
        if bt.check_if_hits(current_row, current_column, self.current_fleet):
            
            (self.current_fleet, ship_hit) = bt.hit(current_row, current_column, self.current_fleet)
            if bt.is_sunk(ship_hit):
                print("You sank a " + bt.ship_type(ship_hit) + "!")
                self.update_ship(ship_hit[3])
                
                if not bt.are_unsunk_ships_left(self.current_fleet):
                  self.game_over = True
                  print('You Won')
                  self.victory =self.end_of_game()
            return True

        else:
            return False

  def initialise_text(self,text):
  # This will initialise the text at the start of the game
    restart=' Click on the restart button to restart the game'

    inst = TextBox(self.screen,[100,580],0,text,self.labelFont,length = 100)
    restart_message= TextBox(self.screen,[580,100],0,restart,self.labelFont)

    # These initialise the different ship types on the right of the grid.
    ships_left_message = TextBox(self.screen,[580,175],0,'Ships left:',self.labelFont,color=self.colors['red'])
    battle_ship_text = TextBox(self.screen,[580,200],0,'Submarine:',self.labelFont)
    cruiser_text = TextBox(self.screen,[580,225],0,'Destroyer:',self.labelFont)
    Destroyer_text = TextBox(self.screen,[580,250],0,'Cruiser:',self.labelFont)
    Submarine_text = TextBox(self.screen,[580,275],0,'BattleShip:',self.labelFont)
    # This adds labels to the two axis of the grid
    self.add_labels_to_axis(1)
    self.add_labels_to_axis(0)
    self.ship_numbers=self.init_ship_numbers([660,200],25)


  def end_of_game(self):
    victory = TextBox(self.screen,[100,700],4,'YOU HAVE WON', self.AnnounceFont,length = 100,color=self.colors['red'])
    #victory.clear_text(self.screen,[100,700])
    return victory

  def init_numbers(self,top_left,initial_number):
    # This will create a ship number for each of the ships  
    ship_number=TextBox(self.screen,top_left,0,initial_number,self.labelFont)
    return ship_number

  def init_ship_numbers(self,top_left,gap):
    # This function will initialise all of the ship numbers and then place them in a list so that they can be updated
    ships={}
    for x in range(0,4):
      number_of_ships = 4
      ships[x]=self.init_numbers([top_left[0],top_left[1]+(gap*x)],str(number_of_ships-x))
    
    return ships

  def update_ship(self,ship_length):
    # This updates the number of ships of a certain type.
    self.ships_left[ship_length-1]=self.ships_left[ship_length-1]-1
    self.ship_numbers[ship_length-1].update_text(self.screen,self.ships_left[ship_length-1],self.labelFont)
        
class TextBox(Button):
  def __init__(self,screen,top_left,padding,message,font,color = (0,0,0),background_color=(255,255,255),length = 30):
    #This class will set up text boxes using the Button class.
    #This class will allow for text to appear in the game window,flash and update with new values

    dimensions = super().text_dimensions(font,message)
    lines = self.split_up_text(message,length)
    
    x=top_left[0]

    self.texts={}

    for i in range(0,len(lines)):
        y = top_left[1] +(dimensions[1]*i)
        self.texts[i]=super().__init__(screen,[x,y],0,lines[i],font,color = color,background_color=background_color)
    
    self.dimensions=dimensions
    self.top_left = top_left
    text = super().return_text()

  
  def split_up_text(self,text,char_length):
    # This will split up the text of the message into the length of the box specified
    split_text = text.split()
    
    line=''
    lines=[]
    for x in split_text:
      if len(line)+len(x) < char_length:
        line += x + " "
    
        
      else:

        lines.append(line)
        line=''
        line += x +' '
        
        
        
    
    lines.append(line)
  
    return lines    
            

  def clear_text(self,screen,topleft):
      # This will put a rectangle on top of the text in order to clear it.
      x = Rectangle(screen,topleft[0],topleft[1],self.dimensions[0],0,(255,255,255),height=self.dimensions[1])

  def set_text(self,screen,top_left,padding,lines,height,message,color=(0,0,0),background_color=(255,255,255)):
    # This function will update the text in the box
    for x in range(0,len(lines)):
        super().__init__(screen,top_left,padding,message,font,color = color,background_color=background_color)
        
    pass

  def update_text(self,screen,newtext,font):
    # This will update the text with a new value
    
    self.clear_text(screen,self.top_left)
    text = font.render(str(newtext),True,(0,0,0))
    screen.blit(text,(self.top_left[0],self.top_left[1]))              

      


  
  

      

      

if __name__ == "__main__":
    
    app = BattleField()
    