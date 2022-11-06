import sys
import mariadb
import xlwt
from pymysql import*
import pandas.io.sql as sql
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction, QLabel, QMessageBox
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QIcon, QIcon, QMovie, QPixmap
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from random import randint
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer,QDateTime
c = ""
global x
global combo
global x_1
global combo_1
global x_2
global combo_2
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(800,500)
        self.setWindowTitle("Electric Vehicles Evaluation System") 
        self.resize(800, 500) #Tamaño inicial de la ventana 800x500
        #Barra de estado
        self.statusBar().showMessage("Welcome")
        
        self.l1 = QLabel("g",self)
        self.l1.resize(800,460)
        self.l1.move(0,20)
        self.movie = QMovie("ev.gif")
        self.l1.setMovie(self.movie)
        self.movie.start() 

        # Create new action
        evaluationAction = QAction(QIcon(), '&Evaluation', self)        
        evaluationAction.setStatusTip('Evaluation')
        evaluationAction.triggered.connect(self.evaluationCall)

        # Create new action
        eliminateAction = QAction(QIcon(), '&Eliminate', self)        
        eliminateAction.setStatusTip('Eliminate')
        eliminateAction.triggered.connect(self.eliminateCall)
        
        # Create new action
        visualizeAction = QAction(QIcon(), '&Visualize', self)        
        visualizeAction.setStatusTip('Visualize')
        visualizeAction.triggered.connect(self.visualizeCall)
        
        # Create new action
        vehicleAction = QAction(QIcon(), '&Data Base', self)        
        vehicleAction.setStatusTip('Vehicle')
        vehicleAction.triggered.connect(self.vehicleCall)
        
        # Create new action
        exportAction = QAction(QIcon(), '&Export', self)        
        exportAction.setStatusTip('Export')
        exportAction.triggered.connect(self.exportCall)

        # Create exit action
        exitAction = QAction(QIcon(), '&Exit', self)        
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)
        
        # Create help action
        helpAction = QAction(QIcon(), '&Abot Us', self)        
        helpAction.setStatusTip('About Us')
        helpAction.triggered.connect(self.helpCall)

        # Create menu bar and add action
        menu = self.menuBar()
        #Menú padre
        fileMenu = menu.addMenu("&File")
        #Menú padre
        fileTools = menu.addMenu("&Tools")
        #Menú padre
        fileHelp = menu.addMenu("&Help")
        
        fileTools.addAction(evaluationAction)
        fileTools.addAction(eliminateAction)
        fileTools.addAction(visualizeAction)
        fileTools.addAction(vehicleAction)
        fileTools.addAction(exportAction)
        fileMenu.addAction(exitAction)
        fileHelp.addAction(helpAction)

    def eliminateCall(self):
        print('Eliminate')
        eliminateWin.show()
        mainWin.close()

    def evaluationCall(self):
        print('Evaluation')
        evaluationWin.show()
        mainWin.close()
        
    def visualizeCall(self):
        print('Visualize')
        visualizeWin.show()
        mainWin.close()
        
    def vehicleCall(self):
        print('Vehicle')
        global tableWin
        tableWin = Table()
        tableWin.show()
        
    def exportCall(self):
        print('Export')
        exportWin.show()
        mainWin.close()

    def exitCall(self):
        msgBox = QMessageBox.information(self, "Exit", "Do you want to Exit?", QMessageBox.Ok|QMessageBox.Cancel)
        if msgBox == QMessageBox.Ok:
          app.quit()
          
    def helpCall(self):
        about = QMessageBox.about(self, "About Us", "This system is intelectual property of Eng. Pablo Guagalango Gómez. Made in Toluca, Mexico 2021. For more information contact us by the cellphone number 5587679270")
          
          
