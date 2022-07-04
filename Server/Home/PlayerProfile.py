from ByteStream.Writer import Writer
from DB.DB import DB
import random

class PlayerProfile(Writer):
    def __init__(self, client, player, id):
        super().__init__(client)
        self.player = player
        self.id = 24113
        self.plrid = id
        
    def encode(self):
        db = DB()
        data = db.loadPlayer(self.plrid)
        self.writeVInt(0)
        self.writeVInt(self.plrid)
        self.writeBoolean(False)
        self.writeVInt(len([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])) #Brawlers
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]:
            self.writeScId(16, i)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(9)
                
                
        self.writeVInt(15)
        
        self.writeVInt(1)
        self.writeVInt(data["v3"]) #3vs3 wins
        
        self.writeVInt(2)
        self.writeVInt(data["xp"]) #X
        
        self.writeVInt(3)
        self.writeVInt(data["trophies"]) #HighestTrophies
        
        self.writeVInt(4)
        self.writeVInt(data["trophies"]) #Trophies
        
        self.writeVInt(5)
        self.writeVInt(len([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])) #Brawlers list
        
        self.writeVInt(7)
        self.writeVInt(28000000 + data["icon"]) #ProfileIcon
        
        self.writeVInt(8)
        self.writeVInt(0) #SoloWins
        
        self.writeVInt(9)
        self.writeVInt(0) #Roborumble LVL
        
        self.writeVInt(11)
        self.writeVInt(0) #DuoWins
        
        self.writeVInt(12)   
        self.writeVInt(0) #BossFight LVL
        
        self.writeVint(13)
        self.writeVint(0) # Highest power player points 
        
        self.writeVint(14)
        self.writeVint(0) # Highest power play rank
        
        self.writeVInt(15)
        self.writeVInt(0) #Most chalenges wins
        
        self.writeVInt(16)
        self.writeVInt(0) #CityFight LVL
        
        self.writeVInt(19)
        self.writeVInt(0) #Highest Club League
        
        self.writeString(data["name"])
        self.writeVInt(0)
        self.writeVInt(28000000 + data["icon"])
        self.writeVInt(43000000 + data["color"])
        self.writeVInt(0) #Gradients
        self.writeBoolean(False)  # Is in club
		
		#self.writeInt(0)
#		self.writeInt(1) #Club ID
#		
#		self.writeString(f"<c3200ff>V<c6500ff>o<c9800ff>k<ccb00ff>e<cff00ff>s<cff00cc>B<cff0099>r<cff0066>a<cff0033>w<cff0001>l</c>")  # club name
#		self.writeVInt(8)
#		self.writeVInt(18)  # Club badgeID
#		self.writeVInt(3)  # club type | 1 = Open, 2 = invite only, 3 = closed
#		self.writeVInt(1)  # Current members count
#		self.writeVInt(0) #Club Trophies
#		self.writeVInt(0)  # Trophy required
#		self.writeVInt(0)  # (Unknown)
#		self.writeString("RU")  # region
#		self.writeVInt(0)  # (Unknown)
#		self.writeVInt(0) # (Unknown)
#		self.writeVInt(25)
#		self.writeVInt(2)
		