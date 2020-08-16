import chess
import chess.svg


class UniBoard(chess.Board):
    def __init__(self, fen=chess.STARTING_FEN):
        super().__init__(fen)
        self.uni_save("w")

    def uni_save(self, mode="a"):
        with open("jogo.txt", mode) as fd:
            fd.write(self.fen() + "\n")

    def uni_load(self):
        try:
            with open("jogo.txt") as fd:
                lines = fd.readlines()
                if len(lines) > 0:
                    self = chess.Board(lines[-1])
        except FileNotFoundError:
            self.reset()
            self.uni_save("w")

    def uni_render(self):
        return chess.svg.board(board=self)

    def uni_move(self, uci):
        movement = chess.Move.from_uci(uci)
        if movement in self.legal_moves:
            self.push(movement)
            self.uni_save()
