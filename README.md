<p align="center"><img src="https://raw.githubusercontent.com/likeadragonmaid/Ongaku/main/ongaku/resources/images/logos/ongaku-logo_github.png"></p>
A **smol and fluffy** bot to update your telegram bio with music playing around you (Pixel) or on your android phone in real time!

### Requirements
* An android device capable of running Termux
* A music player app capable of showing notifications of current music being played
* Optionally a Google Pixel device if you want to detect Music playing around you.
### Getting started

* Install [Termux](https://f-droid.org/en/packages/com.termux/) and [Termux:API](https://f-droid.org/en/packages/com.termux.api/) apps from F-Droid.
* Launch Termux and run the following command

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/anonymousx97/Ongaku/main/scripts/installation.sh)"
```

> Optionally you can also add neofetch support by running

```
apt install -y neofetch python-pillow
```

* When you run the installation command you are asked to enter your phone number to create a session. Ongaku uses this session to work with your telegram account.

* You can get `API_ID` and `API_HASH` from [here](https://my.telegram.org/).

* By default Ongaku automatically checks for commonly used [music players](https://github.com/anonymousx97/Ongaku/blob/360830eb5532c2525d4d2b61039df73d707ec2ae/ongaku/extra_config.py#L58). But if you want to only check for a specific app or your music player isn't covered in default players, you can use this [app](https://f-droid.org/en/packages/com.oF2pks.applicationsinfo/) to check package name of your music player app and add it to `MUSIC_PLAYER` value.

* If you want to detect Music playing around you (pixel devices only) uncomment `PREFER_NOW_PLAYING_PIXEL_MODE` and set it to 1. If enabled it will override all other Music Players.

* You will be asked to provide notification access to Termux:API app. You must provide Termux:API app all the required permissions. You may be required to do `Ctrl+C` to continue.
> On A13 and above you might need to allow restricted setting permission to the api before allowing notification access.
> Open termux-api's app info settings and allow restricted settings from the 3 dot menu on top right.

* Run `ong` from any directory to start Ongaku.

* If everything went well you should be up and running. At this point you can start playing music and you should see current playing song in the Termux app and your telegram bio.

### Tips

* Ongaku may stop detecting notifications and responding to commands if you `RELEASE WAKELOCK` while it is running! It handles android wakelocks automatically.


### Known Limitations

* Ongaku cannot yet differentiate between the states of music player itself i.e. `Playing`, `Paused` and `Stopped`. It simply assumes existing music player notification as a `Playing` state.
* It is not yet possible to run Ongaku on a baremetal server or a VPS/PaaS such as Heroku.
* Devices running MIUI are unsupported as Xiaomi loves to corrupt notification permission after X amount of hours and even at each device reboot. However you can still use Ongaku if you are willing to provide notification access manually by uninstalling Termux:API app, reinstalling it again, running `termux-notification-list` and lastly doing `Ctrl + C` each time Ongaku starts malfunctioning! This is something you can also fix by running a reputable custom rom such as [LineageOS](https://lineageos.org/). (**#RipBozo** 💯🤣🤣 if you choose to run MIUI on your phone anyway)

### Optional commands
Send in any DM or Group chat

`.about` to view info about the project.

`.history` to get list of music played in current session.

`.sync` to force sync bio with latest notification.

`.nf` to get environment's neofetch information in GIF format (not actual mp4 video with no audio scam format).

`.nf -t` to get environment information in text format.

### Authors
* [Shoko](https://github.com/likeadragonmaid)
* [Ryuk](https://github.com/anonymousx97)
* [Meliodas](https://github.com/thedragonsinn)

### Disclaimer

This project is provided as is without any warranty. Telegram may `ban` your account for using Ongaku if your account is only `6 months old` or for any other reason but it MAY be recovered as well if you explain your situtaion by writing to them at `recover@telegram.org`. The authors take no responsibilty of your device or your Telegram acount!
