from numpy import *
import matplotlib.pyplot as plt


dx   = 0.1
dt   = 0.01
step = 30
X    = [round(i*dx, 2) for i in range(-int(n/2),int(n/2)+1)]

#計算点数
n = 41

#初期値設定
pl   = 1
rhol = 1
ul   = 0

pr   = 0.1
rhor = 0.125
ur   = 0

e = 2

#初期化
P0   = array([pl]*int(n/2) + [pr]*(n - int(n/2)))
Rho0 = array([rhol]*int(n/2) + [rhor]*(n - int(n/2)))
U0   = array([ul]*int(n/2) + [ur]*(n - int(n/2)))

Q     = zeros((3,n))
Qstar = zeros((3,n))
E     = zeros((3,n))
Estar = zeros((3,n))

#Qの計算（初期値）
Q[0,:] = Rho0                              #rho
Q[1,:] = Rho0 * U0                         #m
Q[2,:] = 0.5 * Rho0 * U0**2 + P0/(1.4-1) #e
print("Q",Q)

#出力用配列
P   = zeros(n)
Rho = zeros(n)
U   = zeros(n)

#MacCormack法メインプログラム
for i in range(step):
    #Pの計算
    P = (1.4-1) * (Q[2,:] - 0.5 * Q[1,:]**2 / Q[0,:])
    #print("P",P)
    
    #Eの計算
    E[0,:] = Q[1,:]
    E[1,:] = (1.4-1) * Q[2,:] + 0.5 * (3-1.4) * Q[2,:]**2 / Q[0,:]
    E[2,:] = 1.4 * Q[2,:] * Q[1,:] / Q[0,:] - 0.5 * (1.4-1) * Q[2,:]**3 / Q[0,:]**2
    #print(E)
    
    #Q*の計算
    for j in range(1,n-1):
        Qstar[:,j] = Q[:,j] - (dt/dx)*(E[:,j] - E[:,j-1])
    Qstar[:,0]   = Q[:,0]     #境界処理
    Qstar[:,n-1] = Q[:,n-1]
    #print("Q*",Qstar)
        
    #E*の計算
    Estar[0,:] = Qstar[1,:]
    Estar[1,:] = (1.4-1) * Qstar[2,:] + 0.5 * (3-1.4) * Qstar[2,:]**2 / Qstar[0,:]
    Estar[2,:] = 1.4 * Qstar[2,:] * Qstar[1,:] / Qstar[0,:] - 0.5 * (1.4-1) * Qstar[2,:]**3 / Qstar[0,:]**2
    #print(Estar)
    
    #Qの計算
    for j in range(1,n-1):
        Q[:,j] = 0.5 * (Q[:,j] + Qstar[:,j]) - 0.5 * (dt/dx)*(E[:,j+1] - E[:,j]) + e * abs(P[j+1] - 2*P[j] + P[j-1]) / abs(P[j+1] + 2*P[j] + P[j-1]) * (Q[:,j+1] - 2*Q[:,j] + Q[:,j-1] )
    print("Q",Q)
    
#状態量計算
Rho = Q[0,:]
U   = Q[1,:] / Q[0,:]
P   = (1.4-1) * (Q[2,:] - 0.5 * Q[1,:]**2 / Q[0,:])   

print(U)
print(P)

print("")
print("t={}における速度・圧力分布".format(step*dt))
plt.plot(X,U)
plt.plot(X,P)
plt.show()