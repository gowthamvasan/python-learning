from mysqlx import Auth
from numpy import object_
from jira import JIRA
import pandas as pd

jac = JIRA('https://milvik.atlassian.net',basic_auth=('gowtham.srinivasan@milvik.se', 'tVOBalrv1pPFWgteYYk74F8D'))

# print(dir(jac))
# print(help(jac.issue))

jql_str= '''project = "BIMA Customers Helpdesk" AND status = "In Progress" '''

srch_issues = jac.search_issues(jql_str)
# print(srch_issues)
key=srch_issues[0]
df_jira = pd.DataFrame()
for object in srch_issues:
    df_jira = df_jira.append({
    "created_time" : object.fields.created,
    "assignee" :  object.fields.assignee,
    "status" :  object.fields.status,
    "reporter" : object.fields.reporter
    },ignore_index=True)
    print(df_jira)
df_jira.to_csv('python-learning/JIRA-project/jira_dataset.csv', sep=',', na_rep='None',quotechar='\'',encoding='utf-8', index=False)
# created
# assignee
# status

#region  bucket-names
# data = {'us-east-1': ['1','2','3','4'], 'us-west-1': ['4','5'],
#         'ap-south-1': ['7']}

