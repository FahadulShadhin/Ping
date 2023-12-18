from plyer import notification
import os
import time
from dotenv import load_dotenv
from config.logger import logger_config
import psutil
import sys

logger = logger_config()
load_dotenv()


def check_teams_running():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'ms-teams.exe':
            return True
    return False


def notifier():
    notification_title = os.getenv('NOTIFICATION_TITLE', 'Take a break')
    notification_message = os.getenv(
        'NOTIFICATION_MESSAGE', 'Time to take a break!')
    teams_running = check_teams_running()

    if teams_running:
        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=5,
            app_icon=os.path.abspath(
                'static\icons\emoji-smiley-emoticon-sleep-sticker-emoji-face-5ea322ba869679fbd044b8acdc0e4605.ico'),
            toast=False,
        )

        logger.info(f'Teams running={teams_running}')
        logger.info(
            f"Notification sent: Title='{notification_title}', Message='{notification_message}'")
    else:
        logger.warning(f'Teams running={teams_running}')


def main():
    time_interval = int(os.getenv('INTERVAL', 3600))
    logger.info('Notifier started!')
    time.sleep(time_interval)

    try:
        while True:
            notifier()
            time.sleep(time_interval)
    except KeyboardInterrupt:
        logger.warning('Script terminated by user.')


if __name__ == '__main__':
    main()
