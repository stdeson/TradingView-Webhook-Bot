import os


sec_key = (
    "MDeson987"  # 这个是用来校验是否是自己的消息
)

# Telegram Settings
send_telegram_alerts = False
tg_token = ""  # Bot token. Get it from @Botfather
channel = 0  # Channel ID (ex. -1001487568087)

# Discord Settings
send_discord_alerts = False
discord_webhook = ""  # Discord Webhook URL (https://support.discordapp.com/hc/de/articles/228383668-Webhooks-verwenden)

# Slack Settings
send_slack_alerts = False
slack_webhook = ""  # Slack Webhook URL (https://api.slack.com/messaging/webhooks)

# Twitter Settings
send_twitter_alerts = False
tw_ckey = ""
tw_csecret = ""
tw_atoken = ""
tw_asecret = ""

# Email Settings
send_email_alerts = True
email_sender = "decenfrontier@gmail.com"  # Your email address
email_receivers = ["stdeson@gmail.com", "ws156858@163.com"]  # Receivers, can be multiple
email_subject = "Trade Alert!"

email_port = 465  # SMTP SSL Port (ex. 465)
email_host = "smtp.gmail.com"  # SMTP host (ex. smtp.gmail.com)
email_user = email_sender  # SMTP Login credentials
email_password = os.getenv('EMAIL_PWD')  # SMTP Login credentials
