# Python3 program for Shannon Fano Algorithm
from collections import defaultdict
#erwthma 4

# declare structure node
class node :
	def __init__(self) -> None:
		# for storing symbol
		self.sym=''
		# for storing probability or frequency
		self.pro=0.0
		self.arr=[0]*20
		self.top=0
p=[node() for _ in range(28)]

# function to find shannon code
def shannon(l, h, p):
	pack1 = 0; pack2 = 0; diff1 = 0; diff2 = 0
	if ((l + 1) == h or l == h or l > h) :
		if (l == h or l > h):
			return
		p[h].top+=1
		p[h].arr[(p[h].top)] = 0
		p[l].top+=1
		p[l].arr[(p[l].top)] = 1
		
		return
	
	else :
		for i in range(l,h):
			pack1 = pack1 + p[i].pro
		pack2 = pack2 + p[h].pro
		diff1 = pack1 - pack2
		if (diff1 < 0):
			diff1 = diff1 * -1
		j = 2
		while (j != h - l + 1) :
			k = h - j
			pack1 = pack2 = 0
			for i in range(l, k+1):
				pack1 = pack1 + p[i].pro
			for i in range(h,k,-1):
				pack2 = pack2 + p[i].pro
			diff2 = pack1 - pack2
			if (diff2 < 0):
				diff2 = diff2 * -1
			if (diff2 >= diff1):
				break
			diff1 = diff2
			j+=1
		
		k+=1
		for i in range(l,k+1):
			p[i].top+=1
			p[i].arr[(p[i].top)] = 1
			
		for i in range(k + 1,h+1):
			p[i].top+=1
			p[i].arr[(p[i].top)] = 0
			

		# Invoke shannon function
		shannon(l, k, p)
		shannon(k + 1, h, p)
	


# Function to sort the symbols
# based on their probability or frequency
def sortByProbability(n, p):
	temp=node()
	for j in range(1,n) :
		for i in range(n - 1) :
			if ((p[i].pro) > (p[i + 1].pro)) :
				temp.pro = p[i].pro
				temp.sym = p[i].sym

				p[i].pro = p[i + 1].pro
				p[i].sym = p[i + 1].sym

				p[i + 1].pro = temp.pro
				p[i + 1].sym = temp.sym
			
def getCode():
	# Input number of symbols
    paths = ["files/CA_3.csv"]
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
        total =0
        n=0
        for el in dd:
            print (el[0] + ' '+ str(el[1])+" -> p(x) = "+str(el[1]/count))
            p[n].sym +=el[0] 
            p[n].pro=el[1]/count
            total=total+p[n].pro
            n+=1
        

       # their probability or frequency
        sortByProbability(n, p)

        for i in range(n):
            p[i].top = -1

        # Find the shannon code
        shannon(0, n - 1, p)

        # Display the codes
        display(n, p)
		
	


# function to display shannon codes
def display(n, p):
	print("\n\n\n\tSymbol\tProbability\tCode",end='')
	for i in range(n - 1,-1,-1):
		print("\n\t", p[i].sym, "\t\t", f"{p[i].pro:.4f}","\t",end='')
		for j in range(p[i].top+1):
			print(p[i].arr[j],end='')
	


# Driver code
if __name__ == '__main__':
	total = 0
	if input("show code? y/n\n")=='y':
		getCode()
	encoding={
		"a":"000",
		"e":"001",
		"n":"0100",
		"i":"0101",
		"r":"0110",
		"l":"0111",
		"o":"1000",
		"s":"1001",
		"h":"1010",
		"t":"10110",
		"m":"10111",
		"d":"11000",
		"c":"11001",
		"u":"11010",
		"y":"11011",
		"k":"11100",
		"g":"111010",
		"b":"111011",
		"j":"111100",
		"p":"1111010",
		"v":"1111011",
		"w":"1111100",
		"f":"1111101",
		"z":"1111110",
		"x":"11111110",
		"q":"11111111",
		"000":"a",
		"001 ":"e",
		"0100":"n",
		"0101":"i",
		"0110":"r",
		"0111":"l",
		"1000":"o",
		"1001":"s",
		"1010":"h",
		"10110":"t",
		"10111":"m",
		"11000":"d",
		"11001":"c",
		"11010":"u",
		"11011":"y",
		"11100":"k",
		"111010":"g",
		"111011":"b",
		"111100":"j",
		"1111010":"p",
		"1111011":"v",
		"1111100":"w",
		"1111101":"f",
		"1111110":"z",
		"11111110":"x",
		"11111111":"q",
		}
