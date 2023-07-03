import numpy as np
from utils.curves import Curves

class Surfaces():
    def bezier(points):
        
            def p(s, t):
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
            
                return [X[0][0],Y[0][0]]

            new_points = []
            for s in np.arange(0, 1.04, 0.04):
                for t in np.arange(0, 1.04, 0.04):
                    new_points.append(p(s,t))
            
            return new_points

    def surfaceFwdDiff(points):
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
                    for B_col in zip(*D)] 
                        for A_row in ETt] 
            
            return D
            
         
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
        
        MB = [
                [-1,3,-3,1],
                [3,-6,3,0],
                [-3,3,0,0],
                [1,0,0,0]
            ]
        
        CX = calculateCoefficients(MB, GBx, MB)
        CY = calculateCoefficients(MB, GBy, MB)
        
        deltas =  1/(20-1)
        deltat =  1/(20-1)
        
        EdeltaS = [[0,0,0,1],
                   [deltas**3,deltas**2,deltas,0],
                   [6*(deltas**3),2*(deltas**2),0,0],
                   [6*(deltas**3),0,0,0]]
        
        EdeltaTt = [[0,0,0,1],
                   [deltat**3,deltat**2,deltat,0],
                   [6*(deltat**3),2*(deltat**2),0,0],
                   [6*(deltat**3),0,0,0]]
        
        EdeltaTt = [[0,deltat**3,6*(deltat**3),6*(deltat**3)],
                    [0,deltat**2,2*(deltat**2),0],
                    [0,deltat,0,0],
                    [1,0,0,0],
                    ]
        
        DDX = createDFM(EdeltaS, CX, EdeltaTt)
        DDY = createDFM(EdeltaS, CY, EdeltaTt)
        
        points =  Curves.fwdDiff(20, 
                                 DDX[0][0], DDX[0][1], DDX[0][2], DDX[0][3],
                                 DDY[0][0], DDY[0][1], DDY[0][2], DDY[0][3]
                                 )

        DDX = createDFM(EdeltaS, CX, EdeltaTt)
        DDY = createDFM(EdeltaS, CY, EdeltaTt)
        DDXt = np.array(DDX).T
        DDYt = np.array(DDY).T
        
        points +=  Curves.fwdDiff(20, 
                                 DDXt[0][0], DDXt[0][1], DDXt[0][2], DDXt[0][3],
                                 DDYt[0][0], DDYt[0][1], DDYt[0][2], DDYt[0][3]
                                 )
        
        
        return points
            
            
            