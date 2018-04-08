#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import pandas as pd
from flask import Flask, request, render_template
import CQNZ1
import RQSN1
import RQCN1
# from pyfladesk import init_gui
# import webbrowser

app = Flask(__name__)

@app.route('/')
@app.route('/<page>', methods=['GET', 'POST'])
def home(page='index'):
    func = []
    arr_RD = []
    arr_XD = []
    if request.method == 'POST':
        ANS = request.form.to_dict(flat=True)
        func = getattr(globals()[page], page)(ANS)
        savefile = open("./history/"+ datetime.datetime.now().isoformat() + "-" + page + ".txt", "w")
        savefile.write('----------------------------------------------------\n')
        savefile.write(datetime.datetime.now().strftime("%d.%m.%y") + ' ' + datetime.datetime.now().strftime("%H:%M") + '\n' + 'Результаты расчета подпрограммы ' + page + ':\n')
        savefile.write('----------------------------------------------------\n')
        for key in func: savefile.write(key + ' = ' + str(func[key]) + '\n')
        savefile.write('----------------------------------------------------\n')
        savefile.write('Входные параметры:\n')
        savefile.write('----------------------------------------------------\n')
        for key in ANS:
            if str(key)[:2] == 'RD':
                arr_RD.append(ANS[key])
            elif str(key)[:2] == 'XD':
                arr_XD.append(ANS[key])
            else:
                savefile.write(key + ' = ' + str(ANS[key]) + '\n')
        if len(arr_RD) != 0: savefile.write('\n' + str(pd.DataFrame({'RD': arr_RD, 'XD': arr_XD})) + '\n')
        savefile.write('----------------------------------------------------\n')
        savefile.close()
    return render_template(page + '.html', title=page, A=func)

if __name__ == '__main__':
    app.run(debug=True)
    # init_gui(app, width=1150, height=620)
    # webbrowser.open("http://localhost:5000")
