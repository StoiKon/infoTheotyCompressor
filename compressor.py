import translitcodec
import codecs
from collections import defaultdict
import re
import math
#filtering characters in order
# to make them lating
#and deleting jap and arab chars
2
if input("filter files y/n\n")=='y':

    for file in ["files/CA_2.csv","files/ES_2.csv","files/FR_2.csv","files/GB_2.csv"]:
        print("opening file "+file)
        words=""
        with open(file,"r+") as f:
            print("translating words")
            #latin
            words=codecs.encode(f.read().lower(),'translit/short')
            print("updating file contents to new file")
            with open(file.replace('2','3'),"w") as f2:
                for word in words.split("\n"):
                    #no jap or arabs
                    if word.isascii():
                        f2.write(re.sub("[^a-zA-Z]+", "",word.lower())+"\n")
if input("erwthma 1 y/n\n")=='y':
    paths = ["files/GB_3.csv","files/FR_3.csv"]
    #counting symbols inside file 
    for path in paths:
        count=0 
        print(f"counting chars in {path} file")
        with open(path, 'r') as fl:
            for word in fl:
                for ch in word:
                    #if word[0] == ch:
                    if ch!=',' and ch!='\n':
                        count += 1
        count = count -1 #EOF character
        #ERWTHMA 1
        d_list = defaultdict(int)

        with open(path, 'r') as fl:
            for word in fl:
                for ch in word:
                    if ch!=',' and ch!='\n':
                        d_list[ch] += 1



        dd = sorted(d_list.items(), key=lambda v:v[1], reverse=True)

        Hx=0
        for el in dd:
            Hx+=-1*(el[1]/count)*math.log2(el[1]/count)
            print (el[0] + ' '+ str(el[1])+" -> p(x) = "+str(el[1]/count))
        print(f"Total symbols:{count}")
        print(f"H(xn) = {Hx}")
if input("erwthma 2 y/n\n")=='y':
    paths = ["files/GB_3.csv","files/FR_3.csv"]
    #counting symbols inside files 
    for path in paths:
        count=0 
        print(f"counting chars in {path} file")
        with open(path, 'r') as fl:
            for word in fl:
                for ch in word:
                    if ch!=',' and ch!='\n':
                        count += 1
        count = count -1 #EOF character
        #choosing two neighbouring characters
        #choose a number from 0 to N-1 = N numbers 
        d_list = defaultdict(int)
        #p=1/count
        with open(path, 'r') as fl:
            for word in fl.readlines():
                adjadentchars=[word[i:i+2] for i in range(len(word)-1)]
                for i in adjadentchars:
                    if  "\n" not in i:
                        d_list[i]+=1
        
        dd = sorted(d_list.items(), key=lambda v:v[1], reverse=True)
        Hx=0

        for el in dd:
            Hx+=-1*(el[1]/count)*math.log2(el[1]/count)
            print (el[0] + ' '+ str(el[1])+f" -> p(x(i)x(i+1)) = {el[1]/count:.10f}")
        print(f"H(xn,xn+1)) = {Hx}")
        print(f"Μια βασική ιδιότητα της συνδετικής εντροπίας δύο πηγών είναι ότι δεν μπορεί να υπερβεί το άθροισμα των εντροπιών των δύο επιμέρους πηγών\nδιοτι αν υπάρχει κοινή πληροφορία αφαιρείται")
        def ypoSyn8hkhEntropia(dd):
            global path
            d_list = defaultdict(int)
            with open(path, 'r') as fl:
                for word in fl:
                    for ch in word:
                        if ch!=',' and ch!='\n':
                            d_list[ch] += 1
            Hx=0
            for element in dd:
                #px,y/py
                #einai kai ta dyo /count ara den xreiazetai
                conditionalP=(element[1]/d_list[element[0][1]])
                #print(f"{conditionalP:.10f}")
                Hx+=conditionalP*(-math.log2(conditionalP))
            print(f"H(xn|xn+1) = {Hx}")
        ypoSyn8hkhEntropia(dd)
        