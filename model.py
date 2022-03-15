from random import random

def run(p, num_offspring = 16):
    alleles = []
    for _ in range(num_offspring):
        current = ''
        for __ in range(2):
            if random() < p:
                current += 'A'
            else:
                current += 'B'
        alleles.append(current)
    
    num_p = 0
    num_total = 0
    for allele in alleles:
        if 'AA' in allele:
            num_p += 2
        elif 'A' in allele:
            num_p += 1
        num_total += 2
    p = num_p/num_total
    return p