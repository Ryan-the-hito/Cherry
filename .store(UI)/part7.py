
class CustomDialog_warn(QDialog):  # 提醒权限
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setUpMainWindow()
        self.center()
        self.resize(500, 490)
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

    def setUpMainWindow(self):
        l0 = QLabel('Please grant Cheer with Accessibility and Full Disk Access\n\n'
                    'in System Preferences, then open Settings and set your paths!', self)
        font = PyQt6.QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(15)
        l0.setFont(font)

        l1 = QLabel(self)
        #png = PyQt6.QtGui.QPixmap('setpath.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        #l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setMaximumSize(425, 250)
        l1.setScaledContents(True)

        btn_can = QPushButton('Got it!', self)
        btn_can.clicked.connect(self.cancel)
        btn_can.setFixedWidth(150)
        btn_can.setStyleSheet('''
                    border: 1px outset grey;
                    background-color: #FFFFFF;
                    border-radius: 4px;
                    padding: 1px;
                    color: #000000
                ''')

        w0 = QWidget()
        blay0 = QHBoxLayout()
        blay0.setContentsMargins(0, 0, 0, 0)
        blay0.addStretch()
        blay0.addWidget(l0)
        blay0.addStretch()
        w0.setLayout(blay0)

        w1 = QWidget()
        blay1 = QHBoxLayout()
        blay1.setContentsMargins(0, 0, 0, 0)
        blay1.addStretch()
        blay1.addWidget(l1)
        blay1.addStretch()
        w1.setLayout(blay1)

        w2 = QWidget()
        blay2 = QHBoxLayout()
        blay2.setContentsMargins(0, 0, 0, 0)
        blay2.addStretch()
        blay2.addWidget(btn_can)
        blay2.addStretch()
        w2.setLayout(blay2)

        w3 = QWidget()
        blay3 = QVBoxLayout()
        blay3.setContentsMargins(0, 0, 0, 0)
        blay3.addStretch()
        blay3.addWidget(w0)
        blay3.addStretch()
        blay3.addWidget(w1)
        blay3.addStretch()
        blay3.addWidget(w2)
        blay3.addStretch()
        w3.setLayout(blay3)
        w3.setStyleSheet('''
            border: 1px solid #ECECEC;
            background: #ECECEC;
            border-radius: 9px;
        ''')

        op = QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        w3.setGraphicsEffect(op)
        w3.setAutoFillBackground(True)

        blayend = QHBoxLayout()
        blayend.setContentsMargins(0, 0, 0, 0)
        blayend.addWidget(w3)
        self.setLayout(blayend)

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def cancel(self):  # 设置取消键的功能
        self.close()