from numpy import genfromtxt, mean, std, array, arange
import matplotlib.pyplot as plt
plt.style.use('bmh')

data = genfromtxt('Datos/giro.txt', skip_header=1)

ang = array([mean(data[:,0]),mean(data[:,1]),mean(data[:,2]),mean(data[:,3]),mean(data[:,4]),mean(data[:,5]),mean(data[:,6]),mean(data[:,7]),mean(data[:,8]),mean(data[:,9])])
err_ang = array([std(data[:,0]),std(data[:,1]),std(data[:,2]),std(data[:,3]),std(data[:,4]),std(data[:,5]),std(data[:,6]),std(data[:,7]),std(data[:,8]),std(data[:,9])])

long = arange(10,110,10)

plt.errorbar(long, ang, yerr=err_ang, marker='o', label='datos experimentales')
plt.grid(True)
plt.hlines(360, 10, 100, color='orange', label='un giro completo', linestyle='--')
plt.hlines(720, 10, 100, color='red', label='dos giros completos', linestyle='--')
plt.title('Gráfico de ángulo de giro con respecto a la longitud de tiro', size=11)
plt.xlabel('Longitud $[cm]$')
plt.ylabel('Ángulo de giro $[deg]$')

plt.legend(loc='lower right')
plt.savefig('grafico-long-vs-ang.pdf')
