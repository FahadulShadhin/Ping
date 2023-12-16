from plyer import notification
import os
import time
from dotenv import load_dotenv
from config.logger import logger_config

logger = logger_config()
load_dotenv()


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5,
        app_icon=os.path.abspath(
            'static\icons\emoji-smiley-emoticon-sleep-sticker-emoji-face-5ea322ba869679fbd044b8acdc0e4605.ico'),
        toast=False,
    )


if __name__ == '__main__':
    notification_title = os.getenv('NOTIFICATION_TITLE', 'Take a break')
    notification_message = os.getenv(
        'NOTIFICATION_MESSAGE', 'Time to take a break!')
    time_interval = int(os.getenv('INTERVAL', 3600))

    try:
        while True:
            send_notification(notification_title, notification_message)
            logger.info(
                f"Notification sent: Title='{notification_title}', Message='{notification_message}'")

            time.sleep(time_interval)

    except KeyboardInterrupt:
        logger.info("Script terminated by user.")
