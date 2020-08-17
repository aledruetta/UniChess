import chess
import chess.svg


class UniBoard(chess.Board):
    def __init__(self, board_id, fen=chess.STARTING_FEN):
        super().__init__(fen)
        self.id = board_id
        self.uni_load()

    def uni_save(self, uci=None, mode="a"):
        with open("jogo.txt", mode) as fd:
            if uci:
                fd.write(uci + "\n")

    def uni_load(self):
        try:
            with open("jogo.txt") as fd:
                for line in fd.readlines():
                    self.push_uci(line.strip())
        except FileNotFoundError:
            self.reset()
            self.uni_save(mode="w")

    def uni_render(self):
        return chess.svg.board(board=self)

    def uni_move(self, uci):
        movement = chess.Move.from_uci(uci)
        if movement in self.legal_moves:
            self.push(movement)
            self.uni_save(uci)
