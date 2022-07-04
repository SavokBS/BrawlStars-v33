from ByteStream.Reader import Reader
from DB.DB import DB
import random, string
from Server.Home.OwnHomeData import OwnHomeData
from Server.Login.LoginOk import LoginOk
class Login(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readInt()
        self.ID = self.readInt()
        self.Token = self.readString()
        self.Major = self.readInt()
        self.Minor = self.readInt()
        self.Build = self.readInt()

    def process(self):
        db = DB()
        if self.Major != 33:
            pass
        else:
            if self.ID == 0:
                lettersAndDigits = string.ascii_letters + string.digits
                self.player.ID = int(''.join([str(random.randint(0, 10)) for _ in range(6)]))
                self.player.Token = ''.join(random.choice(lettersAndDigits) for i in range(40))
                db.createAccount(self.player.ID, self.player.Token, self.player.newData(self.player.ID, self.player.Token))
                LoginOk(self.client, self.player).send()
                OwnHomeData(self.client, self.player).send()
            else:
                user = db.loadAccount(self.player, str(self.Token))
                print(user)
                if user:
                    print("[DB] User found.")
                    LoginOk(self.client, self.player).send()
                    OwnHomeData(self.client, self.player).send()
                else:
                    print("[DB] Obama.")
                    db.createAccount(self.ID, self.Token, self.player.newData(self.ID, self.Token))
                    LoginOk(self.client, self.player).send()
                    OwnHomeData(self.client, self.player).send()



            print(f"[LOG IN] New Login! {self.ID} | {self.Token} | v{self.Major}.{self.Build}")