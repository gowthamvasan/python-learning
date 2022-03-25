import csv
with open('/Users/user/Documents/Git_repos/Personal/python-learning/pygithub_project/project_dataset.csv', 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
    # Notice that we don't need the `csv` module.
        print(tuple(row))