class Player:
    ID = 0
    Token = ""
    name = "Tara's clone"
    nameSet = 0
    trophies = 0
    ppp = 0
    v3 = 0
    xp = 0
    icon = 0
    color = 0
    brawler = 0
    skin = 0


    def __init__(self):
        pass

    def newData(self, id, token):
        self.ID = id
        self.Token = token
        
        Data = {
		"ID": self.ID, 
		"Token": self.Token, 
		"name": self.name, 
		"nameSet": self.nameSet, 
        "trophies": self.trophies,
        "ppp": self.ppp,
        "v3": self.v3,
        "xp": self.xp,
        "icon": self.icon,
        "color": self.color,
        "brawler": self.brawler,
        "skin": self.skin,
		}
        return Data