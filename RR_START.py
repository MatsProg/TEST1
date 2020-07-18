# VJOY CONFIGURE		AXIS - ALL		|		Buttons 128		|		POV HAT Switch 4 Directions : 1
"""######################################################################################################################################
				INSTRUKCJA																												#
																																		#
		TWOJA NAZWA URZĄDZEIA z kontrolerów gier																						#
device = "USB Steering wheel"																											#
																																		#
				USTAW PO ZDEBUGOWANIU OSI I BUTTONOW NA KONTROLERZE	:																	#
																																		#
joyy = -joy.y 						#twoja oś hamulca																			 		#
joyzRotation = -joy.zRotation		#twoja oś gazu																			 			#
joyx = joy.x						#twoja oś sterowania																	 			#
key_brake1 = joy.getDown(9) 		#button hamulca na zakrety - nie blokuje kol											 			#
shakeIT = joy.getDown(8)			#button do ratowania poslizgu																 		#
																																		#
																																		#
				DODATKOWE INFO	:																										#
																																		#
dodac = keyboard.getPressed(Key.NumberPad8) 					podnosi poziom TC na osi gazu										 	#
odjac = keyboard.getPressed(Key.NumberPad7) 					obniza poziom TC na osi gazu									 		#
dodacABS = keyboard.getPressed(Key.NumberPad5) 							podnosi poziom ABS na osi hamulca				 				#
odjacABS = keyboard.getPressed(Key.NumberPad4)									obniza poziom ABS na osi hamulca					 	#
dodacABS1 = keyboard.getPressed(Key.NumberPad2)					podnosi poziom ABS na BUTTONIE										 	#
odjacABS1 = keyboard.getPressed(Key.NumberPad1)					obniza poziom ABS na BUTTONIE										 	#
																																		#
toggle = keyboard.getPressed(Key.NumberPadPeriod)					wlacza wylacza ABS  i  TC na osiach								 	#
																																		#
toggleST = keyboard.getPressed(Key.NumberPad0)					auto centrowanie w slizgu | domyslnie wylaczone					 		#
																																		#
"""  ######################################################################################################################################

import time

start = time.time()

from System import Int16
from START import *
from raceroom_telemetry_reader import *


def update():
	global joy
	global v
	global ex
	global enable_TC_ABS
	global a_max
	global a_min
	global device
	global wheelRL
	global wheelRR
	global wheelFR
	global wheelFL
	global speed


# update()


def konwers(wartosc, mini, maxi):
	wartosc = max(wartosc, mini)
	wartosc = min(wartosc, maxi)
	return wartosc


def Clutch():  # nie używane
	key_clutch = keyboard.getKeyDown(Key.Q)
	if key_clutch:
		cl_axis += cl_inc
	else:
		cl_axis -= cl_dec
	if cl_axis > a_max:
		cl_axis = a_max
	elif cl_axis < a_min:
		cl_axis = a_min

	v.rx = cl_axis


def GasPedal():
	start1 = time.time()
	global nowyRRiRL

	if joyzRotation > -5000 and enable_TC_ABS and RRiRL >= SPIN and v.ry > -5000:

		v.ry = max(v.ry - (ratiogaz * 2), -5000)
		nowyRRiRL = abs(float(RRiRL - nowyRRiRL))

		if joyzRotation > -5000 and nowyRRiRL > SPIN and v.ry > -5000:
			v.ry = max(v.ry - (ratiogaz * 2), -5000)
			nowyRRiRL = abs(float(RRiRL - nowyRRiRL))


	elif joyzRotation > -5000 and enable_TC_ABS and RRiRL < SPIN and v.ry > -5000:

		v.ry += ratiogaz * 10
		nowyvry = v.ry
		nowyRRiRL = abs(float(RRiRL - nowyRRiRL))

		if joyzRotation > (nowyvry + 500) and nowyRRiRL < SPIN:

			v.ry += ratiogaz * 100
			nowyRRiRL = abs(float(RRiRL - nowyRRiRL))

		else:
			v.ry = joyzRotation
	else:
		v.ry = joyzRotation


