with open('sample.bed', 'r') as fi:
    with open('chr_plus.bed', 'w') as topl_file:
        with open('chr_minus.bed', 'w') as tomi_file:
                for i in fi:
                    l = i.strip().split()
                    if l[5]=='+':
                        topl_file.write('chr{}\t{}\t{}\t{}\n'.format(l[0], l[1], l[2], l[5]))
                    else:
                        tomi_file.write('chr{}\t{}\t{}\t{}\n'.format(l[0], l[1], l[2], l[5]))
        