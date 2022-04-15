import pickle

with open('sample2.fasta', "r") as a_file:
    with open('NH_count_dna', 'wb') as my_new:
        dic = {}
        for line in a_file:
            if line.startswith('>'):
                stripped_line = line.strip().split('.')
                if stripped_line[1] in dic:
                    dic[stripped_line[1]] += 1
                else:
                    dic[stripped_line[1]] = 1
        pickle.dump(dic, my_new)