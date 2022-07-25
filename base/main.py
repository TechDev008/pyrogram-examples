# Cosas necesarias de pyrogram, y cosas que a lo mejor no usaremos pero lo puse por que quise asi de facil
from pyrogram import Client, types, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ChatPermissions
# Importamos el archivo de configuracion donde tengo el token del bot el api_id y api_hash, si no quieres usarlo te la mamas
from cfg import*
# ESTOY USANDO UNA DISTRO NUEVA PERDON POR LAS FALTAS DE ORTOGRAFIA ES QUE NO SE SACAR TILDE XD


# Funcion principal de nuestro codigo
def main():

    print('\nPreparando Bot...\n') # Mensajito to chulo en consola de que el bot se esta preparando para iniciar

    # Aca ponemos los datos de nuestro bot en mi caso lo tengo en variables desde el archivo cfg.py
    bot = Client("example",api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

    # Nuestros comandos estaran todos en esta funcion, tu sae python funciona mejor en una sola funcion
    @bot.on_message()
    async def process(bot: Client, app: Message): # Estoy encerrando el Client dentro de la variable bot y el Message dentro de la variable app asi que no comas mierda y mira bien lo que haces

        user_id = app.from_user.id # Obtenemos el user_id del usuario

        chat_id = app.chat.id # Obtenemos el id del chat donde se recojar


        # Nuestro primer comando va a ser /start 
        if text.lower().startswith('/start'):

            # En este ejemplo estamos haciendo que el bot mande el mensaje al chat, ya sea en un grupo o en privado
            await app.reply(f'Hola 👋, unete a mi canal [@arKrozzDev](https://t.me/arKrozzDev)') 
        
        # Nuestro segundo comando va a ser /link
        elif text.lower().startswith('/link'):

            # En este ejemplo estamos haciendo que el bot le mande el mensjae directamente al privado al id del usuario que se le pase
            # Si estamos en un grupo el bot mandara el mensaje al privado del usuario
            # El usuario ya tendria que haber iniciado el bot en privado o el mensaje no llegara
            await bot.send_message(user_id, 'Este es el enlace de mi canal prro, unete: https://t.me/arKrozzDev')
            # Como pueden ver estamos usando la variable bot para mandar el mensaje, esta variable contiene del Client dentro
            # Se usa para enviar archivos, descargarlos, etcetera, esto lo veremos mas adelante



    # Aca es lo que hace que el bot funcione
    bot.start() # Decimos que inicie
    print("Iniciado") # Mensajito to chulo para que diga que ya se inicio el bot
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop_policy().get_event_loop() #etc
    loop.run_forever() #etc

if __name__ == '__main__':
    main()

# FIN del ejemplo...