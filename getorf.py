!pip install biopython

from Bio import SeqIO

#An ORF is a continuous stretch of codons that begins with a start codon (usually AUG) 
#and ends at a stop codon (usually UAA, UAG or UGA).

records = list(SeqIO.parse("python7.fasta", "fasta"))

codon = str(records[0].seq) # first record

print(codon)

fim = "TAA", "TAG","TGA"

if len(codon)%3 == 0:
  print("Seu comprimento é múltiplo de 3")

if (fim[0] in codon) == True:
  print(f"O códon de terminação {fim[0]} se encontra na sequência imputada")

if (fim[1] in codon) == True:
  print(f"O códon de terminação {fim[1]} se encontra na sequência imputada")

if (fim[2] in codon) == True:
  print(f"O códon de terminação {fim[2]} se encontra na sequência imputada")

import re
fim1 = re.search('ATG(.+?)TAG',codon).group(1)
fim2 = re.search('ATG(.+?)TAA',codon).group(1)
fim3 = re.search('ATG(.+?)TGA',codon).group(1)

if len(fim1) > len(fim2) and len(fim1) > len(fim3):
  maior = 'ATG'+fim1+'TAG'
elif len(fim2) > len(fim3):
  maior = 'ATG'+fim2+'TAA'
else:
  maior = 'ATG'+fim3+'TGA'

from Bio.Seq import Seq

minha_sequencia = Seq(maior)
complementar = minha_sequencia.complement()
print(f"O maior ORF identificado foi: {minha_sequencia}")
print(f"O peptídeo codificado complementar gerado foi: {complementar}")
