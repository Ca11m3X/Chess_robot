# from time import sleep
import chess
import chess.engine

# Nap engine:
engine = chess.engine.SimpleEngine.popen_uci(
    r'/home/drx/Chess_robot/chess_engine/stockfish_15_linux_x64/stockfish_15_src/src/stockfish')

engine.configure({'Skill Level': 20})


# Khai bao:
board = chess.Board()
grave = 1


def abc(move, grave, capture=False):
    import AtoB

    A, B = move[:2], move[2:4]

    if capture:
        AtoB.AtoB_capture(A, B, grave)
        print("Capture")
    else:
        AtoB.AtoB(A, B)


# Choi:
while not board.is_game_over():

    user_input = input("Nhap nuoc di: ")
    if user_input == "exit":
        break
    move = chess.Move.from_uci(user_input)

    while not move in board.legal_moves:
        move = chess.Move.from_uci(input("Nhap nuoc di: "))

    board.push(move)
    print(board)
    print('*'*100)

    capture = False

    result = engine.play(board, chess.engine.Limit(time=0.1))
    if board.is_capture(result.move):
        grave += 1
        capture = True
    board.push(result.move)
    move = str(result.move)
    abc(move, grave, capture)
    # sleep(5)
    print(board)
    print('*'*100)

a = board.outcome()

engine.quit()
print("End")
