# Makespan Minimization in Split Learning: From Theory to Practice

This code is for the paper “Makespan Minimization in Split Learning: From Theory to Practice”, authors: Robert Ganian, Fionn Mc Inerney, Dimitra Tsigkari, accepted for publication at IEEE INFOCOM 2026.

## Requirements
1. Python 3
2. Libraries: numpy, cvxpy, time, gurobipy
3. Testbed measurements available here: [1], [2]
4. Gurobi license 

## Code
The following scripts contain the functions and the code for evaluation.
- scenarios_generator.py contains the function to generate scenarios for the different time measurements, heterogeneity levels, etc. 
- code_for_evaluation.py contains the code for the proposed algorithm (EquiD). The code uses the CVXPY library and multiple solvers (e.g., SCIP and Gurobi) can be used subject to licensing.
- code_for_evaluation_gurobi.py contains the code for the proposed algorithm (EquiD) that uses gurobipy (i.e., the Gurobi Python interface). Information on gurobipy can be found here: [3].
- ED_FCFS_baseline.py contains the code for the ED-FCFS baseline. 
- balanced_greedy.py contains the code for balanced-greedy method proposed in [2]. This code is based on the implementation available at [1] and adapted for our problem parameters. Please note that the implementation of the optimal solution of GENSL-MAKESPAN is based on the code of this paper as well.

## References 
[1] https://github.com/jtirana98/SFL-workflow-optimization \
[2] J. Tirana, D. Tsigkari, G. Iosifidis, and D. Chatzopoulos, “Workflow optimization for parallel split learning,” in Proc. of INFOCOM 2024-IEEE Conference on Computer Communications, pp. 1331–1340, 2024 \
[3] https://www.gurobi.com/faqs/gurobipy/



## Citation
If you find this repository useful, please cite our paper:

```
@inproceedings{ganian2026makespan,
  title     = {Makespan Minimization in Split Learning: From Theory to Practice},
  author={Ganian, Robert and Mc~Inerney, Fionn and Tsigkari, Dimitra},
  booktitle={To appear in Proc. of IEEE INFOCOM 2026-IEEE Conference on Computer Communications},
  year      = {2026}
}
```

## Acknowledgements
This work was funded by the Austrian Science Fund (FWF) [10.55776/Y1329 and 10.55776/COE12], the WWTF Vienna Science and Technology Fund (Project 10.47379/ICT22029), the Smart Networks and Services Joint Undertaking (SNS JU) under the European Union’s Horizon Europe and innovation programme under Grant Agreement No 101139067 (ELASTIC), and the Horizon MSCA Postdoctoral Fellowship OPALS (grant agreement 101210495).
