# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        width=(C-A)+(G-E)-(max(C,G)-min(A,E))
        height=(D-B)+(H-F)+(max(D,H)-min(B,F))
        area1=(C-A)*(D-B)
        area2=(G-E)*(H-F)
        return area2+area1-(width*height)
