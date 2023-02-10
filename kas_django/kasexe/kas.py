from PyQt5 import QtWidgets , QtGui
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow , self).__init__()
        
        #show web view
        self.browser = QWebEngineView()
        
        #set url 
        self.browser.setUrl(QUrl('http://127.0.0.1:8000'))
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        
        #Main screen
        self.setCentralWidget(self.browser)
        
        #Full screen
        self.showMaximized()
        
        #navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        self.dict_btn ={
            'Back':self.browser.back,
            'Next':self.browser.forward,
            'Reload':self.browser.reload,
            'Home':self.navigate_home
        }
        
        def create_btn(name_btn: str):
            btn = QAction(name_btn,self)
            btn.triggered.connect(self.dict_btn[name_btn])
            navbar.addAction(btn)
        
        create_btn('Back')
        create_btn('Next')
        create_btn('Reload')
        create_btn('Home')
        
        self.url_bar=QLineEdit()
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.browser.urlChanged.connect(self.update_url)
    
    def navigate_home(self):
            self.browser.setUrl(QUrl('http://127.0.0.1:8000'))
            
        
        
        #Search bằng Url 
        
        
    def navigate_to_url(self):
        url='http://' + self.url_bar.text() 
        self.browser.setUrl(QUrl(url))
            
    def update_url(self,q):
        q = q.toString().replace('http://','')
        self.url_bar.setText(q)
            
        
app = QApplication(sys.argv)
QApplication.setApplicationName('Kas')

window = MainWindow()
app.exec_()        