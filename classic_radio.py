# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classic_radio.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


##########################################
#程式檔名：classic_radio
#程式名稱：古典音樂台 - 經典重現
#程式類別：PyQt5
#建立日期：2018-12-02
##########################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import  datetime
import os
import webbrowser

class Ui_f_dialog(object):
    def setupUi(self, f_dialog):
        f_dialog.setObjectName("f_dialog")
        f_dialog.resize(630, 480)
        f_dialog.setMinimumSize(QSize(630, 480))
        f_dialog.setFocusPolicy(Qt.ClickFocus)
        f_dialog.setContextMenuPolicy(Qt.ActionsContextMenu)
        f_dialog.setWhatsThis("")
        self.gridLayout = QGridLayout(f_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.f_dateEdit = QDateEdit(f_dialog)
        self.f_dateEdit.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers)
        self.f_dateEdit.setObjectName("f_dateEdit")
        self.horizontalLayout.addWidget(self.f_dateEdit)
        self.f_qry = QPushButton(f_dialog)
        self.f_qry.setObjectName("f_qry")
        self.horizontalLayout.addWidget(self.f_qry)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.f_table = QTableWidget(f_dialog)
        self.f_table.setSortingEnabled
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.f_table.sizePolicy().hasHeightForWidth())
        sizePolicy.setHorizontalPolicy(QSizePolicy.Expanding)
        self.f_table.setSizePolicy(sizePolicy)
        self.f_table.setMinimumSize(QSize(0, 420))
        self.f_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.f_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.f_table.setObjectName("f_table")
        self.f_table.setColumnCount(3)
        self.f_table.setRowCount(0)
        item = QTableWidgetItem()
        font = QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.f_table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.f_table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.f_table.setHorizontalHeaderItem(2, item)
        self.f_table.horizontalHeader().setCascadingSectionResizes(True)
        self.f_table.horizontalHeader().setSortIndicatorShown(True)
        self.f_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.f_table)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.retranslateUi(f_dialog)
        f_dialog.setTabOrder(self.f_dateEdit, self.f_qry)
        f_dialog.setTabOrder(self.f_qry, self.f_table)
        self.f_dateEdit.setDate(QDate(datetime.now()))
        print('self.f_dateEdit:', type(self.f_dateEdit))
        print(self.f_dateEdit)
        print('datetime.now:',type(QDate(datetime.now())))
        print(QDate(datetime.now()))
        self.siginal_trigger()
        self.createContextMenu(f_dialog)
        self.cpp =QApplication.clipboard()
        

    def retranslateUi(self, f_dialog):
        _translate = QCoreApplication.translate
        f_dialog.setWindowTitle(_translate("f_dialog", "古典音樂台 - 經典重現"))
        self.f_qry.setText(_translate("f_dialog", "查詢"))
        item = self.f_table.horizontalHeaderItem(0)
        item.setText(_translate("f_dialog", "節目名稱"))
        item = self.f_table.horizontalHeaderItem(1)
        item.setText(_translate("f_dialog", "播出時段"))
        item = self.f_table.horizontalHeaderItem(2)
        item.setText(_translate("f_dialog", r"mms連結(雙擊網址直接收聽)"))
        f_dialog.setWindowIcon(QIcon('music.ico'))
        #item.setSizeHint(QSize(500,0))
        #item.setMinimumSize(
    
    def qry_url(self):
        l_datetime = self.f_dateEdit.dateTime().toPyDateTime().strftime('%Y%m%d') #取得存檔時間
        l_datetime = str(l_datetime)
        html = urlopen("http://www1.family977.com.tw/Reprogress_00.asp?strDay=%s#" % l_datetime) 
        bs = BeautifulSoup(html,'html5lib')
        soup1 = bs.find_all('td',{'class':'t2-2'})
        self.table_init()
        l_i = 0
        for item in soup1:
            for cell in item.find_all('tr'):
                #rint(cell.find_all('td')
                #print(cell.td.text)
                l_list = []
                #取得節目名稱、節目播放時間
                for item1 in cell.select('td a')[1:3]:
                    if item1.text.strip() is not None:
                        l_list.append(item1.text.strip())
                if l_list == []:
                    continue
                try:
                    #取得mms連結
                    l_list.append(cell.find('a',{"href":'#'}).attrs['onclick'].split(sep=',')[0]
                              .split(sep='=')[1][:-1])
                except:
                    pass
                self.f_table.insertRow(l_i)   #新增一列
                self.table_insert(l_i, l_list)
                print(l_list)
                l_i += 1
                
    def siginal_trigger(self):
        QMetaObject.connectSlotsByName(f_dialog)
        self.f_qry.clicked.connect(self.qry_url)
        self.f_table.itemDoubleClicked.connect(self.listen_now)
    
    def table_init(self):
        self.f_table.setRowCount(0)
        
    def table_insert(self, p_ind, p_row):
        #[列號,col1_vaule,col2_value,col3_value]
        item0 = QTableWidgetItem()
        item1 = QTableWidgetItem()
        item2 = QTableWidgetItem()
        str0 = p_row[0]
        try:
            str1 = p_row[1]
        except:
            str1= None
        try:
            str2 = p_row[2]
        except:
            str2 = None
        item0.setText(str0)
        item0.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        self.f_table.setItem(p_ind, 0, item0)
        item1.setText(str1)
        item1.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        self.f_table.setItem(p_ind, 1, item1)
        item2.setText(str2)
        item2.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        self.f_table.setItem(p_ind, 2, item2)
        
    def createContextMenu(self, f_dialog):
        '''
        创建右键菜单
        '''
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        f_dialog.setContextMenuPolicy(Qt.CustomContextMenu)
        f_dialog.customContextMenuRequested.connect(self.showContextMenu)
 
        # 创建QMenu
        self.contextMenu = QMenu()
        self.actionA = self.contextMenu.addAction(u'複製到剪貼簿')
        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.actionA.triggered.connect(self.actionHandler)
    def actionHandler(self):
        #菜单中的具体action调用的函数
        print('菜单中的具体action调用的函数')
        try:
            #取得當前滑鼠選取cell中的值
            l_current_text = self.f_table.currentItem().text()
        except:
            pass
        #複製到剪貼簿
        self.cpp.setText(l_current_text)
        print(l_current_text)
    def showContextMenu(self, f_dialog):
        '''
        右键点击时调用的函数
        '''
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.popup(QCursor.pos())
    def listen_now(self):
        try:
            l_url = (self.f_table.currentItem().text())
        except:
            return
        if l_url[0:3] == 'mms':
            print(l_url)
            webbrowser.open_new_tab(l_url)
        
#--------------------- 
#作者：tinym87 
#来源：CSDN 
#原文：https://blog.n.net/tinym87/article/details/6922199 
#版权声明：本文为博主原创文章，转载请附上博文链接！


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    f_dialog = QDialog()
    ui = Ui_f_dialog()
    ui.setupUi(f_dialog)
    f_dialog.show()
    sys.exit(app.exec_())

