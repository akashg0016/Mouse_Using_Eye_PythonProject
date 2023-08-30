import math
class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def find_distance(p1,p2):
        return  math.sqrt((p1.x-p2.x)**2+ (p1.y - p2.y)**2)
    def brute_force(points,n):
        minimum = float('inf')
        for i in range(n):
            for j in range(i+1 , n):
                if points.find_distance(points[i], points[j])< minimum:
                    minimum = points.find_distance(points[i], points[j])

        return minimum


#
# n = int(input())
# x = []
# y =[]
# for i in range(n):
#     x = int(input())
#     y = int(input())
# def points():
#     return (x,y)
# r=Point()
# r.brute_force(points(),n)
#
#
#
#
#
