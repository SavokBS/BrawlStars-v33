from ByteStream.Reader import Reader
from DB.DB import DB
from Server.Home.ChangeAvatarNameResponce import ChangeAvatarNameResponce
from Server.Home.PlayerProfile import PlayerProfile
class GetPlayerProfile(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readInt()
        self.plrid = self.readInt()

    def process(self):
        PlayerProfile(self.client, self.player, self.plrid).send()