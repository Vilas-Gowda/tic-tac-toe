import random

class tictacktoe:
    
        print('''
            TIC-TACK-TOE        
        
            1. Start
            2. How to play
            3. Exit
            ''')
        bi = int(input("Enter choice : "))
        while(bi>3 or bi<1):
            bi = int(input("Enter valid choice : "))
    
        def howto():
            print(''' 
            Player one plays X
            Player two plays O
            1 2 3
            4 5 6
            7 8 9
            select respective place value to place your mark
            ''')

        if(bi ==2):
            howto()
        
        a = ['-' for x in range(9)]

        def reset():
            a = ['-' for x in range(9)]
        
        def printa(self):
            for i in range(1,6,3):
                for y in range(i,i+3):
                    print(self.a[y] , end = '')
        
        
test = tictacktoe()
test.printa()
        

    