from ByteStream.Writer import Writer
from Files.CsvLogic.Cards import Cards


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        self.writeVInt(2021122)  # Timestamp (Year * 1000 + DayOfYear)
        self.writeVInt(75735)  # Second Timestamp
        self.writeVInt(self.player.trophies)  # Score
        self.writeVInt(self.player.trophies)  # Highest Score
        
        self.writeVInt(100)
        self.writeVInt(200)  # Trophy Road rewardnik
        self.writeVInt(5000)  # Exp
        
        self.writeDataReference(28, self.player.icon)  # Player Icon
        self.writeDataReference(43, self.player.color)  # Name Color
        
        self.writeVInt(0)  # Array
        self.writeVInt(1)
        for i in range(1):
            self.writeDataReference(29, self.player.skin)
        self.writeVInt(271)  # Array
        for i in range(271):
            self.writeDataReference(29, i)
        self.writeVint(0)

        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeByte(0)
        self.writeVInt(1000)
        self.writeVInt(10)
        self.writeVInt(20)
        self.writeVInt(30)
        
        #===sub_53AF00===#
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Array
        #================#
        
        self.writeByte(0)  # 3 Boolean
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVint(1)
        for i in range(1):

            self.writeVint(1)

            self.writeVint(10) # ItemID
            self.writeVint(6974) # Ammount
            self.writeScId(16, 0)
            self.writeVint(0)
            self.writeVint(0)  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(0)  # Cost
            self.writeVint(0) # Timer

            self.writeVint(1)
            self.writeVint(100)
            self.writeBoolean(False)  # is Offer Purchased

            self.writeBoolean(False)
            self.writeVint(1)  # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(False)
            self.writeVint(0)
            
            self.writeInt(0)
            self.writeString("svk")
            self.writeBoolean(False)
            self.writeString()
            self.writeVint(0)
            self.writeBoolean(False)
            self.writeVint(2)
            self.writeVint(0) # % Extra Text

        
        self.writeVInt(0)  # Array (v20)
        
        self.writeVInt(200)
        self.writeVInt(0)
        
        self.writeVInt(0)  # Array (v23)
        
        self.writeVInt(99999)
        self.writeVInt(0)
        
        self.writeDataReference(16, self.player.brawler)  # Selected Brawler
        
        self.writeString("RU")
        self.writeString("SaVok")  # content creator
        
        self.writeVInt(1)  # Array (v25)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeVInt(1)  # Array (v28)
        self.writeVInt(0)
        self.writeDataReference(16, 0)
        self.writeVInt(0)
        
        self.writeVInt(2)  # Array (v31) Season Data
        for i in [3, 4]:
            self.writeVInt(i)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(30)
            
            self.writeByte(2)
            for i in range(4):
                self.writeInt(0)
                
            self.writeByte(1)
            for i in range(4):
                self.writeInt(0)
        
        self.writeVInt(1)  # PowerPlay ig
        self.writeVInt(1) #Season
        self.writeVInt(6974) #Points
        
  
        
        self.writeByte(1)
        self.writeVInt(0)
        
        self.writeByte(1)
        self.writeVInt(0)
        
        
        # LogicClientHome CHUNK 2
        
        self.writeVInt(0)  # v4
        
        self.writeVInt(16)
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 21, 22, 23, 24]:
            self.writeVInt(x)
        
        self.writeVInt(1)  # Events
        #Event Start
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(15, 7)
        self.writeVInt(3)
        self.writeVInt(3)
        self.writeString("TID_WEEKEND_EVENT")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Array (v4) modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeByte(0)  #sub_5F0248
        self.writeVInt(0)
        #Event End
        
        self.writeVInt(0)  # Upcoming Events
        
        self.writeArrayVint([20, 35, 75, 140, 290, 480, 800, 1250])  # Array
        self.writeArrayVint([1, 2, 3, 4, 5, 10 ,15, 20])  # Array
        self.writeArrayVint([20, 50, 140, 280])  # Array
        self.writeArrayVint([150, 400, 1200, 2600])  # Array
        
        self.writeByte(0)
        
        self.writeVInt(0)  # Array (v18)
        
        self.writeVInt(1)  # Array (v21)
        self.writeInt(1)
        self.writeInt(41000000 + 21)
        
        self.writeVInt(0)  # Array (v24)
        
        self.writeVInt(0)  # Array (v27)
        
        self.writeByte(0)  # 2 boolean arrays
        
        self.writeInt(0)
        self.writeInt(1)
        
        self.writeVInt(0)  # v8 (Notification Factory)
        self.writeVInt(0)  # v9
        # Array for v8 Here (yes, under v9)
        
        self.writeByte(0)  # v10
        self.writeVInt(0)  # Array (v11)
        
        self.writeVInt(0)  # Array result
        
        # LogicClientAvatar
        
        self.writeVInt(0)
        self.writeVInt(self.player.ID)
        self.writeVInt(0)
        self.writeVInt(self.player.ID)
        self.writeVInt(0)
        self.writeVInt(self.player.ID)
        
        self.writeString(self.player.name)  # Name
        self.writeByte(self.player.nameSet) # NameSetByUser
        self.writeInt(0)
        
        self.writeVInt(8)  # Commodity Array Count
        cardosik = Cards.getBrawlersUnlockID()
        sps = Cards.getStarpowersID()
        print(sps)
        
        self.writeVInt(2 + len(cardosik))
        for i in cardosik:
            self.writeDataReference(23, i)
            self.writeVInt(1)
        self.writeDataReference(5, 8) #Coins
        self.writeVInt(100)
        
        self.writeDataReference(5, 10) #Starpoints
        self.writeVInt(0)
		
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0)
        
        self.writeVInt(45) #LVL
        for x in range(44):
            self.writeDataReference(16, x)
            self.writeVInt(8)
        self.writeDataReference(16, 44)
        self.writeVInt(8)
        self.writeVInt(len(sps)) #76, 135
        for i in sps:
            self.writeDataReference(23, i)
            self.writeVInt(1)
      #  self.writeVInt(0)
        
        self.writeVInt(0) #Gemz
        self.writeVInt(0) #Fre gemz
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(2)  # Tutorial State
        
        self.writeVInt(2)
	
	#охд негры своровали