def Brake():
	start2 = time.time()
	global nowyFRiFL
	maxspeed = 20
	key_brake = joy.getDown(19)  # 9 #NOT USED

	currentz = abs(v.rz)

	if key_brake and joyy < key_brake_MOC:
		v.rz = key_brake_MOC

	elif joyy > key_brake_MOC or key_brake1 == True:

		if joyy > key_brake_MOC and speed >= maxspeed and enable_TC_ABS and (FRiFL >= SPINABS):
			v.rz = max(v.rz - (ratiobrake * 2), -4000)
			nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if joyy > key_brake_MOC and speed >= maxspeed and nowyFRiFL < SPINABS:
				v.rz += ratiobrake * 2

			if joyy > key_brake_MOC and speed >= maxspeed and nowyFRiFL > SPINABS:
				v.rz = max(v.rz - (ratiobrake * 2), -4000)



		elif joyy > key_brake_MOC and speed >= maxspeed and enable_TC_ABS and v.rz > 0 and (FRiFL < SPINABS):
			v.rz += ratiobrake * 10
			nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if v.rz > a_max and key_brake1 == False and joyy > key_brake_MOC and speed >= maxspeed and enable_TC_ABS and (
					FRiFL < SPINABS):
				v.rz = a_max
				nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if joyy > key_brake_MOC and speed >= maxspeed and nowyFRiFL > SPINABS:
				v.rz = max(v.rz - (ratiobrake * 2), -4000)
				nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if joyy > key_brake_MOC and speed >= maxspeed and nowyFRiFL < SPINABS:
				v.rz += ratiobrake * 10
				nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

				if v.rz > a_max and joyy > key_brake_MOC and speed >= maxspeed and nowyFRiFL < SPINABS:
					v.rz = a_max
					nowyFRiFL = abs(float(FRiFL - nowyFRiFL))



		elif key_brake1 == True and enable_TC_ABS and (FRiFL >= SPIN_ABS_button):
			v.rz -= ratiobrake * 2
			nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if key_brake1 == True and nowyFRiFL < SPIN_ABS_button:
				v.rz += ratiobrake * 10
				if v.rz > a_max:
					v.rz = a_max
					nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if key_brake1 == True and nowyFRiFL > SPIN_ABS_button:
				v.rz = max(v.rz - (ratiobrake * 10), -14000)
				nowyFRiFL = abs(float(FRiFL - nowyFRiFL))


		elif key_brake1 == True and enable_TC_ABS and (FRiFL < SPIN_ABS_button):
			v.rz += ratiobrake * 110
			nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if v.rz > a_max:
				v.rz = a_max
				nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if key_brake1 == True and nowyFRiFL < SPIN_ABS_button:
				v.rz += ratiobrake * 10

				if v.rz > a_max:
					v.rz = a_max
					nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

			if key_brake1 == True and nowyFRiFL > SPIN_ABS_button:
				v.rz = max(v.rz - (ratiobrake * 10), -14000)
				nowyFRiFL = abs(float(FRiFL - nowyFRiFL))

		else:
			v.rz = joyy
	else:
		v.rz = joyy


def Steering():
	start3 = time.time()
	obl = konwers(int(ratio), 1, 300)

	if enable_auto_steeringCare and RRiRL > SPIN_auto_centre and accGX > 17:
		v.x += obl

	elif enable_auto_steeringCare and RRiRL > SPIN_auto_centre and accGX < -17:
		v.x -= obl

	elif shakeIT and accGX > 2 and localAngularVelY < -1:
		v.x += obl * 2

	elif shakeIT and accGX < -2 and localAngularVelY > 1:
		v.x -= obl * 2

	else:
		v.x = joyx


if starting:
	diagnostics.debug("Skrypt START")

	nowyFRiFL = float(0.0)
	nowyRRiRL = float(0.0)

	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 0  # loop delay

	device = "Thrustmaster T150 Racing Wheel"  # TWOJA NAZWA URZĄDZEIA z kontrolerów gier				TWOJA NAZWA URZĄDZEIA z kontrolerów gier				TWOJA NAZWA URZĄDZEIA z kontrolerów gier
	joy = joystick[device]
	joy.setRange(Int16.MinValue / 2.001, Int16.MaxValue / 2.001)

	v = vJoy[0]
	a_max = 1 + v.axisMax
	a_min = -1 - v.axisMax

	enable_TC_ABS = True
	enable_auto_steeringCare = False
	ex = Example()
	SPIN = 5  # TC MINIMUM LIMIT
	SPINABS = 4  # ABS MINIMUM LIMIT
	SPIN_ABS_button = 2  # ABS MINIMUM LIMIT ON BUTTON
	key_brake_MOC = -7500
	key_brake1_MOC = 10000
	SPIN_auto_centre = SPIN + 3  # min slizg do auto centrowania | enableST = True

	# clutch 	-		nie używane
	cl_axis = a_min
	cl_inc = 2000
	cl_dec = 600
	# end clutch

	r3reader = RaceRoomData()
############################

r3reader.start()
data = r3reader.getData()

##########################							USTAW OSIE					USTAW OSIE					USTAW OSIE					USTAW OSIE
joyy = -joy.y
joyzRotation = -joy.zRotation
joyx = joy.x
key_brake1 = joy.getDown(9)  # BUTTON HAMULCA
shakeIT = joy.getDown(8)  # BUTTON POSLIZGOW
########################
dodac = keyboard.getPressed(Key.NumberPad8)
odjac = keyboard.getPressed(Key.NumberPad7)
dodacABS = keyboard.getPressed(Key.NumberPad5)
odjacABS = keyboard.getPressed(Key.NumberPad4)
dodacABS1 = keyboard.getPressed(Key.NumberPad2)
odjacABS1 = keyboard.getPressed(Key.NumberPad1)

toggle = keyboard.getPressed(Key.NumberPadPeriod)
if toggle:
	enable_TC_ABS = not enable_TC_ABS
