import winsound
import time


winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
time.sleep(2)
winsound.PlaySound(None, winsound.SND_PURGE)