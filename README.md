# project_3

## Introduction

The project is based on python, using requests to cover all the requirements. This project includes five files:

* init.py
* githubClient.py
* requirements.txt
* README.md
* .gitignore

## Information
To run the project, you should first import the *github_client.py* in your test file. Here are some information about how to run the project correctly:

* import the client module in your test file
* call functions to test the project
* the personal_access_token should be created on the github, or the clinet will not work well.

## Function on GithubClient

* GithubClient.init(self, personal_access_token)

  This is the constructed function and send the persoanl_access_token as a parameter to initial the client.
  
* GithubClient.ListStars(self)

  This function is used to get the list of your star repositories, including id, name, full_name, login and url

* GithubClient.ListFollowers(self)

  This function is used to get the list of your followers, including login and url
  
* GirhubClient.ListRepositories(self)

  This function is used to get the list of your repositories, including id, name, full_name, login and url
  
* GithubClient.StarRepository(self, owner_id, repo_id)

  This function is used to star the repository you want according to the owner_id and repo_id you give, returning {"success": "ok"} if the query was donw successfully
  
* GithubClient.FollowUser(self, username)

  This function is used to follow the user you want according to the username you give, returning {"success": "ok"} if the query was donw successfully
  
* GithubClient.UnfollowUser(self, username)

  This function is used to unfollow the user you want according to the username you give, returning {"success": "ok"} if the query was donw successfully
  
* GithubClient.CreateRepository(self, repo_name)

  This function is used to create the repository you want according to the repo_name you give, returning {"success": "ok", "id":<created_repo_id>} if the query was donw successfully
  
* GithubClient.DeleteRepository(self, owner_id, repo_id)

  This function is used to delete the repository you want according to the owner_id and repo_id you give, returning {"success": "ok"} if the query was donw successfully
  
## Exceptions raised the cases
Every function are dealt with exceptions, if the query is not done successfully, corresponding messages will be print to let you know the error.




