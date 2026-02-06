import numpy as np
import random


def BG_policy(I, J, T1_times, T2_times, T3_times, T4_times, T5_times, mem_capacity_helper, mem_footprint):
    # 1st step: assign clients to helpers (load balancing)
    load = np.zeros(I) # tracks the number of assigned clients per helper
    available_memory = np.copy(mem_capacity_helper)
    BG_assign = np.zeros((I,J))
    
    for client in range(J):
        avail_helpers = np.argwhere(available_memory >= mem_footprint[client, 1]).astype('int32').flatten()
        # the if below covers the case where BG cannot find a feasible allocation
        if np.size(avail_helpers) == 0:
            print('no available helpers for client:', client)
        else: 
            ind_least_load = np.argsort(load[avail_helpers]).astype('int32')
            lucky_helper = avail_helpers[ind_least_load][0] # index of the chosen helper (in set I)
            load[lucky_helper] = load[lucky_helper] + 1 # increase the load of the chosen helper by 1
            available_memory[lucky_helper] = available_memory[lucky_helper] - mem_footprint[client, 1]
            BG_assign[lucky_helper, client] = 1 # track the client-helper assign. for balanced greedy 
    
    # 2nd step: implement FCFS
    BG_comp = np.zeros(J) # to track completion time for all clients
    if np.sum(BG_assign) != J:
        print('no feasible client-helper allocation')
    else:
        for helper in range(I):
            Y_i = (np.argwhere(BG_assign[helper, :] == 1)).astype('int32')
            numb_jobs = np.shape(Y_i)[0]
            Y_i = np.reshape(Y_i, (np.shape(Y_i)[0])) # the list of clients (indices) that are assigned to this helper
            release_times = T1_times[Y_i]
            sort_release = np.sort(release_times)
            ind_sort_release = np.argsort(release_times).astype('int32')
            time_counter = 0
            qu = Y_i[ind_sort_release] # queue initialized, INDICES tracing back to the set of clients J
            fwd_check = np.zeros(numb_jobs) # it tracks if fwd is completed or not 
            while np.size(qu) != 0: # while queue is not empty
                if fwd_check[ind_sort_release[0]] == 0: # i.e., we need to schedule the fwd task first
                    if time_counter <= release_times[ind_sort_release[0]]:
                        time_counter = release_times[ind_sort_release[0]] + T2_times[helper, qu[0]]
                    else:
                        time_counter += T2_times[helper, qu[0]]
                    fwd_check[ind_sort_release[0]] = 1 
                    release_times[ind_sort_release[0]] = time_counter + T3_times[qu[0]] 
                    # replacing the release time of this client with the release time of the bwd task:
                    ind_sort_release = np.argsort(release_times).astype('int32')
                    qu = Y_i[ind_sort_release] # update queue
                else:
                    if time_counter <= release_times[ind_sort_release[0]]:
                        time_counter = release_times[ind_sort_release[0]] + T4_times[helper, qu[0]]
                    else:
                        time_counter += T4_times[helper, qu[0]]
                    # track completion time:
                    BG_comp[qu[0]] = time_counter + T5_times[qu[0]]
                    release_times = np.delete(release_times, ind_sort_release[0])
                    Y_i = np.delete(Y_i, ind_sort_release[0])
                    fwd_check = np.delete(fwd_check, ind_sort_release[0])
                    ind_sort_release = np.argsort(release_times).astype('int32')
                    # now delete the client from queue (since fwd+bwd completed)
                    qu = Y_i[ind_sort_release] # update queue
    
    return BG_assign, BG_comp, max(BG_comp)