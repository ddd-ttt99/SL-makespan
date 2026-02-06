import cvxpy as cp
import numpy as np
import time
import random
from scenarios_generator import *
from balanced_greedy import *
from ED_FCFS_baseline import *

import gurobipy as gp
# options = {}

# from os import path
np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

DT = np.empty((0, 10)) 

# example values below, to be adjusted for specific scenarios:
for (J,I) in [ (20,1), (30,1), (20,2), (30,2)]:
    a = 1
    b = 3
    rrss = 25
    capcar = 0
    
    (T1_times, T2_times, T3_times, T4_times, T5_times, 
     mem_capacity_helper, mem_footprint, client_conn_type, client_conn_speeds, 
     client_device_type, helper_device_type) = create_scenario(I, J, a, b, rrss, capcar) # I, J defined above
    
    
    pij_new = T2_times + T4_times    
    ass_aux = np.ones(J).astype(int)
    
    # # Define assignment variables (y_{ij})
    # Y = cp.Variable((I, J))
    Y = cp.Variable((I, J), integer = True)
    
    
    # # Define constraints
    constraints = [Y >= 0,
                   Y <= 1,
                   Y @ mem_footprint[:,1] <= mem_capacity_helper.T, # capacity constraint (non extended)
                   cp.sum(Y, axis=0) == 1] # each client is assigned to at least one helper (in practice, exactly one)

    # Define the objective
    obj = cp.Minimize(cp.max(cp.sum(cp.multiply(Y, pij_new), axis=1)))
    if np.sum(mem_footprint[:, 1]) >= np.sum(mem_capacity_helper):
        print('There should be more helpers, capacity and total footpr:', np.sum(mem_capacity_helper), np.sum(mem_footprint[:, 1]))
        DT = np.append(DT, [[I, J, a, b, rrss, capcar, -1, -1, -1, -1]], axis = 0)
        
    else:
        print('capacity and total footpr:', np.sum(mem_capacity_helper), np.sum(mem_footprint[:, 1]))
        try:
            start_time = time.time()
            prob = cp.Problem(obj, constraints)
            prob.solve(solver=cp.SCIP, verbose=False, warm_start=True)
            ## replace SCIP with other solvers compatible with CVXPY for this type of problem, e.g., GUROBI:
            ## check here : https://www.cvxpy.org/tutorial/solvers/index.html
            
            Y_new = np.rint(Y.value).astype(int)
            comp=np.zeros(J) # completion times (set to zero)
            
            for helper in range(I):
                time_counter=0
                Y_i = (np.argwhere(Y_new[helper, :] == 1)).astype('int32')
                Y_i = np.reshape(Y_i, (np.shape(Y_i)[0])) # the list of clients (indices) that are assigned to this helper
                release = T1_times[Y_i] # set of release dates of T2 of the assigned clients
                tthree = T3_times[Y_i]
                tfive = T5_times[Y_i]
                W_j = np.ones(np.shape(Y_i)[0])*np.inf # set to infinity the release dates of the T4 (cannon be processed until T2 is processed)
                Qjobs = -np.sort(-tthree) # T3 times, sorted  in descending order
                ind_Qjobs = (np.argsort(-tthree)).astype('int32')  # indices related to ordering
                Qprimejobs = -np.sort(-tfive) # T5 times, sorted  in descending order
                ind_Qprimejobs = (np.argsort(-tfive)).astype('int32')   # indices related to ordering
                while np.size(Qjobs)!=0 or np.size(Qprimejobs)!=0:
                    time_counter = max(np.concatenate(([time_counter], [min(np.concatenate((release[ind_Qjobs], W_j[ind_Qprimejobs])))])))
                    if np.size(Qjobs)!= 0 and time_counter >= min(release[ind_Qjobs]):
                        # first we find the indices of clients whose release date of T2 is <= time_counter
                        ind_rele_t = np.argwhere(release[ind_Qjobs]<=time_counter).astype('int32').flatten().tolist()
                        # I assign the T2 of the first element (client) of the list above: ind_rele_t[0]
                        temp1 = Y_i[ind_Qjobs] # temporary variable 
                        ind_temp1 = temp1[ind_rele_t[0]] # the index of the job in set I (tracing it back to Y_i)
                        time_counter += T2_times[helper, ind_temp1]
                        lala = ind_Qjobs[ind_rele_t[0]]
                        W_j[lala] = time_counter + T3_times[ind_temp1]
                        Qjobs = np.delete(Qjobs, ind_rele_t[0])
                        ind_Qjobs = np.delete(ind_Qjobs, ind_rele_t[0])
                    else:
                        ind_wj_t = np.argwhere(W_j[ind_Qprimejobs]<=time_counter).astype('int32').flatten().tolist()
                        temp2 = Y_i[ind_Qprimejobs] # temporary variable
                        ind_temp2 = temp2[ind_wj_t[0]] # the index of the job in set I
                        Qprimejobs = np.delete(Qprimejobs, ind_wj_t[0])
                        ind_Qprimejobs = np.delete(ind_Qprimejobs, ind_wj_t[0])
                        time_counter += T4_times[helper, ind_temp2]
                        comp[ind_temp2] = time_counter + T5_times[ind_temp2] # set completion time
                    
             
            print("--- %s seconds ---" % (time.time() - start_time))
            tt = time.time() - start_time
            # makespan achieved by EquiD policy:
            print('the makespan is...', max(comp))
        
            # now balanced-greedy:
            (BG_assign, BG_comp, COMP) = BG_policy(I, J, T1_times, T2_times, T3_times, T4_times, T5_times, mem_capacity_helper, mem_footprint)
            print(' ^^^ balanced-greedy completion', COMP, np.sum(BG_comp==0))
            
            # now ED-FCFS baseline:
            (OB_comp, OB_makespan)= ED_FCFS(I, J, T1_times, T2_times, T3_times, T4_times, T5_times, Y_new)
            
            DT = np.append(DT, [[I, J, a, b, rrss, capcar, tt, max(comp), COMP, OB_makespan]], axis = 0)
        
    
        except:
            print('an error occured')
            DT = np.append(DT, [[I, J, a, b, rrss, capcar, -1, -1, -1, -1]], axis = 0)
            
        
#np.savetxt('results.txt', DT, fmt='%.2f', delimiter=' ', newline='\n')