# oledInfo

the core setup was based on a pihole setup:

https://learn.adafruit.com/pi-hole-ad-blocker-with-pi-zero-w/install-pioled


additionally we have MPD (music player demon) installed

and configured 

sudo nano /etc/mpd.conf

to output to usb - alsa adapter and a fifo pipeline (test)

```

audio_output {
 type  "fifo"
 name  "my_fifo"
 path  "/tmp/mpd.fifo"
 enabled  "yes"
 format                  "44100:16:2"
}


audio_output {
        type            "alsa"
        name            "My ALSA Device"
        device          "hw:1,0"        # optional
        mixer_type      "software"      # optional
#       mixer_device    "default"       # optional
#       mixer_control   "PCM"           # optional
#       mixer_index     "0"             # optional
}

```


## current usecase

1. play halloween sounds via home automation
2. get status of mpd via audioTrigger.py
3. todo: move a servo in a sceleton mouth


## starup up stuff

(not sudo) crontab -e
-> the oled display is triggered every once in a while
`sudo systemctl enable mpd` installs mpd
`sudo systemctl start mpd` starts mpd
`sudo systemctl status mpd.service` status of service in errorcase





