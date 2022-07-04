from csv import writer


from ByteStream.Writer import Writer
class ChangeAvatarNameResponce(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVInt(201)
        self.writeString(self.player.name)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(-1)
        self.writeVInt(0)
        self.writeVInt(0)