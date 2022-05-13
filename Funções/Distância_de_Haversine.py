import math
def haversine(r,l1,f1,l2,f2):
    parte1=(math.sin(math.radians((l2-l1)/2)))**2
    parte2=math.cos(math.radians(l1))* math.cos(math.radians(l2))*(math.sin(math.radians((f2-f1)/2)))**2
    resposta = 2*r*math.asin((parte1+parte2)**0.5)
    return resposta