class Eliminate(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        global cursor
        global x
        global combo
        global x_1
        global combo_1
        global x_2
        global combo_2
        combo = QComboBox(self)
        combo.move(530, 260)
        x = []
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for item in tables:
          x.extend(item)
            #print(x)
        for option in x:
          combo.addItem(option)
        cursor.close()
        conn.close()

        self.setFixedSize(800,500)
        self.setWindowTitle("Electric Vehicles Evaluation System") 
        self.resize(800, 500) #Tamaño inicial de la ventana 800x500
        #Barra de estado
        self.statusBar().showMessage("Welcome")
        
        self.l1 = QLabel("g",self)
        self.l1.resize(400,300)
        self.l1.move(0,100)
        self.movie = QMovie("trash.gif")
        self.l1.setMovie(self.movie)
        self.movie.start()
        
        self.button1 = QPushButton(self)
        self.button1.setText("Eliminate")
        self.button1.move(600,300)
        self.button1.clicked.connect(self.erase)

        self.button2 = QPushButton(self)
        self.button2.setText("Back")
        self.button2.move(450,300)
        self.button2.clicked.connect(self.back_win)

        #self.lineEdit = QtWidgets.QLineEdit(self)
        #self.lineEdit.setGeometry(QtCore.QRect(140, 60, 113, 20))
        #self.lineEdit.move(530,260)
        #self.lineEdit.textChanged.connect(self.text_changed)

        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 60, 47, 13))
        self.label.resize(70,15)
        self.label.move(450,260)
        self.label.setText("Vehicle :")

        # Create new action
        vehicleAction = QAction(QIcon(), '&Data Base', self)        
        vehicleAction.setStatusTip('Vehicle')
        vehicleAction.triggered.connect(self.vehicleCall)
        
        # Create exit action
        exitAction = QAction(QIcon(), '&Exit', self)        
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menu = self.menuBar()
        #Menú padre
        fileMenu = menu.addMenu("&File")
        #Menú padre
        fileTools = menu.addMenu("&Tools")
        
        fileTools.addAction(vehicleAction)
        fileMenu.addAction(exitAction)
        
    def vehicleCall(self):
        print('Vehicle')
        global tableWin
        tableWin = Table()
        tableWin.show()
        
    def exitCall(self):
        msgBox = QMessageBox.information(self, "Exit", "Do you want to Exit?", QMessageBox.Ok|QMessageBox.Cancel)
        if msgBox == QMessageBox.Ok:
          app.quit()
          
    def back_win(self):
        eliminateWin.close()
        mainWin.show()
        global x_1
        global combo_1
        global x_2
        global combo_2
        combo_1.clear()
        x_1=[]
        #combo_2.clear()
        x_2=[]
        visualizeWin.combo_2.clear()
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for item in tables:
          x_1.extend(item)
            #print(x)
        for option in x_1:
          combo_1.addItem(option)
        for item in tables:
          x_2.extend(item)
            #print(x)
        for option in x_2:
          visualizeWin.combo_2.addItem(option)
        cursor.close()
        conn.close()
        
        
    def update_plot_data(self):
        combo.clear()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for item in tables:
          x.extend(item)
        print(x)
        for option in x:
          combo.addItem(option)
        
    #def text_changed(self):
        #if self.lineEdit.text() != "" :
          #self.button1.setEnabled(True)
        #else :
         # self.button1.setEnabled(False)
          
    def erase(self):
        global combo
        global b
        b = combo.currentText()
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        results = cursor.fetchall()
        print('All existing tables:', results)
        results_list = [item[0] for item in results]
        if b in results_list:
          combo.clear()
          print(b, 'was found!')
          msgBox = QMessageBox.information(self, "", "Vehicle Eliminated", QMessageBox.Ok)
          cursor.execute("DROP TABLE IF EXISTS %s" %b)          
          cursor.close()
          conn.close()
          combo.clear()
          if msgBox == QMessageBox.Ok:
           combo.clear()
           x = []
           conn = mariadb.connect( 
            user="pablo", 
            password="pabloggg", 
            host="localhost", 
            port=3306, 
            database="EV_evaluation" )
           cursor = conn.cursor()
           cursor.execute("SHOW TABLES")
           tables = cursor.fetchall()
           for item in tables:
             x.extend(item)
           print(x)
           for option in x:
             combo.addItem(option)
           cursor.close()
           conn.close()
             #else:
          #print(b, 'was NOT found!')
          #msgBox = QMessageBox.warning(self, "", "Vehicle Does not Exist", QMessageBox.Ok)
        #self.lineEdit.clear()
        
