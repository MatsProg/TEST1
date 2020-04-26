from __future__ import absolute_import
import mmap
from struct import *
from collections import namedtuple
#from obliczenia import Obliczenia as Ob  #importuje plik
import math
import time

def konwersSlip(wartosc, x):
        wartosc = wartosc / 5
        wartosc = max(wartosc, 0)
        wartosc = min(wartosc, 1)
        math.radians(wartosc)
        return pow(wartosc, x)

class Example(object):
	def __init__(self):
		print u'PROCESS CREATED'
		#self.name = 'OVERLAY'
		self.mmapPhysic = mmap.mmap(0, 1024, u"Local\\acpmf_physics")
		self.bityTuple = namedtuple(u'Liczby',
									u'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR')
		#self.ovl = Overlay()

	def bits(self):  #Odbiera bytes
		self.mmapPhysic.seek(0)  # to mowi zeby zaczac czytac od 0
		self.bytesValue = self.mmapPhysic.read(120)  # obiekt wskazuje na +120 znakow
		self.unpackTuple = self.bityTuple._make(unpack(u'ifffiiffffffffffffffffffffffff', self.bytesValue))
		self.wheelSlip = konwersSlip(getattr(self.unpackTuple, u'wheelSlipFL'), 3), konwersSlip(getattr(self.unpackTuple, u'wheelSlipFR'), 3), konwersSlip(getattr(self.unpackTuple, u'wheelSlipRL'),2), konwersSlip(getattr(self.unpackTuple, u'wheelSlipRR'), 2)

		#self.ovl.updateWheelSlip(self.wheelSlip[2], self.wheelSlip[3], self.wheelSlip[0], self.wheelSlip[1])  # [FL, FR, RL, RR]


ex = Example()

if __name__ == u'__main__':
	# time.sleep(1)
	ex.bits()
	#ex.main()
