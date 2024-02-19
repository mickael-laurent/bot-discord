import discord
import os
from dotenv import load_dotenv
import asyncio

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Créer le client Discord
client = discord.Client(intents=discord.Intents.all())


# Événement de démarrage du bot
@client.event
async def on_ready():
    print(f'{client.user} a démarré')
    # Démarre la boucle d'envoi de messages toutes les 10 heures
    await send_loop()


# Fonction pour envoyer le message en boucle
async def send_loop():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel(VOTRE_ID_DE_CHANNEL)  # Remplacez VOTRE_ID_DE_CHANNEL par l'ID du canal où vous souhaitez envoyer les messages

        await channel.send("Ceci est un message en boucle.")
        # Répète toutes les 10 heures (36000 secondes)
        await asyncio.sleep(36000)


# Démarrer le bot

client.run(TOKEN)
