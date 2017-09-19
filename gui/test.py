# encoding: utf-8
'''
Created on 2017年6月13日

@author: haoweizh
'''
import unittest
import Tkinter as tk

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    root = tk.Tk()
    root.configure(bd=0)
    canvas = tk.Canvas(root, bg="white", highlightthickness=0)
    canvas.pack(expand=1, fill="both")
#     item = TreeWidget.FileTreeItem("/")
#     #item=['1','2','3']
#     node = TreeWidget.TreeNode(canvas, None, item)
#     node.update()
    canvas.focus_set()
    root.mainloop() 