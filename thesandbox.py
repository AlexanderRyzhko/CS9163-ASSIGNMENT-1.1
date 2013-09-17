from sys import argv
var_dic = {'a': 0, 'b': 0, 'c': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,'q': 0, 'r': 0, 's': 0,'t': 0, 'u': 0, 'v': 0,'w': 0, 'x': 0, 'y': 0, 'z':0, 'R': 0, 'd': 0}

instr_all = []

spisok_instrukciy = ["EQL","NEQ","GRE","LES","GRQ", "LEQ", "LOG", "ASS", "ADD", "SUB", "MUL", "DEV", "MOD",  "ADD", "OR", "NOT", "JUM","DEC"]
spisochek_instrukciy = spisok_instrukciy [:6]


ERROR = ["ERROR0:Wrong number of arguments!","ERROR1:Could not open file","ERROR2:Instruction line is too long!", "ERROR3: INVALID INSTRUCTION!", "ERROR4:INVALID VARIABLE OR VALUE", "ERROR5:ASSIGGMENT ERROR!", "ERROR6:DIVIDING BY 0", "ERROR7:SYNTAX ERROR","ERROR8:LIMITS OR BOUNDS ERROR","ERROR9: DOUBLE ENTRY", "ERROR" ]
col_arg = len(argv)
max_char_lenght = 60
#max_ifs = 20
#max_whl = 5
max_instrs = 10000
max_var = max_instrs 
max_var_len = 7
cur_instr = 0

if (col_arg) != 2:
	print(ERROR[0])
	exit(1)
	
filename = argv[1]

def next():
	global cur_instr
	cur_instr += 1
	if(cur_instr >= len(instr_all)):
		exit(0)
def jump(num):
	global cur_instr
	cur_instr = num
	if(cur_instr<-1):
		print(ERROR[8])
		exit(1)
	elif(cur_instr >= len(instr_all)):
		exit(0)

def open_file(filename):
	try:
		inst_file = open(filename, 'r')
	except:
		print(ERROR[1])
		exit(1)
	return inst_file

def read_my_line(fily, max_size = max_char_lenght ):
	red = ""
	while(max_size !=0 ):
		char = fily.read(1)
		if(char==''):
			return ''
		red = red + char
		
		if(red[-1:] == '\n' ):
			return red[:-1].split()
		max_size-= 1
	print(ERROR[2])
	exit(1)

def load_inst(inst_file):
	listy =[]
	line = read_my_line(inst_file)
	while(line != ''):
		listy+= [line]	
		line = read_my_line(inst_file)
		if (len(listy)> max_instrs):
			print(ERROR[8])
			exit(1)
		
	return listy

def check_instr(instr):
	if (instr == []):
		exit(1)
	if not(instr[0] in spisok_instrukciy):
		print(ERROR[3])
		exit(1)
def check_sub_instr(instr):
	if not(instr[0] in spisochek_instrukciy):
		print(ERROR[3])
		exit(1)

def var_check(var):
	
	if not(var in var_dic):
		print(ERROR[4])
		exit(1)

def one_var(var1):
	
	if(var1.isdigit()):
		try:	
			temp1 = int(var1)
		except:
			print(ERROR[4])
			exit(1)
		if(type(temp1) != type(2)):
			print(ERROR[4])
			exit(1)
	else:
		var_check(var1)
		temp1 = var_dic[var1]
	return temp1

def two_var(instr):
	
	if(len(instr)!=3):
		print(ERROR[3])
		exit(1)
	var1 = instr[1]
	var2 = instr[2]
	if(var1.isdigit()):
		try:	
			temp1 = int(var1)
		except:
			print(ERROR[4])
			exit(1)
		if(type(temp1) != type(2)):
			print(ERROR[4])
			exit(1)
	else:
		var_check(var1)
		temp1 = var_dic[var1]

	if(var2.isdigit()):
		try:
			
			temp2 = int(var2)
			
			
		except:
			
			print(ERROR[4])
			exit(1)
		if(type(temp2) != type(2)):
			print(ERROR[4])
			exit(1)
	else:
		var_check(var2)
		temp2 = var_dic[var2]
	return [temp1, temp2]


def log(instr):
	if(len(instr)<2):
		print(ERROR[3])
		exit(1)
	p_list = []
	for v in instr[1:]:
		p_list+=[one_var(v)]
	for i in p_list[:-1]:
		print i,
	print p_list[-1]
	

def ass(instr):
	if(len(instr)!=3):
		print(ERROR[3])
		exit(1)
	var_check(instr[-1])
	var = instr[-1]
	value = one_var(instr[1])
	var_dic[var] = value	


def add(instr):
	a,b = two_var(instr)
	r = a+b	
	if(type(r) != type(2)):
		print(ERROR[4])
		exit(1)
	var_dic['R'] = r
	 
