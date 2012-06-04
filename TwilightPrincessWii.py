from PIL import ImageDraw, Image
import glob, os, sys, re
def convert(a):
    if(a==" "):
        return "space"
    if(a=="."):
        return "period"
    if(a==","):
        return "comma"
    if(a==";"):
        return "semicolon"
    if(a==":"):
        return "colon"
    if(a=="!"):
        return "exclamation"
    a = re.sub("[^a-zA-Z]",'',a)
    if(a==""):
        return "null"
    return a
def translate(name,text):
    path = sys.path[0]+"\TP\\"
    im = Image.open(path+"space.bmp")
    line = text.split("@")
    length = 0
    for i in line:
        if len(i) > length:
            length = len(i)
    height = len(line)
    length *= 42
    height *= 40
    diagram = Image.new("RGBA",(length,height),(255,255,255))
    longest = 0
    for i in range(0,len(line)):
        letters = []
        pos = 0
        for j in range(0,len(line[i])):
            temp = convert(line[i][j])
            if(temp != "null"):
                letters.append(temp)
        for j in range(0,len(letters)):
            k = len(letters)-j-1
            im = Image.open(path+letters[k]+".bmp")
            (le,up,ri,bo) = im.getbbox()
            diagram.paste(im,(pos,i*40,pos+ri,(i+1)*40))
            pos+=ri+1
        if(pos > longest):
            longest = pos
    diagram = diagram.crop((0,0,longest-1,len(line)*40))
    diagram.save(path+name+".png")
    diagram.show()
translate("lol","if you can read this, then you are@a massive nerd, and i love you.@long live the twilight princess!")