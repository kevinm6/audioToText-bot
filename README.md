# AudioToText-Bot

> I just hate voice messages, this is the result.

---

## Requirements

- `python` >= v3.9
- `API_TOKEN` from [BotFather](t.me/BotFather)

---

## Usage
```bash
# Open Terminal
# Clone the repo
# https
git clone https://github.com/kevinm6/audioToText-bot.git # or
# ssh (this could require additional steps to generate ssh key)
git clone git@github.com:kevinm6/audioToText-bot.git

# Create file named `token` that stores it
echo "<token_from_BotFather>" > token

# After
$(which python3) -m venv audioToText-bot
cd audioToText-bot/
source bin/activate
pip install -r requirements.txt

# and
python transcriptBot.py # this start the bot (press <Ctrl+c> to stop it)
```
