#from __future__ import print_function

import winsound
import keyboard
from START import *


global listRPM
global ex
global nowyRPMs
listRPM = []
ex = Example()


class overlay():
	def __init__(self):
		pass

	def percentage(percent, whole):
		return (percent * whole) / 100.0
	def kibord(self):
		global listRPM
		global nowyRPMs
		if keyboard.is_pressed('r'):
			listRPM.clear()
			RPMsound = 0
			#listRPM.append(1)


	def RPM1(self):
		#global RPMs
		global RPMs
		global nowyRPMs

		ex.bits()
		#self.RPMsound = 5900
		RPMs = ex.RPM
		self.GEARs = ex.GEAR
		self.tc1 = ex.TC1

		listRPM.append(RPMs)
		self.proc = overlay.percentage(5, max(listRPM))
		RPMsound = max(listRPM)
		# self.unpackTuplee = self.ex.unpackTuple
		# print(str(self.tc1) + ' tc1')
		# print(str(self.unpackTuplee) + ' unpackTuplee')

		while self.GEARs <= 4 and RPMs > (RPMsound - (self.proc + self.proc)):  # 1st gear
			#winsound.PlaySound('alarm1.wav', winsound.SND_LOOP)
			winsound.PlaySound(None, winsound.SND_PURGE)
			winsound.PlaySound('alarm1.wav', winsound.SND_FILENAME | winsound.SND_LOOP)#winsound.PlaySound('alarm.wav', winsound.SND_LOOP)
			break
		while self.GEARs >= 5 and RPMs > (RPMsound - self.proc):
			#winsound.PlaySound('alarm1.wav', winsound.SND_LOOP)
			winsound.PlaySound(None, winsound.SND_PURGE)
			winsound.PlaySound('alarm1.wav', winsound.SND_FILENAME | winsound.SND_LOOP)
			break
		else:
			winsound.PlaySound(None, winsound.SND_PURGE)

		klasa.kibord()
		keyboard.unhook_all()

	def debug1(self):
		print("RPM = " + str(nowyRPMs))
		print(self.proc + self.proc)
		print(listRPM)


#####
klasa = overlay()

while (True):
	if __name__ == '__main__':
		klasa.RPM1()




# time.sleep(1)


