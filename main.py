import discord


TOKEN = 'MTA2MzU4MDM2NzIxNjQ0NzUxOA.G0ABEa.QaFD8FJSKO_0O3kqhoHeUHAXjUACjXMFVw0Q4U'
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Energy-bot is now running!')



client.run(TOKEN)