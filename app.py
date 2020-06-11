from flask import Flask,render_template
from pathlib import Path
import time

app=Flask(__name__)

@app.route("/")
def homePage():
    # print("###/")
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/articles_list")
def article_list():

    article_list=[str(x) for x in  (Path('./data').glob("**/*.txt"))]
    article_time=[ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Path(x).stat().st_ctime)) for x in article_list]
    article_dict=zip(article_list,article_time)
    
    article_dict=sorted(article_dict,key=lambda x: x[1],reverse=True)
    return render_template("articles_list.html",article_dict=article_dict)


@app.route("/data/<url_path>")
def article_display(url_path):
    article_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Path(r"data/{}".format(url_path)).stat().st_ctime))

    with open(r"data/{}".format(url_path),"r",encoding="utf-8")as f:
        data=f.readlines()
    return render_template("articles.html",article=data,the_time=article_time)


if __name__ == "__main__":
    app.run(debug=True)