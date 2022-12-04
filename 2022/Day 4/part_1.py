import re

with open('input') as f:
    input_data = f.read()

range_matcher = '([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)'

pairs = input_data.splitlines()
print(pairs)


def fully_contains(range1, range2):
    if range1.start <= range2.start and range1.stop >= range2.stop:
        return True
    elif range2.start <= range1.start and range2.stop >= range1.stop:
        return True
    else:
        return False


# match: e.g. [('2', '9', '9', '51')]
def clean_up_matches(match):
    return [int(i) for i in match[0]]


ranges = [clean_up_matches(match) for match in [re.findall(range_matcher, pair) for pair in pairs]]
print(ranges)

pair_ranges = []

for pair in ranges:
    # current_pair = [list(range(pair[0], pair[1] + 1)), list(range(pair[2], pair[3] + 1))]
    current_pair = [range(pair[0], pair[1] + 1), range(pair[2], pair[3] + 1)]
    pair_ranges.append(current_pair)

print(pair_ranges)

num_fully_contained = 0

for pair in pair_ranges:
    if fully_contains(*pair):
        num_fully_contained += 1

print('Solution:', num_fully_contained)