def sub(instr):
	a,b = two_var(instr)
	r = a-b
	if(type(r) != type(2)):
	
		print(ERROR[4])
		exit(1)
	var_dic['R'] = r
	
def mul(instr):
	a,b = two_var(instr)
	r = a*b
	if(type(r) != type(2)):
		print(ERROR[4])
		exit(1)
	var_dic['R'] = r
def dev(instr):
	a,b = two_var(instr)
	if(b == 0):
		print(ERROR[6])
		exit(1)
	r = a/b
	if(type(r) != type(2)):
		print(ERROR[4])
		exit(1)
	var_dic['R'] = r 

def mod(instr):
	a,b = two_var(instr)
	if(b == 0):
		print(ERROR[6])
		exit(1)
	r = a%b
	if(type(r) != type(2)):
		print(ERROR[4])
		exit(1)
	var_dic['R'] = r 
def eql(instr):
	a,b = two_var(instr)
	r = int(a==b)
	var_dic['R'] = r 
def neq(instr):
	a,b = two_var(instr)
	r = int(a!=b)
	var_dic['R'] = r

def gre(instr):
	a,b = two_var(instr)
	r = int(a>b)
	var_dic['R'] = r
def les(instr):
	
	a,b = two_var(instr)
	r = int(a<b)
	var_dic['R'] = r

def grq(instr):
	a,b = two_var(instr)
	r = int(a>=b)
	var_dic['R'] = r

def leq(instr):	
	a,b = two_var(instr)
	r = int(a<=b)
	var_dic['R'] = r

def AND(instr):
	a,b = two_var(instr)
	r = a&b
	var_dic['R'] = r

def OR(instr):
	a,b = two_var(instr)
	r = a|b
	var_dic['R'] = r

def NOT(instr):
	a = one_var(instr[-1])
	r = (~a)
	var_dic['R'] = r

def instr_sub_fork(instr):
	
	check_sub_instr(instr)
	instr_c = instr[0] 
	if(instr_c == "EQL"):
		eql(instr)
	elif(instr_c == "NEQ"):
		neq(instr)
	elif(instr_c == "GRE"):
		gre(instr)
	elif(instr_c == "LES"):
		les(instr)
	elif(instr_c == "GRQ"):
		grq(instr)
	elif(instr_c == "LEQ"):
		leq(instr)
	else:
		print(ERROR[3])
		exit(1)	
	
def jum(instr):
	if(len(instr) ==6) : 
		instr_sub_fork(instr[1:-2])
		if(var_dic['R']):
			var = one_var(instr[-2])
			jump(var-2)
		else:
			var = one_var(instr[-1])
			jump(var-2)
	elif(len(instr) ==5):
		instr_sub_fork(instr[1:-1])
		if(var_dic['R']):
			var = one_var(instr[-1])
			jump(var-2)
			
	else:
		print(ERROR[3])
		exit(1)	
def DEC(instr):
	if (len(instr)!=2):
		print(ERROR[3])
		exit(1)
	if (instr[-1] in var_dic):
		print(ERROR[9])
		exit(1)
	if (instr[-1].isdigit()):
		print(ERROR[4])
		exit(1)
	if(len(instr[-1].split('.'))!=1):
		print(ERROR[4])
		exit(1)
	if(len(instr[-1])>max_var_len):
		print(ERROR[4])
		exit(1)
	try:
		var_dic[instr[-1]] = 0
	except:
		print(ERROR[-1])
		exit(1)
	if (len(var_dic)>max_var):
		print(ERROR[8])
		exit(1)
	
def instr_fork(instr):
	
	check_instr(instr)
	instr_c = instr[0]
	if instr_c == "LOG":
		log(instr)
	elif(instr_c == "ASS"):
		ass(instr)
	elif(instr_c == "ADD"):
		add(instr)
	elif(instr_c == "SUB"):
		sub(instr)
	elif(instr_c == "MUL"):
		mul(instr)
	elif(instr_c == "DEV"):
		dev(instr)
	elif(instr_c == "MOD"):
		mod(instr)
	elif(instr_c == "EQL"):
		eql(instr)
	elif(instr_c == "NEQ"):
		neq(instr)
	elif(instr_c == "GRE"):
		gre(instr)
	elif(instr_c == "AND"):
		AND(instr)
	elif(instr_c == "OR"):
		OR(instr)
	elif(instr_c == "LES"):
		les(instr)
	elif(instr_c == "GRQ"):
		grq(instr)
	elif(instr_c == "LEQ"):
		leq(instr)
	elif(instr_c == "NOT"):
		NOT(instr)
	elif (instr_c == "JUM"):
		jum(instr)
	elif (instr_c == "DEC"):
		DEC(instr)
	else:
		print(ERROR[3])
		exit(1)

inst_file = open_file(filename)	
instr_all = load_inst(inst_file)



while(cur_instr< len(instr_all)):
	instr_fork(instr_all[cur_instr])	
	next()
	
	



