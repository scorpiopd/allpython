# Docstring


def docstring():
    "this is called docsting"
    return docstring

print(docstring.__doc__)

#this is called multi line string

" eqdede" \
"efdewfef"

"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

#function annotation

def myanno(a:"a string",b:"b hello")-> "a string":
    return a * b
print(myanno.__annotations__)


x=3
y=5
def anno(a:str)-> "a repeated " + str(max(x,y)) + " times":
    return a * max(x,y)
print(anno.__annotations__)

#notes
"def is a statement that creates the function & that runs whens" \
"its  first encountered & everytime you call a function it doesnt recreate" \
"function it already has it "

"annotation is metadata that doesnt affect the code "

"where is python use docstring and annotations " \
"it doesnt really it is used by external tools and modules eg:(sphinx)" \
"used by help function"