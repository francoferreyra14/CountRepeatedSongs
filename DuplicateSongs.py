different_songs = []  # holds lines already seen

file = r"C:\Users\usuario\Desktop\01-enero 01 de 2021.lst"
with open(r"C:\Users\usuario\Desktop\ListaBochaSinDup.lst", "w", encoding='latin-1') as output_file:
    for each_line in open(file, "r", encoding='latin-1'):
        each_line = each_line.split('\n')
        for e in each_line:
            if e not in different_songs:
                different_songs.append(e)
            else:
                if "time" in e:
                    different_songs.append(e)
                else:
                    if "PUBLICIDADES -FRASES" in e:
                        different_songs.append(e)
    different_songs.remove('')
    for f in different_songs:
        output_file.write(f+"\n")
