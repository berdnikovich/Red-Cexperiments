from sys import argv

in_fi = argv[1]#'chr_minus.bed'
out_fi = argv[2]#'extr_chr_minus.bed'#
coor = argv[3]#'5023354-5024222'#

cor = coor.split('-')
from_i = int(cor[0])
to_i = int(cor[1])

with open(in_fi, 'r') as fi:
    with open(out_fi, 'w') as ofi:
        for i in fi:
            i_ = i.strip().split('\t')
            froi = int(i_[1])
            toi = int(i_[2])
            if froi >= from_i and toi <= to_i:
                ofi.write(i)