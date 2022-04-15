import pysam
samfile = pysam.AlignmentFile("../K562_2_AG_7_S1_dna_sorted_XM2.bam", "rb")

with open('dna_XM2_NH.fasta', 'w') as to_file:
    ind = 0
    for i in samfile:
        if i.query_name != ind:
            try:
                to_file.write('>{0}.{1}\n'.format(i.query_name, i.tags[-1]))
                to_file.write('{0}\n'.format(i.query_sequence))
                ind = i.query_name
            except IndexError:
                with open('worst_reads_dna.sam', 'w') as to_bed_file:
                    to_bed_file.write('{0}\n'.format(i.query_name)) 
        else:
            ind = i.query_name