import numpy as np
from utils.curves import Curves

class Surfaces():
    def bezier(matrix):
        
            def p(points, s, t):
                MS = [[s**3,s**2,s,1]]
                
                MB = [
                    [-1,3,-3,1],
                    [3,-6,3,0],
                    [-3,3,0,0],
                    [1,0,0,0]
                ]

                GBx = [
                    [points[0][0],points[1][0],points[2][0],points[3][0]],
                    [points[4][0],points[5][0],points[6][0],points[7][0]],
                    [points[8][0],points[9][0],points[10][0],points[11][0]],
                    [points[12][0],points[13][0],points[14][0],points[15][0]]
                ]

                GBy = [
                    [points[0][1],points[1][1],points[2][1],points[3][1]],
                    [points[4][1],points[5][1],points[6][1],points[7][1]],
                    [points[8][1],points[9][1],points[10][1],points[11][1]],
                    [points[12][1],points[13][1],points[14][1],points[15][1]]
                    ]
                
                GBz = [
                    [points[0][2],points[1][2],points[2][2],points[3][2]],
                    [points[4][2],points[5][2],points[6][2],points[7][2]],
                    [points[8][2],points[9][2],points[10][2],points[11][2]],
                    [points[12][2],points[13][2],points[14][2],points[15][2]]
                    ]
                                
                MTt = [[t**3],
                    [t**2],
                    [t],
                    [1]]

                MSXMB = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*MB)] 
                        for A_row in MS] 

                X = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*GBx)] 
                        for A_row in MSXMB] 

                X = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*MB)] 
                        for A_row in X] 

                X = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*MTt)] 
                        for A_row in X] 
                   
                Y = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*GBy)] 
                        for A_row in MSXMB] 

                Y = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*MB)] 
                        for A_row in Y] 

                Y = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*MTt)] 
                        for A_row in Y] 
                
                
                Z = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*GBz)] 
                        for A_row in MSXMB] 

                Z = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*MB)] 
                        for A_row in Z] 

                Z = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*MTt)] 
                        for A_row in Z] 
            
                return [X[0][0],Y[0][0],Z[0][0]]

            points = []
            for line in matrix:
                for s in np.arange(0, 1.04, 0.04):
                    for t in np.arange(0, 1.04, 0.04):
                        points.append(p(line,s,t))
                    
            return points

    def surfaceFwdDiff(matrix):
        def calculateCoefficients(M, G, Mt):
            C = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*G)] 
                        for A_row in M] 
        
            C = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*Mt)] 
                        for A_row in C] 
            
            return C
        
        def createDFM(ES,C,ETt):
            D = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*C)] 
                        for A_row in ES] 
        
            D = [[sum(a * b for a, b in zip(A_row, B_col))  
                    for B_col in zip(*ETt)] 
                        for A_row in D] 
            
            return D
        
        def updateD(D):
            for i in range(3):
                for j in range(4):
                    D[i][j] = D[i][j] + D[i+1][j]

            
        points = []
        for i  in range(len(matrix) - 3):
            for j in range(len(matrix) - 3):
                GBx = [
                        [matrix[i][j][0],matrix[i][j+1][0],matrix[i][j+2][0],matrix[i][j+3][0]],
                        [matrix[i+1][j][0],matrix[i+1][j+1][0],matrix[i+1][j+2][0],matrix[i+1][j+3][0]],
                        [matrix[i+2][j][0],matrix[i+2][j+1][0],matrix[i+2][j+2][0],matrix[i+2][j+3][0]],
                        [matrix[i+3][j][0],matrix[i+3][j+1][0],matrix[i+3][j+2][0],matrix[i+3][j+3][0]]
                    ]

                GBy = [
                        [matrix[i][j][1],matrix[i][j+1][1],matrix[i][j+2][1],matrix[i][j+3][1]],
                        [matrix[i+1][j][1],matrix[i+1][j+1][1],matrix[i+1][j+2][1],matrix[i+1][j+3][1]],
                        [matrix[i+2][j][1],matrix[i+2][j+1][1],matrix[i+2][j+2][1],matrix[i+2][j+3][1]],
                        [matrix[i+3][j][1],matrix[i+3][j+1][1],matrix[i+3][j+2][1],matrix[i+3][j+3][1]]
                    ]

                GBz = [
                        [matrix[i][j][2],matrix[i][j+1][2],matrix[i][j+2][2],matrix[i][j+3][2]],
                        [matrix[i+1][j][2],matrix[i+1][j+1][2],matrix[i+1][j+2][2],matrix[i+1][j+3][2]],
                        [matrix[i+2][j][2],matrix[i+2][j+1][2],matrix[i+2][j+2][2],matrix[i+2][j+3][2]],
                        [matrix[i+3][j][2],matrix[i+3][j+1][2],matrix[i+3][j+2][2],matrix[i+3][j+3][2]]
                    ]
       
                MB = [
                        [-1,3,-3,1],
                        [3,-6,3,0],
                        [-3,3,0,0],
                        [1,0,0,0]
                    ]

                CX = calculateCoefficients(MB, GBx, MB)
                CY = calculateCoefficients(MB, GBy, MB)
                CZ = calculateCoefficients(MB, GBz, MB)
                
                
                deltas =  1/(20-1)
                deltat =  1/(20-1)
                
                EdeltaS = [[0,0,0,1],
                        [deltas**3,deltas**2,deltas,0],
                        [6*(deltas**3),2*(deltas**2),0,0],
                        [6*(deltas**3),0,0,0]]
                
                EdeltaT = [[0,0,0,1],
                        [deltat**3,deltat**2,deltat,0],
                        [6*(deltat**3),2*(deltat**2),0,0],
                        [6*(deltat**3),0,0,0]]
                
                EdeltaTt = [
                    [0, deltat**3,6*(deltat**3),6*(deltat**3)],
                    [0, deltat**2,2*(deltat**2), 0],
                    [0, deltat,0,0],
                    [1,0,0,0]
                ]

                
                
                DDX = createDFM(EdeltaS, CX, EdeltaTt)
                DDY = createDFM(EdeltaS, CY, EdeltaTt)
                DDZ = createDFM(EdeltaS, CZ, EdeltaTt)
                
                for k in range(20):
                    points +=  Curves.fwdDiff(20, 
                                            DDX[0][0], DDX[0][1], DDX[0][2], DDX[0][3],
                                            DDY[0][0], DDY[0][1], DDY[0][2], DDY[0][3],
                                            DDZ[0][0], DDZ[0][1], DDZ[0][2], DDZ[0][3]
                                            )
                    
                    updateD(DDX)
                    updateD(DDY)
                    updateD(DDZ)

                
                
                
                DDX = createDFM(EdeltaS, CX, EdeltaTt)
                DDY = createDFM(EdeltaS, CY, EdeltaTt)
                DDZ = createDFM(EdeltaS, CZ, EdeltaTt)
                
                
                DDXt = np.array(DDX).T
                DDYt = np.array(DDY).T
                DDZt = np.array(DDZ).T
                
                for k in range(20):
                    points +=  Curves.fwdDiff(20, 
                                            DDXt[0][0], DDXt[0][1], DDXt[0][2], DDXt[0][3],
                                            DDYt[0][0], DDYt[0][1], DDYt[0][2], DDYt[0][3],
                                            DDZt[0][0], DDZt[0][1], DDZt[0][2], DDZt[0][3]
                                            )
                    
                    updateD(DDXt)
                    updateD(DDYt)
                    updateD(DDZt)
                    
        return points    



