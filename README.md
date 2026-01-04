# bioinf
Intro to programming assignment & files

## Folders

- `c_examples` - C examples shown during class.
- `exercise_1` - Attempted solution for Exercise 1 (see bellow)


## DNA/RNA Subsequence Finder (Exercise 1)

A Python CLI tool for finding subsequences in DNA or RNA sequences using start and stop codons.

- Detects DNA vs RNA
- Finds subsequences starting with corresponding start codon and ending at valid stop codons.
- For DNA, scans both original and reverse complement
- For each sequence, it prints start position, end position, length, and the sequence itself

## Usage
```bash
cd exercise_1
python script.py data/input1.seq
```

## Implementation notes
- Python 3.12 (stdlib only)
- This was tested in an *buntu system.
