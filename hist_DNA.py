import matplotlib.pyplot as plt

NH = open("/home/berdnikovich/dna/results/K562_2_AG_7_S1_dna_NH.txt", 'r')
dic = {}
for i in NH:
    find_num = i.strip().split("\t")[1]
    #print(find_num)
    if find_num in dic.keys():
        #print('hey')
        dic[find_num] = dic[find_num] + 1
    else:
        dic[find_num] = 1

        
output_dict = {}
for key in dic:
    output_dict[int(key)] = dic[key]       
    
plt.hist(output_dict, density=True, bins=50, color='#0504aa') 
plt.ylabel('count')
plt.xlabel('n map')
plt.title('DNA')
plt.xticks(range(0, 1001, 100))
plt.savefig('/home/berdnikovich/dna/results/reads_dna.png')

NH.close()