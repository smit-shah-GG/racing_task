base_names =['lEwiS_HaMiLton', 'MaX_vERsTapPen', 'SebASTIaN_vEtTeL','ChaRLeS_lEcLeRc']
indices=list()
drivers=list()
for i, name in enumerate(base_names):
    indices.append(i)
    drivers.append(name.lower().replace('_', '-'))
    
n=lambda a:len(a)
temp=list(map(n,drivers))

indices=list(map(sum,(zip(indices,temp))))
indices.sort(reverse=True)

F1_drivers=dict(zip(indices,drivers))
print(F1_drivers)