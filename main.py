import os

clear = lambda: os.system('cls')
clear()


class tictacktoe:

    a = ['-' for _ in range(9)]

    def __init__(self):
        print("---- game started ---")
        
    

    def howto():
            print(''' 
Player one plays X
Player two plays O

    0 1 2
    3 4 5
    6 7 8
            
select respective place value to place your mark

            ''')
    

    def reset(self):
            self.a = ['-' for _ in range(9)]
    

    def printa(self):
            for i in range(0,9,3):
                for _ in range(i,i+3):
                    print("    ",end="")
                    print(self.a[_], end = " ")
                print("")
    
    
    
    while(True):
        
        print('''
TIC-TACK-TOE        
        
1. Start
2. How to play
3. Exit
            ''')
        
        bi = int(input("Enter choice : "))
        
        while(bi>3 or bi<1):
            bi = int(input("Enter valid choice : "))
    
        if(bi ==2):
            clear()
            howto()
            print("Press enter to continue")
            input()
            clear()

        if(bi == 3):
            clear()
            print('''
            
---- thanks for playing ----
            
            
            ''')
            exit()
        
        if(bi == 1):
            reset()
            ipt = []
            p1 = False
            p2 = False
            turn = 1
            tries = 0
            while(not p1 and not p2):
                
                for i1 in range(0,9,3):
                    if(a[i1].upper == 'X' and a[i1+1].upper == 'X' and a[i1+2].upper == 'X'):
                        p1 = True
                    elif (a[i1].upper == 'O' and a[i1+1].upper == 'O' and a[i1+2].upper == 'O'):
                        p2 = True
                
                for i1 in range(0,3):
                    if(a[i1].upper == 'X' and a[i1+3].upper == 'X' and a[i1+6].upper == 'X'):
                        p1 = True
                    elif (a[i1].upper == 'O' and a[i1+3].upper == 'O' and a[i1+6].upper == 'O'):
                        p2 = True

                if(a[2].upper == 'X' and a[4].upper == 'X' and a[6].upper == 'X'):
                    p1 = True
                elif (a[2].upper == 'O' and a[4].upper == 'O' and a[6].upper == 'O'):
                    p2 = True

                if(a[0].upper == 'X' and a[4].upper == 'X' and a[8].upper == 'X'):
                    p1 = True
                elif (a[0].upper == 'O' and a[4].upper == 'O' and a[8].upper == 'O'):
                    p2 = True

                clear()
                print("\n\n")

                printa()
                print(f"Player {turn}'s turn, enter index")
                
                index = int(input())
                ipt.append(index)
                
                while(index>8 and index<0):
                    index = int(input("Enter correct index : "))
                
                while(index in ipt):
                    index = int(input("Enter another index : "))
                
                if(turn==1):
                    a[index] = 'X'
                elif(turn==2):
                    a[index] = 'O'
                
                if(turn==1):
                    turn=2
                elif(turn==2):
                    turn=1
                tries += 1
                if(tries ==8):
                    break
            
            if(p1):
                clear()
                print("\n\n----Player 1 WINS!!----")
            if(p2):
                clear()
                print("\n\n----Player 2 WINS!!----")
            if(tries == 8):
                clear()
                print("\n\n----DRAW----")
            
            print("\n\nPress enter to continue")
            input()
            

    

gamestart = tictacktoe()

        


        
        
        

        

            
  
        

    