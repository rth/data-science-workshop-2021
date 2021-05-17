a = np.random.randn(1000, 3)
print(a.shape)

a_select = a[:, [1,2]]
print(a_select.shape)

mean_select = a_select.mean(axis=0)
print(mean_select)