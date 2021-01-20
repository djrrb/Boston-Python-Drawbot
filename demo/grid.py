grid = 100
for page in range(10):
    newPage(1000, 1000)
    for y in range(0, height(), grid):
        for x in range(0, width(), grid):
            fill(random(), random(), random())
            oval(x, y, 100, 100)
    
saveImage('~/desktop/grid.pdf')