#oding:utf-8
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import random
import os

app = Flask(__name__)

@app.route('/')
def logick():
    def GetRandom():
        random = np.random.choice(["Rank5 servant","Rank4 servant","Rank3 servant",
                                   "Rank5 reisou","Rank4 reisou","Rank3 reisou"],
                                p=[0.01, 0.03, 0.04, 0.12, 0.4, 0.4])
        return random

    sh1 = False
    sh2 = False
    count = 0
    imgs_path = []

    while sh1 == False or sh2 == False:
        sh1 = False
        sh2 = False
        haisyutu = []
        count += 1

        for i in range(10):
            haisyutu.append(GetRandom())

        for t in haisyutu:
            if "servant" in t:
                sh1 = True
                break

        for t in haisyutu:
            if "Rank4" in t or "Rank5" in t:
                sh2 = True
                break

    for s in haisyutu:
        if "Rank5 servant" in s:
            nameselect5s = random.choice(os.listdir("static/img/5servant"))
#            print(nameselect5s)
            imgs_path.append("static/img/5servant/" + nameselect5s)

        elif "Rank4 servant" in s:
            nameselect4s = random.choice(os.listdir("static/img/4servant"))
#            print(nameselect4s)
            imgs_path.append("static/img/4servant/" + nameselect4s)

        elif "Rank3 servant" in s:
            nameselect3s = random.choice(os.listdir("static/img/3servant"))
#            print(nameselect3s)
            imgs_path.append("static/img/3servant/" + nameselect3s)

        elif "Rank5 reisou" in s:
            nameselect5r = random.choice(os.listdir("static/img/5reisou"))
#            print(nameselect5r)
            imgs_path.append("static/img/5reisou/" + nameselect5r)

        elif "Rank4 reisou" in s:
            nameselect4r = random.choice(os.listdir("static/img/4reisou"))
#            print(nameselect4r)
            imgs_path.append("static/img/4reisou/" + nameselect4r)

        elif "Rank3 reisou" in s:
            nameselect3r = random.choice(os.listdir("static/img/3reisou"))
#            print(nameselect3r)
            imgs_path.append("static/img/3reisou/" + nameselect3r)

    return render_template("fgo.html", imgurl=imgs_path)

if __name__ == "__main__":
    app.run(debug=True)

