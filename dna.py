# import the dictionary that can be used for the amino acid translation.
from scov import amacid_dict
import numpy as np

#This is the core module developed as part of the effort.
class dna:

    # Constructor method
    def __init__(self,dna_seq):
        dna_seq = dna_seq.upper() # Convert the nucleotide bases to Upper Case 
        for seq in dna_seq:
            # Valid nucleotide bases. If not a valid sequence raise an Error
            if seq not in ['A','T','G','C',' ','N']: 
                error = 'Wrong DNA Sequence {}!!'.format(seq)
                raise ValueError(error)
        # Remove all of the empty characters in the nucleotide sequence.
        dna_seq = dna_seq.replace(' ','') 
        self.dir_3_5=dna_seq
        self.dir_5_3=self.dir_5_3_strand()
        self.mRna = None
        self.amino_acid = None
        self.num_array = None
        self.nucl_len = len(dna_seq)

    def __repr__(self):
        return "DNA has {} nucleotide and they are {} :".format(self.nucl_len,self.dir_3_5)

    def __eq__(self, other):
        if other is None:
            return False
        return self.seq == other.seq

    #def replicate(self):
    #    return

    def transcription(self):
        # This is a method that imitates the transcription of a gene to mRNA for Protein transalation.
        # This is mostly of the future use.
        trans=''
        for nuc in self.dir_5_3:
            if nuc == 'A':
                trans += 'U'
            if nuc == 'T':
                trans += 'A'
            if nuc == 'C':
                trans += 'G'
            if nuc == 'G':
                trans += 'C'
            if nuc == 'N':
                trans += 'N'
        self.mRna = trans
        return self.mRna

    def translation(self):
        # This is the method where the transcripted mRNA gets translated into Amino Acid. Each 3
        # base in the mRNA codes for an amino acid.
        begin = 'No'
        ac = ''
        for i in range(0,len(self.mRna)-3,3):
            if self.mRna[i:3] == 'AUG':
                begin = 'Yes'
            if self.mRna[i:3] in ('UAA','UAG','UGA'):
                being = 'No'
            if begin == 'Yes':
                ac+= amacid_dict[self.mRna[i:3+i]][0]
        self.amino_acid = ac
        return self.amino_acid

    def dir_5_3_strand(self):
        dir_5_3 = ''
        # This is a method which reads the 3 - 5 prime sequence and creates the 5 - 3 prime sequence.
        for nuc in self.dir_3_5:
            if nuc == 'A':
                dir_5_3 += 'T'
            if nuc == 'T':
                dir_5_3 += 'A'
            if nuc == 'C':
                dir_5_3 += 'G'
            if nuc == 'G':
                dir_5_3 += 'C'
            if nuc == 'N':
                dir_5_3 += 'N'
        return dir_5_3

    def numpfy(self):
        # This method takes in a dna sequence and convert them into numpy array.
        # Each of the nucleotide sequence is converted into one of the below numbers 
        # which then can be used in for analysis and comparison.
        arr = ''
        for i in self.dir_3_5:
            if i == 'A':
                arr += '0 '
            if i == 'T':
                arr += '255 '
            if i == 'C':
                arr += '100 '
            if i == 'G':
                arr += '200 '
            if i == 'N':
                arr += '75 '   
        arr_np = np.fromstring(arr,dtype=np.uint8,sep=' ')        
        self.num_array = arr_np
        return self.num_array
    
    
    
