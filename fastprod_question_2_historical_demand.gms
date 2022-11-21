Set
   p 'plants' /p1*p3/
   l 'line' /l1*l3/
   r 'retail stores' /r1*r8/
   m 'months'/m1*m12/;


Table SUC(p,r) 'shipping cost per unit'

          r1      r2      r3      r4      r5      r6      r7      r8
p1      1.07    1.02    0.63    0.50    0.37    0.33    0.36    0.25
p2      0.77    1.06    0.61    0.19    0.48    0.03    0.41    0.27
p3      0.43    0.70    0.63    0.23    0.82    0.36    0.74    0.61;

Table UPH(p,l) 'unit per hour'
         l1      l2      l3
p1      6.0     2.0     1.0
p2      5.0     2.0     1.0
p3      4.0     3.0     0.5;

Table f_ecpu(p,l) 'fastprod ECPU'
        l1     l2     l3
 p1  5.625  5.625  5.625
 p2  6.75   6.75   6.75
 p3  3.375  3.375  3.375;



Scalar f_uph 'fastprod UPH' /8/;

Table D(r,m) 'demand'
         m1      m2      m3      m4      m5      m6      m7      m8      m9     m10     m11     m12
r1      200     150     225     250     250     180     180     200     150     150     200     300
r2      100     125     150     200     175     175     200     150     100     100     75      200
r3      125     100     75      100     75      100     125     200     150     100     150     175
r4      250     300     250     200     200     300     250     300     350     350     400     450
r5      225     200     225     200     250     175     200     150     200     250     300     400
r6      400     425     375     350     300     400     250     200     225     400     500     475
r7      50      75      100     125     75      50      100     150     25      50      150     150
r8      75      100     125     150     125     100     125     150     100     75      100     150;

Positive Variables
   x(p,l,m) 'production quantities'
   s(p,r,m) 'shipment quantities'
   y(p,m)   'base production';
Variable
   z_m(m) 'total production and transportation costs at month m'
   z      'total production and transportation costs';


Equation
   cost      'overall cost'
   monthly_cost(m) 'montly cost'
   production_amount(p,l,m) 'production assignment'
   production_base(p,m) 'production goal'
   production_capacity(p,l,m) 'production capacity'
   supply(p,m) 'observe supply limit at plant p'
   demand(r,m) 'satisfy demand at retail store r';

cost..      z =e= sum(m,z_m(m));

monthly_cost(m).. z_m(m)=e=sum((p,l), f_ecpu(p,l)*x(p,l,m))+1.2*sum((p,r), SUC(p,r)*s(p,r,m));

production_amount(p,l,m).. x(p,l,m)=e=UPH(p,l)*y(p,m);

production_base(p,m).. y(p,m)=e=sum(r, D(r,m))/(3*sum(l, UPH(p,l)));

production_capacity(p,l,m).. x(p,l,m)=l=160*f_uph;

supply(p,m).. sum(l, UPH(p,l))*y(p,m)=e=sum(r,s(p,r,m));

demand(r,m).. sum(p,s(p,r,m))=e=D(r,m);

Model dino_toys / all /;

solve dino_toys using lp minimizing z;


display x.l, y.l, s.l,z.l,z_m.l;

