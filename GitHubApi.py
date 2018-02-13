#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/13 14:58
# @Author  : Kaiwen Xue
# @File    : GitHubApi.py
# @Software: PyCharm
import json
import urllib.request, urllib.parse, urllib.error


def get_information(user):
    repo_url = 'https://api.github.com/users/' + user + '/repos'
    repo_uh = urllib.request.urlopen(repo_url)
    repo_data = repo_uh.read().decode()
    js1 = json.loads(repo_data)
    max_repo = len(js1) - 1
    repos = list()

    for i in (0, max_repo):
        repos.append(js1[i]['name'])

    commits = list()

    for repo in repos:
        commit_url = 'https://api.github.com/repos/' + user + '/' + repo + '/commits'
        commit_uh = urllib.request.urlopen(commit_url)
        commit_data = commit_uh.read().decode()
        js2 = json.loads(commit_data)
        commits.append(len(js2))

    return max_repo, repos, commits


def main():
    user = input('Please input username: ')
    results = get_information(user)

    print('User: ' + user)
    for n in (0, results[0]):
        print('Repo: ' + str(results[1][n]) + '  Number of commits: ' + str(results[2][n]))


if __name__ == '__main__':
    main()