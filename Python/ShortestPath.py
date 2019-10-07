#格子点における最短経路の探索アルゴリズム
import numpy as np

#input
f = ["0000000",
     "0s00W00",
     "000W000",
     "00W000g",
     "0000000"] 

#process the input
H = len(f)     #タテ
W = len(f[0])  #よこ
print("H:{},W:{}".format(H, W))

F = -np.ones((H,W))           #何もないマス: -1
for i in range(H):
    for j in range(W):
        if f[i][j] == "s":    #スタート   :  0
            F[i,j] = 0
            (si, sj) = (i, j) 
        elif f[i][j] == "g":  #ゴール    : -5
            F[i,j] = -5
            (gi, gj) = (i, j)
        elif f[i][j] == "W":  #壁       : -8 として F 行列に代入
            F[i,j] = -8
print("initial F")
print(F)

#main algorithm
n = 0
V = [[1,0],[-1,0],[0,1],[0,-1]] #4方向

while F[gi,gj] == -5: #ゴールに p が到達するまで
    
    P = []            #点 p は1stepおきに4方向へ分身する
    #カウントが0のマスをリストアップ
    for i in range(H):
        for j in range(W):
            if F[i,j] == n:
                P.append([i,j])
    print("P:")        
    print(P)
    
    #Pの全ての要素から1マスとなりを n+1 にする
    for p in P:              #今の全ての点pは、
        for v in V:            #4方向に1マス動き
            pi = p[0] + v[0]
            pj = p[1] + v[1]   #進んだ先が
            if 0 <= pi < H and 0 <= pj < W and (F[pi,pj] == -1 or F[pi,pj] == -5):
                F[pi,pj] = n + 1    #Field内 かつ 到達したことのない場所なら、n+1 を代入し移動する
                
    n += 1   #次ステップ

    print("F:")   #pがn回の移動で到達できる範囲は、1→2→3→4→...と波動のように広がっていく
    print(F)
    print("n:",n)
    print("")

print("goalまでの最短距離は",int(F[gi,gj]))