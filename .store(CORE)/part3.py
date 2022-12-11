if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w3 = MyWidget()
    app.setStyleSheet(style_sheet_ori)
    app.exec()
