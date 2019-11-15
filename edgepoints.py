import imutils
import cv2
import numpy as nP

def line_check(i,j,edge,check,lines,lno):
    if i-1 >= 0 and j-1 >= 0:
        if  edge[i-1][j-1] > 0 and check[i-1][j-1] == False:
            check[i-1][j-1] = True
            coord = (i,j)
            lines[lno].append(coord)
            line_check(i-1,j-1,edge,check,lines,lno)
        else:
            check[i-1][j-1] = True

    if i-1 >= 0:
        if edge[i-1][j] > 0 and check[i-1][j] == False:
            check[i-1][j] = True
            coord = (i,j)
            lines[lno].append(coord)
            line_check(i-1,j,edge,check,lines,lno)
        else:
            check[i-1][j] = True

    if i-1 >= 0 and j+1 < len(edge[i]) and edge[i-1][j+1] > 0 and check[i-1][j+1] == False:
        check[i-1][j+1] = True
        coord = (i,j)
        lines[lno].append(coord)
        line_check(i-1,j+1,edge,check,lines,lno)
    elif i-1 >= 0 and j+1 < len(edge[i]):
        check[i-1][j+1] = True

    if j-1 >= 0 and edge[i][j-1] > 0 and check[i][j-1] == False:
        check[i][j-1] = True
        coord = (i,j)
        lines[lno].append(coord)
        line_check(i,j-1,edge,check,lines,lno)
    elif j-1 >= 0:
        check[i][j] = True

    if j+1 < len(edge[i]) and edge[i][j+1] > 0 and check[i][j+1] == False:
        check[i][j+1] = True
        coord = (i,j)
        lines[lno].append(coord)
        line_check(i,j+1,edge,check,lines,lno)
    elif j+1 < len(edge[i]):
        check[i][j+1] = True

    if i+1 < len(edge) and j-1 >= 0 and edge[i+1][j-1] > 0 and check[i+1][j-1] == False :
        check[i][j] = True
        coord = (i,j)
        lines[lno].append(coord)
        line_check(i+1,j-1,edge,check,lines,lno)
    elif i+1 < len(edge) and j-1 >= 0:
        check[i+1][j-1] = True

    if i+1 < len(edge) and edge[i+1][j] > 0 and check[i+1][j] == False:
        check[i+1][j] = True
        coord = (i,j)
        lines[lno].append(coord)
        line_check(i+1,j,edge,check,lines,lno)
    elif i+1 < len(edge):
        check[i+1][j] = True

    if i+1 < len(edge) and j+1 < len(edge[i]) and edge[i+1][j+1] > 0 and check[i+1][j+1] == False:
        check[i+1][j+1] = True
        coord = (i,j)
#        print(lno)
        lines[lno].append(coord)
        line_check(i+1,j+1,edge,check,lines,lno)
    elif i+1 < len(edge) and j+1 < len(edge[i]):
        check[i+1][j+1] = True



#print(checked)

def generate_edgepoints(edges):
    cv2.imwrite('./edges.png', edges)
    checked = [ [False for x in edges[0]] for x in edges]
    lineno = 0
    lines = [[]]
    for i in range(0,len(edges)):
        for j in range(0,len(edges[i])):
            if not checked[i][j]:
                if edges[i][j] > 0:
                    line_check(i,j,edges,checked,lines,lineno)
                    lineno += 1
                    lines.append([])
                else:
                    checked[i][j] = True
    del lines[-1]
    return lines


