board={'1':'-','2':'-','3':'-',
       '4':'-','5':'-','6':'-',
       '7':'-','8':'-','9':'-',}
def printboard():
    print(board['1']+" | "+board['2']+" | "+board['3'])
    print("__________")
    print(board['4']+" | "+board['5']+" | "+board['6'])
    print("__________")
    print(board['7']+" | "+board['8']+" | "+board['9'])
    print()

turn='x'
i=1
while i<10:
    printboard()
    print("its "+turn+" turn enter a location")
    ch=input()
    if board[ch]=='-':
        board[ch]=turn
    else:
        print("Wrong position please re enter")
        continue

    i=i+1
    if i>5:
        if board['1'] == board['2'] == board['3'] != '-': 
            printboard()
            print("\nThe end .\n")                
            print(" **** " +turn + " is the winner ****")                
            break
        elif board['4'] == board['5'] == board['6'] != '-': 
            printboard()
            print("\nThe end .\n")                
            print(" **** " +turn + " is the winner ****")
            break
        elif board['7'] == board['8'] == board['9'] != '-': 
            printboard()
            print("\nThe end .\n")                
            print(" **** " +turn + " is the winner ****")
            break
        elif board['1'] == board['4'] == board['7'] != '-':
            printboard()
            print("\nThe end .\n")                
            print(" **** " +turn + " is the winner ****")
            break
        elif board['2'] == board['5'] == board['8'] != '-': 
            printboard()
            print("\nThe end .\n")                
            print(" **** " +turn + " is the winner ****")
            break
        elif board['3'] == board['6'] == board['9'] != '-':
            printboard()
            print("\nThe end .\n")                
            print(" **** " +turn + " is the winner ****")
            break 
        elif board['7'] == board['5'] == board['3'] != '-': 
            printboard()
            print("\nThe end .\n")                
            print(" **** " +turn + " is the winner ****")
            break
        elif board['1'] == board['5'] == board['9'] != '-':
            printboard()
            print("\nThe end .\n")                
            print(" **** " +turn + " is the winner ****")
            break 
    if turn=='x':
        turn='o'
    else:
        turn='x'
    if i==9:
        print("\nIts a tie \n")