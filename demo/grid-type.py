from random import choice
inch = 72

grid = 100

def pageSetup():
    newPage('Letter')
    rect(0, 0, width(), height())
    for y in range(0, height(), grid):
        for x in range(0, width(), grid):
            fill(random(), random(), random())
            oval(x, y, 100, 100)

m = 42


with open('assets/gatsby-short.txt', 'r', encoding="utf-8") as textfile:
    myText = textfile.read()
    while myText:
        pageSetup()
        marginWidth = width()-m*2
        marginHeight = height()-m*2

        innerWidth = marginWidth-m*2
        innerHeight = marginHeight-m*2
        font('InputMonoNarrow-Light')
        fontSize(22)

        fill(1)
        rect(m, m, marginWidth, marginHeight)
        fill(0)
        myText = textBox(myText, (m*2, m*2, innerWidth, innerHeight))

#saveImage('grid.gif')