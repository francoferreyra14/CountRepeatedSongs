import os
import tkinter
from tkinter import filedialog

lists_concatenated = []
ordered_list = []

# directory =  "C:\\Users\\usuario\\Desktop\\Listas\\"
root = tkinter.Tk()
directory = filedialog.askdirectory(parent=root, initialdir="/", title='Seleccionar carpeta donde se encuentran las '
                                                                       'listas')
directory = directory+"//"
#print(directory)
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
    sort_orders = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        ordered_list.append(i)
    # print(ordered_list)
    for song_times in ordered_list:
        output_file.write(str(song_times) + "\n")
