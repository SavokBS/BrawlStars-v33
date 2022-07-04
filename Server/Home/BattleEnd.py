from ByteStream.Writer import Writer
import random


class BattleEnd(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player  = player
    def encode(self):
        self.writeLong(self.player.ID)
        self.writeLong(self.player.ID)

        self.writeVInt(1)

        self.writeVInt(0)

        self.writeVint(100)
        self.writeVint(1250)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)


        self.writeBoolean(False)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(32)
        self.writeBoolean(False)

        self.writeVInt(1)

        self.writeByte(1)
        self.writeDataReference(16, 0)
        self.writeDataReference(29, 0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBool(True)
        self.writeLong(self.player.ID)

        self.writeString(self.player.name)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(-1)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeDataReference(28, 0)

        self.writeBool(False)
        self.writeBool(False)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBool(False)

