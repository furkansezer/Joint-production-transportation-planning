Set
   p 'plants' /p1*p3 /
   l 'line' /l1*l3/
   r 'retail stores' /r1*r8 /
   m 'months'/m1*m12/;

Table ECPU(p,l) 'energy cost per unit'
       l1           l2      l3
p1      5.000   19.125  41.250
p2      7.560   22.950  49.500
p3      4.950   7.0500  54.000;

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


Table D(r,m) 'forecasted demand'
        m1      m2      m3      m4      m5      m6      m7      m8      m9      m10     m11     m12
r1      312     312     312     312     312     312     312     312     312     312     312     312
r2      187     187     187     187     187     187     187     187     187     187     187     187
r3      233     233     233     233     233     233     233     233     233     233     233     233
r4      629     629     629     629     629     629     629     629     629     629     629     629
r5      452     452     452     452     452     452     452     452     452     452     452     452
r6      631     631     631     631     631     631     631     631     631     631     631     631
r7      136     136     136     136     136     136     136     136     136     136     136     136
r8      169     169     169     169     169     169     169     169     169     169     169     169;




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

monthly_cost(m).. z_m(m)=e=sum((p,l), ECPU(p,l)*x(p,l,m))+1.2*sum((p,r), SUC(p,r)*s(p,r,m));

production_amount(p,l,m).. x(p,l,m)=e=UPH(p,l)*y(p,m);

production_base(p,m).. y(p,m)=e=sum(r, D(r,m))/(3*sum(l, UPH(p,l)));

production_capacity(p,l,m).. x(p,l,m)=l=160*UPH(p,l);

supply(p,m).. sum(l, UPH(p,l))*y(p,m)=e=sum(r,s(p,r,m));

demand(r,m).. sum(p,s(p,r,m))=e=D(r,m);

Model dino_toys / all /;

solve dino_toys using lp minimizing z;

display x.l,y.l,s.l,z.l,z_m.l;
