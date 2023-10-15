# HasturBot
Discord bot for Kasztany RPG server.

## Setup
```
# Setup environment with at least Python 3.10
virtualenv -p python3.10 .env
# Windows
.\.env\Scripts\activate
# Linux
source .env/bin/activate

# Install production / development packages
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Create template config file, add Discord API token
python run.py update_config -c config.cfg

# Run bot and enjoy
python run.py update_config -c config.cfg -l discord.log
```