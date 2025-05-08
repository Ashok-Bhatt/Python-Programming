
from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(title="Drink Water",
                            message="Water is an essential part of life.\nWithout water, everything is waste.",
                            app_icon="glass.ico",
                            timeout=10)
        time.sleep(60)