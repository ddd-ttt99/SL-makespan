import numpy as np
import random

# from os import path
np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

def create_scenario( I, J, a, b, rrss, capcar):
    """
    Parameters
    ----------
    I : number of helpers
    J : number of clients
    a : model and dataset used (1 for ResNet101-CIFAR, 2 for ResNet101-MNIST, 
                                3 for VGG19-CIFAR, 4 for VGG19-MNIST)
    b : heterogeneity level of the instance (1 to 4, 1 for low heterogeneity)
    rrss: random seed
    capcar: 1 for cardinality constraints

    Returns
    -------
    Scenario's parameters (times T1-T5, connectivity info between helpers and clients, type of devices, etc.)

    """
    
    # random seed 
    np.random.seed(rrss)
    
    
    # NOTE: each tab of the excel sheets (of the testbed measurements) has been saved as text (tab delimited) and 
    # the file name is of the form: model_dataset_[device type or memory].txt
    if a == 1:
        fhand = open('resnet101_CIFAR_VM.txt')
        VM=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            VM = np.append(VM, [[float(s) for s in li]], axis=0)
            
        VM = np.c_[VM[:,0], VM[:,1]+VM[:,2]]
        VM = np.rint(VM).astype(int) # we assume that proc. times are integers (rounding)
       
    
        fhand = open('resnet101_CIFAR_laptop.txt')
        laptop=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            laptop = np.append(laptop, [[float(s) for s in li]], axis=0)
    
        laptop = np.c_[laptop[:,0], laptop[:,1]+laptop[:,2]]
        laptop = np.rint(laptop).astype(int)
        
    
        fhand = open('resnet101_CIFAR_d1.txt')
        d1=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            d1 = np.append(d1, [[float(s) for s in li]], axis=0)
    
        d1 = np.c_[d1[:,0], d1[:,1]+d1[:,2]]
        d1 = np.rint(d1).astype(int)
    
    
        fhand = open('resnet101_CIFAR_d2.txt')
        d2=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            d2 = np.append(d2, [[float(s) for s in li]], axis=0)
    
        d2 = np.c_[d2[:,0], d2[:,1]+d2[:,2]]
        d2 = np.rint(d2).astype(int)
    
    
        fhand = open('resnet101_CIFAR_jetsoncpu.txt')
        jcpu=np.empty((0,3), float)
    
    
        for line in fhand:
            li = line.split()
            jcpu = np.append(jcpu, [[float(s) for s in li]], axis=0)
    
        jcpu = np.c_[jcpu[:,0], jcpu[:,1]+jcpu[:,2]]
        jcpu = np.rint(jcpu).astype(int)
    
    
        fhand = open('resnet101_CIFAR_jetsongpu.txt')
        jgpu=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            jgpu = np.append(jgpu, [[float(s) for s in li]], axis=0)
    
        jgpu = np.c_[jgpu[:,0], jgpu[:,1]+jgpu[:,2]]
        jgpu = np.rint(jgpu).astype(int)
    
        fhand = open('resnet101_CIFAR_memory.txt')
        memory=np.empty((0,2), float)
        for line in fhand:
            li = line.split()
            memory = np.append(memory, [[float(s) for s in li]], axis=0)
    
        memory = np.rint(memory).astype(int)
        
        
    elif a == 2:
        fhand = open('resnet101_MNIST_VM.txt')
        VM=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            VM = np.append(VM, [[float(s) for s in li]], axis=0)
            
        VM = np.c_[VM[:,0], VM[:,1]+VM[:,2]]
        VM = np.rint(VM).astype(int) 
        
    
        fhand = open('resnet101_MNIST_laptop.txt')
        laptop=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            laptop = np.append(laptop, [[float(s) for s in li]], axis=0)
    
        laptop = np.c_[laptop[:,0], laptop[:,1]+laptop[:,2]]
        laptop = np.rint(laptop).astype(int)
        
    
        fhand = open('resnet101_MNIST_d1.txt')
        d1=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            d1 = np.append(d1, [[float(s) for s in li]], axis=0)
    
        d1 = np.c_[d1[:,0], d1[:,1]+d1[:,2]]
        d1 = np.rint(d1).astype(int)
    
    
        fhand = open('resnet101_MNIST_d2.txt')
        d2=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            d2 = np.append(d2, [[float(s) for s in li]], axis=0)
    
        d2 = np.c_[d2[:,0], d2[:,1]+d2[:,2]]
        d2 = np.rint(d2).astype(int)
       
    
    
        fhand = open('resnet101_MNIST_memory.txt')
        memory=np.empty((0,2), float)
        for line in fhand:
            li = line.split()
            memory = np.append(memory, [[float(s) for s in li]], axis=0)
    
        memory = np.rint(memory).astype(int)
        
        
    elif a == 3:
        fhand = open('vgg19_CIFAR_VM.txt')
        VM=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            VM = np.append(VM, [[float(s) for s in li]], axis=0)
            
        VM = np.c_[VM[:,0], VM[:,1]+VM[:,2]]
        VM = np.rint(VM).astype(int) 
    
        fhand = open('vgg19_CIFAR_laptop.txt')
        laptop=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            laptop = np.append(laptop, [[float(s) for s in li]], axis=0)
    
        laptop = np.c_[laptop[:,0], laptop[:,1]+laptop[:,2]]
        laptop = np.rint(laptop).astype(int)
        
    
        fhand = open('vgg19_CIFAR_d1.txt')
        d1=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            d1 = np.append(d1, [[float(s) for s in li]], axis=0)
    
        d1 = np.c_[d1[:,0], d1[:,1]+d1[:,2]]
        d1 = np.rint(d1).astype(int)
    
    
        fhand = open('vgg19_CIFAR_d2.txt')
        d2=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            d2 = np.append(d2, [[float(s) for s in li]], axis=0)
    
        d2 = np.c_[d2[:,0], d2[:,1]+d2[:,2]]
        d2 = np.rint(d2).astype(int)
    
    
        fhand = open('vgg19_CIFAR_jetsoncpu.txt')
        jcpu=np.empty((0,3), float)
    
    
        for line in fhand:
            li = line.split()
            jcpu = np.append(jcpu, [[float(s) for s in li]], axis=0)
    
        jcpu = np.c_[jcpu[:,0], jcpu[:,1]+jcpu[:,2]]
        jcpu = np.rint(jcpu).astype(int)
    
    
        fhand = open('vgg19_CIFAR_jetsongpu.txt')
        jgpu=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            jgpu = np.append(jgpu, [[float(s) for s in li]], axis=0)
    
        jgpu = np.c_[jgpu[:,0], jgpu[:,1]+jgpu[:,2]]
        jgpu = np.rint(jgpu).astype(int)
    
        fhand = open('vgg19_CIFAR_memory.txt')
        memory=np.empty((0,2), float)
        for line in fhand:
            li = line.split()
            memory = np.append(memory, [[float(s) for s in li]], axis=0)
    
        memory = np.rint(memory).astype(int)
        
        
    elif a == 4:
        fhand = open('vgg19_MNIST_VM.txt')
        VM=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            VM = np.append(VM, [[float(s) for s in li]], axis=0)
            
        VM = np.c_[VM[:,0], VM[:,1]+VM[:,2]]
        VM = np.rint(VM).astype(int) 
    
        fhand = open('vgg19_MNIST_laptop.txt')
        laptop=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            laptop = np.append(laptop, [[float(s) for s in li]], axis=0)
    
        laptop = np.c_[laptop[:,0], laptop[:,1]+laptop[:,2]]
        laptop = np.rint(laptop).astype(int)
        
    
        fhand = open('vgg19_MNIST_d1.txt')
        d1=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            d1 = np.append(d1, [[float(s) for s in li]], axis=0)
    
        d1 = np.c_[d1[:,0], d1[:,1]+d1[:,2]]
        d1 = np.rint(d1).astype(int)
    
    
        fhand = open('vgg19_MNIST_d2.txt')
        d2=np.empty((0,3), float)
        for line in fhand:
            li = line.split()
            d2 = np.append(d2, [[float(s) for s in li]], axis=0)
    
        d2 = np.c_[d2[:,0], d2[:,1]+d2[:,2]]
        d2 = np.rint(d2).astype(int)
       
        fhand = open('vgg19_MNIST_memory.txt')
        memory=np.empty((0,2), float)
        for line in fhand:
            li = line.split()
            memory = np.append(memory, [[float(s) for s in li]], axis=0)
    
        memory = np.rint(memory).astype(int)
        
        
    if b == 1:
        
        # device type of clients
        client_device_type = np.zeros(J).astype(int) 
        # 0 for d1 (in case of a single type of device)
        # client_device_type = np.random.randint(0,2, size=J) 
        # 0 for d1, 1 for d2 (for 2 diff. types of devices)
        
        # device type of helpers
        helper_device_type = np.random.randint(0,2, size=I) 
        # 0 for VM, 1 for laptop
        
        
        if a == 1 or a == 2:
            # for d2 and ResNet-CIFAR, split_1 could be 2 or 3 and split_2 could be 35
            split_1 = (np.ones(J)*3).astype(int)
            split_2 = (np.ones(J)*35).astype(int)

        
        else:
            split_1 = (np.ones(J)*3).astype(int)
            split_2 = (np.ones(J)*24).astype(int)
            
    elif b == 2:
        if a == 1 or a == 3:
            # device type of clients
            client_device_type = np.random.randint(0,4, size=J) 
            # 0 for d1, 1 for d2, 2 for jcpu, 3 for jgpu
        else: 
            # device type of clients
            client_device_type = np.random.randint(0,2, size=J) 
            # 0 for d1, 1 for d2
        
        # device type of helpers
        helper_device_type = np.random.randint(0,2, size=I) 
        # 0 for VM, 1 for laptop

        
        if a == 1 or a == 2:
            # for d2 and ResNet-CIFAR, split_1 could be 2 or 3 and split_2 could be 35
            split_1 = (np.ones(J)*3).astype(int)
            split_2 = (np.ones(J)*35).astype(int)
        
        else:
            split_1 = (np.ones(J)*3).astype(int)
            split_2 = (np.ones(J)*24).astype(int)
            
    elif b == 3 or b == 4:
        if a == 1 or a == 3:
            # device type of clients
            client_device_type = np.random.randint(0,4, size=J) 
            # 0 for d1, 1 for d2, 2 for jcpu, 3 for jgpu
        else: 
            # device type of clients
            client_device_type = np.random.randint(0,2, size=J) 
            # 0 for d1, 1 for d2
        
        # device type of helpers
        helper_device_type = np.random.randint(0,2, size=I) 
        # 0 for VM, 1 for laptop
           
        if a == 1:
            
            split_1 = np.random.randint(2,10, size=J)
            split_2 = np.random.randint(27,35, size=J)
            
            # NOTE: some restrictions may apply for some devices (based on the measurements) that can be adjusted as in the examples below: 
            for j in range(J):
                if client_device_type[j] == 1 or client_device_type[j] == 2:
                    split_1[j] = 2+np.random.randint(0,2) # 2 or 3
                    split_2[j] = 34+np.random.randint(0,2) # 34 or 35
        
        elif a == 2: 
            split_1 = np.random.randint(2,10, size=J)
            split_2 = np.random.randint(27,35, size=J)

            for j in range(J):
                if client_device_type[j] == 1:
                    split_1[j] = 3+np.random.randint(0,2)*2 # 3 or 5
                    split_2[j] = 34
                    
        elif a == 3:
            split_1 = np.random.randint(2,10, size=J)
            split_2 = np.random.randint(20,24, size=J)
            for j in range(J):
                if client_device_type[j] == 2:
                    split_1[j] = 1
                    split_2[j] = 24
            for j in range(J):
                if client_device_type[j] == 1:
                    split_1[j] = 3
                    split_2[j] = 24
            for j in range(J):
                if client_device_type[j] == 0:
                    split_1[j] = 1
                    split_2[j] = 24
        

                    
        elif a == 4:
            split_1 = np.random.randint(2,10, size=J)
            split_2 = np.random.randint(20,24, size=J)
            
            for j in range(J):
                if client_device_type[j] == 1:
                    #split_1[j] = 5+np.random.randint(0,2)*2 # 5 or 7
                    split_1[j] = 5 # 5 
                    split_2[j] = 24
                    
    # calculating transmission delays
    data_to_helper = memory[split_1 - 1][0]
    data_to_client = memory[split_2 - 1][0]

    '''
    Connectivity classes (for Germany) [Akamai connectivity report]:

    class-0        >=2 and < 4 Mbps  --> 11%
    class-1        >=4 and < 10   --> 39%
    class-2        >=10 and < 15  --> 20%
    class-3        >= 15 and < 45 --> 30%
    average speed = 14.56 as in Akamai report
    '''

   
    num_class0 = int(J*0.11)
    num_class1 = int(J*0.39)
    num_class2 = int(J*0.2)
    num_class3 = J - num_class0 - num_class1 - num_class2


    client_conn_type = [0]*num_class0+[1]*num_class1+[2]*num_class2+[3]*num_class3
    client_conn_type = np.array(client_conn_type)

    class0_speeds = np.random.randint(2,4,size=num_class0)
    class1_speeds = np.random.randint(4,10,size=num_class1)
    class2_speeds = np.random.randint(10,15,size=num_class2)
    class3_speeds = np.random.randint(15,45,size=num_class3)
        
    client_conn_speeds = np.concatenate((class0_speeds, class1_speeds, class2_speeds, class3_speeds), axis=None)
    
    # shuffle clients since right now slow clients are always the first ones
    shuff = np.random.permutation(J)

    client_conn_speeds = (client_conn_speeds[shuff])
    client_conn_type = (client_conn_type[shuff])
    
    T1_times=np.zeros(J).astype(int)
    T3_times=np.zeros(J).astype(int)
    T5_times=np.zeros(J).astype(int)
    T2_times = np.zeros([I,J]).astype(int)
    T4_times = np.zeros([I,J]).astype(int)
    
    mem_footprint = np.zeros([J,2]).astype(int) # first column for client, second for helper
    
    if b <= 3:
        mem_capacity_helper = (np.ones(I)*16000).astype(int) # for Mbytes
        for client in range(J):
            for i in range(split_1[client], split_2[client]):
                mem_footprint[client][1] += memory[i][0] + memory[i][1]
            if client_device_type[client] == 0:
                for i in range(0, split_1[client]):
                    T1_times[client] += d1[i][0]
                    T5_times[client] += d1[i][1]
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                #now we add the time needed to send the activations
                T1_times[client] += memory[split_1[client]-1][0]*0.008/client_conn_speeds[client]*1000
                # multiplied by 0.008 to convert Kbyte into Mbit and multiplied with 1000 to 
                # have the time in msec
                T5_times[client] += memory[split_1[client]][0]*0.008/client_conn_speeds[client]*1000
                for i in range(split_2[client],len(d1)):
                    T3_times[client] += d1[i][0] + d1[i][1]
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                # now we add the transmission times
                T3_times[client] += memory[split_2[client]-1][0]*0.008/client_conn_speeds[client]*1000
                T3_times[client] += memory[split_2[client]][0]*0.008/client_conn_speeds[client]*1000
            elif client_device_type[client] == 1:
                for i in range(0, split_1[client]):
                    T1_times[client] += d2[i][0]
                    T5_times[client] += d2[i][1]
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                #now we add the time needed to send the activations
                T1_times[client] += memory[split_1[client]-1][0]*0.008/client_conn_speeds[client]*1000
                # multiplied by 0.008 to convert Kbyte into Mbit and multiplied with 1000 to 
                # have the time in msec
                T5_times[client] += memory[split_1[client]][0]*0.008/client_conn_speeds[client]*1000
                for i in range(split_2[client],len(d2)):
                    T3_times[client] += d2[i][0] + d2[i][1]
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                # now we add the transmission times
                T3_times[client] += memory[split_2[client]-1][0]*0.008/client_conn_speeds[client]*1000
                T3_times[client] += memory[split_2[client]][0]*0.008/client_conn_speeds[client]*1000
            elif client_device_type[client] == 2:
                for i in range(0, split_1[client]):
                    T1_times[client] += jcpu[i][0]
                    T5_times[client] += jcpu[i][1]
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                #now we add the time needed to send the activations
                T1_times[client] += memory[split_1[client]-1][0]*0.008/client_conn_speeds[client]*1000
                # multiplied by 0.008 to convert Kbyte into Mbit and multiplied with 1000 to 
                # have the time in msec
                T5_times[client] += memory[split_1[client]][0]*0.008/client_conn_speeds[client]*1000
                for i in range(split_2[client],len(jcpu)):
                    T3_times[client] += jcpu[i][0] + jcpu[i][1]
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                # now we add the transmission times
                T3_times[client] += memory[split_2[client]-1][0]*0.008/client_conn_speeds[client]*1000
                T3_times[client] += memory[split_2[client]][0]*0.008/client_conn_speeds[client]*1000
            elif client_device_type[client] == 3:
                for i in range(0, split_1[client]):
                    T1_times[client] += jgpu[i][0]
                    T5_times[client] += jgpu[i][1]
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                #now we add the time needed to send the activations
                T1_times[client] += memory[split_1[client]-1][0]*0.008/client_conn_speeds[client]*1000
                # multiplied by 0.008 to convert Kbyte into Mbit and multiplied with 1000 to 
                # have the time in msec
                T5_times[client] += memory[split_1[client]][0]*0.008/client_conn_speeds[client]*1000
                for i in range(split_2[client],len(jgpu)):
                    T3_times[client] += jgpu[i][0] + jgpu[i][1]
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                # now we add the transmission times
                T3_times[client] += memory[split_2[client]-1][0]*0.008/client_conn_speeds[client]*1000
                T3_times[client] += memory[split_2[client]][0]*0.008/client_conn_speeds[client]*1000
            for helper in range(I):
                if helper_device_type[helper] == 0:
                    for i in range(split_1[client], split_2[client]):
                        T2_times[helper, client] += VM[i][0]
                        T4_times[helper, client] += VM[i][1]
                elif helper_device_type[helper] == 1:
                    for i in range(split_1[client], split_2[client]):
                        T2_times[helper, client] += laptop[i][0]
                        T4_times[helper, client] += laptop[i][1]
                        
    else:
        for client in range(J):
            for i in range(split_1[client], split_2[client]):
                mem_footprint[client][1] += memory[i][0] + memory[i][1]
            if client_device_type[client] == 0:
                for i in range(0, split_1[client]):
                    T1_times[client] += np.random.randint(min(d1[:,0]),max(d1[:,0]))
                    T5_times[client] += np.random.randint(min(d1[:,1]),max(d1[:,1]))
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                #now we add the time needed to send the activations
                T1_times[client] += memory[split_1[client]-1][0]*0.008/client_conn_speeds[client]*1000
                # multiplied by 0.008 to convert Kbyte into Mbit and multiplied with 1000 to 
                # have the time in msec
                T5_times[client] += memory[split_1[client]][0]*0.008/client_conn_speeds[client]*1000
                for i in range(split_2[client],len(d1)):
                    T3_times[client] += np.random.randint(min(d1[:,0]),max(d1[:,0])) + np.random.randint(min(d1[:,1]),max(d1[:,1]))
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                # now we add the transmission times
                T3_times[client] += memory[split_2[client]-1][0]*0.008/client_conn_speeds[client]*1000
                T3_times[client] += memory[split_2[client]][0]*0.008/client_conn_speeds[client]*1000
            elif client_device_type[client] == 1:
                for i in range(0, split_1[client]):
                    T1_times[client] += np.random.randint(min(d2[:,0]),max(d2[:,0]))
                    T5_times[client] += np.random.randint(min(d2[:,1]),max(d2[:,1]))
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                #now we add the time needed to send the activations
                T1_times[client] += memory[split_1[client]-1][0]*0.008/client_conn_speeds[client]*1000
                # multiplied by 0.008 to convert Kbyte into Mbit and multiplied with 1000 to 
                # have the time in msec
                T5_times[client] += memory[split_1[client]][0]*0.008/client_conn_speeds[client]*1000
                for i in range(split_2[client],len(d2)):
                    T3_times[client] += np.random.randint(min(d2[:,0]),max(d2[:,0])) + np.random.randint(min(d2[:,1]),max(d2[:,1]))
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                # now we add the transmission times
                T3_times[client] += memory[split_2[client]-1][0]*0.008/client_conn_speeds[client]*1000
                T3_times[client] += memory[split_2[client]][0]*0.008/client_conn_speeds[client]*1000
            elif client_device_type[client] == 2:
                for i in range(0, split_1[client]):
                    T1_times[client] += np.random.randint(min(jcpu[:,0]),max(jcpu[:,0]))
                    T5_times[client] += np.random.randint(min(jcpu[:,1]),max(jcpu[:,1]))
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                #now we add the time needed to send the activations
                T1_times[client] += memory[split_1[client]-1][0]*0.008/client_conn_speeds[client]*1000
                # multiplied by 0.008 to convert Kbyte into Mbit and multiplied with 1000 to 
                # have the time in msec
                T5_times[client] += memory[split_1[client]][0]*0.008/client_conn_speeds[client]*1000
                for i in range(split_2[client],len(jcpu)):
                    T3_times[client] += np.random.randint(min(jcpu[:,0]),max(jcpu[:,0])) + np.random.randint(min(jcpu[:,1]),max(jcpu[:,1]))
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                # now we add the transmission times
                T3_times[client] += memory[split_2[client]-1][0]*0.008/client_conn_speeds[client]*1000
                T3_times[client] += memory[split_2[client]][0]*0.008/client_conn_speeds[client]*1000
            elif client_device_type[client] == 3:
                for i in range(0, split_1[client]):
                    T1_times[client] += np.random.randint(min(jgpu[:,0]),max(jgpu[:,0]))
                    T5_times[client] += np.random.randint(min(jgpu[:,1]),max(jgpu[:,1]))
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                #now we add the time needed to send the activations
                T1_times[client] += memory[split_1[client]-1][0]*0.008/client_conn_speeds[client]*1000
                # multiplied by 0.008 to convert Kbyte into Mbit and multiplied with 1000 to 
                # have the time in msec
                T5_times[client] += memory[split_1[client]][0]*0.008/client_conn_speeds[client]*1000
                for i in range(split_2[client],len(jgpu)):
                    T3_times[client] += np.random.randint(min(jgpu[:,0]),max(jgpu[:,0])) + np.random.randint(min(jgpu[:,1]),max(jgpu[:,1]))
                    mem_footprint[client][0] += memory[i][0] + memory[i][1]
                # now we add the transmission times
                T3_times[client] += memory[split_2[client]-1][0]*0.008/client_conn_speeds[client]*1000
                T3_times[client] += memory[split_2[client]][0]*0.008/client_conn_speeds[client]*1000
            for helper in range(I):
                if helper_device_type[helper] == 0:
                    for i in range(split_1[client], split_2[client]):
                        T2_times[helper, client] += np.random.randint(min(VM[:,0])+1,max(VM[:,0]))
                        T4_times[helper, client] += np.random.randint(min(VM[:,1])+1,max(VM[:,1]))
                elif helper_device_type[helper] == 1:
                    for i in range(split_1[client], split_2[client]):
                        T2_times[helper, client] += np.random.randint(min(laptop[:,0])+1,max(laptop[:,0]))
                        T4_times[helper, client] += np.random.randint(min(laptop[:,1])+1,max(laptop[:,1]))
                        # the +1 was added above to avoid pathogenic cases where the rounded 
                        # proc. times where 0
                        
        # now change memory capacity for level 4 scenario
        mem_capacity_helper = (np.random.randint(4,16, size = I)*1000) # for Mbytes 
    # #    
    mem_footprint = mem_footprint/1000 # for MBytes (data is in KBytes)
    if capcar == 1: #if I have cardinality contraints
        mem_footprint = np.ones([J,2]).astype(int)
        if b <= 3:
            mem_capacity_helper= (np.ones(I)*16).astype(int)
        else:
            mem_capacity_helper = (np.random.randint(4,16, size = I))
        
    T1_times = np.rint(T1_times).astype(int)
    T2_times = np.rint(T2_times).astype(int)
    T3_times = np.rint(T3_times).astype(int)
    T4_times = np.rint(T4_times).astype(int)
    T5_times = np.rint(T5_times).astype(int)
    
    mem_footprint = np.rint(mem_footprint).astype(int)
                
    return T1_times, T2_times, T3_times, T4_times, T5_times, mem_capacity_helper, mem_footprint, client_conn_type, client_conn_speeds, client_device_type, helper_device_type