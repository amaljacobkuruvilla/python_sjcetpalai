from flask import Flask

app=Flask(__name__)


@app.route("/")
def index():
    return "welcome to sjcet"


@app.route("/home")
def home():
    return "nice to meet you "

@app.route("/contact")
def contact():
    return "ebin,harish,thala,ashik,immanuel,amal,delight,joshua,charles"


@app.route("/about")
def about():
    return "ebin-programer*/harish-brocoder*/thala-thala hero ahda hero*/ashik-petta*/immanuel-kunjava pavamada*/delight-keedam*/joshua-thug*/charles-kumman"



if(__name__=="__main__"):
    app.run()
