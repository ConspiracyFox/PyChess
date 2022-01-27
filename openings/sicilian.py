import chess
import time

board = chess.Board()

time.sleep(2.5)

board.push_san("e4")
print(board)
time.sleep(2.5)

print("\n")
board.push_san("c5")
print(board)
time.sleep(2.5)

print("\n")
board.push_san("Nf3")
print(board)
time.sleep(2.5)

print("\n")
board.push_san("d6")
print(board)
time.sleep(2.5)

print("\n")
board.push_san("d4")
print(board)
time.sleep(2.5)

print("\n")
board.push_san("c5xd4")
print(board)
time.sleep(2.5)

print("\n")
board.push_san("Nd4")
print(board)
time.sleep(2.5)

print("\n")
board.push_san("Nf6")
print(board)
time.sleep(2.5)

print("\n")
board.push_san("Nc3")
print(board)