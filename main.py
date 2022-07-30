import os

clear = lambda: os.system('cls')
clear()




    

   
print("---- game started ---")
        
    

def howto():
            print(''' 
Player one plays X
Player two plays O

    1 2 3
    4 5 6
    7 8 9
            
select respective place value to place your mark

            ''')
    



def printa(a):
            for i in range(1,10,3):
                for _ in range(i,i+3):
                    print("    ",end="")
                    print(a[_], end = "")
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
        a = ['-' for _ in range(10)]
        ipt = []
        p1 = False
        p2 = False
        turn = 1
        tries = 0
        while(True):
                
            for i1 in range(1,10,3):
                if(a[i1] == 'X' and a[i1+1] == 'X' and a[i1+2] == 'X'):
                    p1 = True
                elif (a[i1] == 'O' and a[i1+1] == 'O' and a[i1+2] == 'O'):
                    p2 = True
                    
                
            for i1 in range(1,4):
                if(a[i1] == 'X' and a[i1+3] == 'X' and a[i1+6] == 'X'):
                    p1 = True   
                elif (a[i1] == 'O' and a[i1+3] == 'O' and a[i1+6] == 'O'):
                    p2 = True
                    

            if(a[2] == 'X' and a[4] == 'X' and a[6] == 'X'):
                p1 = True  
            elif (a[2] == 'O' and a[4] == 'O' and a[6] == 'O'):
                p2 = True
                

            if(a[0] == 'X' and a[4] == 'X' and a[8] == 'X'):
                p1 = True   
            elif (a[0] == 'O' and a[4] == 'O' and a[8] == 'O'):
                p2 = True
                

            if(p1 or p2):
                break
            clear()
            print("\n\n")
            print(a)
            

            printa(a)
            print('\n\n')
            print(f"Player {turn}'s turn, enter index")
                
            index = int(input())
                
                
            while(index>9 or index<0):
                index = int(input("Enter correct index : "))
                
            while(index in ipt):
                index = int(input("Enter another index : "))

            ipt.append(index)
                
            if(turn==1):
                a[index] = 'X'
            elif(turn==2):
                a[index] = 'O'
                
            if(turn==1):
                turn=2
            elif(turn==2):
                turn=1
            tries += 1
            print(tries)
            if(tries==9):
                break
            
        if(p1):
            clear()
            print("\n\n----Player 1 WINS!!----")
            print("\n\nPress enter to continue")
            input()
        if(p2):
            clear()
            print("\n\n----Player 2 WINS!!----")
            print("\n\nPress enter to continue")
            input()
        if(tries == 8):
            clear()
            print("\n\n----DRAW----")
            print("\n\nPress enter to continue")
            input()
            
            
        clear()
