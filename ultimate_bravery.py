from dotenv import load_dotenv
import os
import discord
import random

class UltimateBravery:
    def __init__(self):
        load_dotenv()
        self.discord_token = self.get_token()
        self.guild_id = self.get_guild()
        self.setup_client()
    
    def get_token(self):
        discord_token = os.getenv("DISCORD_TOKEN")
        if not discord_token:
            raise RuntimeError("Set DISCORD_TOKEN in .env file")
        return discord_token
    
    def get_guild(self):
        guild = os.getenv("DISCORD_GUILD")
        if not guild:
            raise RuntimeError("Set DISCORD_GUILD in .env file")
        return guild
    
    def setup_client(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        self.client = discord.Client(intents=intents)
        self.client.event(self.on_ready)
        self.client.event(self.on_message)

                
    def get_perks(self):
        killer_perks = []
        survivor_perks = []

        with open ("killer.txt", "r") as file:
            for line in file:
                    clean_line = line.strip("\n")
                    killer_perks.append(clean_line)

        with open ("survivor.txt", "r") as file:
            for line in file:
                    clean_line = line.strip("\n")
                    survivor_perks.append(clean_line)

        message = ""

        for i in range(1, 5):
            message += f"**Survivor {i}:**\n"
            perks = random.sample(survivor_perks, 4)
            message += f"  • {perks[0]}\n"
            message += f"  • {perks[1]}\n"
            message += f"  • {perks[2]}\n"
            message += f"  • {perks[3]}\n\n"

        message += f"**Killer: **\n"
        k_perks = random.sample(killer_perks, 4)
        message += f"  • {k_perks[0]}\n"
        message += f"  • {k_perks[1]}\n"
        message += f"  • {k_perks[2]}\n"
        message += f"  • {k_perks[3]}\n\n"

        items = ["Medkit", "Flashlight", "Firecracker", "Keys", "Maps", "Toolboxes", "Fog Vials"]
        banned_item = random.choice(items)

        message += f"**Banned Item:**\n"
        message += f"  • {banned_item}"

        return message

    async def on_ready(self):
        guild = self.client.get_guild(int(self.guild_id))

        if guild:
            print(f"{self.client.user} has connected to {guild.name} id: {guild.id}")
        else:
            print(f"Could not connect to guild {self.guild_id}")
    
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith('!DBD') or message.content.startswith('!dbd'):
                try:
                    await message.channel.send(self.get_perks())
                except Exception as e:
                    await message.channel.send(f"Failed to Generate Perks. {e}")

    def run(self):
        try:
            self.client.run(self.discord_token)
        except discord.LoginFailure:
            print("Failed to login: Invalid token")
        except Exception as e:
            print(f"Connection failed: {e}")