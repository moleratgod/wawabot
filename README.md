# Wawabot

A python based Discord bot with various random commands. There is no real consistency with any of the features I add, so this is not a very practical bot.

## Installation & Usage

Before you can use Wawabot, you will need to install some dependencies.
```bash
pip install py-cord
pip install bs4
```

To install and run Wawabot itself, clone the repository and run the `wawabot.py` file.
```bash
git clone https://github.com/moleratgod/wawabot
cd wawabot
python3 wawabot.py
```

In a `.env` file, you will store your discord bot token, as well as the id of a channel you choose to send debug messages to. The contents of the file should look like this:
```bash
# .env
DISCORD_TOKEN=your_token_goes_here
DEBUG_CHANNEL=your_channel_id_goes_here
```