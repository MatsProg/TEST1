import pygame
import win32api
import os
from START import *
import win32gui
import win32con
import keyboard
ex = Example()
import time
import math
import subprocess

clock = pygame.time.Clock()
FPS = 5
while True:
	delta_t = clock.tick(FPS)  # tick() function will calculate the delta time since it was called in last frame

	class App:
		def __init__(self):
			self._running = True
			self._display_surf = None
			self.size = self.weight, self.height = 1920, 500
			self.position = 955
			self.orygpos = self.position
			self.wartoscSter = 2
			self.STEER = 2
			self.nowywartoscSter = 0
			self.pasek = False
			self.nowywartoscSterOLD = 0
			self.nowywartoscSter1OLD = 0
			self.enabled = True
			self.nowyGAS1 = 0
			self.maxRPM = 0



		def on_init(self):
			icon = pygame.image.load('car.png')
			pygame.display.set_icon(icon)
			pygame.init()
			os.environ['SDL_VIDEO_WINDOW_POS'] = '5, 500' # miejsce okienka
			self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.NOFRAME)
			self._running = True

		def on_event(self, event):
			if event.type == pygame.QUIT:
				self._running = False


		def on_loop(self):

			self.kibord()

			""" ACC """
			ex.bits()
			self.spin = ex.wheelSlip
			self.wheelFLP = min(100, math.floor(self.spin[0] * 20.9))
			self.wheelFRP = min(100, math.floor(self.spin[1] * 20.9))
			self.wheelFL = round(max(min(self.spin[0], 244) - 0.5, 0), 1)
			self.wheelFR = round(max(min(self.spin[1], 244) - 0.5, 0), 1)
			self.wheelRL = round(max(min(self.spin[2], 244) - 0.5, 0), 1)
			self.wheelRR = round(max(min(self.spin[3], 244) - 0.5, 0), 1)
			self.tires = [self.wheelFL, self.wheelFR, self.wheelRL, self.wheelRR]
			self.STEER = ex.STEER
			self.RLiRR = float(self.wheelRL + self.wheelRR) / 2
			self.FRiFL = float(self.wheelFL + self.wheelFR) / 2
			self.angularVelYRad = ex.localAngularVelY
			self.angularVelXRad = ex.localAngularVelX
			self.angularVelZRad = ex.localAngularVelZ
			self.SPEED = int(ex.SPEED)
			self.GAS = ex.gas
			self.BRAKE = ex.brake
			self.RPM = ex.RPM
			self.GEAR = ex.GEAR
			""" ACC """
			for x in self.tires:
				if x >0:
					colorTires = 255
				else:
					colorTires = 0



			self.fuchsia = (255, 0, 128)  # Transparency color

			hwnd = pygame.display.get_wm_info()["window"]
			win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
			                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
			win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*self.fuchsia), 0, win32con.LWA_COLORKEY)
			self._display_surf.fill(self.fuchsia)  # Transparent background
			win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
			win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
			#########################

			self.RED = (255, 0, 0)
			self.BLACK = (0, 0, 0)

			#################################


			#print(self.orygpos - self.angularVelYDegPOS)

			if self.enabled:

				self.steerbar()
				self.CarDamage()
				#self.Scale()
				#self.slide()
				self.slideTEST()
				#self.circle()
				self.wheelspin()
				self.GasFunkcja()
				self.RPMy()

			#self.travel()

			pygame.display.update()
			self._running = True

			##30fps
			font = pygame.font.SysFont(None, 18)
			fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
			self._display_surf.blit(fps, (0, 0))
			pygame.display.flip()
			clock.tick(30)
			##  END 30fps
		def kibord(self):
			if keyboard.is_pressed('*'):
				self.enabled = not self.enabled
				time.sleep(0.1)

		def _Firewall(self):
			name = "Assetto Corsa Competizione"
			name1 = "Steam Client Bootstrapper"
			path = "C:\\Program Files (x86)\\Steam New\\steamapps\\common\\Assetto Corsa Competizione\\acc.exe"
			path1 = "C:\\program files (x86)\\steam new\\steam.exe"
			if keyboard.is_pressed(']'):
				time.sleep(0.1)
				delete = subprocess.Popen('netsh advfirewall firewall delete rule name="' + name)
				delete1 = subprocess.Popen('netsh advfirewall firewall delete rule name="' + name1)
			if keyboard.is_pressed('p'):
				add = subprocess.Popen('netsh advfirewall firewall add rule name="' + name + '" dir=in action=block program= "' + path + '" enable=yes profile=any')
				add1 = subprocess.Popen(
					'netsh advfirewall firewall add rule name="' + name1 + '" dir=in action=block program= "' + path1 + '" enable=yes profile=any')
				time.sleep(0.1)
			if keyboard.is_pressed('['):
				add = subprocess.Popen('netsh advfirewall firewall add rule name="' + name + '" dir=in action=allow program= "' + path + '" enable=yes profile=any')
				add = subprocess.Popen(
					'netsh advfirewall firewall add rule name="' + name1 + '" dir=in action=allow program= "' + path1 + '" enable=yes profile=any')
				time.sleep(0.1)
		def wheelspin(self):

			pygame.draw.rect(self._display_surf, (255, self.wheelRL, 128), pygame.Rect(850, 320, 60, 60),5)
			pygame.draw.rect(self._display_surf, (255, self.wheelRR, 128), pygame.Rect(1000, 320, 60, 60),5)



			sysfont = pygame.font.get_default_font()
			font = pygame.font.SysFont(None, 48)
			fontXL = pygame.font.SysFont(None, 118)
			img = font.render(str(self.wheelRL), True, self.RED)
			img1 = font.render(str(self.wheelRR), True, self.RED)
			self.imgwheelspinFL = font.render(str(self.wheelFL), True, self.RED)
			self.imgwheelspinFR = font.render(str(self.wheelFR), True, self.RED)


			self._display_surf.blit(img, (858, 330))
			self._display_surf.blit(img1, (1008, 330))
			if self.wartoscSter > 1:
				wheelspinshowFL = self._display_surf.blit(self.imgwheelspinFL, [956 + self.wartoscSter, 165])  # (858, 210))
				#pygame.draw.rect(self._display_surf, (self.r, self.g, self.b), pygame.Rect(950 + self.wartoscSter, 160, 60, 60), 5)
			elif self.wartoscSter < -1:
				wheelspinshowFR = self._display_surf.blit(self.imgwheelspinFR, [936 + self.wartoscSter, 165])  # (858, 210))
				#pygame.draw.rect(self._display_surf, (self.r, self.g, self.b), pygame.Rect(930 + self.wartoscSter, 160, 60, 60), 5)
			#self.wheelspinshowFR = self._display_surf.blit(self.imgwheelspinFR, (1008, 210))

			if self.SPEED > 120:
				r = 0
				g = 255
				b =255
			elif self.SPEED > 100:
				r = 255
				g = 255
				b=0
			elif self.SPEED > 90:
				r = 255
				g = 0
				b= 0
			else:
				r= 255
				g= 255
				b= 255


			speedcolor = min(self.SPEED, 255)
			imgSPEED = fontXL.render(str(self.SPEED), True, (r, g, b))
			self._display_surf.blit(imgSPEED, (973, 180))

			self._running = True
		def travel(self):
			self.padLifeFL = round(ex.padLifeFL*1000,1)
			self.padLifeFR = round(ex.padLifeFR*1000,1)
			self.padLifeRL = round(ex.padLifeRL*1000,1)
			self.padLifeRR = round(ex.padLifeRR*1000,1)

			self.discLifeFL = round(ex.discLifeFL * 1000, 1)
			self.discLifeFR = round(ex.discLifeFR * 1000, 1)
			self.discLifeRL = round(ex.discLifeRL * 1000, 1)
			self.discLifeRR = round(ex.discLifeRR * 1000, 1)
			font = pygame.font.SysFont(None, 18)
			color = (255, 255, 128)
			imgRL = font.render(str(self.padLifeRL), True, color)
			imgRR = font.render(str(self.padLifeRR), True, color)
			imgFL = font.render(str(self.padLifeFL), True, color)
			imgFR = font.render(str(self.padLifeFR), True, color)
			self._display_surf.blit(imgRL, (858, 310))
			self._display_surf.blit(imgRR, (1008, 310))
			self._display_surf.blit(imgFL, (858, 190))
			self._display_surf.blit(imgFR, (1008, 190))

			imgRL1 = font.render(str(self.discLifeRL), True, color)
			imgRR1 = font.render(str(self.discLifeRR), True, color)
			imgFL1 = font.render(str(self.discLifeFL), True, color)
			imgFR1 = font.render(str(self.discLifeFR), True, color)
			self._display_surf.blit(imgRL1, (858, 360))
			self._display_surf.blit(imgRR1, (1008, 360))
			self._display_surf.blit(imgFL1, (858, 250))
			self._display_surf.blit(imgFR1, (1008, 250))




			self._running = True
		def CarDamage(self):
			center = min(ex.carDamagecentre*2, 254)
			front = min(ex.carDamagefront*2, 254)
			rear = min(ex.carDamagerear*2, 254)
			left = min(ex.carDamageleft*2, 254)
			right = min(ex.carDamageright*2, 254)

			if center <= 0:
				dmgCNT = pygame.draw.rect(self._display_surf, (0, 0, 0), [940, 260, 30, 60], 1)
			else:
				dmgCNT1 = pygame.draw.rect(self._display_surf, (center, 255-center, 0), [940, 260, 30, 60])
				dmgCNT = pygame.draw.rect(self._display_surf, (0, 0, 0), [940, 260, 30, 60], 1)
			if front <= 0:
				dmgFRONT = pygame.draw.rect(self._display_surf, (0, 0, 0), [940, 250, 30, 10], 1)
			else:
				dmgFRONT1 = pygame.draw.rect(self._display_surf, (front, 255-front, 0), [940, 249, 30, 10])
				dmgFRONT = pygame.draw.rect(self._display_surf, (0, 0, 0), [940, 249, 30, 10], 1)
			if rear <= 0:
				dmgREAR = pygame.draw.rect(self._display_surf, (0, 0, 0), [940, 320, 30, 10], 1)
			else:
				dmgREAR1 = pygame.draw.rect(self._display_surf, (rear, 255-rear, 0), [940, 321, 30, 10])
				dmgREAR = pygame.draw.rect(self._display_surf, (0, 0, 0), [940, 321, 30, 10], 1)
			if left <= 0:
				dmgLEFT = pygame.draw.rect(self._display_surf, (0, 0, 0), [930, 260, 10, 60], 1)
			else:
				dmgLEFT1 = pygame.draw.rect(self._display_surf, (left, 255-left, 0), [929, 260, 10, 60])
				dmgLEFT = pygame.draw.rect(self._display_surf, (0, 0, 0), [929, 260, 10, 60], 1)
			if right <= 0:
				dmgRIGHT = pygame.draw.rect(self._display_surf, (0, 0, 0), [970, 260, 10, 60], 1)
			else:
				dmgRIGHT1 = pygame.draw.rect(self._display_surf, (right, 255-right, 0), [971, 260, 10, 60])
				dmgRIGHT = pygame.draw.rect(self._display_surf, (0, 0, 0), [971, 260, 10, 60], 1)
			#dmgREAR = pygame.draw.rect(self._display_surf, (0, 0, 0), [90, 120, 30, 10], 1)
			#dmgFRONT = pygame.draw.rect(self._display_surf, (0, 0, 0), [90, 50, 30, 10], 1)
			#dmgLEFT = pygame.draw.rect(self._display_surf, (0, 0, 0), [120, 60, 10, 60], 1)
			#dmgRIGHT = pygame.draw.rect(self._display_surf, (0, 0, 0), [80, 60, 10, 60], 1)
			self._running = True
		def circle(self):

			self.angularVelYDeg = int(self.angularVelYRad * 57)
			self.angularVelYDegPOS = int(self.orygpos + (self.angularVelYDeg * 4))

			pygame.draw.circle(self._display_surf, (255, 0, 0), [self.angularVelYDegPOS, 80], 8)


		def steerbar(self):
			global wartoscSter
			self.pasek1 = False
			if ((self.wheelFR + (self.wheelRR*0.5)) > 0.45 and self.STEER < -0.15) or ((self.wheelFL+(self.wheelRL*0.5)) > 0.9 and self.STEER > 0.15):
				self.r = 255
				self.g = 0
				self.b=0
				self.pasek = False
				self.pasek1 = True
			elif ((self.wheelFR + (self.wheelRR*0.5)) > 0.4 and self.STEER < -0.15) or ((self.wheelFL+(self.wheelRL*0.5)) > 0.7 and self.STEER > 0.15):
				self.r = 255
				self.g = 255
				self.b=0
				self.pasek = False
			elif ((self.wheelFR + (self.wheelRR*0.5)) > 0.3 and self.STEER < -0.15) or ((self.wheelFL+(self.wheelRL*0.5)) > 0.5 and self.STEER > 0.15):
				self.r = 0
				self.g = 255
				self.b =0
				self.pasek = True
			else:
				self.r= 255
				self.g= 255
				self.b=255
				self.pasek = True
			self.wartoscSter = int(self.STEER * 1000)
			pygame.draw.rect(self._display_surf, (0, 0, 0), pygame.Rect(954, 150, 3, 55)) #dlugosc black pasek
			pygame.draw.rect(self._display_surf, (self.r,self.g, self.b), pygame.Rect(956, 165, int(self.wartoscSter), 10))
			pygame.draw.rect(self._display_surf, (self.r, self.g, 0), pygame.Rect(956, 165, int(self.wartoscSter), 20), 3)

			if self.pasek:
				self.nowywartoscSter = max(self.nowywartoscSter, (self.wartoscSter+956))
				self.nowywartoscSterOLD = self.nowywartoscSter
				self.nowywartoscSter1 = min(self.nowywartoscSter, (self.wartoscSter + 956))
				self.nowywartoscSter1OLD = self.nowywartoscSter1
			#elif not self.pasek:
				#self.nowywartoscSter = self.nowywartoscSterOLD
				#self.nowywartoscSter1 = self.nowywartoscSter1OLD
			if self.STEER < 0.01 and self.STEER > -0.01:
				self.nowywartoscSter = 956
				self.nowywartoscSter1 = 956
			if self.pasek1 and self.STEER>0:
				pygame.draw.rect(self._display_surf, (self.r, self.g, 0), pygame.Rect(self.wartoscSter+956, 80, 200, 80))
				#pygame.draw.rect(self._display_surf, (self.r, self.g, 0), [self.wartoscSter+956, 80, 200, 80])
			if self.pasek1 and self.STEER < 0:
				pygame.draw.rect(self._display_surf, (self.r, self.g, 0), pygame.Rect(self.wartoscSter + 756, 80, 200, 80))




			#pygame.draw.line(self._display_surf, (self.r, self.g, self.b), [self.nowywartoscSter, 0], [self.nowywartoscSter, 280], 1)
			pygame.draw.line(self._display_surf, (self.r, self.g, self.b), [self.nowywartoscSter1, 0],[self.nowywartoscSter1, 280], 1)


			self._running = True

		def slide(self):
			localVelocityZ = ex.localVelocityZ * 100
			localVelocityX = ex.localVelocityX * 100
			accGX = ex.accGX * 100
			slideRatio = abs(localVelocityX / max(1, localVelocityZ))

			if slideRatio > 0.001 and accGX < -5:
				self.position = self.orygpos -  slideRatio*2500
				self.efektywnosc_skretu = int(self.orygpos + -(self.STEER * (1 - self.wheelFLP)) * 45)

			elif slideRatio > 0.001  and accGX > 5:
				self.position = self.orygpos + slideRatio*2500
				self.efektywnosc_skretu = int(self.orygpos + -(self.STEER * (1 - self.wheelFRP)) * 45)
			else:
				self.position = self.orygpos
				self.efektywnosc_skretu = 955

		def slideTEST(self):
			accGX = ex.accGX * 1000.0
			slideRatioL = ((self.wheelRR - self.wheelFR)) * 100.0
			slideRatioR = ((self.wheelRL - self.wheelFL)) * 100.0

			#if slideRatio > 0.0 and accGX < -1.0 :
			if (self.wheelRR - self.wheelFR) > 0.0 and accGX > 1:
				self.position = self.orygpos - slideRatioL
				#self.efektywnosc_skretu = int(self.orygpos + -(self.STEER * (1 - self.wheelFLP)) * 45)

			elif (self.wheelRL - self.wheelFL) > 0.0 and accGX < -1:
				self.position = self.orygpos + slideRatioR
				#self.efektywnosc_skretu = int(self.orygpos + -(self.STEER * (1 - self.wheelFRP)) * 45)
			else:
				self.position = self.orygpos
				self.efektywnosc_skretu = 955

			#self.steeringlige = pygame.draw.lines(self._display_surf, (color, 0, 0),[[self.efektywnosc_skretu, 0], [int(self.position), 150], [955, 280]], 4)
			#pygame.draw.lines(self._display_surf, (color, 0, 0), False, [[self.efektywnosc_skretu, 0], [int(self.position), 150], [955, 280]], 5)
			pygame.draw.line(self._display_surf, (self.r, self.g, self.b), [int(self.position), 150], [955, 280], 4)
			pygame.draw.line(self._display_surf, (self.r, self.g, self.b), [int(self.position), 0], [int(self.position), 150], 4)
			#pygame.draw.circle(self._display_surf, (0, 0, 0), [self.efektywnosc_skretu, 0], 8)
			self._running = True

		#[240, 260, 30, 60]
	#def on_render(self):
	#	pass


		def ScalePorsche(self):
			pygame.draw.line(self._display_surf, (255, 255, 255), [955, 0], [955, 280], 1)           #   straight scale
			pygame.draw.line(self._display_surf, (self.r, self.g, self.b), [900, 0],[1010, 0], 1)    # upperscale

			pygame.draw.aaline(self._display_surf, (self.r, self.g, self.b), [875, 80], [1035, 80]) #   circle aaline
			pygame.draw.circle(self._display_surf, (self.r,self.g, self.b), [955, 80], 80, 1)       # circle line

			pygame.draw.line(self._display_surf, (255, 255, 0), [855, 150], [400, 900], 4)           #       #border left

			pygame.draw.line(self._display_surf, (255, 255, 0), [1150, 150], [1850, 950], 4)           #       #border right
		def Scale(self):
			pygame.draw.line(self._display_surf, (255, 255, 255), [955, 0], [955, 280], 1)           #   straight scale
			pygame.draw.line(self._display_surf, (self.r, self.g, self.b), [900, 0],[1010, 0], 1)    # upperscale

			pygame.draw.aaline(self._display_surf, (self.r, self.g, self.b), [875, 80], [1035, 80]) #   circle aaline
			pygame.draw.circle(self._display_surf, (self.r,self.g, self.b), [955, 80], 80, 1)       # circle line

			pygame.draw.line(self._display_surf, (255, 255, 0), [845, 80], [0, 900], 4)           #       #border left

			pygame.draw.line(self._display_surf, (255, 255, 0), [1150, 150], [1850, 950], 4)           #       #border right

		def GasFunkcja(self):
			gascolor = 0
			self.GAS1 = (self.GAS*200)
			self.nowyGAS1 = max(self.nowyGAS1, self.GAS1)
			if self.nowyGAS1 == self.GAS1:
				r =0
				g=255
				b=0
			elif self.GAS1 < self.nowyGAS1 * 0.3:
				r=0
				g=255
				b=255
			else:
				r=0
				g=0
				b =255
			self.BRAKE1 = (self.BRAKE * 200)
			dmgCNT1 = pygame.draw.rect(self._display_surf, (r, g, b), [1110, 220, 30, int(-self.GAS1)])
			dmgCNT = pygame.draw.rect(self._display_surf, (255, 0, 0), [1109, 19, 33, 203], 1)
			self.frifrlcolor = min((self.FRiFL*10)*2, 255)
			#print(self.frifrlcolor)
			if self.FRiFL < 2:
				dmgCNT1 = pygame.draw.rect(self._display_surf, (255, 0, 0), [1150, 220, 30, int(-self.BRAKE1)])
				dmgCNT = pygame.draw.rect(self._display_surf, (255, 0, 0), [1149, 19, 32, 203], 1)
			else:
				dmgCNT1 = pygame.draw.rect(self._display_surf, (self.frifrlcolor, self.frifrlcolor, 0), [1150, 220, 30, int(-self.BRAKE1)])
				dmgCNT = pygame.draw.rect(self._display_surf, (self.frifrlcolor, self.frifrlcolor, 0), [1149, 19, 32, 203], 1)
		def RPMy(self):
			if self.GEAR == 1:
				self.maxRPM = max(self.maxRPM, self.RPM)
			self.GearUP = self.maxRPM * 0.93
			self.GearDOWN = self.maxRPM * (0.69 + ((self.GEAR/100)/1.5))
			if self.GEAR == 2 and self.RPM > (self.maxRPM * 0.91):
				pygame.draw.circle(self._display_surf, (255,255, 0), [955, 80], 80, 20) #[955, 80] pozycja
			elif self.RPM > self.GearUP:
				pygame.draw.circle(self._display_surf, (255,255, 255), [955, 80], 80, 20) #[955, 80] pozycja

				if self.RPM > (self.maxRPM * 0.94): #97
					pygame.draw.circle(self._display_surf, (0, 255, 255), [955, 80], 80, 20) #[955, 80] pozycja
			if self.GEAR >=3 and self.RPM < self.GearDOWN:
				pygame.draw.circle(self._display_surf, (255,0, 0), [955, 80], 80, 20)
		def on_cleanup(self):
			pygame.quit()

		def on_execute(self):
			if self.on_init() == False:
				self._running = False

			while (self._running):
				for event in pygame.event.get():
					self.on_event(event)
				self.on_loop()


				#self.on_render()

			self.on_cleanup()


	if __name__ == "__main__":
		theApp = App()
		theApp.on_execute()