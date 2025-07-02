import csv

poem_names = ['voluspa', 'havamal', 'vafbrudnismal', 'grimnismal', 'skirnismal', 'harbarsliod', 'hymiskvida', 'lokasenna', 'thrymyskivida', 'volundarkvida', 'alvissmal', 'helgakvida hundingsbana1', 'helgakvida hjorvard', 'helgakvida hundingsbana2', 'gripisspa', 'reginsmal', 'fafnismal', 'sigrdrifumal', 'brot', 'gudrun 1', 'sig skamm', 'helreid', 'gudrun 2', 'gudrun 3', 'oddrun', 'atlakvida', 'atlamal', 'gudrunarhvot', 'hamdismal']

poems = {}
for poem_name in poem_names:
    poems[poem_name] = []



# { VOLUPSA:
#
# [
# []
# []
# []
# []
# ]
#
# HAVAMAL:
#
# [
# []
# []
#
#
#
# ]
# }

num_of_columns = 8

# save all poem lines in dictionary of lists
with open('clean_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count != 0:
            for i in range(len(poem_names)):
                #if row[i*8] != '':
                #    poems[poem_names[i]].append([])
                if row[i*8+1] != '' or row[i*8+2] != '' or row[i*8+3] != '':
                    poems[poem_names[i]].append([])
                if row[i*8+1] != '':
                    word1 = row[i*8+1].strip()
                    word1 = word1.replace('<','')
                    word1 = word1.replace('>', '')
                    poems[poem_names[i]][-1].append(word1)
                if row[i*8+2] != '':
                    word2 = row[i*8+2].strip()
                    word2 = word2.replace('<','')
                    word2 = word2.replace('>', '')
                    poems[poem_names[i]][-1].append(word2)
                if row[i*8+3] != '':
                    word3 = row[i*8+3].strip()
                    word3 = word3.replace('<','')
                    word3 = word3.replace('>', '')
                    poems[poem_names[i]][-1].append(word3)
        line_count += 1

#print(poems['hamdismal'])



# get consolidate roots and counts


consolidated_roots_list = []

with open('consolidated_roots.csv') as csv_file2:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >= 6:
            if row[9] != '':
                word = row[9].strip()
                word = word.replace('<','')
                word = word.replace('>', '')
                consolidated_roots_list.append(word)
        line_count += 1

#print(consolidated_roots_list)

counts_for_consolidated_roots = []
for consolidated_root in consolidated_roots_list:
    counts_for_consolidated_roots.append(0)
    for poemname in poems:
        for linenum in range(len(poems[poemname])):
            for word in poems[poemname][linenum]:
                #print(word, consolidated_root)
                if word.strip() == consolidated_root.strip():
                    counts_for_consolidated_roots[-1] += 1

for i in range(len(consolidated_roots_list)):
    print(consolidated_roots_list[i], counts_for_consolidated_roots[i])




# write counts of consolidated roots to CSV file

with open('counts_for_consolidated_roots.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    header = ["Consolidated Root", "Count"]
    writer.writerow(header)

    for i in range(len(consolidated_roots_list)):
        writer.writerow([consolidated_roots_list[i], counts_for_consolidated_roots[i]])




def alliterates(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    vowels = ['a','e','i','o','u', 'æ', 'ö', 'ø', 'j', 'á', 'é', 'í', 'ó', 'ö', 'ø', 'ú', 'ý']
    if word1[:1] == 'sk' and word2[:1] != 'sk':
        return False
    if word1[:1] == 'sp' and word2[:1] != 'sp':
        return False
    if word1[:1] == 'st' and word2[:1] != 'st':
        return False
    if word1[0] == word2[0]:
        return True
    if word1[0] in vowels and word2[0] in vowels:
        return True
    return False


word_pair_info = {}
# info for each pair




v_count = 0
display = []
for poemname in poems:
    poem_count = 0
    for linenum in range(len(poems[poemname])):
        words = []
        for word in poems[poemname][linenum]:
            words.append(word)
        if words[0][0] == 'v' or words[0][0] == 'V':
            print(words)
            v_count += 1
            poem_count += 1
    display.append("Count for poem " + poemname + " is " + str(poem_count))
for line in display:
    print(line)

print(v_count)

f
