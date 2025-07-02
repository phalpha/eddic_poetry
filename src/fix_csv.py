import csv

lines = []
with open('rawdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        lines.append(row)



def convertLetter(word):
    word = word.lower()
    letter = word[0]
    vowels =  ['a','e','i','o','u', 'æ', 'ö', 'ø', 'j', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'y', 'œ']
    if letter in vowels:
        return 'vowel'
    elif letter == 'b':
        return '.b.'
    elif letter == 'd':
        return '.d.'
    elif letter == 'f':
        return '.f.'
    elif letter == 'g':
        return '.g.'
    elif letter == 'h':
        return '.h.'
    elif letter == 'k':
        return '.k.'
    elif letter == 'l':
        return '.l.'
    elif letter == 'm':
        return '.m.'
    elif letter == 'n':
        return '.n.'
    elif letter == 'p':
        return '.p.'
    elif letter == 'r':
        return '.r.'
    elif letter == 's':
        if word[1] == 'k':
            return '.sk.'
        elif word[1] == 'p':
            return '.sp.'
        elif word[1] == 't':
            return '.st.'
        else:
            return '.s.'
    elif letter == 't':
        return '.t.'
    elif letter == 'v':
        return '.v.'
    elif letter == 'þ':
        return '.þ.'

poem_names = ['voluspa', 'havamal', 'vafbrudnismal', 'grimnismal', 'skirnismal', 'harbarsliod', 'hymiskvida', 'lokasenna', 'thrymyskivida', 'volundarkvida', 'alvissmal', 'helgakvida hundingsbana1', 'helgakvida hjorvard', 'helgakvida hundingsbana2', 'gripisspa', 'reginsmal', 'fafnismal', 'sigrdrifumal', 'brot', 'gudrun 1', 'sig skamm', 'helreid', 'gudrun 2', 'gudrun 3', 'oddrun', 'atlakvida', 'atlamal', 'gudrunarhvot', 'hamdismal']


newlines = []
newlines.append(lines[0])
newlines.append(lines[1])
for linenum in range(len(lines)):
    newline = lines[linenum].copy()
    if linenum >= 2:
        for i in range(len(poem_names)):
            if lines[linenum][i*8+1] != '':
                word = lines[linenum][i*8+1].strip()[1:]
                newline[i*8+4] = convertLetter(word)
                if lines[linenum][i*8+4] != newline[i*8+4]:
                    print(lines[linenum][i*8+1:i*8+1+4], newline[i*8+4])
            elif lines[linenum][i*8+2] != '':
                word = lines[linenum][i*8+2].strip()[1:]
                newline[i*8+4] = convertLetter(word)
                if lines[linenum][i*8+4] != newline[i*8+4]:
                    print(lines[linenum][i*8+1:i*8+1+4], newline[i*8+4])
    newlines.append(newline)

with open('corrected_data.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)


    for line in newlines:
        writer.writerow(line)
