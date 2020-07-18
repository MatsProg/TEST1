import pygame
import win32api
import os
from START import *
import win32gui
import win32con
ex = Example()
import time

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



		def on_init(self):
			icon = pygame.image.load('car.png')
			pygame.display.set_icon(icon)
			pygame.init()
			os.environ['SDL_VIDEO_WINDOW_POS'] = '5, 380' # miejsce okienka
			self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.NOFRAME)
			self._running = True

		def on_event(self, event):
			if event.type == pygame.QUIT:
				self._running = False


		def on_loop(self):


			""" ACC """
			ex.bits()
			spin = ex.wheelSlip

			self.wheelFL = round(max(min(spin[0], 244) - 0.5, 0), 1)
			self.wheelFR = round(max(min(spin[1], 244) - 0.5, 0), 1)
			self.wheelRL = round(max(min(spin[2], 244) - 0.5, 0), 1)
			self.wheelRR = round(max(min(spin[3], 244) - 0.5, 0), 1)
			self.tires = [self.wheelFL, self.wheelFR, self.wheelRL, self.wheelRR]
			self.STEER = ex.STEER
			self.RLiRR = float(self.wheelRL + self.wheelRR) / 2
			FRiFL = min(abs((self.wheelFL + self.wheelFR) / 2) *10, 240)

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

			self.steerbar()
			self.wheelspin()
			self.CarDamage()
			self.slide()

			#self.travel()
			font = pygame.font.SysFont(None, 18)
			fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
			self._display_surf.blit(fps, (0, 0))
			pygame.display.flip()
			clock.tick(30)

			pygame.display.update()
			self._running = True
		def wheelspin(self):

			pygame.draw.rect(self._display_surf, (255, self.wheelRL, 128), pygame.Rect(850, 320, 60, 60),5)
			pygame.draw.rect(self._display_surf, (255, self.wheelRR, 128), pygame.Rect(1000, 320, 60, 60),5)

			pygame.draw.rect(self._display_surf, (255, self.wheelFL, 128), pygame.Rect(850, 200, 60, 60),5)
			pygame.draw.rect(self._display_surf, (255, self.wheelFR, 128), pygame.Rect(1000, 200, 60, 60),5)
			sysfont = pygame.font.get_default_font()
			font = pygame.font.SysFont(None, 48)
			img = font.render(str(self.wheelRL), True, self.RED)
			img1 = font.render(str(self.wheelRR), True, self.RED)
			self.imgwheelspinFL = font.render(str(self.wheelFL), True, self.RED)
			self.imgwheelspinFR = font.render(str(self.wheelFR), True, self.RED)


			self._display_surf.blit(img, (858, 330))
			self._display_surf.blit(img1, (1008, 330))
			if self.wartoscSter > 1:
				wheelspinshowFL = self._display_surf.blit(self.imgwheelspinFL, [956 + self.wartoscSter, 165])  # (858, 210))
			elif self.wartoscSter < -1:
				wheelspinshowFR = self._display_surf.blit(self.imgwheelspinFR, [936 + self.wartoscSter, 165])  # (858, 210))
			#self.wheelspinshowFR = self._display_surf.blit(self.imgwheelspinFR, (1008, 210))
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

		def steerbar(self):
			global wartoscSter
			if (self.wheelFR > 0.9 and self.STEER < -0.15) or (self.wheelFL > 0.9 and self.STEER > 0.15):
				r = 255
				g = 0
				b=0
			elif (self.wheelFR > 0.7 and self.STEER < -0.15) or (self.wheelFL > 0.7 and self.STEER > 0.15):
				r = 255
				g = 255
				b=0
			elif (self.wheelFR > 0.5 and self.STEER < -0.15) or (self.wheelFL > 0.5 and self.STEER > 0.15):
				r = 0
				g = 255
				b =0
			else:
				r= 255
				g= 255
				b=255
			self.wartoscSter = int(self.STEER*900)
			pygame.draw.rect(self._display_surf, (0, 0, 0), pygame.Rect(954, 150, 3, 55)) #dlugosc black pasek
			pygame.draw.rect(self._display_surf, (r, g, b), pygame.Rect(956, 165, self.wartoscSter, 10))
			pygame.draw.rect(self._display_surf, (r, g, 0), pygame.Rect(956, 165, self.wartoscSter, 20), 3)
			self._running = True

		def slide(self):

			localVelocityZ = ex.localVelocityZ * 100
			localVelocityX = ex.localVelocityX * 100
			accGX = ex.accGX * 100
			slideRatio = abs(localVelocityX / max(1, localVelocityZ))

			if slideRatio > 0.001 and accGX < -5:
				self.position = self.orygpos - slideRatio*900
				color = 255
			elif slideRatio > 0.001  and accGX > 5:
				self.position = self.orygpos + slideRatio*900
				color = 255
			else:
				self.position = self.orygpos
				color = 0

			self.steeringlige = pygame.draw.line(self._display_surf, (color, 0, 0), [int(self.position), 000], [955, 280], 4)
			self._running = True
			#print(slideRatio)
			#[240, 260, 30, 60]
		#def on_render(self):
		#	pass




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