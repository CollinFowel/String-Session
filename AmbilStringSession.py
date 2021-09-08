#!/bin/bash
# MusikVCG - Bot Music
# Copyright (C) 2021 MusikVCG
#
# This file is a part of < https://github.com/CollinFowel/MusikVcgV2/ >
#THANKYOU VERY MUCH TO @TeamUltroid

import os
from time import sleep

# https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
if os.name == "posix":
    _ = os.system("clear")
else:
    # for windows platfrom
    _ = os.system("cls")

a = r"""
╔═╗╔═╗──────╔╗╔╗──╔╦═══╦═══╗
║║╚╝║║──────║║║╚╗╔╝║╔═╗║╔═╗║
║╔╗╔╗╠╗╔╦══╦╣║╠╗║║╔╣║─╚╣║─╚╝
║║║║║║║║║══╬╣╚╝╣╚╝║║║─╔╣║╔═╗
║║║║║║╚╝╠══║║╔╗╬╗╔╝║╚═╝║╚╩═║
╚╝╚╝╚╩══╩══╩╩╝╚╝╚╝─╚═══╩═══╝
"""

print(a)
try:
    print("Mohon tunggu, memeriksa Telethon...")

    for x in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)
    import telethon

    x = "\bNanti masukin nomor hp nya pake kode negara ya...\nContoh +6281234567890\n\n"
except BaseException:
    print("Menginstall Telethon...")
    os.system("pip install telethon")

    x = "\bBerhasil menginstall Telethon."
if os.name == "posix":
    _ = os.system("clear")
else:
    # for windows platfrom
    _ = os.system("cls")
print(a)
print(x)

# the imports

from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    "Silahkan ambil dulu API ID & API HASH mu dari my.telegram.org atau kalo ga ngerti tanya @xxstanme di Telegram.\n\n",
)

try:
    API_ID = int(input("Masukan API ID : "))
except ValueError:
    print("Pastikan Anda memasukan APP ID/API HASH dgn benar tanpa spasi. \nKlik RUN ► di kiri atas untuk mengulangi...")
    exit(0)
API_HASH = input("Masukan API HASH : ")

# logging in
try:
    with TelegramClient(StringSession(), API_ID, API_HASH) as ultroid:
        print("Mohon tunggu sebentar...")
        ult = ultroid.send_message(
            "me",
            f"**MusikVCG** `SESSION`:\n\n`{ultroid.session.save()}`\n\n**Support @ChatBotXanon @xxstanme**",
        )
        print("String Session mu telah dikirim ke Pesan Tersimpan silahkan cek!")
        exit(0)
except ApiIdInvalidError:
    print("Kamu memasukan API ID/API HASH yg salah silahkan ulangi kembali \nKlik RUN ► di kiri atas untuk mengulangi...")
    exit(0)
except ValueError:
    print("API HASH tidak boleh kosong!\nKlik RUN ► di kiri atas untuk mengulangi...")
    exit(0)
except PhoneNumberInvalidError:
    print("Nomor yg kamu masukan salah pastikan memasukan nomor diawali +62 bukan 0 dan tanpa garis - \nKlik RUN ► di kiri atas untuk mengulangi...")
    exit(0)
