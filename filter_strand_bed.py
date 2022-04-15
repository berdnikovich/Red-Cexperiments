from sys import argv
strand = argv[1]#'+'
input_file = argv[2]#'sample_bad.bed'
output_file = argv[3]#'sort_bed_plus.bed'

df = open(input_file, 'r')
to_file = open(output_file, 'w')

for i in df:
    line = i.strip().split('\t')
    if line[5] == strand:
        to_file.write(i)
        
to_file.close()
df.close()