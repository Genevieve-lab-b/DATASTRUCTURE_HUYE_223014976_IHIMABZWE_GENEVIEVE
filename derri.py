num=100
for nu in range(1,num+1):
   
  if nu % 2 ==0:
     print(nu)
     array=(1,2,3,4,5,6,7)
for index ,number in enumerate(array):    
  print(number,index)
  
  number=5
  if (number % 2==0):
        print('even')
  else: 
        print('odd')
        
board= [
  ['x','0','x']
  ['0','x','x']
  ['x','o','x']
  
]       
def check_winner(board):
  for row in board:

        if row [0]== row[1]== row[2]:
          return'f winner is (row[0])'
        