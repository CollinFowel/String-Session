#!/usr/bin/env bash
# MusikVCG - Bot Music
# Copyright (C) 2021 MusikVCG
#
# This file is a part of < https://github.com/CollinFowel/MusikVcgV2/ >
#THANKYOU VERY MUCH TO @TeamUltroid

import os
from time import sleep

a = r"""
╔═╗╔═╗──────╔╗╔╗──╔╦═══╦═══╗
║║╚╝║║──────║║║╚╗╔╝║╔═╗║╔═╗║
║╔╗╔╗╠╗╔╦══╦╣║╠╗║║╔╣║─╚╣║─╚╝
║║║║║║║║║══╬╣╚╝╣╚╝║║║─╔╣║╔═╗
║║║║║║╚╝╠══║║╔╗╬╗╔╝║╚═╝║╚╩═║
╚╝╚╝╚╩══╩══╩╩╝╚╝╚╝─╚═══╩═══╝
"""


def spinner(x):
    if x == "tele":
        print("Mohon tunggu, memeriksa Telethon...")
    else:
        print("Mohon tunggu, memeriksa Pyrogram...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Nanti masukin nomor hp nya pake kode negara ya...\nContoh +6281234567890\n\n",
    )
    try:
        API_ID = int(input("Masukan API ID : "))
    except ValueError:
        print("Pastikan Anda memasukan APP ID/API HASH dgn benar tanpa spasi. \nKlik RUN ► di kiri atas untuk mengulangi...")
        exit(0)
    API_HASH = input("Masukan API HASH : ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner("tele")

        x = "\bSilahkan ambil dulu API ID & API HASH mu dari my.telegram.org\nkalo ga ngerti tanya @xxstanme di Telegram.\n\n"
    except BaseException:
        print("Menginstall Telethon...")
        os.system("pip install telethon")

        x = "\bBerhasil menginstall Telethon."
    clear_screen()
    print(a)
    print(x)

    # the imports

    from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as ultroid:
            print("Mohon tunggu sebentar...")
            ult = ultroid.send_message(
                "me",
                f"**MusikVCG** `SESSION`:\n\n`{ultroid.session.save()}`\n\n**Support @ChatBotXanon @xxstanme**",
            )
            print(
                "String Session mu telah dikirim ke Pesan Tersimpan silahkan cek!"
            )
            exit(0)
    except ApiIdInvalidError:
        print(
            "Kamu memasukan API ID/API HASH yg salah silahkan ulangi kembali \nKlik RUN ► di kiri atas untuk mengulangi..."
        )
        exit(0)
    except ValueError:
        print("API HASH tidak boleh kosong!\nKlik RUN ► di kiri atas untuk mengulangi...")
        exit(0)
    except PhoneNumberInvalidError:
        print("Nomor yg kamu masukan salah pastikan memasukan nomor diawali +62 bukan 0 dan tanpa garis - \nKlik RUN ► di kiri atas untuk mengulangi...")
        exit(0)


def pyro_session():
    try:
        spinner("pyro")
        from pyrogram import Client

        x = "\bSilahkan ambil dulu API ID & API HASH mu dari my.telegram.org\nkalo ga ngerti tanya @xxstanme di Telegram.\n\n"
    except BaseException:
        print("Menginstall Pyrogram...")
        os.system("pip install pyrogram tgcrypto")
        x = "\bBerhasil menginstall Pyrogram."
    clear_screen()
    print(a)
    print(x)

    # generate a session
    API_ID, API_HASH = get_api_id_and_hash()
    print("Tunggu sebentar, silahlan isi nomor telepon setalah diminta masukan nomor. \n\n")
    with Client(":memory:", api_id=API_ID, api_hash=API_HASH) as pyro:
        ss = pyro.export_session_string()
        pyro.send_message(
            "me",
            f"`{ss}`\n\nDiatas adalah Session String Pyrogram yg digunakan untuk membuat **MusikVCG** music bot.\n**Support @ChatBotXanon & @xxstanme**",
        )
        print("String Session mu telah dikirim ke Pesan Tersimpan silahkan cek!")
        exit(0)


def main():
    clear_screen()
    print(a)
    try:
        type_of_ss = int(
            input(
                "\nSilahkan pilih String Session mana yg kamu butuhin?\n1. Telethon (buat userbot).\n2. Pyrogram (buat bot musik).\n\nPilih nomor berapa :  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if type_of_ss == 1:
        telethon_session()
    elif type_of_ss == 2:
        pyro_session()
    else:
        print("Pilih 1 atau 2 aja goblok jgn ngetik yg lain.")
        x = input("Ulangi (y/n")
        if x == "y":
            main()
        else:
            exit(0)


main()