#(0, 0, 0),(0, 100, 0),(0, 200, 0),(0, 300, 0),(100, 0, 0),(100, 100, 100),(100, 200, 100),(100, 300, 0),(200, 0, 0),(200, 100, 100),(200, 200, 100), (200, 300, 0),(300, 0, 0),(300, 100, 0),(300, 200, 0),(300, 300, 0)
#(0, 0, 0),(0, 0, 100),(0, 0, 200),(0, 0, 300),(100, 100, 0),(100, 100, 100),(100, 100, 200),(100, 100, 300),(300, 0, 0),(300, 0, 100),(300, 0, 200),(300, 0, 300),(150, -100, 0),(150, -100, 100),(150, -100, 200),(150, -100, 300)
#(0, 0, 0),(0, 100, 0),(0, 200, 0),(0, 300, 0);(100, 0, 0),(100, 100, 100),(100, 200, 100),(100, 300, 0);(200, 0, 0),(200, 100, 100),(200, 200, 100), (200, 300, 0);(300, 0, 0),(300, 100, 0),(300, 200, 0),(300, 300, 0)
#(0, 0, 0),(0, 0, 100),(0, 0, 200),(0, 0, 300);(100, 100, 0),(100, 100, 100),(100, 100, 200),(100, 100, 300);(300, 0, 0),(300, 0, 100),(300, 0, 200),(300, 0, 300);(150, -100, 0),(150, -100, 100),(150, -100, 200),(150, -100, 300)