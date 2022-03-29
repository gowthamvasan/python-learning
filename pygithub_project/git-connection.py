#from git import Repo
from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests,time
from datetime import datetime,timedelta

token_personal = "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"
token_office = "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"
# org='milvik'
#project_list = ['infra-automation','aws-infra-templates']
# project_list = ['milvik/bima-infra-jenkins']
project_list = ['gowthamvasan/python-learning']

def extract_project_info():
    df_commits = pd.DataFrame()
    for project in project_list:
        print(project)
        g = Github(token_personal)
        repo=g.get_repo(project)
        since = datetime.now() - timedelta(days=180)
        all_commits = repo.get_commits(since=since)
        counter=0
        for commit in all_commits:
            #print(dir(commit))
            print(commit.commit.message)
            #print(dir(commit.raw_data))
            while True:
                try:
                    counter += 1
                    print(f"Loop counter {counter}")
                    # print(g.rate_limiting)
                    
                    df_commits = df_commits.append({
                        # 'commit_sha': commit.sha,
                        # 'committer_username': commit.author.login if commit.author is not None else 'None',
                        # 'committer_name': commit.author.name if commit.author is not None else 'None',
                        # 'committer_email': commit.author.email if commit.author is not None else 'None',
                        # 'commit_date': commit.author.created_at if commit.author is not None else 'None',
                        'commit_sha': commit.sha,
                        'committer_username': commit.author.login,
                        'committer_name': commit.author.name,
                        'committer_email': commit.author.email,
                        'commit_msg': commit.commit.message,
                        'commit_date': commit.author.created_at
                    }, ignore_index=True)
                except RateLimitExceededException as e:
                    print(e.status)
                    print('Rate limit exceeded')
                    time.sleep(300)
                    continue
                except BadCredentialsException as e:
                    print(e.status)
                    print('Bad credentials exception')
                    break
                except UnknownObjectException as e:
                    print(e.status)
                    print('Unknown object exception')
                    break
                except GithubException as e:
                    print(e.status)
                    print('General exception')
                    break
                except requests.exceptions.ConnectionError as e:
                    print('Retries limit exceeded')
                    print(str(e))
                    time.sleep(10)
                    continue
                except requests.exceptions.Timeout as e:
                    print(str(e))
                    print('Time out exception')
                    time.sleep(10)
                    continue
                break
    print(df_commits)
    df_commits.to_csv('python-learning/pygithub_project/project_dataset.csv', sep=',', na_rep='None',quotechar='\'',encoding='utf-8', index=False)
        # df_project.to_excel('project_dataset.xlsx', encoding='utf-8', index=True)
    # import pdb;pdb.set_trace()
extract_project_info()


