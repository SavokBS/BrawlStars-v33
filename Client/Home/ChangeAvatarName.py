from ByteStream.Reader import Reader
from DB.DB import DB
from Server.Home.ChangeAvatarNameResponce import ChangeAvatarNameResponce
class ChangeAvatarName(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.Name = self.readString()

    def process(self):
        db = DB()
        user = db.loadPlayer(self.player.ID)
        user["name"] = self.Name
        user["nameSet"] = 1
        self.player.name = self.Name
        db.replaceValue(user, self.player.Token)
        ChangeAvatarNameResponce(self.client, self.player).send()