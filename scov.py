
# This dictionary is used for reshaping the numpy array for each of the genes. 
# For example, the gene ORF1ab numpy array will be reshaped with rows=115 and cols=115.
# The second element in the list represent 'n' number of dummy 'N' to be added at the end of
# each gene nucletode seq to make to compactible with the rows and cols of the array.
numpy_image_dict = {'gene=ORF1ab':[(115,115),7],
                    'gene=S':[(62,62),22],
                    'gene=ORF3a':[(28,30),12],
                    'gene=E':[(15,16),12], 
                    'gene=M':[(26,27),33],
                    'gene=ORF6':[(14,14),10],    
                    'gene=ORF7a':[(19,20),14],
                    'gene=ORF7b':[(12,12),12],
                    'gene=ORF8':[(19,20),14],
                    'gene=N':[(36,36),36],
                    'gene=ORF10':[(11,11),4]}


# This dictionary has the codons for the amino acids from mRNA.
amacid_dict = {'UUU':('F','PHE','Phenylalanine'),'UUC':('F','PHE','Phenylalanine'),
               'UUA':('L','LEU','Leucine'),'UUG':('L','LEU','Leucine'),
               'UCU':('S','SER','Serine'),'UCC':('S','SER','Serine'),
               'UCA':('S','SER','Serine'),'UCG':('S','SER','Serine'), 
               'UAU':('Y','TYR','Tyrosine'),'UAC':('Y','TYR','Tyrosine'),
               'UAA':('STOP'),'UAG':('STOP'),
               'UGU':('C','CYS','Cysteine'),'UGC':('C','CYS','Cysteine'),
               'UGA':('STOP'),'UGG':('W','TRP','Tryptophan'),
               'CUU':('L','LEU','Leucine'),'CUC':('L','LEU','Leucine'),
               'CUA':('L','LEU','Leucine'),'CUG':('L','LEU','Leucine'),
               'CCU':('P','PRO','Proline'),'CCC':('P','PRO','Proline'),
               'CCA':('P','PRO','Proline'),'CCG':('P','PRO','Proline'),
               'CAU':('H','HIS','Histidine'),'CAC':('H','HIS','Histidine'),
               'CAA':('Q','GLU','Glutamine'),'CAG':('Q','GLU','Glutamine'),
               'CGU':('R','ARG','Arginine'),'CGA':('R','ARG','Arginine'),
               'CGG':('R','ARG','Arginine'),'CGC':('R','ARG','Arginine'),
               'AUU':('I','ILE','Isoleucine'),'AUC':('I','ILE','Isoleucine'),
               'AUA':('I','ILE','Isoleucine'),'AUG':('M','MET','Methionine'),
               'ACU':('T','THR','Threonine'),'ACC':('T','THR','Threonine'),
               'ACA':('T','THR','Threonine'),'ACG':('T','THR','Threonine'),
               'AAU':('N','ASN','Asparagine'),'AAC':('N','ASN','Asparagine'),
               'AAA':('K','LYS','Lysine'),'AAG':('K','LYS','Lysine'),
               'AGU':('S','SER','Serine'),'AGC':('S','SER','Serine'),
               'AGG':('R','ARG','Arginine'),'AGA':('R','ARG','Arginine'),
               'GUU':('V','VAL','Valine'),'GUC':('V','VAL','Valine'),
               'GUA':('V','VAL','Valine'),'GUG':('V','VAL','Valine'),
               'GCU':('A','ALA','Alanine'),'GCC':('A','ALA','Alanine'),
               'GCA':('A','ALA','Alanine'),'GCG':('A','ALA','Alanine'),
               'GAU':('D','ASP','Aspartate'),'GAC':('D','ASP','Aspartate'),
               'GAA':('E','GLU','Glutamate'),'GAG':('E','GLU','Glutamate'),
               'GGU':('G','GLY','Glycine'),'GGC':('G','GLY','Glycine'),
               'GGA':('G','GLY','Glycine'),'GGG':('G','GLY','Glycine')
}



