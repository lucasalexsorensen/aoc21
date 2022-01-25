from collections import Counter, defaultdict

result = 0
for line in open("d8.txt", "r"):
    line = line.strip()
    patterns, output = line.split(" | ")
    patterns = patterns.split(" ")
    output = output.split(" ")
    counts = defaultdict(int)
    c = Counter(len(x) for x in output)
    counts[1] += c[2]
    counts[7] += c[3]
    counts[4] += c[4]
    counts[8] += c[7]
    result += counts[1] + counts[7] + counts[4] + counts[8]

print("Part one result: %d" % result)


true_segments = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]
true_scores = Counter("".join(true_segments))
score_to_digits = {sum(true_scores[c] for c in p): i for i, p in enumerate(true_segments)}

result = 0
for line in open("d8.txt", "r"):
    patterns, output = list(map(lambda x: x.split(" "), line.strip().split(" | ")))

    char_scores = Counter("".join(patterns))
    pattern_to_digit = {}
    for p in map(lambda x: "".join(sorted(x)), patterns):
        pattern_score = sum(char_scores[x] for x in p)
        pattern_to_digit[p] = score_to_digits[pattern_score]

    result += int("".join([str(pattern_to_digit["".join(sorted(o))]) for o in output]))

print("Part two result: %d" % result)
