def sizeof_cross_product(dot1,dot2,dot3):
    x1,y1,x2,y2,x3,y3 = *dot1,*dot2,*dot3
    return (x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1) / 2