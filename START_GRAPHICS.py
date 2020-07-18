from __future__ import absolute_import

# from obliczenia import Obliczenia as Ob  #importuje plik
import math
import mmap
from collections import namedtuple
from struct import *


def konwersSlip(wartosc, x):
	wartosc = wartosc / 5
	wartosc = max(wartosc, 0)
	wartosc = min(wartosc, 1)
	math.radians(wartosc)
	return pow(wartosc, x)


class Example(object):
	def __init__(self):
		print('PROCESS CREATED')
		# self.name = 'OVERLAY'
		self.mmapPhysic = mmap.mmap(0, 1024, u"Local\\acpmf_graphics")
		# self.mmapStatic = mmap.mmap(0, 1024, u"Local\\acpmf_static")
		self.bityTuple = namedtuple('Liczby', 'packetId')

	# self.ovl = Overlay()

	def bits(self):  # Odbiera bytes

		self.mmapPhysic.seek(0)  # to mowi zeby zaczac czytac od 0
		self.bytesValue = self.mmapPhysic.read(4)  # obiekt wskazuje na +196 znakow
		self.unpackTuple = self.bityTuple._make(unpack(	'i', self.bytesValue))
		#self.wheelSlip = getattr(self.unpackTuple, 'wheelSlipFL'), getattr(self.unpackTuple, 'wheelSlipFR'), getattr(self.unpackTuple, 'wheelSlipRL'), getattr(self.unpackTuple, 'wheelSlipRR')
		#self.RPM = getattr(self.unpackTuple, 'rpms')
		self.packetId = getattr(self.unpackTuple, 'packetId')
		self.newpacketId = self.packetId
		if self.packetId > 0:

			if self.packetId - self.newpacketId:
				print(self.packetId)



if __name__ == '__main__':
	# time.sleep(1)
	ex = Example()
	while True:
		ex.bits()
# ex.main()
