
from pydriller import Repository
import pandas as pd
repo_name = []
author_name = []
commit = []
commit_Date = []
urls = ["https://github.com/e-commerce-sample/ecommerce-order-service.git","https://github.com/medusajs/medusa.git"]
for i in Repository(path_to_repo=urls).traverse_commits():
    repo_name.append(i.project_name)
    author_name.append(i.author.name)
    commit.append(i.msg)
    commit_Date.append(i.committer_date)

Repo_info = {"Repo_Name" : repo_name,
             "Author_Name" : author_name,
             "Commit_Message" : commit,
             "Date": commit_Date}


dataFrame = pd.DataFrame(Repo_info)
print(dataFrame)
dataFrame.to_csv("GithubCommit.csv",index=False)
