class MyWidget(QWidget):  # 主窗口
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.center()
        self.show()
        self.setFocus()
        self.setWindowTitle('Volume Manager')
        self.setFixedSize(500, 320)

        self.widget1 = QComboBox(self)
        self.widget1.setFixedWidth(300)
        self.defalist = ['Choose your target device']
        dev = sd.query_devices()
        dev = str(dev)
        devlist = dev.split('\n')
        for i in range(len(devlist)):
            devlist[i] = devlist[i].split(',')[0]
            devlist[i] = devlist[i].replace('>', '')
            devlist[i] = devlist[i].replace('<', '')
            devlist[i] = devlist[i].lstrip(' ')
        devstr = '\n'.join(devlist)
        devstr = '\n' + devstr
        devstr = re.sub(r"(\n\d* )", '\n', devstr)
        devstr = devstr.lstrip('\n').rstrip('\n')
        devlist = devstr.split('\n')
        self.defalist = self.defalist + devlist
        self.widget1.addItems(self.defalist)
        self.widget1.setCurrentIndex(0)

        lbl0 = QLabel('Choose an acoustic pressure range:', self)

        self.le1 = QLineEdit(self)
        self.le1.setFixedWidth(120)
        self.le1.setText('0.0000063')
        #self.le1.setValidator(QIntValidator())

        lbl1 = QLabel(' ~ ', self)

        self.le2 = QLineEdit(self)
        self.le2.setFixedWidth(120)
        self.le2.setText('0.00003')
        #self.le2.setValidator(QIntValidator())

        self.pbar = QProgressBar(self)
        self.pbar.setFixedWidth(230)
        self.pbar.setValue(0)

        lbl2 = QLabel('value', self)

        self.pbar2 = QProgressBar(self)
        self.pbar2.setFixedWidth(230)
        self.pbar2.setMinimum(-100)
        self.pbar2.setMaximum(0)
        self.pbar2.setValue(-100)

        lbl3 = QLabel('dB    ', self)

        self.mybutton1 = QPushButton('Start', self)
        self.mybutton1.setFixedWidth(150)
        self.mybutton1.clicked.connect(self.turnonlisten)

        self.mybutton2 = QPushButton('Stop', self)
        self.mybutton2.setFixedWidth(150)
        self.mybutton2.clicked.connect(self.stoplisten)

        qw = QWidget()
        vbox = QHBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addStretch()
        vbox.addWidget(self.widget1)
        vbox.addStretch()
        qw.setLayout(vbox)

        qw2 = QWidget()
        vbox2 = QHBoxLayout()
        vbox2.setContentsMargins(0, 0, 0, 0)
        vbox2.addStretch()
        vbox2.addWidget(lbl0)
        vbox2.addStretch()
        qw2.setLayout(vbox2)

        qw3 = QWidget()
        vbox3 = QHBoxLayout()
        vbox3.setContentsMargins(0, 0, 0, 0)
        vbox3.addStretch()
        vbox3.addWidget(self.le1)
        vbox3.addWidget(lbl1)
        vbox3.addWidget(self.le2)
        vbox3.addStretch()
        qw3.setLayout(vbox3)

        qw4 = QWidget()
        vbox4 = QHBoxLayout()
        vbox4.setContentsMargins(0, 0, 0, 0)
        vbox4.addStretch()
        vbox4.addWidget(self.pbar)
        vbox4.addWidget(lbl2)
        vbox4.addStretch()
        qw4.setLayout(vbox4)

        qw5 = QWidget()
        vbox5 = QHBoxLayout()
        vbox5.setContentsMargins(0, 0, 0, 0)
        vbox5.addStretch()
        vbox5.addWidget(self.pbar2)
        vbox5.addWidget(lbl3)
        vbox5.addStretch()
        qw5.setLayout(vbox5)

        qw6 = QWidget()
        vbox6 = QHBoxLayout()
        vbox6.setContentsMargins(0, 0, 0, 0)
        vbox6.addStretch()
        vbox6.addWidget(self.mybutton1)
        vbox6.addWidget(self.mybutton2)
        vbox6.addStretch()
        qw6.setLayout(vbox6)

        vbox6 = QVBoxLayout()
        vbox6.setContentsMargins(0, 0, 0, 0)
        vbox6.addStretch()
        vbox6.addWidget(qw)
        vbox6.addWidget(qw2)
        vbox6.addWidget(qw3)
        vbox6.addStretch()
        vbox6.addWidget(qw4)
        vbox6.addWidget(qw5)
        vbox6.addStretch()
        vbox6.addWidget(qw6)
        vbox6.addStretch()
        self.setLayout(vbox6)

        windows = subprocess.check_output(
            ['osascript', '-e', 'tell application "Terminal" to get the id of every window']).decode('utf-8').strip()
        for window in windows:
            os.system(f"""osascript -e 'tell application "Terminal" to set miniaturized of window {window} to true'""")

    def volume_to_db(self, volume):  # 定义转换函数
        return 20 * np.log10(volume)

    def turnonlisten(self):
        if self.widget1.currentIndex() != 0 and self.le1.text() != '' and self.le2.text() != '' and float(self.le1.text()) < float(self.le2.text()):
            self.mybutton1.setStyleSheet('''
                                border: 1px outset grey;
                                background-color: #0085FF;
                                border-radius: 4px;
                                padding: 1px;
                                color: #FFFFFF''')
            self.mybutton1.setText('Started')
            self.open = True
            self.corepart()

    def corepart(self):
        if self.open == True:
            # 定义参数
            CHUNK = 1024
            #RATE = 44100

            cmd = f'''AdjustVolume -s 0.01 -n "BlackHole 2ch"'''
            os.system(cmd)
            cmd = f'''AdjustVolume -s 0.01 -n "{self.widget1.currentText()}"'''
            os.system(cmd)
            x = 0.1
            uptime = 0
            downtime = 0

            # 打开音频输入设备
            self.stream = sd.InputStream(channels=1)

            try:
                # 开始流
                self.stream.start()

                while self.open == True:
                    # 读取音频数据
                    data = self.stream.read(CHUNK)

                    # 检查数据类型，并进行转换
                    if isinstance(data, tuple):
                        data = data[0]
                    elif isinstance(data, list):
                        data = np.array(data)

                    # 计算音量（RMS：均方根）
                    volume = np.sqrt(np.mean(data ** 2))
                    #print(volume)

                    # 计算声压
                    pressure = volume * np.sqrt(2) / 20
                    #print('声压', pressure)

                    if pressure > float(self.le2.text()):
                        #print('声音大了')
                        uptime = 0
                        downtime += 1
                        if downtime <= 15:
                            x = x - 0.01
                            if x > 0:
                                cmd = f'''AdjustVolume -s {x} -n "BlackHole 2ch"'''
                                os.system(cmd)
                                cmd = f'''AdjustVolume -s {x} -n "{self.widget1.currentText()}"'''
                                os.system(cmd)
                                #print('执行')
                            if x <= 0:
                                x = 0.01
                                cmd = f'''AdjustVolume -s {x} -n "BlackHole 2ch"'''
                                os.system(cmd)
                                cmd = f'''AdjustVolume -s {x} -n "{self.widget1.currentText()}"'''
                                os.system(cmd)
                                #print('执行')
                        if downtime >= 20 and downtime <= 30:
                            x = x - 0.01
                            if x > 0:
                                cmd = f'''AdjustVolume -s {x} -n "BlackHole 2ch"'''
                                os.system(cmd)
                                cmd = f'''AdjustVolume -s {x} -n "{self.widget1.currentText()}"'''
                                os.system(cmd)
                                #print('执行')
                            if x <= 0:
                                x = 0.01
                                cmd = f'''AdjustVolume -s {x} -n "BlackHole 2ch"'''
                                os.system(cmd)
                                cmd = f'''AdjustVolume -s {x} -n "{self.widget1.currentText()}"'''
                                os.system(cmd)
                                #print('执行')
                    if pressure < float(self.le1.text()) and pressure > 0:
                        #print('声音小了')
                        downtime = 0
                        uptime += 1
                        if uptime <= 15:
                            x = x + 0.01
                            if x < 1:
                                cmd = f'''AdjustVolume -s {x} -n "BlackHole 2ch"'''
                                os.system(cmd)
                                cmd = f'''AdjustVolume -s {x} -n "{self.widget1.currentText()}"'''
                                os.system(cmd)
                                #print('执行')
                            if x >= 1:
                                x = 1
                                cmd = f'''AdjustVolume -s {x} -n "BlackHole 2ch"'''
                                os.system(cmd)
                                cmd = f'''AdjustVolume -s {x} -n "{self.widget1.currentText()}"'''
                                os.system(cmd)
                                #print('执行')
                        if uptime >= 20 and uptime <= 30:
                            x = x + 0.01
                            if x < 1:
                                cmd = f'''AdjustVolume -s {x} -n "BlackHole 2ch"'''
                                os.system(cmd)
                                cmd = f'''AdjustVolume -s {x} -n "{self.widget1.currentText()}"'''
                                os.system(cmd)
                                #print('执行')
                            if x >= 1:
                                x = 1
                                cmd = f'''AdjustVolume -s {x} -n "BlackHole 2ch"'''
                                os.system(cmd)
                                cmd = f'''AdjustVolume -s {x} -n "{self.widget1.currentText()}"'''
                                os.system(cmd)
                                #print('执行')

                    self.pbar.setValue(int(x * 100))

                    if volume > 0:
                        db = int(self.volume_to_db(volume))
                        if -100 <= db <= 0:
                            self.pbar2.setValue(int(db))
                    QApplication.processEvents()

                # 关闭流
                self.stream.stop()
            except Exception as e:
                print("下载失败了", e)

    def stoplisten(self):
        if self.mybutton1.text() == 'Started':
            self.stream.stop()
        self.open = False
        self.pbar.setValue(0)
        self.pbar2.setValue(-100)

        self.mybutton1.setStyleSheet('''
                border: 1px outset grey;
                background-color: #FFFFFF;
                border-radius: 4px;
                padding: 1px;
                color: #000000''')
        self.mybutton1.setText('Start')

        cmd = f'''AdjustVolume -s 0.01 -n "{self.widget1.currentText()}"'''
        os.system(cmd)
        cmd = f'''AdjustVolume -s 0.01 -n "BlackHole 2ch"'''
        os.system(cmd)

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

style_sheet_ori = '''
    QTabWidget::pane {
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 9px;
}
    QPushButton{
        border: 1px outset grey;
        background-color: #FFFFFF;
        border-radius: 4px;
        padding: 1px;
        color: #000000
}
    QPushButton:pressed{
        border: 1px outset grey;
        background-color: #0085FF;
        border-radius: 4px;
        padding: 1px;
        color: #FFFFFF
}
    QPlainTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QPlainTextEdit#edit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #FFFFFF;
        color: rgb(113, 113, 113);
        font: 14pt Helvetica;
}
    QLineEdit{
        border-radius:4px;
        border: 1px outset lightgray;
        background-color: #FFFFFF;
}
    QTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QLCDNumber{
        border: 1px transparent;  
        border-radius:4px;
        padding: 1px 5px 1px 3px;
}
'''