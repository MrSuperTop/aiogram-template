## Very basic vocabulary bot build with the help of aiogram can be used as an example of basic functionality of the library
### Run on your own
* #### Config
The only thing you need to run it for yourself is to create a config file at ./config/main.json and populate it with a similarly looking config:

`{
    telegram_token: 'YOUR_BOT_TOKEN'
}`

For a more detailed information about the config schema see the `package.Config.Config` class

* #### Install dependencies
1. Using poetry
`poetry install`
1. Using pip
`pip install -r requirements.txt`

* #### Run the bot
1. Using Makefile
`make run`
1. Using plain python executable
`python -m package`

