import discord


TOKEN = 'YOUR TOKEN HERE'
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Energy-bot is now running!')



client.run(TOKEN)
