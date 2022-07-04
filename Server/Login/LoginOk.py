from ByteStream.Writer import Writer


class LoginOk(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104

    def encode(self):
        self.writeInt(0) #high
        self.writeInt(self.player.ID) #low
        
        self.writeInt(0) #high
        self.writeInt(self.player.ID) #low

        self.writeString(self.player.Token)
        self.writeString()
        self.writeString()

        self.writeInt(33)
        self.writeInt(96)
        self.writeInt(1)

        self.writeString("dev")

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString()
        self.writeString()
        self.writeString()

        self.writeInt(0)

        self.writeString()
        self.writeString("RU")
        self.writeString()

        self.writeInt(1)
        self.writeString()

        self.writeInt(2)
        self.writeString()
        self.writeString()

        self.writeInt(1)
        self.writeString()