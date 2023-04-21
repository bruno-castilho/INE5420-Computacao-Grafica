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