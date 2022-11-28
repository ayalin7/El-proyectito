from numpy import genfromtxt, array, mean, std, arange
import matplotlib.pyplot as plt
plt.style.use('classic')

#---datos-experimentales----------------------------------------------
data = genfromtxt('datos/giro.txt', skip_header=1)

ang = array([mean(data[:,0]),mean(data[:,1]),mean(data[:,2]),mean(data[:,3]),mean(data[:,4]),mean(data[:,5]),mean(data[:,6]),mean(data[:,7]),mean(data[:,8]),mean(data[:,9])])
err_ang = array([std(data[:,0]),std(data[:,1]),std(data[:,2]),std(data[:,3]),std(data[:,4]),std(data[:,5]),std(data[:,6]),std(data[:,7]),std(data[:,8]),std(data[:,9])])

long = arange(10,110,10)
err_long = [0.05]*10

#---grafico-experimental----------------------------------------------
plt.errorbar(long, ang, xerr=err_long,  yerr=err_ang, fmt='o', color='royalblue', label='datos experimentales')
plt.grid(True)
plt.hlines(360, 0, 120, color='red', label='un giro completo', linestyle='--')
plt.hlines(720, 0, 120, color='darkred', label='dos giros completos', linestyle='--')
plt.xlabel('Longitud $[cm]$')
plt.ylabel('Ángulo de giro $[deg]$')
plt.title('Gráfico de los datos experimentales')

#---guardar----------------------------------------------------------
plt.legend(loc='lower right')
plt.savefig('grafico-datos.pdf')
