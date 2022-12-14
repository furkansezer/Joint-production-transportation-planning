# Joint-production-transportation-planning

The objective is comprised of sum of total production cost and total transportation cost with $20$ percent premium. There are three decision variables. $x_{plm}$ denotes production quantity at plant $p$ in line $l$ and in month $m$. We call $y_{pm}$ as base production at plant $p$ and month $m$ which is used enforce "equal-wear-and-tear." $s_{prm}$ denotes shipped amount of toys from plant $p$ to retail store r in month $m.$ There are several parameters. $ECPU_{pl}$  is electricity cost per unit at plant $p$ in line $l.$ $SUC_{pr}$ is the unit shipping cost from plant $p$ to retail store $r.$ $UPH_{pl}$ is the number of units produced at plant $p$ in line $l.$ We have several sets. $P$ denotes plants, $L$ denotes production lines, $R$ denotes retail stores and M denotes months. 

The liner programming model is given as following:

$$\min_{x_{plm}, y_{pm} s_{prm}} \sum_{p=1}^{3} \sum_{l=1}^{3} \sum_{m=1}^{12} ECPU_{pl}x_{plm}+ 1.2\sum_{p=1}^{3} \sum_{r=1}^{8} \sum_{m=1}^{12} SUC_{pr}s_{prm}, \quad (1) $$

subject to $$x_{plm}=y_{pm}UPH_{pl}, \quad \forall p\in P ,l \in L, m \in M, \quad (2) $$

$$x_{plm} \leq 160 UPH_{pl}, \quad \forall p\in P ,l \in L,\forall m \in M, \quad (3) $$

$$ y_{pm}\sum_{l} UPH_{pl}=\sum_{r=1}^{8} s_{prm}, \quad \forall p \in P, m\in M, \quad (4) $$

$$\sum_{p=1}^{3} s_{prm} =D_{rm}, \quad \forall m\in M, r\in R, \quad (5) $$

$$x_{plm}\geq 0, \quad \forall p \in P, l\in L, m\in M, \quad (6) $$

$$s_{prm}\geq 0, \quad \forall p \in P, r\in R, m\in M, \quad (7) $$


Constraints (2) ensure "equal-wear-and-tear" policy is enforced. Constraints (3) guarantee that production capacity is not exceeded. Constraints (4) are the classical supply constraints in transportation problem. Constraints (5) are the classical demand constraints in transportation problem (Bazaraa et.al, 2009). Constraints (6) and (7) are usual non-negativity constraints. 

Model is implemented via Gurobi Pyhton API.

## Scenario Analysis (Machine Replacement Invesment Analysis)

Parameters $ECPU_{pl}$ and $UPH_{pl}$ are replaced to those of fast-prod lines i.e new machines and solved the model (1)-(7) to compare with current situation. For demand data, we considered historical and forecasted demand scenarios.
