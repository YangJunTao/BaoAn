# -*- coding: utf-8 -*-

import numpy as np

a = -0.0135099860
deltaX=-1.587043
deltaY=1.303017
K=2.011314156531
matrix = np.matrix('%s %s; %s %s'%(np.cos(a),-np.sin(a), np.sin(a), np.cos(a)))

def getTransform(x, y):
# =============================================================================
#     x2, y2 = np.matrix('-1.587043;1.303017')+(1+1.011314156531)*np.mat('%s %s;%s %s'
#                  %(np.cos(a), np.sin(a), -np.sin(a), np.cos(a)))*np.mat('%s;%s'%(x, y))
# =============================================================================
# =============================================================================
#     x2 = (deltaX+(x*np.cos(a) - y*np.sin(a)))*K
#     y2 = (deltaY+(x*np.cos(a) - y*np.sin(a)))*K
# =============================================================================
    x2 = deltaX + K*np.cos(a)*x - K*np.sin(a)*y
    y2 = deltaY + K*np.sin(a)*x + K*np.cos(a)*y
    #res = np.matrix('%s;%s'%(deltaX, deltaY)) + (1+K)*matrix*np.matrix('%s; %s'%(x, y))
    return x2, y2
