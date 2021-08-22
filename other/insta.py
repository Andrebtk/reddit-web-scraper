from instagram_private_api import Client, ClientCompatPatch

username = "pc_master_meme"
password = "665544Ab_"

hastag = "#pc #pcbuild #pcgaming #pcgamers #pcmods #pccase #pccases #pccasemods #custompccase #pcrig #pcrigs #pcgamingrig #pcgaming #pcmasterrace #pcgamer #pcgamers #pcgamerlife #gamingpcparts #pcparts #nvidia #graphicscards #graphicscard #pcgamingmemes #pcmemes #pcgamer #pcgamerlife #pcgameing #pcgamers #gaming #gamingsetup #gamingsetups #pcgaming101 #gaminglife #amd #corsair"
namefile = "*Laughs_in_Arctic*.png"
imageSRC = "test.png"


api = Client(username, password)
results = api.feed_timeline()
items = [item for item in results.get('feed_items', [])
         if item.get('media_or_ad')]
for item in items:
    # Manually patch the entity to match the public api as closely as possible, optional
    # To automatically patch entities, initialise the Client with auto_patch=True
    ClientCompatPatch.media(item['media_or_ad'])
    print(item['media_or_ad']['code'])


