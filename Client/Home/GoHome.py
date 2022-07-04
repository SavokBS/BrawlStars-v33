from ByteStream.Reader import Reader
from Server.Home.OwnHomeData import OwnHomeData
class GoHome(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        OwnHomeData(self.client, self.player).send()