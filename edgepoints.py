import imutils
import cv2
import numpy as nP

def line_check(i,j,edge,check,lines,lno):
#    #a pixel being checked means that it has gone under the conditional statement
#    #pixel > 0
#    #where pixel is the value at a given pixel in edge
#
#    #Top left pixel
#    if i-1 >= 0 and j-1 >= 0: #if these coordinates are within bounds of the image
#        if  edge[i-1][j-1] > 0 and check[i-1][j-1] == False: 
#            check[i-1][j-1] = True 
#            coord = (i,j)
#            lines[lno[0]].append(coord) 
#            line_check(i-1,j-1,edge,check,lines,lno[0])
#        else:
#            check[i-1][j-1] = True
#
#    #Top middle pixel
#    if i-1 >= 0:
#        if edge[i-1][j] > 0 and check[i-1][j] == False:
#            check[i-1][j] = True
#            coord = (i,j)
#            lines[lno[0]].append(coord)
#            line_check(i-1,j,edge,check,lines,lno[0])
#        else:
#            check[i-1][j] = True
#
#    #Top right pixel
#    if i-1 >= 0 and j+1 < len(edge[i]):
#        if edge[i-1][j+1] > 0 and check[i-1][j+1] == False:
#            check[i-1][j+1] = True
#            coord = (i,j)
#            lines[lno[0]].append(coord)
#            line_check(i-1,j+1,edge,check,lines,lno[0])
#        else:
#            check[i-1][j+1] = True
#
#    #Middle left pixel
#    if j-1 >= 0:
#        if edge[i][j-1] > 0 and check[i][j-1] == False:
#            check[i][j-1] = True
#            coord = (i,j)
#            lines[lno[0]].append(coord)
#            line_check(i,j-1,edge,check,lines,lno[0])
#        else:
#            check[i][j] = True
#
#    #Middle Right pixel
#    if j+1 < len(edge[i])
#        if edge[i][j+1] > 0 and check[i][j+1] == False:
#            check[i][j+1] = True
#            coord = (i,j)
#            lines[lno[0]].append(coord)
#            line_check(i,j+1,edge,check,lines,lno[0])
#        else:
#            check[i][j+1] = True
#
#    #Bottom left pixel
#    if i+1 < len(edge) and j-1 >= 0:
#        if edge[i+1][j-1] > 0 and check[i+1][j-1] == False :
#            check[i+1][j-1] = True
#            coord = (i,j)
#            lines[lno[0]].append(coord)
#            line_check(i+1,j-1,edge,check,lines,lno[0])
#        else:
#            check[i+1][j-1] = True
#
#    #Bottom middle pixel
#    if i+1 < len(edge):
#        if edge[i+1][j] > 0 and check[i+1][j] == False:
#            check[i+1][j] = True
#            coord = (i,j)
#            lines[lno[0]].append(coord)
#            line_check(i+1,j,edge,check,lines,lno[0])
#        else:
#            check[i+1][j] = True

    #Loop version of the same damn code
    for m in range(-1,2):
        for n in range(-1,2):
            if j+n >= 0 and i+m >= 0 and i+m < len(edge) and j+n < len(edge[i]):
                if edge[i+m][j+n] > 0 and check[i+m][j+n] == False:	#if the pixel is not black and has not been checked :
                    check[i+m][j+n] = True	#mark that it is being checked
                    coord = (i,j)
                    #print('linenum:', lno[0])
                    #print('lenline:', len(lines))
                    if is_adjacent(coord, lines[lno[0]][-1]):
                        lines[lno[0]].append(coord)	#add this pixel to the lines list
                    else:
                        lno[0] += 1
                        lines.append([coord])

                    line_check(i+m,j+n,edge,check,lines,lno)
                else:
                    check[i+m][j+n] = True

def is_adjacent(current_coord, last_in_line):
    adjacent_to_current = [(x,y) for x in range(current_coord[0]-1, current_coord[0]+2)
                            for y in range(current_coord[1]-1, current_coord[1]+2)]
    print(adjacent_to_current)

    if last_in_line in adjacent_to_current:
        return True
    else:
        return False


def generate_edgepoints(edges):
    cv2.imwrite('./edges.png', edges)
    checked = [ [False for x in edges[0]] for x in edges]

#rotates and flips image to fix the flipping and rotating that happens during linecheck
    edges = cv2.flip(edges, 0)
    edges = imutils.rotate_bound(edges, 90)

    lineno = [0] #do this so lineno is passed by reference, there are better ways but this is easy
    #good luck future self

    lines = [[]]
    for i in range(0,len(edges)):
        for j in range(0,len(edges[i])):
            if not checked[i][j]:
                if edges[i][j] > 0:
                    lines[lineno[0]].append((i,j))
                    line_check(i,j,edges,checked,lines,lineno)
                    lineno[0] += 1
                    lines.append([])
                else:
                    checked[i][j] = True
    del lines[-1]
    return lines


