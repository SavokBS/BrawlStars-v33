from Client.Home.AskForBattleEnd import AskForBattleEndMessage
from Client.Home.ChangeAvatarName import ChangeAvatarName
from Client.Home.EndClientTurn import EndClientTurn
from Client.Home.GetPlayerProfile import GetPlayerProfile
from Client.Home.GoHome import GoHome
from Client.Home.KeepAlive import KeepAlive
from Client.Login.Login import Login
packets = {
    10101: Login,
    10108: KeepAlive,
    10212: ChangeAvatarName,
    14102: EndClientTurn,
    14113: GetPlayerProfile,
    14109: GoHome,
    14110: AskForBattleEndMessage,

    }