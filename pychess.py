import chess


board=chess.Board()
i=0
print(board)

while (i<100):
    a=input()
    board.push_san(a)
    print(board)
    b=input()
    board.push_san(b)
    print(board)
    i= i+1