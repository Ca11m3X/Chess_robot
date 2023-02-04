# from interbotix_xs_modules.arm import InterbotixManipulatorXS
import chess
import chess.engine
import asyncio


def abc():
    import AtoB


async def main() -> None:

    transport, engine = await chess.engine.popen_uci(r'/home/drx/Chess_robot/chess_engine/stockfish_15_linux_x64/stockfish_15_src/src/stockfish')

    board = chess.Board()
    while not board.is_game_over():
        result = await engine.play(board, chess.engine.Limit(time=0.1))
        board.push(result.move)
        abc()
        print(board)

    a = board.outcome()
    print(a.winner)
    await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())
