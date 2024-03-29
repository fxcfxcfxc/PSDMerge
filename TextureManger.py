
from tkinter.constants import HORIZONTAL, W
from typing import List
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QPixmap
from PySide2.QtGui import  QIcon
from PySide2.QtCore import QFile
import tkinter as tk    
from  tkinter import Tk, messagebox
from tkinter import filedialog
from PIL import Image
import os
import json
from psd_tools import PSDImage
from time import sleep



class MainWindow:

    
    def __init__(self):
        self.ui = QUiLoader().load('ui.ui')

        #判断目录下是否存在json文件，如果存在就读取数据
        if os.path.exists('json_data.json'):
            self.tex_data = {}

            with open('json_data.json','r') as f:
                self.tex_data = json.load(f)

            self.ui.basename.setText(self.tex_data['base_name'])
            self.ui.r_name.setText(self.tex_data['r_name'])
            self.ui.g_name.setText(self.tex_data['g_name'])
            self.ui.b_name.setText(self.tex_data['b_name'])
            self.ui.a_name.setText(self.tex_data['a_name'])


        if os.path.exists('mark_data.json'):
            self.tex_data = {}

            with open('mark_data.json','r') as f:
                self.tex_data = json.load(f)

    
            self.ui.mark_r.setText(self.tex_data['r_mark'])
            self.ui.mark_g.setText(self.tex_data['g_mark'])
            self.ui.mark_b.setText(self.tex_data['b_mark'])
            self.ui.mark_a.setText(self.tex_data['a_mark'])




        if os.path.exists('rgba_data.json'):
            self.tex_data = {}

            with open('rgba_data.json','r') as f:
                self.tex_data = json.load(f)

    
            self.ui.default_r.setText(self.tex_data['r_default'])
            self.ui.default_g.setText(self.tex_data['g_default'])
            self.ui.default_b.setText(self.tex_data['b_default'])
            self.ui.default_a.setText(self.tex_data['a_default'])


            self.ui.merge_r_c.setText(self.tex_data['r_mergec'])
            self.ui.merge_g_c.setText(self.tex_data['g_mergec'])
            self.ui.merge_b_c.setText(self.tex_data['b_mergec'])
            self.ui.merge_a_c.setText(self.tex_data['a_mergec'])


        #功能绑定
        
        self.ui.r_pushButton.clicked.connect(self.r_openFile)
        self.ui.g_pushButton.clicked.connect(self.g_openFile)
        self.ui.b_pushButton.clicked.connect(self.b_openFile)
        self.ui.a_pushButton.clicked.connect(self.a_openFile)

        self.ui.psd_Button.clicked.connect(self.psd_openFile)
        self.ui.out_Button.clicked.connect(self.extrac_psd)

        self.ui.mergeButton.clicked.connect(self.merge_texture)
        self.ui.tex_json.clicked.connect(self.name_data)
        self.ui.pushButton.clicked.connect(self.resert)
        self.ui.mark_Button.clicked.connect(self.mark_data)

        self.ui.mark_Button_3.clicked.connect(self.rgba_data)
        self.ui.coust_Button.clicked.connect(self.customExportPath)

    #RGB路径读取文件
    def customExportPath(self):
        filePath = QFileDialog.getExistingDirectory(self.ui, "选择存储路径")
        self.ui.lineEdit_5.setText(filePath)

    def r_openFile(self):
        
        root = tk.Tk()
        root.withdraw()

        Filepath_r = filedialog.askopenfilename()      
        self.ui.r_lineEdit.setText(Filepath_r)

    def g_openFile(self):
        
        root = tk.Tk()
        root.withdraw()

        Filepath_g = filedialog.askopenfilename()
        self.ui.g_lineEdit.setText(Filepath_g)       


    def b_openFile(self):
        
        root = tk.Tk()
        root.withdraw()

        Filepath_b = filedialog.askopenfilename()
        self.ui.b_lineEdit.setText(Filepath_b)


    def a_openFile(self):
        
        root = tk.Tk()
        root.withdraw()

        Filepath_a = filedialog.askopenfilename()
        self.ui.a_lineEdit.setText(Filepath_a)
        
    #获取psd大小
    def psd_size(self,psd_path):


        psd = PSDImage.open(psd_path)
        size = psd.size


        return size

        
    #合并贴图
    def merge_texture(self):
        Filepath_r = self.ui.r_lineEdit.text()
        Filepath_g = self.ui.g_lineEdit.text()
        Filepath_b = self.ui.b_lineEdit.text()
        Filepath_a = self.ui.a_lineEdit.text()



        if Filepath_r =="" and Filepath_g == "" and Filepath_b =="" and Filepath_a =="":
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo( "提示", "请先选择PSD获取通道路径")

        else:
            
            #获取四张图片并转换为RGB
            Filepath_psd = self.ui.psd_lineEdit.text()
            size = self.psd_size(Filepath_psd)

            default_r_c = self.ui.default_r.text()
            default_g_c = self.ui.default_g.text()
            default_b_c = self.ui.default_b.text()
            default_a_c = self.ui.default_a.text()

            self.default_r_image = Image.new('RGBA', size, default_r_c)
            self.default_g_image = Image.new('RGBA', size, default_g_c)
            self.default_b_image = Image.new('RGBA', size, default_b_c)
            self.default_a_image = Image.new('RGBA', size, default_a_c)
            
    
            if self.ui.r_lineEdit.text() == "":            
                self.im1 = self.default_r_image           
            elif self.ui.r_lineEdit.text() != "":
                self.im1 = Image.open(Filepath_r)
                self.im1 = self.im1.convert('RGBA')


            if self.ui.g_lineEdit.text() == "": 
                self.im2 = self.default_g_image
            elif self.ui.g_lineEdit.text() != "":
                self.im2 = Image.open(Filepath_g)
                self.im2 = self.im2.convert('RGBA')



            if self.ui.b_lineEdit.text() == "": 
                self.im3 = self.default_b_image
            elif self.ui.b_lineEdit.text() != "":
                self.im3 = Image.open(Filepath_b)
                self.im3 = self.im3.convert('RGBA')
            

            if self.ui.a_lineEdit.text() == "": 
                self.im4 = self.default_a_image
            elif self.ui.a_lineEdit.text() != "":
                self.im4 = Image.open(Filepath_a)
                self.im4 = self.im4.convert('RGBA')
            

            m_r_c = self.ui.merge_r_c.text()
            m_g_c = self.ui.merge_g_c.text()
            m_b_c = self.ui.merge_b_c.text()
            m_a_c = self.ui.merge_a_c.text()


            self.m_r_image = Image.new('RGBA', size, m_r_c)
            self.m_g_image = Image.new('RGBA', size, m_g_c)
            self.m_b_image = Image.new('RGBA', size, m_b_c)
            self.m_a_image = Image.new('RGBA', size, m_a_c)

            

            self.im1 = Image.composite(self.im1,self.m_r_image,self.im1)
            self.im2 = Image.composite(self.im2,self.m_g_image,self.im2)
            self.im3 = Image.composite(self.im3,self.m_b_image,self.im3)
            self.im4 = Image.composite(self.im4,self.m_a_image,self.im4)

            #分离文件的RGB通道并合并
            r1, g1, b1, a1= self.im1.split()
            r2, g2, b2, a2= self.im2.split()
            r3, g3, b3, a3= self.im3.split()
            r4, g4, b4, a4= self.im4.split()
            self.im5 = Image.merge('RGBA', [r1, r2, r3,r4])

            #获取用户的命名规则
            name1 = self.ui.basename.text()        
            name2 = self.ui.r_name.text()
            name3 = self.ui.g_name.text()
            name4 = self.ui.b_name.text()
            name5 = self.ui.a_name.text()
            name6 = self.ui.tex_file_line.text()
            
            #获取输出的文件路径
            if self.ui.lineEdit_5.isEnabled():

                path1 = self.ui.lineEdit_5.text()
            else:
                path1 = os.path.dirname(Filepath_g)

            path2 = name1+name2+name3+name4+name5+name6
            path3 = os.path.join (path1,path2)#路径拼接
                #保存图片
            self.im5.save(path3)

            #删除png
            for pngpath in wlist :
                if os.path.exists(pngpath):  
                    os.remove(pngpath)  
                else:
                    print('no such file')  

            
            #显示图片到预览窗口
            pixmap = QPixmap(path3)
            self.ui.label_image.setPixmap(pixmap)
            self.ui.label_image.setScaledContents (True)#图片适应label大小
            self.ui.pngname_lineEdit.setText(path2)#显示图片名字

            #打开图片路径
            show_path = os.path.dirname(path3)
            os.startfile(show_path)
