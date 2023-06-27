# Audio -> Text Converter

## Prepare to start

### Get a TOKEN for your telegram bot:
* Open link https://t.me/BotFather
* START a dialog
* Send `/newbot` command
* Enter the Bot name
* Enter the username for a new bot
* Save the TOKEN to `.env` file (use `.env_prod` file as a template)

### Install requirements
* Run `pip install -r requirements.txt`

### Install codecs
* Based on **[ffmpeg-normilizer requirements](https://pypi.org/project/ffmpeg-normalize/0.5.1/)** you must have [ffmpeg](http://ffmpeg.org/) installed in your $PATH (3.x or above recommended). Goto <http://ffmpeg.org/>, click "Download", choose your operation system, and click on build you want to install (for Windows I choose Windows builds by BtbN).
* In a new window click on ffmpeg-master-latest-win64-gpl.zip, download it, and extract 3 executable files to a `<venv>/Scripts` folder.