def main():
    with open('rosalind_revp.txt', 'r') as inp:
        DNA_unclean = inp.read().split('\n')
    DNA = ''
    basedict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    for item in DNA_unclean[1:]:
        DNA += item
    DNA_length = len(DNA)
    palindrome_locations = []
    for search_length in range(4, 13):
        for location in range((DNA_length-search_length)+1):
            sequence = DNA[location:location+search_length]
            compliment = ''
            for base in sequence[::-1]:
                compliment += basedict[base]
            if sequence == compliment:
                start_end = '{} {}'.format(location+1, search_length)
                palindrome_locations.append(start_end)
    with open('palindrome_output.txt', 'w') as output_file:
        for item in palindrome_locations:
            output_file.write(item)
            output_file.write('\n')


if __name__ == '__main__':
    main()