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
    history = []
    lines = []
    for review in reviews:
        for rest in review:
            if rest not in history:
                lines.append(rest + ',%f' %review[rest])
                history.append(rest)
            else:
                idx = history.index(rest)
                lines[idx] = lines[idx] + ',%f' %review[rest]
        for item in history:
            if item not in review:
                idx = history.index(item)
                lines[idx] = lines[idx] + ','
    lines = [l for (y, l) in sorted(zip(history, lines))]
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




