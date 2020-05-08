from __future__ import absolute_import
import mmap
from struct import *
from collections import namedtuple
# from obliczenia import Obliczenia as Ob  #importuje plik
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
		print('PROCESS CREATED')
		# self.name = 'OVERLAY'
		self.mmapPhysic = mmap.mmap(0, 1024, u"Local\\acpmf_physics")
		# self.mmapStatic = mmap.mmap(0, 1024, u"Local\\acpmf_static")
		self.bityTuple = namedtuple('Liczby',
		                            'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR TyrewearFL TyrewearFR TyrewearRL TyrewearRR tyreDirtyLevelFL tyreDirtyLevelFR tyreDirtyLevelRL tyreDirtyLevelRR TyreCoreTempFL TyreCoreTempFR TyreCoreTempRL TyreCoreTempRR camberRADFL camberRADFR camberRADRL camberRADRR suspensionTravelFL suspensionTravelFR suspensionTravelRL suspensionTravelRR drs tc1 heading pitch roll cgHeight  carDamagefront carDamagerear carDamageleft carDamageright carDamagecentre numberOfTyresOut pitLimiterOn abs1 kersCharge kersInput automat rideHeightfront rideHeightrear turboBoost ballast airDensity airTemp roadTemp localAngularVelX localAngularVelY localAngularVelZ finalFF performanceMeter engineBrake ersRecoveryLevel ersPowerLevel ersHeatCharging ersIsCharging kersCurrentKJ drsAvailable drsEnabled brakeTempFL brakeTempFR brakeTempRL brakeTempRR clutch tyreTempI1 tyreTempI2 tyreTempI3 tyreTempI4 tyreTempM1 tyreTempM2 tyreTempM3 tyreTempM4 tyreTempO1 tyreTempO2 tyreTempO3 tyreTempO4 isAIControlled tyreContactPointFLX tyreContactPointFLY tyreContactPointFLZ tyreContactPointFRX tyreContactPointFRY tyreContactPointFRZ tyreContactPointRLX tyreContactPointRLY tyreContactPointRLZ tyreContactPointRRX tyreContactPointRRY tyreContactPointRRZ  tyreContactNormalFLX tyreContactNormalFLY tyreContactNormalFLZ tyreContactNormalFRX tyreContactNormalFRY tyreContactNormalFRZ tyreContactNormalRLX tyreContactNormalRLY tyreContactNormalRLZ tyreContactNormalRRX tyreContactNormalRRY tyreContactNormalRRZ tyreContactHeadingFLX tyreContactHeadingFLY tyreContactHeadingFLZ tyreContactHeadingFRX tyreContactHeadingFRY tyreContactHeadingFRZ tyreContactHeadingRLX tyreContactHeadingRLY tyreContactHeadingRLZ tyreContactHeadingRRX tyreContactHeadingRRY tyreContactHeadingRRZ brakeBias localVelocityX localVelocityY localVelocityZ P2PActivation P2PStatus currentMaxRpm mz1 mz2 mz3 mz4 fx1 fx2 fx3 fx4 fy1 fy2 fy3 fy4 slipRatio1 slipRatio2 slipRatio3 slipRatio4 slipAngle1 slipAngle2 slipAngle3 slipAngle4  tcinAction absInAction suspensionDamage1 suspensionDamage2 suspensionDamage3 suspensionDamage4  tyreTemp1 tyreTemp2 tyreTemp3 tyreTemp4 waterTemp brakePressureFL brakePressureFR brakePressureRL brakePressureRR  frontBrakeCompound rearBrakeCompound padLifeFL padLifeFR padLifeRL padLifeRR discLifeFL discLifeFR discLifeRL discLifeRR ')

	# self.ovl = Overlay()

	def bits(self):  # Odbiera bytes
		self.mmapPhysic.seek(0)  # to mowi zeby zaczac czytac od 0
		self.bytesValue = self.mmapPhysic.read(772)  # obiekt wskazuje na +196 znakow
		self.unpackTuple = self.bityTuple._make(
			unpack('ifffiifffffffffffffffffffffffffffffffffffffffffffffffffffffffiifffiffffffffffffiiiiifiifffffffffffffffffiffffffffffffffffffffffffffffffffffffffffiifffffffffffffffffffffiifffffffffffffiiffffffff', self.bytesValue))
		self.wheelSlip = getattr(self.unpackTuple, 'wheelSlipFL'), getattr(self.unpackTuple, 'wheelSlipFR'), getattr(
			self.unpackTuple, 'wheelSlipRL'), getattr(self.unpackTuple, 'wheelSlipRR')
		self.RPM = getattr(self.unpackTuple, 'rpms')
		self.GEAR = getattr(self.unpackTuple, 'gear')
		self.TC1 = getattr(self.unpackTuple, 'tc1')
		self.ABS1 = getattr(self.unpackTuple, 'abs1')
		self.SPEED = getattr(self.unpackTuple, 'speedKmh')
		self.STEER = getattr(self.unpackTuple, 'steerAngle')
		self.FINALFF = getattr(self.unpackTuple, 'finalFF')
		self.localAngularVelX = getattr(self.unpackTuple, 'localAngularVelX')
		self.localAngularVelY = getattr(self.unpackTuple, 'localAngularVelY')
		self.localAngularVelZ = getattr(self.unpackTuple, 'localAngularVelZ')
		self.localVelocityX = getattr(self.unpackTuple, 'velocity1')
		self.localVelocityY = getattr(self.unpackTuple, 'velocity2')
		self.localVelocityZ = getattr(self.unpackTuple, 'velocity3')
		self.heading = getattr(self.unpackTuple, 'heading')
		self.pitch = getattr(self.unpackTuple, 'pitch')
		self.roll = getattr(self.unpackTuple, 'roll')





# self.ovl.updateWheelSlip(self.wheelSlip[2], self.wheelSlip[3], self.wheelSlip[0], self.wheelSlip[1])  # [FL, FR, RL, RR]


if __name__ == '__main__':
	# time.sleep(1)
	ex = Example()
	ex.bits()
# ex.main()