#---------------------------------psd功能开发-------------------------------------

#获取PSD的路径

    def psd_openFile(self):
        
        root = tk.Tk()
        root.withdraw()      
        Filepath_psd = filedialog.askopenfilename()      
        self.ui.psd_lineEdit.setText(Filepath_psd)
    
    #png到处方法
    def extractLayerImage(self,layer,list_b):

        Filepath_psd = self.ui.psd_lineEdit.text()
        psd_Path = os.path.dirname(Filepath_psd)    
        png_name = "%s.png"%(layer.name)
        png_path = os.path.join (psd_Path,png_name)
        layer_image=layer.composite()        
        layer_image.save(png_path)

        list_b.append(png_path)

        return list_b

    wlist = []
    #分析psd贴图导出PNG
    def extrac_psd(self): 
        mark_r = self.ui.mark_r.text()
        mark_g = self.ui.mark_g.text()
        mark_b = self.ui.mark_b.text()
        mark_a = self.ui.mark_a.text()
        Filepath_psd = self.ui.psd_lineEdit.text()

        if Filepath_psd == "":
            messagebox.showinfo( "提示", "请先选择PSD")
        else:
            psd = PSDImage.open(Filepath_psd)            
            list_b = []
        
            x =100/len(list(psd.descendants()))
            b = 5
            self.ui.progressBar1.setValue(b)                   
            for layer in psd.descendants():
                if layer.name in mark_r or layer.name in mark_g or layer.name in mark_b  or layer.name in mark_a:               
                    global wlist
                    wlist = self.extractLayerImage(layer,list_b)
                b= b+x    
                self.ui.progressBar1.setValue(b)
            #导入路径匹配  
            for f_path in wlist:
                if mark_r in f_path:
                    self.ui.r_lineEdit.setText(f_path)
                elif mark_g in f_path:
                    self.ui.g_lineEdit.setText(f_path)
                
                elif mark_b in f_path:
                    self.ui.b_lineEdit.setText(f_path)

                elif mark_a in f_path:
                    self.ui.a_lineEdit.setText(f_path)

                else:
                    print("无标签匹配")

            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo( "提示", "导入成功，检查正确的文件名，并点击合并输出")
        return 0

    def waring(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo( "提示", "保存成功！")    
#------------------------------------------------------------
    #数据写入json
    def name_data(self):
        self.tex_data = {}
        self.tex_data['base_name'] = self.ui.basename.text()
        self.tex_data['r_name'] = self.ui.r_name.text()
        self.tex_data['g_name'] = self.ui.g_name.text()
        self.tex_data['b_name'] = self.ui.b_name.text()
        self.tex_data['a_name'] = self.ui.a_name.text()

        with open('json_data.json', 'w') as f:
            json.dump(self.tex_data, f)
        self.waring()

    def mark_data(self):
        self.tex_data = {}
        
        self.tex_data['r_mark'] = self.ui.mark_r.text()
        self.tex_data['g_mark'] = self.ui.mark_g.text()
        self.tex_data['b_mark'] = self.ui.mark_b.text()
        self.tex_data['a_mark'] = self.ui.mark_a.text()

        with open('mark_data.json', 'w') as f:
            json.dump(self.tex_data, f)
        self.waring()

    def rgba_data(self):
        self.tex_data = {}
        
        self.tex_data['r_default'] = self.ui.default_r.text()
        self.tex_data['g_default'] = self.ui.default_g.text()
        self.tex_data['b_default'] = self.ui.default_b.text()
        self.tex_data['a_default'] = self.ui.default_a.text()

        self.tex_data['r_mergec'] = self.ui.merge_r_c.text()
        self.tex_data['g_mergec'] = self.ui.merge_g_c.text()
        self.tex_data['b_mergec'] = self.ui.merge_b_c.text()
        self.tex_data['a_mergec'] = self.ui.merge_a_c.text()

        with open('rgba_data.json', 'w') as f:
            json.dump(self.tex_data, f)
        self.waring()

    def  resert(self):
        self.tex_data = {}
        self.tex_data['base_name'] = self.ui.basename.setText('T')
        self.tex_data['r_name'] = self.ui.r_name.setText('_Rock')
        self.tex_data['g_name'] = self.ui.g_name.setText('_06')
        self.tex_data['b_name'] = self.ui.b_name.setText('_m')
        self.tex_data['b_name'] = self.ui.a_name.setText('')
        
        with open('json_data.json', 'w') as f:
            json.dump(self.tex_data, f)

 # 在 if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行
 # 而 import 到其他脚本中是不会被执行的
    
if __name__ == "__main__":
    
    
    #判断app销毁
    app = QApplication.instance()
    if app == None:
        app = QApplication([])
    app.setWindowIcon(QIcon('logo.png'))
    #实列一个窗口对象
    mainwindow = MainWindow()
    mainwindow.ui.show()
    app.exec_()

