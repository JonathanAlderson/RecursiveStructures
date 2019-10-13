import tkinter,random,math,time
def createTree(treeStartX,treeStartY,branchingChance,branchingMin,branchingMax,bearing,depth,distance):
    finalX = treeStartX + distance * (math.sin(bearing*((2*math.pi) /360)))
    finalY = treeStartY - distance * (math.cos(bearing*((2*math.pi) /360)))
    if depth > 0:
        for i in range(0,int(distance)):
            if random.random() < branchingChance:
                createTree(treeStartX + (finalX-treeStartX)*(i/distance),treeStartY + (finalY-treeStartY)*(i/distance),branchingChance,branchingMin,branchingMax,bearing + random.choice([1,-1]) * random.randint(branchingMin,branchingMax),depth-1,distance/2) 
    mycanvas.create_line(treeStartX,treeStartY,finalX,finalY)
    mycanvas.update()
window = tkinter.Tk()
mycanvas = tkinter.Canvas(width=600,height=600)
mycanvas.pack()
while True:
    createTree(600/2,600,0.04,5,20,0,4,600/2)
    mycanvas.update()
    time.sleep(1)
    mycanvas.delete('all')
tkinter.mainloop()
