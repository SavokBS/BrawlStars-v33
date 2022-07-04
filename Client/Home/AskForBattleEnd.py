from ByteStream.Reader import Reader
from Server.Home.BattleEnd import BattleEnd

class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.players = {}

    def decode(self):
        pass

    def process(self):
        

        BattleEnd(self.client, self.player).send()