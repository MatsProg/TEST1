from __future__ import absolute_import
import mmap
from struct import *
from collections import namedtuple
#from obliczenia import Obliczenia as Ob  #importuje plik
import math
import sys
import time


def konwersSlip(wartosc, x):
        wartosc = wartosc / 5
        wartosc = max(wartosc, 0)
        wartosc = min(wartosc, 1)
        math.radians(wartosc)
        return pow(wartosc, x)

class Example(object):
	def __init__(self):
		print ('PROCESS CREATED')
		#self.name = 'OVERLAY'
		self.mmapPhysic = mmap.mmap(0, 1024, u"Local\\acpmf_physics")
		#self.mmapStatic = mmap.mmap(0, 1024, u"Local\\acpmf_static")
		self.bityTuple = namedtuple('Liczby',
									'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR TyrewearFL TyrewearFR TyrewearRL TyrewearRR tyreDirtyLevelFL tyreDirtyLevelFR tyreDirtyLevelRL tyreDirtyLevelRR TyreCoreTempFL TyreCoreTempFR TyreCoreTempRL TyreCoreTempRR camberRADFL camberRADFR camberRADRL camberRADRR suspensionTravelFL suspensionTravelFR suspensionTravelRL suspensionTravelRR drs tc1 heading pitch roll cgHeight carDamagefront carDamagerear carDamageleft carDamageright carDamagecentre numberOfTyresOut pitLimiterOn abs1 kersCharge kersInput automat rideHeightfront rideHeightrear turboBoost')
		#self.ovl = Overlay()

	def bits(self):  #Odbiera bytes
		self.mmapPhysic.seek(0)  # to mowi zeby zaczac czytac od 0
		self.bytesValue = self.mmapPhysic.read(280)  # obiekt wskazuje na +196 znakow
		self.unpackTuple = self.bityTuple._make(unpack('ifffiifffffffffffffffffffffffffffffffffffffffffffffffffffffffiifffifff', self.bytesValue))
		self.wheelSlip = getattr(self.unpackTuple, 'wheelSlipFL'), getattr(self.unpackTuple, 'wheelSlipFR'), getattr(self.unpackTuple, 'wheelSlipRL'), getattr(self.unpackTuple, 'wheelSlipRR')
		self.RPM = getattr(self.unpackTuple, 'rpms')

		#self.ovl.updateWheelSlip(self.wheelSlip[2], self.wheelSlip[3], self.wheelSlip[0], self.wheelSlip[1])  # [FL, FR, RL, RR]

if __name__ == '__main__':
	# time.sleep(1)
	ex = Example()
	ex.bits()
	#ex.main()
