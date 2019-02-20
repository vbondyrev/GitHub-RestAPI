#!/usr/bin/python3

import requests
from flask import Flask, render_template, request, jsonify, url_for, redirect  # Response
from pymongo import MongoClient

app = Flask(__name__)

# Official limit - the GitHub Search API provides up to 1,000 results for each search.
# https://developer.github.com/v3/search/#about-the-search-api

# URL`s and headers with token
url_query_sorted_p1 = 'https://api.github.com/search/repositories?q=+language:python+stars:>2000&sort=stars&page=1&per_page=100'
url_query_top10 = 'https://api.github.com/search/repositories?q=+language:python+stars:>=20000&sort=stars&order=desc&page=1&per_page=10'
url_users = 'https://api.github.com/users/'

headers = {'authToken': '922de9f974e83725bd3b41b6c78460159f21c426'}

# init connection to MongoDB
uri_prod = "mongodb://localhost:27017/git_db"
try:
    conn = MongoClient("mongodb://mongo:27017/", connect=False)
    # conn = MongoClient("mongodb://localhost:27017/git_db", connect=False) # DEVENV
    db = conn["git_db"]
    coll = db["git_col"]
except ConnectionError as e:
    print(jsonify({'Error message:': e}))


@app.route("/db/get")
def mongo_get():
    """ Get data from Mongo DB
    """
    cursor = coll.find({}, {'_id': 0})
    data = []
    for ids in cursor:
        data.append(ids)
    return render_template("get.html", repos=data)


@app.route("/db/save")
def mongo_save():
    """ Save result of requests to collection Mongo DB
    """
    coll.drop()

    # start = time()
    res = requests.get(url_query_sorted_p1, headers=headers)
    repos = res.json()
    repos_list = repos['items']

    # pagination - fetch 1000 repositories with 100 per requests with authToken.( By default 30)
    while 'next' in res.links.keys():
        res = requests.get(res.links['next']['url'], headers=headers)
        repos = res.json()
        # res_list_new = repos_new['items']
        repos_list.extend(repos['items'])

    output = []
    for item in repos_list:
        new_data = {}
        new_data['id'] = item['id']
        new_data['full_name'] = item['full_name']
        new_data['url'] = item['url']
        new_data['description'] = item['description']
        new_data['stargazers_count'] = item['stargazers_count']
        new_data['language'] = item['language']
        # coll.insert_one(new_data) #(this way - 35sec)
        output.append(new_data)

    coll.insert_many(output)  # (this way - 7sec)
    # print(' Saving took: {:.2f} seconds'.format(time() - start), sep='\n')

    return render_template("get.html", repos=repos_list)


@app.route("/user/<string:user_name>")
def user_detail(user_name):
    """ Get info about user and detail info about his repo.
    """
    response_user = requests.get(url_users + user_name, headers=headers)
    response_repos = requests.get(url_users + user_name + "/repos", headers=headers)

    user_info = response_user.json()
    repos = response_repos.json()

    if "message" in user_info:
        return render_template("user.html", error="User not found, please, try again")
    else:
        return render_template("user.html", profile=user_info, repos=repos)


@app.route("/db/delete")
def mongo_del():
    """ Delete collection from Mongo DB
    """
    coll.drop()
    message = {
        'status': '200',
        'message': 'All rows from MongoDB - deleted'}
    return render_template("del.html", repos=jsonify(message))


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """ By default -  "GET" info about TOP 10 stars repo.
        POST -  get info about user
    """
    if request.method == "POST":
        github_username = request.form.get("github_username")
        return redirect(url_for('.user_detail', user_name=github_username))

    else:
        response = requests.get(url_query_top10, headers=headers)
        resp_dict = response.json()
        resp_list = resp_dict['items']
        return render_template("index.html", repos=resp_list)


if __name__ == '__main__':
    app.run(debug=False, threaded=False, host='0.0.0.0', port=5000)
