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
```

### Usage on macOS with Homebrew (brew services)

```bash
# Open Terminal
# Clone the repo
# https
git clone https://github.com/kevinm6/audioToText-bot.git # or
# ssh (this could require additional steps to generate ssh key)
git clone git@github.com:kevinm6/audioToText-bot.git
```

```ruby
# edit file .rb with the url
url "file:///path/to/dir/where/archive/script/audioToText-bot.tar.gz"

# populate env variables for brew services (wrap of macOS LaunchAgents & LaunchDaemons)
environment_variables BOT_TOKEN: "token_from_bot_father", VIRTUAL_ENV: "path_to_python_venv_of_bot"
```

```bash
# create compressed file for Homebrew
tar cf audioToText-bot.tar.gz path/to/cloned_repo/audioToText-bot/*
# the path of the archive-file (.tar.gz) is the `url` field inside .rb file

# is now possible to install the local homebrew tap
# compact
brew install name/repo/transcriptbot

# full command
brew tap name/repo urL_to_local_folder_with_targz_file
brew install transcriptbot

# run the service
brew services run transcriptbot

# or start the brew service (this will be run even at every login)
brew services start transcriptbot
```
