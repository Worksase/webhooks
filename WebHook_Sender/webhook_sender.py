from discord_webhook import DiscordWebhook
import discord
from discord.ext import commands
import os
import colorama
from os import name, system, getenv
from colorama import Fore, init


if name == "nt":
    system("title Webhook_sender")
    def clear():
        system("cls")
else:
    def clear():
        system("clear")

mainbanner = (Fore.RED + """

                                 ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
                                 ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
                                 ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
                                 ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
                                 ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
                                  ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
""") 
choix = (Fore.GREEN + """
                                 ____________________________________________________________
                                                                                                                      
                                            1 : Envoyer un message    2 : Crédit                                                                                                                                                                                                           
                                 ____________________________________________________________  

                                                https://discord.gg/SaDR4jgKt6                                                            

""")
print(mainbanner)
print(choix)

user_answer = input('[>]Veuillez entrer votre réponse: ')

if user_answer == "1":

    webhook = input(Fore.YELLOW + "[>]Veuillez entrer le lien de votre webhook: ")
    message = input("[>]Veuillez entrer le message à envoyer: ")

    webhook = DiscordWebhook(url=webhook, content=message)
    response = webhook.execute()

    print("Le message " + Fore.RED + message + Fore.YELLOW +  " à bien été envoyé !")
    input("Pressez [ENTRER] pour retourner au menu")

if user_answer == "2":
    print(Fore.YELLOW + "https://discord.gg/SaDR4jgKt6")

    input("Pressez [ENTRER] pour retourner au menu")















    
