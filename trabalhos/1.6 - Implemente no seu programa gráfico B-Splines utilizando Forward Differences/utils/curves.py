import numpy as np

class Curves():
    def bezier(points):
            def p(t, p1_k, p2_k, p3_k, p4_k):
                    return p1_k*(2*(t**3) - 3*(t**2) + 1) + p4_k*(-2*(t**3) + 3*(t**2)) + 3*(p2_k - p1_k)*(t**3 - 2*(t**2) + t) + 3*(p4_k - p3_k)*(t**3 - t**2)
            
            new_points = []

            for i in range(int(len(points)/3)):
                    index = i*3
                    p1 = points[index]
                    p2 = points[index+1]
                    p3 = points[index+2]
                    p4 = points[index+3]

                    for t in np.arange(0, 1.001, 0.001):
                            x = p(t, p1[0], p2[0], p3[0], p4[0])
                            y = p(t, p1[1], p2[1], p3[1], p4[1])
                            z = 1
                            new_points.append([x,y,z])
                            
            
            return new_points
    
    def B_Spline(points):
           E = [
                [0, 0, 0, 1],
                [0.000000001, 0.000001, 0.001, 0],
                [0.000000006, 0.000002, 0, 0],
                [0.000000006, 0, 0, 0],
           ]

           M = [
                  [-1/6, 1/2, -1/2, 1/6],
                  [1/2, -1, 1/2, 0],
                  [-1/2, 0, 1/2, 0],
                  [1/6, 2/3, 1/6, 0]
           ]

           curves = []

           for i in range(3, len(points)):
                GX = [
                        [points[i-3][0]],
                        [points[i-2][0]],
                        [points[i-1][0]],
                        [points[i][0]]
                ]

                GY = [
                        [points[i-3][1]],
                        [points[i-2][1]],
                        [points[i-1][1]],
                        [points[i][1]]
                ]

                
                
                CX = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*GX)] 
                                                for A_row in M] 

                CY = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*GY)] 
                                                for A_row in M] 
                DX = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*CX)] 
                                                for A_row in E] 
                DY = [[sum(a * b for a, b in zip(A_row, B_col))  
                                                for B_col in zip(*CY)] 
                                                for A_row in E] 
           
                curves += Curves.fwdDiff(1000, DX[0][0], DX[1][0], DX[2][0], DX[3][0], DY[0][0], DY[1][0], DY[2][0], DY[3][0])

           return curves

    def fwdDiff(n, x, dx, d2x, d3x, y, dy, d2y, d3y):
           points = []
           points.append([x,y])
           
           i = 1
           while i < n:
                i += 1
                x = x + dx
                dx = dx + d2x
                d2x = d2x + d3x

                y = y + dy
                dy = dy + d2y
                d2y = d2y + d3y

                points.append([x,y])
           
           return points
                  

