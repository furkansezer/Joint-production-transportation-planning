# Joint-production-transportation-planning

The objective is comprised of sum of total production cost and total transportation cost with $20$ percent premium. We have three decision variables. $x_{plm}$ denotes production quantity at plant $p$ in line $l$ and in month $m$. We call $y_{pm}$ as base production at plant $p$ and month $m$ which is used enforce "equal-wear-and-tear." $s_{prm}$ denotes shipped amount of toys from plant $p$ to retail store r in month $m.$ We have several parameters. $ECPU_{pl}$  is electricity cost per unit at plant $p$ in line $l.$ $SUC_{pr}$ is the unit shipping cost from plant $p$ to retail store $r.$ $UPH_{pl}$ is the number of units produced at plant $p$ in line $l.$ We have several sets. P denotes plants, $L$ denotes production lines, $R$ denotes retail stores and M denotes months. 

The liner programming model is given as following:

$$\min_{x_{plm}, y_{pm} s_{prm}} \sum_{p=1}^{3} \sum_{l=1}^{3} \sum_{m=1}^{12} ECPU_{pl}x_{plm}+ 1.2\sum_{p=1}^{3} \sum_{r=1}^{8} \sum_{m=1}^{12} SUC_{pr}s_{prm} $$

$$\text{s.t} /; y_{pm}\sum_{l} UPH_{pl}=\frac{1}{3}\sum_{r=1}^{8}D_{rm}, \quad \forall p\in P, m \in M $$

 $$x_{plm}=y_{pm}UPH_{pl}, \quad \forall p\in P ,l \in L, m \in M $$
 $$x_{plm} \leq 160 UPH_{pl}, \quad \forall p\in P ,l \in L,\forall m \in M $$
$$ y_{pm}\sum_{l} UPH_{pl}=\sum_{r=1}^{8} s_{prm}, \quad \forall p \in P, m\in M $$
$$\sum_{p=1}^{3} s_{prm} =D_{rm}, \quad \forall m\in M, r\in R $$
$$x_{plm}\geq 0, \quad \forall p \in P, l\in L, m\in M $$
$$s_{prm}\geq 0, \quad \forall p \in P, r\in R, m\in M $$


Constraints \eqref{eq_current} ensure that every factory produces exactly one third of total demand. Constraints \eqref{eq_wear_tear} ensures "equal-wear-and-tear" policy is enforced. Constraints \eqref{eq_prod} guarantee that production capacity is not exceeded. Constraints \eqref{eq_supp} are the classical supply constraints in transportation problem. Constraints \eqref{eq_demand} are the classical demand constraints in transportation problem \cite{bazaraa2009}. Constraints \eqref{eq_non1} and \eqref{eq_non2} are usual non-negativity constraints. 

We first solved the base model \eqref{eq_obj}-\eqref{eq_non2} which reflects current situation. To answer Question $1$, we removed constraints \eqref{eq_current} and solved the model \eqref{eq_obj}-\eqref{eq_non2}. To answer Question $2$, we replaced all values of parameters $ECPU_{pl}$ and $UPH_{pl}$ to those of fast-prod lines and solved the model \eqref{eq_obj}-\eqref{eq_non2}. For demand data, we considered historical and forecasted demand scenarios.
