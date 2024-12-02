import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer le token depuis les variables d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")

# Initialisation du bot avec les intents
intents = discord.Intents.default()
intents.messages = True  # Permet d'écouter les messages (ou ajuste les intents selon tes besoins)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est maintenant en ligne !")

# Démarrage du bot
bot.run(TOKEN)
