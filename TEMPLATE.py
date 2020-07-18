
############# porownanie wartosci
poprzednia_wartosc = -1

for i in range(10):
  print("obecna", i, "poprzednia", poprzednia_wartosc)
  poprzednia_wartosc = i
############# porownanie wartosci  END

#####################################
"""
zrobilem generyczne wykrywanie min i max wychylenia
steerMin = 0
steerMax = 0
to  w starting
a potem nizej normalnie:
steer = joy.x
steerMin = min(steer, steerMin)
steerMax = max(steer, steerMax)
i wystarczy ze raz wychylisz joystick na maksa w lewo, potem na maksa w prawo i masz juz zapisane min/max
"""
#####################################################
