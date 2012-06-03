from PIL import ImageDraw, Image
import glob, os, sys, re
def invert(a):
    (m,n,x,y) = a.getbbox()
    x-=3
    a = a.crop((m,n,x,y))
    for i in range(0,int(x/2)):
        for j in range(0,y):
            pic1 = a.getpixel((i,j))
            pic2 = a.getpixel((x-i-1,j))
            a.putpixel((i,j),pic2)
            a.putpixel((x-i-1,j),pic1)
    return a
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
            im = Image.open(path+letters[j]+".bmp")
            im = invert(im)
            (le,up,ri,bo) = im.getbbox()
            diagram.paste(im,(pos,i*40,pos+ri,(i+1)*40))
            pos+=ri+3
        pos = pos
        if(pos > longest):
            longest = pos
    diagram = diagram.crop((0,0,longest-3,len(line)*40))
    diagram.save(path+name+".jpg")
    diagram.show()
translate("lol","the legend of zelda: twilight princess@translating rocks!")