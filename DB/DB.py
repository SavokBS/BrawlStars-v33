import sqlite3
import json
import traceback

reason = traceback.format_exc()

class DB():
    def __init__(self):
        self.conn = sqlite3.connect("db.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (ID int, Token text, Data json)""")
        except:
            pass
        
    def createAccount(self, id, token, data):
        try:
            self.cursor.execute("INSERT INTO main (ID, Token, Data) VALUES (?, ?, ?)", (id, token, json.dumps(data, ensure_ascii=0)))
            self.conn.commit()
        except Exception:
            print(traceback.format_exc())
            
    def loadAccount(self, player, token):
        try:
            self.cursor.execute(f"SELECT * from main where Token=?", (str(token), ))
            this = json.loads(self.cursor.fetchall()[0][2])
            player.ID = this["ID"]
            player.Token = this["Token"]
            player.name = this["name"]
            player.nameSet = this["nameSet"]
            player.trophies = this["trophies"]
            player.ppp = this["ppp"]
            player.v3 = this["v3"]
            player.xp = this["xp"]
            player.icon = this["icon"]
            player.color = this["color"]
            player.brawler = this["brawler"]
            player.skin = this["skin"]
            return this
        except Exception:
            print(traceback.format_exc())
            
    def loadPlayer(self, id):
        try:
            self.cursor.execute(f"SELECT * FROM main WHERE ID={id}")
            this = json.loads(self.cursor.fetchall()[0][2])
            return this
        except Exception:
            print(traceback.format_exc())
            
    def loadAll(self):
        a = []
        self.cursor.execute("SELECT * FROM main")
        this = self.cursor.fetchall()
        for db in this:
            data = json.loads(db[2])
            a.append(data)
        return a
        
        
    def replaceValue(self, data, token):
        try:
            self.cursor.execute(f"UPDATE main SET Data=? WHERE Token=?", (json.dumps(data, ensure_ascii=0), token))
            self.conn.commit()
        except Exception:
            print(traceback.format_exc())
            
    def sortPlayers(self, value):
        result = self.loadAll()
        sorter = sorted(result, key=lambda x:x[value], reverse=True)
        return sorter
			
			