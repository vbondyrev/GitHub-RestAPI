#!/usr/bin/python3
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# URL`s
# headers with token  - save in .ini
url_query_sorted = 'https://api.github.com/search/repositories?q=+language:python+stars:>=500&sort=stars&order=desc'
url_users = 'https://api.github.com/users/'
headers = {'authToken': 'da04e59533d87da7905cee38c1539646413b072d'}


# !!!! Temporary connection troubles with mlab mongodb service, previously work well
# init connection to MongoDB
# app.config.from_object('config')

def get_user_git(user):
    """ Get info for one person
    """
    response_user = requests.get(url_users + user, headers=headers)
    response_repos = requests.get(url_users + user + "/repos")

    user_info = response_user.json()
    repos = response_repos.json()

    if "message" in user_info:
        return render_template("index.html", error="User not found, please, try again")
    else:
        return render_template("index.html", profile=user_info, repos=repos)


# !!!! Temporary connection troubles with mlab mongodb service, previously work well
# @app.route("/json")
# def my_mongodata(n):
#     """ Json data from Mongo DB
#     """
#     # get data from mongo DB
#     # Error Object of type ObjectId is not JSON serializable:  ids.pop('_id') OR find({}, {'_id': 0})
#     cursor = db.git_col.find({}, {'_id': 0}).limit(n)
#     data = []
#     for ids in cursor:
#         data.append(ids)
#     return render_template("top.html", repos=jsonify(data))


@app.route("/top")
def get_top500():
    response = requests.get(url_query_sorted, headers=headers).json()

    output = []
    for item in response['items']:
        new_data = {}
        new_data['id'] = item['id']
        new_data['full_name'] = item['full_name']
        new_data['url'] = item['url']
        new_data['description'] = item['description']
        new_data['stargazers_count'] = item['stargazers_count']
        new_data['language'] = item['language']
        # OR collection.insert_one(todo_data)
        output.append(new_data)

    # !!!! Temporary connection troubles with mlab mongodb service, previously work well
    # coll.drop()
    # coll.insert_many(output)

    repos = response['items']
    return render_template("top.html", repos=repos)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """ By default -  'GET' info about USER Repos
    """
    if request.method == "POST":
        github_username = request.form.get("github_username")
        return get_user_git(github_username)

    # Default: IF methods=["GET"] - BY DEFAULT FIRST RANKED ACCOUNT
    else:
        response = requests.get(url_query_sorted, headers=headers).json()
        login = response['items'][0]['owner']['login']
        return get_user_git(login)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
