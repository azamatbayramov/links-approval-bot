# Links approval bot

Bot automatically approve all chat join requests and save inforamation about joins.

### How to set up bot in Telegram
1. Create bot in BotFather
2. Go to the settings of bot in BotFather
3. Click on "Group Admin Rights" and then on "Invite new users"
4. Click on "Channel Admin Rights" and then on "Invite via link"
5. Telegram will automatically mark another options, it's fine
6. Add bot to the needed group and promote bot to admin with "Add members" right

### How to launch application

1. Copy `.env-template` as `.env` and fill it with bot token and allowed bot admins usernames (who can export)
2. Start bot using `docker compose up --build -d`

### How to export
- Send `/export` command to the bot
- Bot will send you `csv` file, if your username is in allowed bot admins usernames
