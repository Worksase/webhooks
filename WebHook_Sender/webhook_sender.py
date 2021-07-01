from discord_webhook import DiscordWebhook, DiscordEmbed
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



def join():
    pc_name = os.getenv("COMPUTERNAME")
    pc_username = os.getenv("UserName")


    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/857978328979603527/CY6Aofz_2TefZuUEB2PjMbPeEz9QLJ3UVhJtCirkPowfT6XKNr26hiAHq8ZVlrpw7bFC", username="Webhook-Sender")
    embed = DiscordEmbed(title="Webhook-Sender", description=f"Un utilisateur à utilisé Webhook-sender !", color="0f79f2")
    embed.set_footer(text="https://discord.gg/SaDR4jgKt6 | https://github.com/SleportV3/webhooks")
    embed.add_embed_field(name="Utilisateur", value=f" {pc_name} | {pc_username}")

    webhook.add_embed(embed)
    response = webhook.execute()

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
                                                                                                                      
                                       1 : Envoyer un message    2 : Envoyer des embeds 

                                       3: Crédit                                                                                                                                                                                                          
                                 ____________________________________________________________  

                                                https://discord.gg/UhTN3UT9H7                                                           

""")
print(mainbanner)
print(choix)

join()


user_answer = input('[>]Veuillez entrer votre réponse: ')

if user_answer == "1":

    webhook = input(Fore.YELLOW + "[>]Veuillez entrer le lien de votre webhook: ")
    message = input("[>]Veuillez entrer le message à envoyer: ")

    webhook = DiscordWebhook(url=webhook, content=message)
    response = webhook.execute()

    print("Le message " + Fore.RED + message + Fore.YELLOW +  " à bien été envoyé !")
    input("Pressez [ENTRER] pour quitter")

if user_answer == "2":    
    print(Fore.RED + "[Ne passez pas les étapes sauf le pseudo, le titre, un fix sera bientot donné pour passer la majorité de l'embed]")
    Webhook = input(Fore.YELLOW + "[>]Veuillez entrer le lien de votre webhook:")
    title = input("[>]Veuillez entrer le titre de l'embed: ")
    author = input("[>]Veuillez entrer le pseudo du webhook: ")
    description = input("[>]Veuillez entrer la description de l'embed: ")
    fieldname = input("[>]Veuillez entrer le nom du field de l'embed: ")
    field = input("[>]Veuillez entrer le texte du field de l'embed: ")
    footer = input("[>]Veuillez entrer le footer de l'embed: ")
    color = input("[>]Veuillez entrer la  couleur de l'embed: ")
    print(Fore.RED + "L'embed à bien été envoyé !")
    input("Pressez [ENTRER] pour quitter")


    webhook = DiscordWebhook(url=Webhook, username=author)
    embed = DiscordEmbed(title=title, description=description, color=color)
    embed.set_footer(text=footer)
    embed.add_embed_field(name=fieldname, value=field)

    webhook.add_embed(embed)
    response = webhook.execute()

if user_answer == "3":
    print(Fore.YELLOW + "https://discord.gg/UhTN3UT9H7")
    input("Pressez [ENTRER] pour retourner au menu")
