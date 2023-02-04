import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci(
    r'/home/drx/Chess_robot/chess_engine/stockfish_15_linux_x64/stockfish_15_src/src/stockfish')

engine.configure({'Skill Level': 20})

board = chess.Board()
print(board)

while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)

a = board.outcome()

print(a.winner)

engine.quit()
# while not board.is_game_over():
    # move = chess.Move.from_uci(input("Nhap nuoc di: "))

    # while not move in board.legal_moves:
    #     move = chess.Move.from_uci(input("Nhap nuoc di: "))

    # board.push(move)
    # print(board)
    # print('*'*10)

#     result = engine.play(board, chess.engine.Limit(time=0.1))

#     if board.is_capture(result.move):
#         print("Is capture, mother fuker")
#     if board.is_castling(result.move):
#         print("CASTLING, bitch!!!")

    # move = str(result.move)
    # A, B = move[:2], move[2:4]

#     print("Move of may uci: " + move)
#     print('Machine:' + A + '....' + B)

#     board.push(result.move)
#     print(board)




# print(engine.options.items())
# engine.configure(options=)
# print(engine.options['Skill Level'])
# engine.configure({"Skill Level": 7})


# print(engine.options.items())

# print(type(result.move))


