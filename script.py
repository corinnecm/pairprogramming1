# Save arg names as variables
from sys import argv
from collections import defaultdict
import re

def txt2review(path):
    review = defaultdict(list)
    with open(path) as f:
        for line in f:
            try:
                rest = re.findall(r'(?<=-)([\w\s\'\.]+)(?=\t)',line)[0]
            except IndexError:
                print('Couldnt find restaurant in: ' + line)
            rating = re.findall(r'\d+', line)[0]
            print(rest, rating)
            rest = rest.lower()
            review[rest].append(float(rating))
    return review

def mean(review): 
    means = {}
    for rest in review:
        rates = review[rest]
        means[rest] = sum(rates)/len(rates)
    return means

def output(*reviews):
    master = set(sum([list(r.keys()) for r in reviews], []))
    lines = defaultdict()
    for review in reviews:
        for rest in review:
            lines[rest] = lines.get(rest, rest) + ',%.3g' %review[rest]
        for item in master:
            if item not in review:
                lines[item] = lines.get(item, item) + ','
    lines = [l for (y, l) in sorted(lines.items())]
    with open(out, 'w') as f:
        for line in lines:
            f.write(line + '\n')

if __name__ == '__main__':
    filename = argv[0]
    sources = argv[1:-1]
    out = argv[-1]
    reviews = [txt2review(path) for path in sources]
    means = [mean(rev) for rev in reviews]
    output(*means)




