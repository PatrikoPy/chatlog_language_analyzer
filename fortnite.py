import fortnitepy
import csv


class MyClient(fortnitepy.Client):
    def __init__(self):
        super().__init__(
            email='chatka_na_marsie@gmail.com',
            password='Sh1',
            net_cl='8371783'
        )

    async def event_ready(self):
        print('----------------')
        print('Client ready as')
        print(self.user.display_name)
        print(self.user.id)
        print('----------------')

    async def event_friend_request(self, request):
        await request.accept()

    async def event_party_invite(self, invitation):
        await invitation.accept()

    async def event_friend_message(self, message):
        print(f'Received message from {message.author.display_name} | Content: "{message.content}"')
        # await message.reply('Thanks for your message!')

        with open('FortniteLog.tsv', 'a', newline='') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            tsv_writer.writerow([str(message.created_at), message.author.display_name, message.content, 'whisper'])

    async def event_party_message(self, message):
        print(f'Received message from {message.author.display_name} | Content: "{message.content}"')
        # await message.reply('Thanks for your message!')

        with open('FortniteLog.tsv', 'a', newline='') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            tsv_writer.writerow([str(message.created_at), message.author.display_name, message.content, 'party'])


client = MyClient()
client.run()
