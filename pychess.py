import chess

board=chess.Board()

i=0

print(board)

while (i<100):

    a=input()

    try:

        board.push_san(a)

    except:

        print("An error accoured")

    print(board)

    b=input()

    try:

        board.push_san(b)

    except:

        print("An error accoured")

    print(board)

    i= i+1