import string

def setmain(filepath):
    mainfile = filepath
    

def find(text):                # Find string in main file and return line and line number (line, linenumber)
    search = text
    linenum=1 
    with open(mainfile, 'r') as inF:
        for line in inF:                   
            if search in line:
                return line, linenum
            else:
                linenum=linenum+1

def findin(text, filepath):                # Find string in specified file and return line and line number (line, linenumber)
    search = text                                      
    linenum=1                                           
    with open(file, 'r') as inF:              
        for line in inF:                   
            if search in line:
                return line, linenum                    
            else:
                linenum=linenum+1

def write(text):            # Write string to main file (appending).
    datafile = open(mainfile, 'a')
    datafile.write(text)
    datafile.close

def rewrite(text):               # Write string to main file (overwriting)
    datafile = open(mainfile, 'w')
    datafile.write(text)
    datafile.close

def writeto(text, filepath):            # Write string to specified file (appending).
    datafile = open(filepath, 'a')
    datafile.write(text)
    datafile.close

def rewriteto (text, filepath):              # Write string to specified file (overwriting).
    datafile = open(filepath, 'w')
    datafile.write(text)
    datafile.close
    
def getline(line):              # Get text at specified line in main file.
        linenum=1
        datafile = open(mainfile, 'r')
        while line>linenum:
            text = datafile.readline()
            linenum=linenum+1
        print(text)
        return(text)

def getlinein(line, filepath):              # Get text at specified line in specified file.
        linenum=1
        datafile = open(filepath, 'r')
        while line>linenum:
            text = datafile.readline()
            linenum=linenum+1
        print(text)
        return(text)

def comparelines(line1,line2):           # Compare 2 lines in main file and return similarity as a percentage.
        line1txt = getline(line1)
        line2txt = getline(line2)
        if line1txt == line2txt:
            return("100")
        else:
            print("ITS ALL GONE A BIT WRONG")
