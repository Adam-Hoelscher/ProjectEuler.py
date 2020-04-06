from itertools import permutations


def Solve(size=5):

    # An n-gon will have 2n nodes and n lines. When modeling n-gons we'll use
    # a list. Positions [0 : n-1] will represent outer nodes in a clockwise 
    # order and postiions [n : 2n-1] will reprsent inner nodes in clockwise
    # order, with outer node i connected to inner node i+n.

    # The n-gon will have values from 1 to 2n. We'll order these descending so
    # that we test higher values first.
    node_values = range(2 * size, 0, -1)

    # Make a list of all the lines that will be formed by the n-gon. Because the
    # n-gon is cyclic, the last node of the last line is the same as the second
    # node of the 1st line.
    lines = [[i, i + size, (i + size + 1)] for i in range(size)]
    lines[-1][-1] = lines[0][1]

    # We'll need to be able to add up the nodes in a line.
    def sum_nodes(n_gon, nodes):
        return sum(n_gon[idx] for idx in nodes)

    # Encode one line of an n-gon.
    def stringify_line(line):
        return ''.join(str(n_gon[position]) for position in line)

    # Encode an entire n-gon.
    def stringify_n_gon(n_gon):
        return ''.join(stringify_line(l) for l in lines)

    # Half of the numbers are on external nodes. If the all the external numbers
    # are from higher half, then the lowest external node is 1 more than the
    # size of the n-gon. Because the representations start with the numerically
    # lowest external node, the first number in the representation cannot be
    # higher than 1 more than the size of n-gon
    for head in range(size + 1, 0, -1):

        # Get a list of the remaining values in descending order.
        tail = [n for n in node_values if n != head]

        # Because the second number in the representation is from an inner node,
        # we want to start by testing the highest values of that number.
        for inner in permutations(tail, size):

            # The outer numbers need to be in the tail, but not in the inner
            # set and not less than the head number. List them in descending
            # order.
            outer_numbers = [n for n in tail if n not in inner and not n < head]

            # Specify that we have to draw size-1 numbers from the set, because
            # it might not be big enough to accomodate. If it is not big enough,
            # the iterator will stop immediately and we'll move on to the next
            # inner set.
            for outer in permutations(outer_numbers, size - 1):

                # Build a n-gon based on the permutations we've selected.
                n_gon = [head] + list(outer) + list(inner)

                # Compute the sums of all lines in the n-gon.
                sums = [sum_nodes(n_gon=n_gon, nodes=l) for l in lines]

                # If there is only one unique sum then we've found a magic
                # n-gon. Because we tested n-gons in decreasing key value order,
                # we know that the one we found has the highest key of any magic
                # n-gon and we can return it.
                if len(set(sums)) == 1:
                    magic = stringify_n_gon(n_gon)
                    return magic


if __name__ == '__main__':
    print(Solve())
