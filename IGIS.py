def determine_longest_subsequence(sequence, order):
    """ Determines longest subsequence from input sequence permutation. """
    subsequences = [0] * len(sequence)
    for iterator in range(len(sequence) - 2, -1, -1):
        for jterator in range(len(sequence) - 1, iterator, -1):
            if order == "INCREASING":
                if sequence[iterator] < sequence[jterator] and subsequences[iterator] <= subsequences[jterator]:
                    subsequences[iterator] += 1
            if order == "DECREASING":
                if sequence[iterator] > sequence[jterator] and subsequences[iterator] <= subsequences[jterator]:
                    subsequences[iterator] = subsequences[jterator] + 1
    maximum_subsequence, longest_subsequence = max(subsequences), list()
    for iterator in range(len(subsequences)):
        if maximum_subsequence == subsequences[iterator]:
            longest_subsequence.append(str(sequence[iterator]))
            maximum_subsequence -= 1
    return longest_subsequence

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "rosalind_lgis.txt"
    FILEPATHWRITE = "LGIS-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        π = [int(item) for item in fr.readlines()[1].split(" ")]

    longest_subsequences = dict()
    for order in ("INCREASING", "DECREASING"):
        longest_subsequences["LONGEST_{}_SUBSEQUENCE".format(order)] = determine_longest_subsequence(π, order)

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write("\n".join([" ".join(longest_subsequences["LONGEST_{}_SUBSEQUENCE".format(order)]) for order in ("INCREASING", "DECREASING")]))

    return print("\nThe Increasing Subsequences dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()