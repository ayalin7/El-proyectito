from numpy import genfromtxt, mean, std, array, arange, linspace, diagonal, sin, cos
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.style.use('classic')

#---datos-experimentales----------------------------------------------
data = genfromtxt('datos/giro.txt', skip_header=1)

ang = array([mean(data[:,0]),mean(data[:,1]),mean(data[:,2]),mean(data[:,3]),mean(data[:,4]),mean(data[:,5]),mean(data[:,6]),mean(data[:,7]),mean(data[:,8]),mean(data[:,9])])
err_ang = array([std(data[:,0]),std(data[:,1]),std(data[:,2]),std(data[:,3]),std(data[:,4]),std(data[:,5]),std(data[:,6]),std(data[:,7]),std(data[:,8]),std(data[:,9])])
long = arange(10,110,10)
err_long = [0.05]*10

#---subplots----------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, figsize=(10,5))

#---grafico-experimental----------------------------------------------
ax1.errorbar(long, ang, xerr=err_long,  yerr=err_ang, marker='o', color='royalblue', label='datos experimentales')
ax1.grid(True)
ax1.hlines(360, 0, 120, color='red', label='un giro completo', linestyle='--')
ax1.hlines(720, 0, 120, color='darkred', label='dos giros completos', linestyle='--')
ax1.set_xlabel('Longitud $[cm]$')
ax1.set_ylabel('Ángulo de giro $[deg]$')

#---modelo-------------------------------------------------------------
def f(x, a, b, c, d): 
	modelo = a * b*sin(x) + c*x**d
	return modelo

#---grafico-modelo-----------------------------------------------------
pcurv, pcov = curve_fit(f, long, ang, sigma=1/err_ang, absolute_sigma=True)

longg = linspace(min(long)-10, max(long)+20, len(long)*20)
ax1.plot(longg, f(longg, pcurv[0], pcurv[1], pcurv[2], pcurv[3]), color='g', label='modelo $a\sin(b)$', linewidth=2)

#---grafico-residuos---------------------------------------------------
res = ang - f(long, pcurv[0], pcurv[1], pcurv[2], pcurv[3]) 
ax2.scatter(long, res)

#---graficar-----------------------------------------------------------
plt.title('error a = 2e-5, error b = 1e-9', size=11)
plt.legend(loc='lower right')
plt.savefig('grafico-modelo-asinb.pdf')

