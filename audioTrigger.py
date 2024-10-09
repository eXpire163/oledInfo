from mpd import MPDClient
from time import sleep

client = MPDClient()
client.connect("localhost", 6600)

while True:
  status = client.status().get("state")
  if status == "stop":
    print("no")
    sleep(0.8)
  else:
    print("open")
    sleep(0.8)
    print("close")
    sleep(0.8)
client.close()
client.disconnect()

# print(f"Current Volume: {status}")
