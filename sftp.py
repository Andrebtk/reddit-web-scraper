import pysftp
import os


listFiles = os.listdir('/home/r3try/code/python/bot_meme/newMeme')

with pysftp.Connection('192.168.1.37', username='pi', password='azerty') as sftp:
    with sftp.cd('memeBot/bestMeme'):
        for i in listFiles:
            print("[!] Uploading...")
            sftp.put('/home/r3try/code/python/bot_meme/newMeme/'+i,'')
            sftp.listdir()
            print("[!] Deleting file...\n")
            os.remove("/home/r3try/code/python/bot_meme/newMeme/"+i)
            