class Evaluation(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(800,500)
        self.setWindowTitle("Electric Vehicles Evaluation System") 
        self.resize(800, 500) #Tamaño inicial de la ventana 800x500
        #Barra de estado
        self.statusBar().showMessage("Welcome")
                
        self.label_im = QLabel(self)
        self.pixmap = QPixmap('car.png')
        self.label_im.setPixmap(self.pixmap)
        self.label_im.resize(512,512)
        self.label_im.move(20,20) 
        
        self.button1 = QPushButton(self)
        self.button1.setText("Next")
        self.button1.move(600,300)
        self.button1.clicked.connect(self.tabla)
        self.button1.setEnabled(False)

        self.button2 = QPushButton(self)
        self.button2.setText("Back")
        self.button2.move(450,300)
        self.button2.clicked.connect(self.back_win)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 113, 25))
        self.lineEdit.move(530,260)
        self.lineEdit.textChanged.connect(self.text_changed)

        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 60, 47, 13))
        self.label.resize(70,15)
        self.label.move(450,260)
        self.label.setText("Vehicle :")

        # Create new action
        vehicleAction = QAction(QIcon(), '&Data Base', self)        
        vehicleAction.setStatusTip('Vehicle')
        vehicleAction.triggered.connect(self.vehicleCall)
        
        # Create exit action
        exitAction = QAction(QIcon(), '&Exit', self)        
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menu = self.menuBar()
        #Menú padre
        fileMenu = menu.addMenu("&File")
        #Menú padre
        fileTools = menu.addMenu("&Tools")
        
        fileTools.addAction(vehicleAction)
        fileMenu.addAction(exitAction)
        
    def vehicleCall(self):
        print('Vehicle')
        global tableWin
        tableWin = Table()
        tableWin.show()
        
    def exitCall(self):
        msgBox = QMessageBox.information(self, "Exit", "Do you want to Exit?", QMessageBox.Ok|QMessageBox.Cancel)
        if msgBox == QMessageBox.Ok:
          app.quit()
          
    def back_win(self):
        global x
        global combo
        global x_1
        global combo_1
        combo_1.clear()
        combo.clear()
        visualizeWin.combo_2.clear()
        x=[]
        x_1=[]
        x_2=[]
        evaluationWin.close()
        mainWin.show()
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for item in tables:
          x.extend(item)
            #print(x)
        for option in x:
          combo.addItem(option)
        for item in tables:
          x_1.extend(item)
            #print(x)
        for option in x_1:
          combo_1.addItem(option)
        for item in tables:
          x_2.extend(item)
            #print(x)
        for option in x_2:
          visualizeWin.combo_2.addItem(option)
        cursor.close()
        conn.close()
        
    def text_changed(self):
        if self.lineEdit.text() != "" :
          self.button1.setEnabled(True)
        else :
          self.button1.setEnabled(False)
          
    def tabla(self):
        import mariadb
        import warnings
        global c
        c = self.lineEdit.text()
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        results = cursor.fetchall()
        print('All existing tables:', results)
        results_list = [item[0] for item in results]
        if c in results_list:
          print(c, 'was found!')
          msgBox = QMessageBox.warning(self, "", "Existing Vehicle", QMessageBox.Ok)
          if msgBox == QMessageBox.Ok:
              self.lineEdit.clear()
        else:
          print(c, 'was NOT found!')
          cursor.execute("CREATE TABLE IF NOT EXISTS %s (time_ms int UNSIGNED, voltage_V float UNSIGNED, current_A float SIGNED, power_KW float SIGNED)" %c)
          self.lineEdit.clear()
          evaluationWin.close()
          evalmain.show()
        
