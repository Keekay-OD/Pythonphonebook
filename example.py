

from time import clock
start = clock()

# Need csv for importing files, decimal for proper rounding
import csv
import itertools
from decimal import *

# Difference constants
DELTA_HI = 0.0010
DELTA_LO = 0.0015

def main(filename1, filename2):
    # Open file1, skip header
    file1reader = csv.reader(open(filename1, 'rU'), delimiter=',')
    header1 = file1reader.next()

    # Mapping of ID to date string
    source_dts = dict(file1reader)

    # Will hold details of matching first rows (i.e. before finding delta row)
    matches = []

    # Will hold details of first rows and deltas (i.e. final results)
    deltas = []

    # Open file2, skip header
    file2reader = csv.reader(open(filename2, 'rU'), delimiter=',')
    header2 = file2reader.next()

    for row in file2reader:
        dt, bid, ask = row[3:]

        # Calculate deltas. Need this for checking matches and for storing. Round to 6 decimals.
        bid = round(Decimal(float(bid)), 6)
        hi = round(Decimal(bid + DELTA_HI), 6)
        lo = round(Decimal(bid - DELTA_LO), 6)

        # Check if we have a >= match from the first file.
        for k in source_dts.keys():
            if dt >= k:
                # Store a 3-tuple of (high, low, file1&2 rowdata)
                data = (hi, lo, ([k, source_dts[k]] + row))
                matches.append(data)

                # Remove source entry so we don't match it again
                del source_dts[k]

        # Check if we have a match for a previous row. A match is when the bid is
        # within a previous row's low / high.
        for idx, (p_hi, p_lo, p_row) in enumerate(matches):
            # This row's bid has exceeded the delta
            if (bid >= p_hi) or (bid <= p_lo):
                deltas.append((p_row, row))
                # Remove from previous rows so we don't match again
                del matches[idx]
                break

    # Deltas should have 2-tuples of row data. For each tuple, first is row data
    # for the datetime specified in file1, second is earliest row data after first
    # with a bid that exceeds the delta.
    writer = csv.writer(open('d:/output.csv', 'wb'), delimiter=",")
    writer.writerows(list(itertools.chain(*t)) for t in deltas)
    return deltas

if __name__ == "__main__":
    import sys
    f1, f2 = sys.argv[1:3]
    results = main(f1, f2)
    for a, b in results:
        print a, b


print clock() - start, 'Seconds'
