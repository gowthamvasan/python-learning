#from git import Repo
from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests
import time

org='milvik'
#project_list = ['infra-automation','aws-infra-templates']
project_list = ['milvik/infra-automation']
g = Github("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")
# repo = g.get_repo('milvik/infra-automation')
# print(dir(repo))
print(g.get_organization('milvik').get_repos('aws-infra-templates'))

'''
def extract_project_info():
    df_project = pd.DataFrame()
    for repo in project_list:
        g = Github("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")
        output=g.get_repo(repo)
        
        print(output)
        PRs = output.get_pulls(state='all')
        all_commits = output.get_commits()
        # print(help(output.get_commits()))
        print(all_commits)
        print(all_commits.totalCount)
        # import pdb;pdb.set_trace()
        for commit in all_commits:
            pass
        # print(dir(PRs))
        # print(output.id)
        df_project = df_project.append({
            'Project_ID': output.id,
            'Name': output.name,
            'Full_name': output.full_name,
            'Language': output.language,
            'Forks': output.forks_count,
            'Stars': output.stargazers_count,
            'Watchers': output.subscribers_count,
            'PRs_count': PRs.totalCount
        }, ignore_index=True)
        # print(df_project)
        # df_project.to_csv('project_dataset.csv', sep=',', encoding='utf-8', index=True)
        df_project.to_excel('project_dataset.xlsx', encoding='utf-8', index=True)
        # print(dir(output))
    import pdb;pdb.set_trace()
extract_project_info()
'''

