from utils.object import Object
from globals import displayfile
class File():
    def read(objt_file: str):
        ref_arquivo = open(f'{objt_file}', "r")
        
        objects = []
        v = {}
        i = 1
        for value in ref_arquivo:
            value = value.split(' ')
            if value[0] == 'o':
                objects.append(Object(value[1],-1,[]))
                
            if value[0] == 'v':
                v[i] = (float(value[1]),float(value[2]),float(value[3]))
                i += 1
                
            if value[0] == 'f':
                objects[-1].setType(2)
                for j in range(1, len(value)):
                    v1 = int(value[j].split('/')[0])
                    objects[-1].addPoint(v[v1])

                
            if value[0] == 'p':
                objects[-1].setType(0)
                objects[-1].addPoint(v[int(value[1])])
                
            if value[0] == 'l':
                objects[-1].setType(1)
                objects[-1].addPoint(v[int(value[1])])
                objects[-1].addPoint(v[int(value[2])])
                
            for object in objects:
                displayfile['CW'][object.getName()] = object
                
        ref_arquivo.close()
    
    def write(objt_file: str):
        ref_arquivo = open(objt_file, "w")
        
        i = 1
        for name in displayfile['CW'].keys():
            object = displayfile['CW'][name]
            type  = object.getType()
            points = object.getPoints()
            
            if type == 0:
                ref_arquivo.write(f'o {name}' + "\n")
                ref_arquivo.write(f'v {points[0][0]} {points[0][1]} {points[0][2]}' + "\n")
                ref_arquivo.write(f'p {i}' + "\n")
                i += 1
            
            if type == 1:
                ref_arquivo.write(f'o {name}' + "\n")
                ref_arquivo.write(f'v {points[0][0]} {points[0][1]} {points[0][2]}' + "\n")
                ref_arquivo.write(f'v {points[1][0]} {points[1][1]} {points[1][2]}' + "\n")
                ref_arquivo.write(f'l {i} {i+1}' + "\n")
                i += 2
            
            if type == 2:
                ref_arquivo.write(f'o {name}' + "\n")
                i_before = i
                for v in points:  
                    ref_arquivo.write(f'v {v[0]} {v[1]} {v[2]}' + "\n")
                    i += 1
                
                for j in range(int((i-i_before)/3)):
                    ref_arquivo.write(f'f {j*3+i_before} {j*3+i_before+1} {j*3+i_before+2}' + "\n")
                    
                if (i-i_before)%3 == 2:
                    ref_arquivo.write(f'f {i-2} {i-1}' + "\n")
                
                if (i-i_before)%3 == 1:
                    ref_arquivo.write(f'f {i-1}' + "\n")
            
            
        ref_arquivo.close() 
    





