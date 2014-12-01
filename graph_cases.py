import matplotlib.pyplot as plt

from cs143sim.simulation import Controller
from cs143sim.constants import DEBUG


CASES = [ 11]
SIMULATION_DURATION = 80000  # ms
X_STEP = 100  # ms


for case in CASES:
    c = Controller(case='cs143sim/cases/case' + str(case) + '.txt')
   
    c.run(SIMULATION_DURATION)
    print c.packet_loss
    categories1 = ['Flow Rate']
    categories2 = ['Buffer Occupancy','Window Size', 'Packet Delay']
    categories3 = ['Link Rate']
    categories4 = ['Packet Loss']
    
    for category in categories1:
        print category
        fig = plt.figure()
        ax = plt.axes()
        ax.set_title('Case ' + str(case) + ' ' + category)
        ax.set_xlabel('Time (s)')
        record_name = '_'.join(category.lower().split(' '))
        record = c.__dict__[record_name]
        for actor in record:
            x = [0]
            y = [0]
            actor_name = [key for actor_dict in (c.flows, c.links)
                          for key in actor_dict
                          if actor_dict[key] == actor][0]
            print '  ', actor_name
            for time, value in record[actor]:
                #print '    ', time, value
                if time > x[-1]:
                    x.append(x[-1] + X_STEP)
                    y.append(0)
                y[-1] += value if value != None else 1
            x = [time / 1000.0 for time in x]
            y = [value *1.0 / X_STEP for value in y]
            #ax.plot(x, y, '.', label=actor_name)
            ax.plot(x, y, label=actor_name)
        ax.legend()
        
    for category in categories2:
        print category
        fig = plt.figure()
        ax = plt.axes()
        ax.set_title('Case ' + str(case) + ' ' + category)
        ax.set_xlabel('Time (s)')
        record_name = '_'.join(category.lower().split(' '))
        record = c.__dict__[record_name]
        for actor in record:
            x = [0]
            y = [0]
            actor_name = [key for actor_dict in (c.flows, c.links)
                          for key in actor_dict
                          if actor_dict[key] == actor][0]
            print '  ', actor_name
            for time, value in record[actor]:
                # print '    ', time, value
                x.append(time/1000)
                y.append(value)
            #ax.plot(x, y, '.', label=actor_name)
            ax.plot(x, y, label=actor_name)
        ax.legend()
        
    for category in categories3:
        print category
        fig = plt.figure()
        ax = plt.axes()
        ax.set_title('Case ' + str(case) + ' ' + category)
        ax.set_xlabel('Time (s)')
        record_name = '_'.join(category.lower().split(' '))
        record = c.__dict__[record_name]
        for actor in record:
            x = [0]
            y = [0]
            actor_name = [key for actor_dict in (c.flows, c.links)
                          for key in actor_dict
                          if actor_dict[key] == actor][0]
            print '  ', actor_name
            for time, value in record[actor]:
                # print '    ', time, value
                if time > x[-1]:
                    x.append(x[-1] + X_STEP)
                    y.append(0)
                y[-1] += value if value != None else 1
            x = [time / 1000.0 for time in x]
            y = [value * 1.0 * c.links[actor_name].rate / X_STEP for value in y]
            #ax.plot(x, y, '.', label=actor_name)
            ax.plot(x, y, label=actor_name)
        ax.legend()
        
    for category in categories4:
        print category
        fig = plt.figure()
        ax = plt.axes()
        ax.set_title('Case ' + str(case) + ' ' + category)
        ax.set_xlabel('Time (s)')
        record_name = '_'.join(category.lower().split(' '))
        record = c.__dict__[record_name]
        for actor in record:
            x = [0]
            y = [0]
            actor_name = [key for actor_dict in (c.flows, c.links)
                          for key in actor_dict
                          if actor_dict[key] == actor][0]
            print '  ', actor_name
            for time, value in record[actor]:
                #print '    ', time, value
                if time > x[-1]:
                    x.append(x[-1] + X_STEP)
                    y.append(0)
                y[-1] += value if value != None else 1
            x = [time / 1000.0 for time in x]
            y = [value *1.0 for value in y]
            #ax.plot(x, y, '.', label=actor_name)
            ax.plot(x, y, label=actor_name)
        ax.legend()
        
    plt.show()
    