class Export(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        global cursor
        global x_1
        global combo_1
        combo_1 = QComboBox(self)
        combo_1.move(530, 260)
        x_1 = []
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for item in tables:
          x_1.extend(item)
            #print(x)
        for option in x:
          combo_1.addItem(option)
        cursor.close()
        conn.close()

        self.setFixedSize(800,500)
        self.setWindowTitle("Electric Vehicles Evaluation System") 
        self.resize(800, 500) #Tamaño inicial de la ventana 800x500
        #Barra de estado
        self.statusBar().showMessage("Welcome")
        
        self.label_im = QLabel(self)
        self.pixmap = QPixmap('download.png')
        self.label_im.setPixmap(self.pixmap)
        self.label_im.resize(512,512)
        self.label_im.move(60,15)

        
        self.button1 = QPushButton(self)
        self.button1.setText("Export")
        self.button1.move(600,300)
        self.button1.clicked.connect(self.exp)
        #self.button1.setEnabled(False)

        self.button2 = QPushButton(self)
        self.button2.setText("Back")
        self.button2.move(450,300)
        self.button2.clicked.connect(self.back_win)

        #self.lineEdit = QtWidgets.QLineEdit(self)
        #self.lineEdit.setGeometry(QtCore.QRect(140, 60, 113, 20))
        #self.lineEdit.move(530,260)
        #self.lineEdit.textChanged.connect(self.text_changed)

        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 60, 47, 13))
        self.label.resize(70,15)
        self.label.move(450,260)
        self.label.setText("Vehicle :")

        # Create new action
        vehicleAction = QAction(QIcon(), '&Data Base', self)        
        vehicleAction.setStatusTip('Vehicle')
        vehicleAction.triggered.connect(self.vehicleCall)
        
        # Create exit action
        exitAction = QAction(QIcon(), '&Exit', self)        
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menu = self.menuBar()
        #Menú padre
        fileMenu = menu.addMenu("&File")
        #Menú padre
        fileTools = menu.addMenu("&Tools")
        
        fileTools.addAction(vehicleAction)
        fileMenu.addAction(exitAction)
        
    def vehicleCall(self):
        print('Vehicle')
        global tableWin
        tableWin = Table()
        tableWin.show()
        
    def exitCall(self):
        msgBox = QMessageBox.information(self, "Exit", "Do you want to Exit?", QMessageBox.Ok|QMessageBox.Cancel)
        if msgBox == QMessageBox.Ok:
          app.quit()
          
    def back_win(self):
        exportWin.close()
        mainWin.show()
        
    def text_changed(self):
        if self.lineEdit.text() != "" :
          self.button1.setEnabled(True)
        else :
          self.button1.setEnabled(False)
          
    def exp(self):
        global a
        global combo_1
        a = combo_1.currentText()
        #a = self.lineEdit.text()
        # connect the mysql with the python
        con=connect(user="pablo",password="pabloggg",host="localhost",database="EV_evaluation")
        # read the data
        df=sql.read_sql('select * from %s'%a,con)
        # print the data
        print(df)
        # export the data into the excel sheet
        df.to_excel(a+'.xls')
        #self.lineEdit.clear()

