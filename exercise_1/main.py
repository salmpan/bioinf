import argparse
import sys
from typing import (
    List,
    Tuple,
    Union
)
from pathlib import Path

DNA_START_CODON = "ATG"
RNA_START_CODON = "AUG"

DNA_END_CODONS = {"TAA", "TAG", "TGA"}
RNA_END_CODONS = {"UAA", "UAG", "UGA"}


def load_data(filepath: Union[Path, str]) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return "".join(f.read().split()).upper()


def detect_sequence_type(seq_data: str) -> Tuple[str, str, set[str]]:
    if "U" in seq_data:
        return "RNA", RNA_START_CODON, RNA_END_CODONS

    return "DNA", DNA_START_CODON, DNA_END_CODONS


def reverse_complement(seq: str) -> str:
    trans = str.maketrans({"A": "T", "T": "A", "G": "C", "C": "G"})
    return seq.translate(trans)[::-1]


def find_subsequences(
        seq: str,
        start_codon: str,
        end_codons: set[str]
) -> List[Tuple[int, int, str]]:
    subsequences: List[Tuple[int, int, str]] = []

    # NOTE: Scan each char in order to not miss start
    # codons in any frame.
    for start in range(0, len(seq) - 2):
        if seq[start:start + 3] != start_codon:
            continue

        stop_start = -1
        for i in range(start + 3, len(seq) - 2, 3):
            codon = seq[i:i + 3]
            if codon in end_codons:
                stop_start = i
                break

        if stop_start != -1:
            end_exclusive = stop_start + 3
            subsequences.append((start, end_exclusive, seq[start:end_exclusive]))

    return subsequences


def score(sequences: List[Tuple[int, int, str]]) -> Tuple[int, int]:
    longest = max((len(gene) for _, __, gene in sequences), default=0)
    return (longest, len(sequences))


def run(seq_data: str) -> None:
    seq_type, start_codon, end_codons = detect_sequence_type(seq_data)
    print(f"Sequence type: {seq_type}\n")

    original_seqs = find_subsequences(seq_data, start_codon, end_codons)
    if seq_type == "DNA":
        complement = reverse_complement(seq_data)
        complement_seqs = find_subsequences(complement, start_codon, end_codons)

        original_score = score(original_seqs)
        rev_score = score(complement_seqs)

        print(f"Original: {len(original_seqs)} sequences, longest = {original_score[0]}")
        print(f"Complement: {len(complement_seqs)} sequences, longest = {rev_score[0]}\n")

        if not original_seqs and not complement_seqs:
            print("No subsequences found.")
            sys.exit(1)

        best_label, best_sequences = "Original", original_seqs
        if rev_score > original_score:
            best_label, best_sequences = "Complement", complement_seqs

        print(f"Best: {best_label}\n")

        for start, end, gene in best_sequences:
            print(f"Start: {start}, End: {end}, Length: {len(gene)}\n{gene}\n")

        sys.exit(0)

    for start, end, gene in original_seqs:
        print(f"Start: {start}, End: {end}, Length: {len(gene)}\n{gene}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find subsequences in DNA/RNA sequences"
    )

    parser.add_argument(
        "filename",
        help="Path to the input file"
    )

    args = parser.parse_args()
    print(f"Processing file: {args.filename}")

    data = load_data(args.filename)
    if len(data) < 9:
        print("Data is too short.")
        sys.exit(1)

    run(data)
