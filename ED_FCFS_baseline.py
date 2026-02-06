import numpy as np
import random

# the function below takes as input the same client-helper assingments as in EquiD (Y_new)
def ED_FCFS(I, J, T1_times, T2_times, T3_times, T4_times, T5_times, Y_new):
    # implement FCFS
    OB_comp = np.zeros(J) # to track completion time for all clients
    for helper in range(I):
        Y_i = (np.argwhere(Y_new[helper, :] == 1)).astype('int32')
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
                OB_comp[qu[0]] = time_counter + T5_times[qu[0]]
                release_times = np.delete(release_times, ind_sort_release[0])
                Y_i = np.delete(Y_i, ind_sort_release[0])
                fwd_check = np.delete(fwd_check, ind_sort_release[0])
                ind_sort_release = np.argsort(release_times).astype('int32')
                # now delete the client from queue (fwd+bwd completed)
                qu = Y_i[ind_sort_release] # update queue
    

    return OB_comp, max(OB_comp)