class Visualize(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Visualize, self).__init__(*args, **kwargs)
        global cursor
        global x_2
        global combo_2
        
        self.widget = QWidget()
        self.layout = QGridLayout()
        self.widget.setLayout(self.layout)
        self.setWindowTitle("Electric Vehicles Evaluation System")
        self.statusBar().showMessage("Welcome")
        
        self.showV = QLabel("", self)
        self.button1 = QPushButton('Visualize')
        self.button2 = QPushButton('Back')
        self.combo_2 = QComboBox(self)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget_2 = pg.PlotWidget()
        self.layout.addWidget(self.graphWidget, 0, 1, 3, 1)
        self.layout.addWidget(self.graphWidget_2, 5, 1, 3, 1)
        self.layout.addWidget(self.button1, 0, 0)
        self.layout.addWidget(self.button2, 1, 0)
        self.layout.addWidget(self.combo_2 , 5, 0)
        self.layout.addWidget(self.showV, 3, 1)
        self.setCentralWidget(self.widget)
        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('bottom', 'Time (ms)', **styles)
        self.graphWidget_2.setLabel('bottom', 'Time (ms)', **styles)
        self.graphWidget_2.setTitle("<span style=\"color:white;font-size:30pt\">Voltage</span>")
        self.graphWidget.setTitle("<span style=\"color:white;font-size:30pt\">Current</span>")
        self.graphWidget_2.setLabel('left', "<span style=\"color:white;font-size:20px\">Volts (V)</span>")
        self.graphWidget_2.setLabel('bottom', "<span style=\"color:white;font-size:20px\">miliseconds (*10,000)</span>")
        self.graphWidget.setLabel('left', "<span style=\"color:white;font-size:20px\">Amperes (A)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:white;font-size:20px\">miliseconds (*10,000)</span>")
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget_2.showGrid(x=True, y=True)
        
        #combo_2 = QComboBox(self)
        #combo_2.move(530, 260)
        x_2 = []
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for item in tables:
          x_2.extend(item)
            #print(x)
        for option in x_2:
          self.combo_2.addItem(option)
        cursor.close()
        conn.close()

        
        #self.button1 = QPushButton("Visualize")
        #self.button1.setText("Visualize")
        #self.button1.move(600,300)
        self.button1.clicked.connect(self.exp)
        #self.button1.setEnabled(False)

        #self.button2 = QPushButton("Back")
        #self.button2.setText("Back")
        #self.button2.move(450,300)
        self.button2.clicked.connect(self.back_win)

        #self.lineEdit = QtWidgets.QLineEdit(self)
        #self.lineEdit.setGeometry(QtCore.QRect(140, 60, 113, 20))
        #self.lineEdit.move(530,260)
        #self.lineEdit.textChanged.connect(self.text_changed)

        
        #self.label = QtWidgets.QLabel(self)
        #self.label.setGeometry(QtCore.QRect(100, 60, 47, 13))
        #self.label.resize(70,15)
        #self.label.move(450,260)
        #self.label.setText("Vehicle :")
        
        # Create new action
        vehicleAction = QAction(QIcon(), '&Data Base', self)        
        vehicleAction.setStatusTip('Vehicle')
        vehicleAction.triggered.connect(self.vehicleCall)
        
        # Create exit action
        exitAction = QAction(QIcon(), '&Exit', self)        
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menu = self.menuBar()
        #Menú padre
        fileMenu = menu.addMenu("&File")
        #Menú padre
        fileTools = menu.addMenu("&Tools")
        
        fileTools.addAction(vehicleAction)
        fileMenu.addAction(exitAction)
        
    def vehicleCall(self):
        print('Vehicle')
        global tableWin
        tableWin = Table()
        tableWin.show()
        
    def exitCall(self):
        msgBox = QMessageBox.information(self, "Exit", "Do you want to Exit?", QMessageBox.Ok|QMessageBox.Cancel)
        if msgBox == QMessageBox.Ok:
          app.quit()
          
    def back_win(self):
        visualizeWin.close()
        mainWin.show()
        self.graphWidget.clear()
        self.graphWidget_2.clear()
                  
    def exp(self):
        global combo_2
        global a
        global v, c, p, t, t_1
        v=[]
        c=[]
        p=[]
        t=0
        t_1=[]
        a = self.combo_2.currentText()
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM "+a)
        record = cursor.fetchall()
        for row in record:
            t=t+100
            t_1.append(t)
            v.append(row[1])
            c.append(row[2])
            p.append(row[3])
        #print(v)
        #print(c)
        print(t_1)
        cursor.close()
        conn.close()
        self.graphWidget.clear()
        self.graphWidget_2.clear()
        self.graphWidget.plot(t_1, c)
        self.graphWidget_2.plot(t_1, v)
              
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
    
