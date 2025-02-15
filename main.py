import discord
import os

# Cargar variables de entorno
TOKEN = os.getenv("DISCORD_TOKEN")
WHATSAPP_LINK = os.getenv("WHATSAPP_LINK")

# Configurar intents del bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Crear el cliente del bot
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Responder con el link de WhatsApp
    await message.channel.send(f'Únete a nuestro grupo de WhatsApp: [NovaGuard]({WHATSAPP_LINK})')

# Iniciar el bot
client.run(TOKEN)