toggleST = keyboard.getPressed(Key.NumberPad0)
if toggleST:
	enable_auto_steeringCare = not enable_auto_steeringCare

if dodac:
	SPIN = SPIN + 0.5
if odjac:
	SPIN = SPIN - 0.5
if dodacABS:
	SPINABS = SPINABS + 0.5
if odjacABS:
	SPINABS = SPINABS - 0.5
if dodacABS1:
	SPIN_ABS_button = SPIN_ABS_button + 0.5
if odjacABS1:
	SPIN_ABS_button = SPIN_ABS_button - 0.5

ex.bits()

wheel = ex.wheelSlip
wheelFL = data['wheelSlip'][0] / 10
wheelFR = data['wheelSlip'][1] / 10
wheelRL = data['wheelSlip'][2] / 10
wheelRR = data['wheelSlip'][3] / 10
RPM = (data['engine_rps'] * 6.000000024)
# tc1 = ex.TC1
# abs1 = ex.ABS1
all = ex.unpackTuple
speed = (data['speed'] * 1.609344) * 2
steer = data['steer_input_raw']
accGX = data['local_g_force'][0] * 100
localAngularVelY = data['angular_velocity'][1] * 100

FRiFL = float((wheelFL + wheelFR) / 2)
RRiRL = float((wheelRL + wheelRR) / 2)
ratiogaz = konwers(abs(RRiRL * 2), 5, 25)
ratiobrake = konwers(abs(FRiFL), 35, 55)
ratio = konwers(abs(localAngularVelY + accGX) * 10, 1, 300)
ratioT = konwers(abs(accGX / 1), 1, 300)

GasPedal()
Brake()
Steering()


def zawszeON():
	diagnostics.watch(SPIN)
	diagnostics.watch(SPINABS)
	diagnostics.watch(enable_TC_ABS)
	diagnostics.watch(enable_auto_steeringCare)
	diagnostics.watch(SPIN_auto_centre)
	diagnostics.watch(SPIN_ABS_button)


def joystickDebug():  ##############################################
	# AXIS
	diagnostics.watch(joy.sliders[0])
	diagnostics.watch(joy.sliders[1])
	diagnostics.watch(joy.x)
	diagnostics.watch(joy.y)
	diagnostics.watch(joy.z)
	diagnostics.watch(joy.xRotation)
	diagnostics.watch(joy.yRotation)
	diagnostics.watch(joy.zRotation)
	diagnostics.watch(joy.pov[0])
	diagnostics.watch(joy.pov[1])
	# BUTTONS
	diagnostics.watch(joy.getDown(1))
	diagnostics.watch(joy.getDown(2))
	diagnostics.watch(joy.getDown(3))
	diagnostics.watch(joy.getDown(4))
	diagnostics.watch(joy.getDown(5))
	diagnostics.watch(joy.getDown(6))
	diagnostics.watch(joy.getDown(7))
	diagnostics.watch(joy.getDown(8))
	diagnostics.watch(joy.getDown(9))
	diagnostics.watch(joy.getDown(10))
	diagnostics.watch(joy.getDown(11))
	diagnostics.watch(joy.getDown(12))

	# po przypisaniu zakres oraz kierunek vjoy i joy ma byc taki sam ++/--
	diagnostics.watch(joyy)
	diagnostics.watch(v.rz)

	diagnostics.watch(joyzRotation)
	diagnostics.watch(v.ry)

	diagnostics.watch(joyx)
	diagnostics.watch(v.x)


def debug():  ##############################################
	diagnostics.watch(accGX)
	diagnostics.watch(localAngularVelY)
	diagnostics.watch(data['angular_velocity'][2])
	diagnostics.watch(RRiRL)
	diagnostics.watch(FRiFL)
	diagnostics.watch(joy.getDown(9))
	diagnostics.watch(joy.getDown(8))
	diagnostics.watch(joy.getDown(6))
	diagnostics.watch(ratio)
	diagnostics.watch(ratiogaz)
	diagnostics.watch(ratiobrake)
	diagnostics.watch(data['acceleration'][0])
	diagnostics.watch(data['acceleration'][1])
	diagnostics.watch(data['acceleration'][2])
	diagnostics.watch(RPM)
	diagnostics.watch(speed)
	diagnostics.watch(steer)
	diagnostics.watch(wheelFL)
	diagnostics.watch(wheelFR)
	diagnostics.watch(wheelRL)
	diagnostics.watch(wheelRR)
	diagnostics.watch(v.rx)
	diagnostics.watch(joyx)
	diagnostics.watch(v.x)
	diagnostics.watch(joyzRotation)
	diagnostics.watch(v.ry)
	diagnostics.watch(joyy)
	diagnostics.watch(v.rz)


######################################

joystickDebug()
zawszeON()
# debug()

#####################################
stop = time.time()  #
if stop - start > 0.01:  #
	diagnostics.debug(stop - start)  #
#####################################