class Table(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vehicles Registration") 
        self.table = QtWidgets.QTableView()
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()

        ## getting all the tables which are present in 'datacamp' database
        cursor.execute("SHOW TABLES")

        tables = cursor.fetchall() ## it returns list of tables present in the database
        print(tables)
        for i in tables:
          print(i)

        self.model = TableModel(tables)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        
class EvalMain(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(EvalMain, self).__init__(*args, **kwargs)
        self.widget = QWidget()
        self.layout = QGridLayout()
        self.widget.setLayout(self.layout)
        self.setWindowTitle("Electric Vehicles Evaluation System")
        self.statusBar().showMessage("Welcome")
        
        self.showV = QLabel("", self)
        #self.showV.setEnabled(False)
        
        self.startBtn=QPushButton('Start')
        self.endBtn=QPushButton('Stop')
        self.endBtn.setEnabled(False)
        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.graphWidget = pg.PlotWidget()
        self.layout.addWidget(self.graphWidget, 0, 1, 3, 1)
        self.layout.addWidget(self.startBtn, 0, 0)
        self.layout.addWidget(self.endBtn, 1, 0)
        self.layout.addWidget(self.showV, 3, 1)
        self.setCentralWidget(self.widget)
        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('bottom', 'Time (ms)', **styles)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,0) for _ in range(100)]  # 100 data points
        self.a = [randint(0,0) for _ in range(100)]
        self.p = [randint(0,0) for _ in range(100)]

        #self.graphWidget.setBackground('w')
        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x=True, y=True)

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen='b', name='Voltage')
        self.data_line_a =  self.graphWidget.plot(self.x, self.a, pen='r', name='Current')
        self.data_line_p =  self.graphWidget.plot(self.x, self.a, pen='g', name='Power')
        self.timer = QtCore.QTimer()
        #self.timer.setInterval(100)
        #self.timer.timeout.connect(self.update_plot_data)
        #self.timer.start()
    def endTimer(self):
        global segu
        segu = 0
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)
        self.data_line.clear()
        self.data_line_a.clear()
        self.data_line_p.clear()
        msgBox = QMessageBox.information(self, "", "Data has been save", QMessageBox.Ok)
        if msgBox == QMessageBox.Ok:
          evalmain.close()
          evaluationWin.show()
          self.x=[]
        
    def startTimer(self):
        self.timer.start(100)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)
        self.timer.timeout.connect(self.update_plot_data)
        self.statusBar().showMessage("Evaluation in Process")
        global segu
        segu = 0
        global cursor
        global conn
        conn = mariadb.connect( 
         user="pablo", 
         password="pabloggg", 
         host="localhost", 
         port=3306, 
         database="EV_evaluation" )
        cursor = conn.cursor()
        self.x = list(range(100))
        

    def update_plot_data(self):
        #ads = ADS.ADS1115(i2c)
        ads = ADS.ADS1115(i2c, gain=1, data_rate=860)
        chan = AnalogIn(ads, ADS.P0)
        chan1 = AnalogIn(ads, ADS.P1)
        v = ((chan.voltage)*100)-1.2
        amp = ((chan1.voltage)-0.0095)*250
        pot = (v*amp)/1000
        global segu
        segu = segu+100
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 10)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first 
        self.y.append(v)  # Add a new random value.
        self.a = self.a[1:]  # Remove the first 
        self.a.append(amp)  # Add a new random value.
        self.p = self.p[1:]  # Remove the first 
        self.p.append(pot)  # Add a new random value.


        self.data_line.setData(self.x, self.y)  # Update the data.
        self.data_line_a.setData(self.x, self.a)  # Update the data.
        self.data_line_p.setData(self.x, self.p)  # Update the data.
        volt = str(round(v, 4))
        current = str(round(amp, 4))
        potencia = str(round(pot, 4))
        print(segu)
        self.showV.setText("Voltage: "+volt+"V       "+"Current: "+current+"A       "+"Power: "+potencia+"kW")
        global c
        global cursor
        global conn
        cursor.execute(
        "INSERT INTO %s (time_ms,voltage_V,current_A, power_KW) VALUES (?, ?, ?, ?)"%c, 
        (segu, v, amp, pot))
        conn.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    visualizeWin = Visualize()
    eliminateWin = Eliminate()
    evaluationWin = Evaluation()
    exportWin = Export()
    evalmain = EvalMain()
    sys.exit( app.exec_() )