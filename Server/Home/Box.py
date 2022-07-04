from ByteStream.Writer import Writer
from random import randint as r

class Box(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVInt(203)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(11)
        
        self.writeVInt(2)

        self.writeVInt(r(100, 500))
        self.writeScId(16, 0)
        self.writeVInt(7)
        self.writeVInt(0) #29
        self.writeVInt(0) #52
        self.writeVInt(0) #23
        self.writeVInt(0)


        
        
        self.writeVInt(1)
        self.writeScId(16, r(1, 44))
        self.writeVInt(1)
        self.writeVInt(0) #29
        self.writeVInt(0) #52
        self.writeVInt(0) #23
        self.writeVInt(0)
        
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeLogicLong(68)
