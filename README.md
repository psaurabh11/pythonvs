![VSImage](https://i0.wp.com/www.acelerartech.com/wp-content/uploads/2017/01/Reasons-to-use-a-virtual-assistant_chapt3.png)
# Virtual Assistant
It works same as `GoogleAssistant` or `Siri`. It can understand our voice,and accordingly execute commands.

## What thi VS can do?
- **Opens a web page** (e.g Hey Nemo or Hey Google --> then say open youtube)
- **Play a video in Youtube** (e.g 'Open youtube and Search CarryMinati')
- **Opens applications installed in your PC** (calc, writer, chrome, vlc) (e.g 'open google chrome')
- **Tells about something, by searching on the internet** (e.g 'Search about lincoln')
- **Tells the current time and/or date** (e.g 'tell me time or date')

## Getting Started
**Prerequisites**
- Python >= 3
- Firstly you need **PIP** to be installed to install other packages [How to install PIP](https://pip.pypa.io/en/stable/installing/).
- After that you need **Virtual Environment**<br />
`pip install virtualenv `
- You will need `Chrome Driver` to able to open pages. Firstly you need to check you Chrome Browser Version and download according to that [Chromium Driver](https://chromedriver.chromium.org/downloads).

**Individual packages listed as follows:**

- Speech Recognition<br />
`pip install SpeechRecognition`

- pyttsx3: (Offline Text to Speech Service)<br />
`pip install pyttsx3`

- selenium: (To open webpages)<br />
`pip install selenium`

- requests: (To request)<br />
`pip install requests`

- datetime: (To get system Date & Time)<br />
`pip install datetime`

- If any of the `Library` is getting error in installation you can download `.whl` for<br />
manual installation [Link](https://www.lfd.uci.edu/~gohlke/pythonlibs/). After downloading the file install it in the project directory
`pip install filename.whl`

## Installation

```sh
# Clone the repository (stable branch)
git clone https://github.com/psaurabh11/pythonvs.git

# Go to the project root
cd pythonvs

# Now we have to create Virtual Environment to Project Directory and venv named folder will be created in project directory.
virtualenv venv
 
# Activate Virtual Environment
venv/Scripts/activate

# Perform prerequisites
pip install -r requirements

# Run main.py
python main.py
```

## How to use

- First it will be Listening for the `Startup Command`, below are the startup commands
> ['activate','hey nemo','wake up','hey google','ok google']

- Then you can say `Some Tasks` like
> open google chrome,<br />
> What's the time,<br />
> close google chrome<br />
etc

- After each `Task` it will be listening for `Startup Command`

- For Exit or Shutdown you can say these `Closing Commands`
> ['shutdown','quit','exit','shutup']

- I have tried to make it as similar as other virtual assistants.

- You can add more functionalities

## Cheers!

