def hammingD(strP, strD):

    hdist = 0

    for nc in range(len(strP)):
        if strP[nc] != strD[nc]:
            hdist += 1

    return hdist

def main():

    fl = open("dataset_9_3.txt", 'r')

    strP = 'CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG'
    strD = 'ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'
    nHamming = hammingD(strP, strD)

    print(nHamming)

main()