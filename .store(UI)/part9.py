if __name__ == '__main__':
    w1 = window_about()  # about
    w2 = window_update()  # update
    action1.triggered.connect(w1.activate)
    action2.triggered.connect(w2.activate)
    action3.triggered.connect(w1.startcherry)
    app.setStyleSheet(style_sheet_ori)
    app.exec()
