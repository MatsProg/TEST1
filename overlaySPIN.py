#from __future__ import print_function

import winsound
import keyboard
from START import *


#global listRPM
#global ex
#global RPMsound
#global nowyRPMs

ex = Example()


class overlay():
	def __init__(self):
		global nowyRPMs
		nowyRPMs = 0

	def percentage(percent, whole):
		return (percent * whole) / 100.0

	def kibord(self):
		global nowyRPMs
		#global nowyRPMs
		if keyboard.is_pressed('*'):
			nowyRPMs = 1000
		if keyboard.is_pressed('/'):
			nowyRPMs = 100000
			#nowyRPMs = 0
			#listRPM.append(1)

	def RPMsMAX(self, a, b):
		if b > a:
			c = b
			return c

	def RPM1(self):
		#global RPMs
		global RPMs
		global nowyRPMs

		ex.bits()
		#self.RPMsound = 5900
		RPMs = ex.RPM
		nowyRPMs = max(nowyRPMs, RPMs)
		self.GEARs = ex.GEAR
		self.brakeAxis = ex.brake
		self.gas = ex.gas
		spin = ex.wheelSlip
		wheelFL = spin[0]
		wheelFR = spin[1]
		wheelRL = spin[2]
		wheelRR = spin[3]
		STEER = ex.STEER

		self.RLiRR = float(wheelRL + wheelRR) /2
		self.proc = overlay.percentage(5, nowyRPMs)
		#nowyRPMs = nowyRPMs
		# self.unpackTuplee = self.ex.unpackTuple
		# print(str(self.tc1) + ' tc1')
		# print(str(self.unpackTuplee) + ' unpackTuplee')
		#print(STEER)

		#if self.RLiRR > 0.6 and (self.brakeAxis > 0.01 or self.gas <= 0.1):  # 1st gear
		if (wheelFL or wheelFR) > 1.18 and (STEER > 0.25 or STEER < -0.25):
			#winsound.PlaySound('alarm1.wav', winsound.SND_LOOP)
			#winsound.PlaySound(None, winsound.SND_PURGE)
			winsound.PlaySound('alarm1.wav', winsound.SND_FILENAME | winsound.SND_LOOP)#winsound.PlaySound('alarm.wav', winsound.SND_LOOP)
			#break
		else:
			winsound.PlaySound(None, winsound.SND_PURGE)

		#klasa.kibord()
		#keyboard.unhook_all()
		#klasa.debug1()

	def debug1(self):
		print(nowyRPMs)
		print(nowyRPMs)
		print("nowy RPM = " + str(klasa.RPMsMAX(nowyRPMs, RPMs)))
		print("RPMsound = MAX = " + str(nowyRPMs))
		print("procent x2  = " + str(self.proc + self.proc))


#####
klasa = overlay()

while (True):
	if __name__ == '__main__':
		klasa.RPM1()




# time.sleep(1)


