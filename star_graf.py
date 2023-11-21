import matplotlib.pyplot as plt
from astropy.io import fits

x_star = []
en_x = []
y_star = []
en_y = []

fot = fits.open('v523cas60s-001(1).fit')
scidata = fot[0].data

star_center = [int(1107), int(1153)]

for i in range(star_center[0] - 20, star_center[0] + 20):
    en_x.append(scidata[star_center[1], i])
    x_star.append(i)

for j in range(star_center[1] - 20, star_center[1] + 20):
    en_y.append(scidata[j, star_center[0]])
    y_star.append(j)

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(x_star, en_x)
plt.xlim(star_center[0] - 20, star_center[0] + 20 )
plt.ylabel('Value')
plt.xlabel("X coord")
plt.title('Value by X')


plt.subplot(1, 2, 2)
plt.plot(y_star, en_y)
plt.xlim(star_center[1] - 20, star_center[1] + 20 )
plt.ylabel('Value')
plt.xlabel("Y coord")
plt.title('Value by Y')
plt.show()