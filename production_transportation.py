# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:15:43 2022

@author: furkan
"""

import gurobipy as gp
from gurobipy import GRB

try:
    plants=['p1','p2','p3']
    prod_line=['l1','l2','l3']
    retail_stores=['r1','r2','r3','r4','r5','r6','r7','r8']
    months=['m1','m2','m3', 'm4','m5','m6','m7', 'm8','m9','m10','m11', 'm12']
    
    
    arcs, cost= gp.multidict({
        ('p1', 'r1'):  1.07,    
        ('p1', 'r2'):  1.02,    
        ('p1', 'r3'):  0.63,    
        ('p1', 'r4'):  0.50,   
        ('p1', 'r5'):  0.37,    
        ('p1', 'r6'):  0.33,    
        ('p1', 'r7'):  0.36, 
        ('p1', 'r8'):  0.25,
        ('p2', 'r1'):  0.77,
        ('p2', 'r2'):  1.06,
        ('p2', 'r3'):  0.61,    
        ('p2', 'r4'):  0.19,    
        ('p2', 'r5'):  0.48,    
        ('p2', 'r6'):  0.03,    
        ('p2', 'r7'):  0.41,   
        ('p2', 'r8'):  0.27,
        ('p3', 'r1'):  0.43,    
        ('p3', 'r2'):  0.70,   
        ('p3', 'r3'):  0.63,    
        ('p3', 'r4'):  0.23,    
        ('p3', 'r5'):  0.82,    
        ('p3', 'r6'):  0.36,    
        ('p3', 'r7'):  0.74,    
        ('p3', 'r8'):  0.61})
    
    
    ECPU= {
          ('p1','l1'):  5.000,         
          ('p1','l2'):  19.125,  
          ('p1','l3'):  5.000,         
          ('p2','l1'):  7.560,   
          ('p2','l2'):  22.950,          
          ('p2','l3'):  49.500,        
          ('p3','l1'):  4.950, 
          ('p3','l2'):  7.0500,      
          ('p3','l3'):  54.000}
    
    
    
    
    UPH= {
          ('p1','l1'):  6.0,         
          ('p1','l2'):  2.0,  
          ('p1','l3'):  1.0,         
          ('p2','l1'):  5.0,   
          ('p2','l2'):  2.0,          
          ('p2','l3'):  1.0,        
          ('p3','l1'):  4.0, 
          ('p3','l2'):  3.0,      
          ('p3','l3'):  0.5}
    
    
    m_demand={
        ('m1'):	1425,
        ('m2'):	1475,
        ('m3'):	1525,
        ('m4'):	1575,
        ('m5'):	1450,
        ('m6'):	1480,
        ('m7'):	1430,
        ('m8'):	1500,
        ('m9'):	1300,
        ('m10'): 1475,
        ('m11'): 1875,
        ('m12'): 2300}
    
    demand={
        ('r1',	'm1'):	200,
        ('r1',	'm2'):	150,
        ('r1',	'm3'):	225,
        ('r1',	'm4'):	250,
        ('r1',	'm5'):	250,
        ('r1',	'm6'):	180,
        ('r1',	'm7'):	180,
        ('r1',	'm8'):	200,
        ('r1',	'm9'):	150,
        ('r1',	'm10'):	150,
        ('r1',	'm11'):	200,
        ('r1',	'm12'):	300,
        ('r2',	'm1'):	100,
        ('r2',	'm2'):	125,
        ('r2',	'm3'):	150,
        ('r2',	'm4'):	200,
        ('r2',	'm5'):	175,
        ('r2',	'm6'):	175,
        ('r2',	'm7'):	200,
        ('r2',	'm8'):	150,
        ('r2',	'm9'):	100,
        ('r2',	'm10'):	100,
        ('r2',	'm11'):	75,
        ('r2',	'm12'):	200,
        ('r3',	'm1'):	125,
        ('r3',	'm2'):	100,
        ('r3',	'm3'):	75,
        ('r3',	'm4'):	100,
        ('r3',	'm5'):	75,
        ('r3',	'm6'):	100,
        ('r3',	'm7'):	125,
        ('r3',	'm8'):	200,
        ('r3',	'm9'):	150,
        ('r3',	'm10'):	100,
        ('r3',	'm11'):	150,
        ('r3',	'm12'):	175,
        ('r4',	'm1'):	250,
        ('r4',	'm2'):	300,
        ('r4',	'm3'):	250,
        ('r4',	'm4'):	200,
        ('r4',	'm5'):	200,
        ('r4',	'm6'):	300,
        ('r4',	'm7'):	250,
        ('r4',	'm8'):	300,
        ('r4',	'm9'):	350,
        ('r4',	'm10'):	350,
        ('r4',	'm11'):	400,
        ('r4',	'm12'):	450,
        ('r5',	'm1'):	225,
        ('r5',	'm2'):	200,
        ('r5',	'm3'):	225,
        ('r5',	'm4'):	200,
        ('r5',	'm5'):	250,
        ('r5',	'm6'):	175,
        ('r5',	'm7'):	200,
        ('r5',	'm8'):	150,
        ('r5',	'm9'):	200,
        ('r5',	'm10'):	250,
        ('r5',	'm11'):	300,
        ('r5',	'm12'):	400,
        ('r6',	'm1'):	400,
        ('r6',	'm2'):	425,
        ('r6',	'm3'):	375,
        ('r6',	'm4'):	350,
        ('r6',	'm5'):	300,
        ('r6',	'm6'):	400,
        ('r6',	'm7'):	250,
        ('r6',	'm8'):	200,
        ('r6',	'm9'):	225,
        ('r6',	'm10'):	400,
        ('r6',	'm11'):	500,
        ('r6',	'm12'):	475,
        ('r7',	'm1'):	50,
        ('r7',	'm2'):	75,
        ('r7',	'm3'):	100,
        ('r7',	'm4'):	125,
        ('r7',	'm5'):	75,
        ('r7',	'm6'):	50,
        ('r7',	'm7'):	100,
        ('r7',	'm8'):	150,
        ('r7',	'm9'):	25,
        ('r7',	'm10'):	50,
        ('r7',	'm11'):	150,
        ('r7',	'm12'):	150,
        ('r8',	'm1'):	75,
        ('r8',	'm2'):	100,
        ('r8',	'm3'):	125,
        ('r8',	'm4'):	150,
        ('r8',	'm5'):	125,
        ('r8',	'm6'):	100,
        ('r8',	'm7'):	125,
        ('r8',	'm8'):	150,
        ('r8',	'm9'):	100,
        ('r8',	'm10'):	75,
        ('r8',	'm11'):	100,
        ('r8',	'm12'):	150}
    
    
    plant_cap={
        'p1':9,
        'p2':8,
        'p3':7.5}
    
    m = gp.Model('production_transportation')
    
    # Create variables
    shipment = m.addVars(arcs, months, obj=cost, name="shipment")
    production= m.addVars(plants,prod_line,months,obj=ECPU,name="production")
    base_prod=m.addVars(plants,months,name='base_production')
    
    
    #production assignment to production lines
    
    m.addConstrs(
        (production[i,j,k]==UPH[i,j]*base_prod[i,k] for i in plants for j in prod_line for k in months),name="production_assignment_to_lines")
    
    
    #working hours constraints
    
    m.addConstrs(
        (production[i,j,k]<=160*UPH[i,j] for i in plants for j in prod_line for k in months),"workhours cap")
    
    #supply constraints
    m.addConstrs(
        (shipment.sum(i,'*',k)==base_prod[i,k]*plant_cap[i] for i in plants for k in months),"supply")
    
    #demand constraints
    m.addConstrs(
        (shipment.sum('*',j,k)==demand[j,k] for j in retail_stores for k in months),"supply")
    
    
    #optimize model
    m.optimize()

except gp.GurobiError as e:
    print('Error code'+str(e.errno)+':'+str(e))
    
    
except AttributeError:
    print('Encountered an attribute error')    


# Print solution
if m.Status == GRB.OPTIMAL:
    solution1 = m.getAttr('X', shipment)
    solution2 = m.getAttr('X', production)

    for h in months:
        print('\nOptimal shipments for %s:' % h)
        for i, j in arcs:
             if solution1[i, j, h] > 0:
                print('%s -> %s: %g' % (i, j, solution1[i, j, h]))
    for h in months:
        print('\nOptimal production for %s:' % h)
        for i in plants:
            for j in prod_line:
                 if solution2[i, j, h] > 0:
                    print('%s -> %s: %g' % (i, j, solution2[i, j, h]))                
