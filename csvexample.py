import csv

quotes = [
        ['Lao Tzu','The journey of a thousand miles begins with one step.'],
        ['Friedrich Nietzsche','That which does not kill us makes us stronger.']
        ]

with open('csvexample_quotes.csv', 'w') as f:
    fields = ['author', 'quote']
    writer = csv.DictWriter(f, fieldnames=fields, delimiter=';')
    writer.writeheader()
    for q in quotes:
        writer.writerow({fields[0]: q[0], fields[1]: q[1]})
