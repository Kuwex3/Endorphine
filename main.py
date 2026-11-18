from engine import player, app_engine
from window import label, app

import signal

def shutdown(signum, frame):
    player.stop()
    app_engine.quit()

signal.signal(signal.SIGINT, shutdown)

label.show()

app_engine.exec()
app.exec()