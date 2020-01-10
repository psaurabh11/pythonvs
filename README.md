# Virtual Assistant
It works same as `GoogleAssistant` or `Siri`. It can understand our voice,and accordingly execute commands.

## What thi VS can do?
- Opens a web page (e.g 'Hey Nemo or Hey Google --> then say open youtube')
- Play a video in Youtube (e.g 'Open youtube and Search CarryMinati')
- Opens applications installed in your PC (calc, writer, chrome, vlc) (e.g 'open google chrome')
- Tells about something, by searching on the internet (e.g 'Search about lincoln')
- Tells the current time and/or date (e.g 'tell me time or date')

## Getting Started
**Prerequisites**
- Python >= 3
Make sure you install these packages before moving forward to other python libraries.<br />
You can run `pip install -r requirements.txt` to install them all.

**Individual packages listed as follows:**

- Speech Recognition
`pip install SpeechRecognition`

- pyttsx3: (Offline Text to Speech Service)
`pip install pyttsx3`

- selenium: (To open webpages)
`pip install selenium`

- requests: (To request)
`pip install requests`

- datetime: (To get system Date & Time)
`pip install datetime`

- If any of the `Library` is getting error in installation you can download `.whl` for<br />
manual installation [Link](https://www.lfd.uci.edu/~gohlke/pythonlibs/).After downloading the file install it in the project directory
`pip install filename.whl`

## Installation
```
- Clone the repository (stable branch)
git clone https://github.com/psaurabh11/pythonvs.git

- Go to the project root
cd pythonvs

# Activate Virtual Environment
venv/Scripts/activate

# Perform prerequisites
pip install -r requirements

# Run main.py
python main.py
```

## How to use

First it will be Listening for the `Startup Command`, below are the startup commands
> ['activate','hey nemo','wake up','hey google','ok google']

Then you can say `Some Tasks` like
> open google chrome
> Whats the time
> close google chrome
etc

After each `Task` it will be listening for `Startup Command`
I have tried to make it as similar as other virtual assistants.

> You can add more functionalities

