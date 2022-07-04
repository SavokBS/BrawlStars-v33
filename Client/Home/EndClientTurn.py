from ByteStream.Reader import Reader
from DB.DB import DB
from Server.Home.Box import Box
class EndClientTurn(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        for i in range(3):
            self.readVInt()
        self.tickCheck = self.readVInt()
        self.commandID = self.readVInt()

    def process(self):
        if self.commandID >= 0:
            print(f"[ECT] New command: {self.commandID}")
        
        db = DB()
        user = db.loadPlayer(self.player.ID)

        def base(num=5):
            for i in range(num):
                self.readVInt()

        if self.commandID == 505:
            base()
            self.player.icon = self.readVInt()
            print(self.player.icon)
            user["icon"] = self.player.icon
            db.replaceValue(user, self.player.Token)
        elif self.commandID == 527:
            base()
            self.player.color = self.readVInt()
            user["color"] = self.player.color
            print(self.player.color)
            db.replaceValue(user, self.player.Token)
        elif self.commandID == 506:
            base()
            self.player.skin = self.readVInt()
            base(6)
            self.player.brawler = self.readVInt()
            user["skin"] = self.player.skin
            user["brawler"] = self.player.brawler
            print(f"[ECT] Brawler and skin selected: {self.player.brawler}:{self.player.skin}")
            db.replaceValue(user, self.player.Token)        
        elif self.commandID == 517:
            Box(self.client, self.player).send()