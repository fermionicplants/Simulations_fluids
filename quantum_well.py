##Plotting wavefunctions of a particle in infinite  well potential
import numpy as np
import matplotlib.pyplot as plt

xl=0 #declaring left side potential barrier
L=6
xr=L #declaring right side potential barrier

xx=np.linspace(xl,xr,1000) #points where ψ and ψ*ψ are to be evaluated


A=pow(2/L,0.5) # Normalization constant
def psi(x,n):
    WF=A*np.sin(n*np.pi*x/L) #declaring the wavefunctions
    return WF
yy_1=psi(xx,1)
yy_2=psi(xx,2)
yy_3=psi(xx,3)
yy_4=psi(xx,4)
prob_1=yy_1**2
prob_2=yy_2**2
prob_3=yy_3**2
prob_4=yy_4**2


##Plotting.......
#fig = plt.figure(figsize=(8,4), dpi=100)
plt.subplot(2,2,1)
plt.plot(xx,yy_1,label="$\psi_1$(x)")
plt.plot(xx,prob_1,label="$\psi_1^{*}\psi_1$")
plt.title('Ground state ')
plt.xlabel('x')
plt.grid()
plt.legend()

plt.subplot(2,2,2)
plt.plot(xx,yy_2,label="$\psi_2$(x)")
plt.plot(xx,prob_2,label="$\psi_2^{*}\psi_2$")
plt.title('First excited state ')
plt.xlabel('x')
plt.grid()
plt.legend()

plt.subplot(2,2,3)
plt.plot(xx,yy_3,label="$\psi_3$(x)")
plt.plot(xx,prob_3,label="$\psi_3^{*}\psi_3$")
plt.title('Second excited state ')
plt.xlabel('x')
plt.grid()
plt.legend()

plt.subplot(2,2,4)
plt.plot(xx,yy_4,label="$\psi_4$(x)")
plt.plot(xx,prob_4,label="$\psi_4^{*}\psi_4$")
plt.xlabel('x')
plt.title('Third excited state ')
plt.grid()
plt.legend()

plt.show()
