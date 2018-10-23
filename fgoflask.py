#oding:utf-8
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import random
import os
import glob

app = Flask(__name__)

@app.route('/')
def logick():
    def GetRandom():
        random = np.random.choice(["Rank5 servant","Rank4 servant","Rank3 servant",
                                   "Rank5 reisou","Rank4 reisou","Rank3 reisou"],
                                p=[0.01, 0.03, 0.04, 0.12, 0.4, 0.4])
        return random

    Check1 = False
    Check2 = False
    Check3 = False
    count = 0
    imgs_path = []
    first_imgs_path = []
    second_imgs_path = []

    while Check1 == False or Check2 == False:
        Check1 = False
        Check2 = False
        haisyutu = []

        for i in range(10):
            haisyutu.append(GetRandom())

        for t in haisyutu:
            if "servant" in t:
                Check1 = True
                break

        for t in haisyutu:
            if "Rank4" in t or "Rank5" in t:
                Check2 = True
                break

    for s in haisyutu:
        if "Rank5 servant" in s:
            nameselect5s = random.choice(os.listdir("static/img/5servant"))
            imgs_path.append("static/img/5servant/" + nameselect5s)

        elif "Rank4 servant" in s:
            nameselect4s = random.choice(os.listdir("static/img/4servant"))
            imgs_path.append("static/img/4servant/" + nameselect4s)

        elif "Rank3 servant" in s:
            nameselect3s = random.choice(os.listdir("static/img/3servant"))
            imgs_path.append("static/img/3servant/" + nameselect3s)

        elif "Rank5 reisou" in s:
            nameselect5r = random.choice(os.listdir("static/img/5reisou"))
            imgs_path.append("static/img/5reisou/" + nameselect5r)

        elif "Rank4 reisou" in s:
            nameselect4r = random.choice(os.listdir("static/img/4reisou"))
            imgs_path.append("static/img/4reisou/" + nameselect4r)

        elif "Rank3 reisou" in s:
            nameselect3r = random.choice(os.listdir("static/img/3reisou"))
            imgs_path.append("static/img/3reisou/" + nameselect3r)

    for select in imgs_path:
        count += 1

        if count <= 5:
            first_imgs_path.append(select)

        if count >= 6:
            second_imgs_path.append(select)

    return render_template("fgo.html", fimgurl=first_imgs_path, simgurl=second_imgs_path)

if __name__ == "__main__":
    app.run(debug=True)

