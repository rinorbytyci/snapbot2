from argparse import ArgumentParser
from SnapWrap import Snapchat

class StorifierBot(Snapchat):
    def on_snap(self, sender, snap):
        print "New snap from: " + repr(sender)
        self.post_story(snap)

    def on_friend_add(self, friend):
        self.add_friend(friend)



parser = ArgumentParser("Storifier Bot")
parser.add_argument('-u', '--username', required=True, type=str, help="Username of the account to run the bot on")
parser.add_argument('-t', '--token', required=True, type=str, help="Password of the account to run the bot on")

args = parser.parse_args()

bot = StorifierBot(*[args.username, args.token])
bot.begin()
