import subprocess
import os
import base64
import random

print("<---------------->Guessing Time<------------------>")
inp = int(input("Enter a number: "))
ranport = random.randint(22,30)
replylist = ["Bad Luck User!! GO SLEEP IN YOUR MAMA's LAP!!" , "What the hell are you sitting here for!! Get off the chair NOW!!" , "HA HA HA HA HA HA HA!! LOOOOOOSSSSEEEEEERRRRRRRRR!!!"]
ranreply = replylist[random.randint(0,len(replylist)-1)]
if inp == ranport and ranport == 22:
    print("<--------------Printing the Keys--------------->")
    capout = subprocess.run(["cat", "/home/breacher/.ssh/id_rsa"] , capture_output=True , text = True)
    utfencode = str.encode(capout.stdout , "utf-8")
    b64encoded = base64.b64encode(utfencode)
    decoded = b64encoded.decode("utf-8")
    print(decoded)
else:
    print(ranreply)    
