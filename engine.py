from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimedia import QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QTimer

import sys

app_engine = QCoreApplication(sys.argv)

timer = QTimer()
timer.timeout.connect(lambda: None)
timer.start(200)

player = QMediaPlayer()
output = QAudioOutput()

player.setAudioOutput(output)

player.setSource(QUrl.fromLocalFile("song.mp3"))
output.setVolume(1)
player.play()