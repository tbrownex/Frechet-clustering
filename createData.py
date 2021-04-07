import numpy as np

def create(cfg):
    ''' return a list where each element is the data for an entity'''
    numPeriods=cfg['numPeriods']
    numEntities=cfg['numEntities']
    data=[]
    z_line = np.linspace(0, 5, numPeriods )
    # Create a batch of graphs for different power factors. Within a batch each will have different scaler
    for n in range(numEntities):
        x_line = np.cos(z_line)
        m=n%3
        if m==0:
            power=1
        elif m==1:
            power=2.5
        else:
            power=3.5
        y_line = z_line**power+np.random.normal(loc=0, scale=1.0)
        ''' if np.random.choice(2)==3:
            x_line = scaler*np.cos(z_line)
            y_line = scaler*np.sin(z_line)
        else:
            x_line = scaler*np.sin(z_line)
            y_line = scaler*np.cos(z_line)
        x_line[0]=y_line[0]=0'''
        z_line=np.reshape(z_line, [-1,1])
        x_line=np.reshape(x_line, [-1,1])
        y_line=np.reshape(y_line, [-1,1])
        final=np.concatenate([x_line, y_line, z_line], axis=1)
        data.append(np.around(final, decimals=2))
    return data