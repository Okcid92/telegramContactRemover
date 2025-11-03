import asyncio
import yaml
from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest, DeleteContactsRequest

# === Charger la config depuis config.yaml ===
with open("config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]
phone_number = config["telegram"]["phone_number"]

# === Le reste du code ===
async def main():
    async with TelegramClient('delete_contacts', api_id, api_hash) as client:
        await client.start(phone_number)
        print("🔍 Récupération des contacts...")

        result = await client(GetContactsRequest(hash=0))
        contacts = result.users

        print(f"📋 {len(contacts)} contact(s) trouvé(s).")
        if contacts:
            await client(DeleteContactsRequest(id=contacts))
            print("✅ Tous les contacts ont été supprimés avec succès !")
        else:
            print("😎 Aucun contact à supprimer.")

if __name__ == "__main__":
    asyncio.run(main())
