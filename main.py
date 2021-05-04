"""Ambil String Session mu disini setelah itu,

String Session akan dikirim ke Saved Messages atau Pesan Tersimpan pada akun Telegram mu,

requirements:

- Pyrogram

- TgCrypto

Ambil Api Key & Api Hash mu di :

https://my.telegram.org/apps

"""

import asyncio

from pyrogram import Client

async def main():

    api_id = int(input("API ID: "))

    api_hash = input("API HASH: ")

    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:

        await app.send_message(

            "me",

            "**Pyrogram Session String**:\n\n"

            f"`{await app.export_session_string()}`"

        )

        print(

            "String Session mu udah dikirim otomatis ke"

            "Pesan Tersimpan atau Saved Messages akun telegram silahkan cek"

        )

if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())
