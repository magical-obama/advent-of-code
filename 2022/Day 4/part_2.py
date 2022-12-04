import re

with open('input') as f:
    input_data = f.read()

range_matcher = '([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)'

pairs = input_data.splitlines()
print(pairs)


def is_overlapping(range1, range2):
    if range1.stop < range2.start:
        return False
    if range2.stop < range1.start:
        return False
    return True


# match: e.g. [('2', '9', '9', '51')]
def clean_up_matches(match):
    return [int(i) for i in match[0]]


ranges = [clean_up_matches(match) for match in [re.findall(range_matcher, pair) for pair in pairs]]
print(ranges)

pair_ranges = []

for pair in ranges:
    current_pair = [range(pair[0], pair[1]), range(pair[2], pair[3])]
    pair_ranges.append(current_pair)

print(pair_ranges)

num_overlapping = 0

for pair in pair_ranges:
    if is_overlapping(*pair):
        num_overlapping += 1

print('Solution:', num_overlapping)
