import os
from sense_hat import SenseHats

hostname = "wdelenclos.fr"

while True:
response = os.system("ping -c 1 " + hostname)
sense.load_image("hello.png")

    if response == 0:
      print hostname, 'is up!'
      sense.load_image("done.png")
    else:
      print hostname, 'is down!'
      sense.load_image("erreur.png")

    print "... prochaine verification dans 60s  \n "
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))