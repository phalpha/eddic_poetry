import csv
import scipy.stats as stats
import numpy as np

data = []
header = []
with open('contingency_tables.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            header = row.copy()
        else:
            data.append(row)
        line_count += 1

new_data = []
new_header = header.copy()
new_header.extend(["Exact Fisher p", "Barnard p", "Boschloo p"])





with open('p_vals.csv', 'w') as f:
    # create the csv writer
    with open('full_p_vals.csv', 'w') as g:
        writer2 = csv.writer(g)
        writer = csv.writer(f)

        # write a row to the csv file
        header = ["Consolidated Root", "Count"]
        writer.writerow(new_header)

        for line in data:
            oddsratio1, pvalue1 = stats.fisher_exact([[int(line[2]), int(line[3])], [int(line[4]), int(line[5])]])
            #res2 = stats.barnard_exact([[int(line[2]), int(line[3])], [int(line[4]), int(line[5])]])
            #pvalue2 = res2.pvalue
            #res3 = stats.boschloo_exact([[int(line[2]), int(line[3])], [int(line[4]), int(line[5])]])
            #pvalue3 = res3.pvalue

            new_line = line.copy()
            new_line.append(pvalue1)
            writer2.writerow(new_line)
            if (pvalue1 != 1) and int(new_line[2]) > 1:
                writer.writerow(new_line)
