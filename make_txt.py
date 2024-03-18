import os
import shutil

path = "raw"
list_file = os.listdir(path)


for f in list_file:
    os.system("whisper " + "raw"+ "\\" + f + " --language Italian --output_format txt --model medium --device cuda")
    shutil.move(f.replace(".mp3", ".txt") , "txt")
    shutil.move("raw\\" + f, "done")


def task (f, materia):
    try:
        with open ("txt"+"\\" +materia + "\\" + data +".txt", "a") as k:
            with open ("txt" +"\\" + f.replace(".mp3", ".txt"), "r") as g:
                k.write(g.read().replace("\n", " ").replace("à", "a").replace("è", "e").replace("é", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u"))
                k.write("\n\n\n\n")
    except:
        with open ("txt"+"\\" +materia + "\\" + data +".txt", "w") as k:
            pass
        with open ("txt"+"\\" +materia + "\\" + data +".txt", "a") as k:
            with open ("txt" +"\\" + f.replace(".mp3", ".txt"), "r") as g:
                k.write(g.read().replace("\n", " ").replace("à", "a").replace("è", "e").replace("é", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u"))
                k.write("\n\n\n\n")


for f in list_file:
    data = f.split("_")[0]
    if "prg" in f:
        task(f, "prg")
        

    if "asd" in f:
        task (f, "asd")
        

    if "adc" in f:
        task(f, "adc")
    
    
    os.system("del " + "txt" +"\\" + f.replace(".mp3", ".txt"))
