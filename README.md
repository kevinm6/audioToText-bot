<p align="center">
   <img src="assets/icon_bot.png"/>
</p>

<h1 style="text-align:center;">AudioToText-Bot</h1>   


> I just hate voice messages, this is the result.

---

## Requirements

- `python` >= v3.9
- `API_TOKEN` from [BotFather](https://t.me/BotFather)

---

## Usage
```bash
# Open Terminal
# Clone the repo
# https
git clone https://github.com/kevinm6/audioToText-bot.git # or
# ssh (this could require additional steps to generate ssh key)
git clone git@github.com:kevinm6/audioToText-bot.git

# Create env var `BOT_TOKEN` that stores it
# the var label is the one that the script expects, so do not change it
export BOT_TOKEN="<token_from_BotFather>"

# After
$(which python3) -m venv audioToText-bot
cd audioToText-bot/
chmod +x transcriptBot
source bin/activate

# and
./transcriptBot # this start the bot (press <Ctrl+c> to stop it)

