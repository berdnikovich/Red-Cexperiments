bed = open('head_first', 'r')
refbed = open('head_first_ref', 'w')

dic_chr = {'X' : '23', 
           'Y' : '24'}#остальные сохраняем как есть

for i in bed:
    line = i.strip().split('\t')
    ch = line[0]
    if ch in dic_chr:
        ch = dic_chr[ch]
    refbed.write(
    ch + '\t' 
        + line[1]+ '\t' 
        + line[2]+ '\t'
        + line[3]+ '\t' 
        + line[4]+ '\t'
        +line[5] + '\t'
        +line[6]+ "\n")
bed.close()
bedref.close()