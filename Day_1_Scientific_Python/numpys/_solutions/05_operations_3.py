import matplotlib.pyplot as plt
%matplotlib inline

pat_0 = 0
pat_last = 10
while pat_last <= len(data):
    ave_inflammation = np.mean(data[pat_0:pat_last], axis=0)
    plt.plot(ave_inflammation)
    pat_0 = pat_last
    pat_last += 10