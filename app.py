from flask import Flask, request, render_template, send_from_directory, url_for
import json
from functions import *
import os
from pathlib import Path

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    hashtags = get_hashtags()
    return render_template("index.html", hashtags=hashtags)



@app.route("/tag/")
def page_tag():
    search = request.args.get("tag")
    matched_posts = get_posts(search)

    return render_template("post_by_tag.html", posts=matched_posts, category=search)




@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == "GET":
        return render_template("post_form.html")
    if request.method == "POST":
        content = request.form.get("content")
        picture = request.files.get('picture')
        path = os.path.join(UPLOAD_FOLDER, f'{picture.filename}')
        post = {"pic": url_for("static_dir", path=picture.filename),
                "content": content}
        picture.save(path)
        add_post(path, content)
        return render_template("post_uploaded.html", content=content, path=path)



@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

