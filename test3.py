import os

lists_concatenated = []
final_list = []

directory = "C:\\Users\\usuario\\Desktop\\Listas\\"
with open(r"C:\Users\usuario\Desktop\ContadorCanciones.txt", "w", encoding='latin-1') as output_file:
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        music_list = open(f, "r", encoding='latin-1')
        for song in music_list:
            if "time" not in song:
                    if "PUBLICIDADES -FRASES" not in song:
                        lists_concatenated.append(song)
    lists_concatenated.remove("\n")
    my_dict = {i: lists_concatenated.count(i) for i in lists_concatenated}
    for s in my_dict:
        song_times = (str(s) + ', ' + str(my_dict[s]))
        song_times = song_times.replace("\t", "")
        song_times = song_times.replace("\n", "")
        song_times = song_times.replace(",", "\t")
        final_list.append(song_times)
        #output_file.write(song_times + "\n")
    final_list = sorted(final_list, key=lambda x: x[2], reverse=True)
    for f in final_list:
        output_file.write(f + "\n")
