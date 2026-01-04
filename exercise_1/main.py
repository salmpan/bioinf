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
    """
    Returns the reverse complement of a DNA sequence.

    Each nucleotide is first replaced with its complementary base
    (A<->T, G<->C), and the resulting sequence is then reversed.
    This is commonly used when analyzing DNA in the opposite
    strand orientation.

    Parameters
    ----------
    seq : str
        DNA sequence consisting of A, T, G, and C characters.

    Returns
    -------
    str
        The reverse-complemented DNA sequence.
    """
    trans = str.maketrans({"A": "T", "T": "A", "G": "C", "C": "G"})
    return seq.translate(trans)[::-1]


def find_subsequences(
        seq: str,
        start_codon: str,
        end_codons: set[str]
) -> List[Tuple[int, int, str]]:
    """
    Finds coding subsequences in a DNA or RNA sequence.

    The function scans the sequence for occurrences of a start codon.
    For each start codon found, it continues scanning forward in the
    same reading frame (steps of three bases) until a valid stop codon
    is encountered.

    All subsequences that begin with the start codon and end with one
    of the provided stop codons are returned.

    The scan begins at every position in the sequence to ensure start
    codons are detected in all possible reading frames.

    Parameters
    ----------
    seq : str
        The input DNA or RNA sequence.
    start_codon : str
        The codon that marks the beginning of a subsequence (e.g. ATG or AUG).
    end_codons : set[str]
        A set of codons that mark the end of a subsequence.

    Returns
    -------
    List[Tuple[int, int, str]]
        A list of tuples containing:
        - start index (inclusive)
        - end index (exclusive)
        - the subsequence itself
    """
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
    """
    Rudimentary/placehodler function for scoring a collection of
    detected subsequences.

    The score consists of two values:
    - The length of the longest subsequence found
    - The total number of subsequences

    This scoring is used to compare results (e.g., original sequence
    vs. reverse complement) by preferring the set with either more
    subsequences or longer ones.
    """
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

        # Select the best scoring set of sequences
        best_label, best_sequences = "Original", original_seqs
        if rev_score > original_score:
            best_label, best_sequences = "Complement", complement_seqs

        print(f"Best: {best_label}\n")

        for start, end, gene in best_sequences:
            seq_length = len(gene)
            chunks = [gene[i:i+3] for i in range(0, len(gene), 3)]
            print(f"Start: {start+1}, End: {end+1}, Sequence length: {seq_length}, Codons length: {seq_length // 3}\n{chunks}\n")

        sys.exit(0)

    # If RNA, just print original sequences
    for start, end, gene in original_seqs:
        seq_length = len(gene)
        chunks = [gene[i:i+3] for i in range(0, len(gene), 3)]
        print(f"Start: {start+1}, End: {end+1}, Sequence length: {seq_length}, Codons length: {seq_length // 3}\n{chunks}\n")


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
