import math

EMPTY = '-'

def is_between(value, min_value, max_value):

    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    return min_value<=value and value<= max_value 
    
# ##############################################################################    
def game_board_full(game_board):
    
    """  (str) -> bool

    Precondition: 
    the length of game_board shouldn't be longer than 81 characters 
    
    Return True if and only if all of the cells in game_board have been chosen
    (which means there is no EMPTY '-'),else the function return False. 
    
    >>> game_board_full('OOOOOOXXX')
    True
    >>>game_board_full('--------o')
    False
    """
    return EMPTY not in game_board

# ##############################################################################    

def get_board_size(game_board):    
         
    """ (str) -> int 
    
    Precondition: 
    the length of game_board shouldn't be longer than 81 characters     
    
    return the length of each side of game_board.    
    
    >>>get_board_size('ooooxxxxx')
    3
    >>>get_board_size('oooo')
    2
    """
    return int(math.sqrt(len(game_board)))

# ##############################################################################
def make_empty_board(board_size):
    
    """ (int) -> str 
    
    Precondition: 1<=board_size<=9 and also board_size should be an int
       
    This function is to return a string for storing information about a     
    game board whose size is calculated by using board_size.  
    Each character in the returned string is to have been set 
    to the EMPTY character, to indicate that no cells have been chosen yet.
    
    >>>make_empty_board(3)
    ---------
    >>>make_empty_board(2)
    ----
    """
    return (board_size**2)*EMPTY    
    
    
# ##############################################################################  
def get_position(row_index,col_index,board_size):
   
    """(int, int, int) -> int  
        
    Precondition: 1<=board_size<=9 and board_size should be an int
                  
                  1<=row_index<=board_size and row_index should be an int
                  
                  1<=row_index<=board_size and row_index should be an int   

    This function is to return the str_index of the cell in the string     
    representation the game board corresponding     
    to the given row_index,col_index and board_size.
    
    >>>get_position(1,2,3)
    1
    >>>get_position(2,3,4)
    6
    """
    return (row_index-1)*board_size+col_index-1        

# ##############################################################################    
def make_move(Nought_or_cross,row_index,col_index,game_board):
    
    """ (str, int, int, str) -> str
    
    Precondition:
    the length of game_board shouldn't be longer than 81 characters
      
    according to the game_board  size the board_size is calculated
    1<=row_index<=board_size and row_index should be an int
    
    1<=row_index<=board_size and row_index should be an int 

    This function is to return game_board that results when     
    the given symbol  which is assigned to Nought_or_cross 
    is placed at the str_index which is calulated by using 
    row_index and col_index  in the given game_board.
    
    >>>make_move('O',1,2,'OOOOOOOXX')
    'OOOOOOOOX'
    >>>make_move('X',2,3,'XXXXOOOXX')
    'XXXXOXOOX'    
    """
    str_index=(row_index - 1)* int((math.sqrt(len(game_board))))+col_index-1           
    return game_board[0:str_index] + Nought_or_cross + game_board[str_index:-1] 
    

# ##############################################################################   
def extract_line(game_board,directions,row_column_number):
    
    """ (str, str, int) -> str
   
   precontidition:  
   the length of game_board shouldn't be longer than 81 characters
     
   the directions should be : 'down','across','up_diagonal','down_diagonal'   
   
   according to the game_board  size the board_size is calculated   
   0<=row_column_number<=board_size
   
   When the second parameter is 'down_diagonal' or 'up_diagonal', 
   the value of the third parameter should not be used.
   
   Return the characters that make up the 
   specified directions such as:row (when the second parameter is 'across'), 
   column (when the second parameter is 'down') or diagonal from the given 
   game_board. The function will use row_column_number when directions is 'down'
   or 'across' to extract the line specified by the row_column_number.
   
   >>>extract_line('OOOXXXOOO','down',2)
   'OXO'
   >>>extract_line('OOXXOOXXO','across',3)
   'XXO'
   """
    
    board_size=int(math.sqrt(len(game_board)))
    
    if directions=='down':
            start=row_column_number-1      
            end=start + board_size*(board_size -1)                
            return game_board[start:end+1:board_size]
        
    if directions=='across':
            start=(row_column_number - 1)*int((math.sqrt(len(game_board))))        
            end=start + board_size -1       
            return game_board[start:end+1]    
            
    if directions=='down_diagonal':
            start=0
            end=(board_size - 1)* board_size+board_size-1
            return game_board[start:end+1:board_size+1]    

    if directions=='up_diagonal':
            start=-(board_size)
            end=board_size-1
            return game_board[start:end-1:-(board_size-1)]
