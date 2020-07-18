#from __future__ import print_function

import winsound
import keyboard
from START import *
from raceroom_telemetry_reader import *

#global listRPM
#global ex
#global RPMsound
#global nowyRPMs

#ex = Example()
r3reader = RaceRoomData()

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

		#ex.bits()
		r3reader.start()
		#self.RPMsound = 5900
		data = r3reader.getData()
		RPMs = (data['engine_rps'] * 6.000000024)
		#RPMs = ex.RPM
		nowyRPMs = max(nowyRPMs, RPMs)
		#self.GEARs = ex.GEAR
		self.GEARs = data['gear']
		self.proc = overlay.percentage(5, nowyRPMs)
		#nowyRPMs = nowyRPMs
		# self.unpackTuplee = self.ex.unpackTuple
		#print(str(RPMs) + ' RPMS')
		#print(str(self.GEARs) + ' gear')
		# print(str(self.unpackTuplee) + ' unpackTuplee')
		#print('R3E data:', r3reader.getData())

		if self.GEARs == 0 and nowyRPMs > 3000:  # 1st gear
			#winsound.PlaySound('alarm1.wav', winsound.SND_LOOP)
			#winsound.PlaySound(None, winsound.SND_PURGE)
			winsound.PlaySound('alarm1.wav', winsound.SND_FILENAME | winsound.SND_LOOP)#winsound.PlaySound('alarm.wav', winsound.SND_LOOP)

		elif self.GEARs <= 3 and RPMs > (nowyRPMs - (self.proc + self.proc)):  # 1st gear
			#winsound.PlaySound('alarm1.wav', winsound.SND_LOOP)
			#winsound.PlaySound(None, winsound.SND_PURGE)
			winsound.PlaySound('alarm1.wav', winsound.SND_FILENAME | winsound.SND_LOOP)#winsound.PlaySound('alarm.wav', winsound.SND_LOOP)
			#break
		elif self.GEARs >= 4 and RPMs > (nowyRPMs - (self.proc + 250)):
			#winsound.PlaySound('alarm1.wav', winsound.SND_LOOP)
			#winsound.PlaySound(None, winsound.SND_PURGE)
			winsound.PlaySound('alarm1.wav', winsound.SND_FILENAME | winsound.SND_LOOP)
			#break
		else:
			winsound.PlaySound(None, winsound.SND_PURGE)

		klasa.kibord()
		keyboard.unhook_all()
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


