from github import Github
import os
# from dotenv import load_dotenv
#
# load_dotenv(ENV_PATH)
token = "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" #os.getenv('GITHUB_TOKEN')
if not token:
    print("Error: Personal Access Token not found. Please set GITHUB_TOKEN environment variable.")
    exit()

# Create a PyGithub instance using the Personal Access Token
g = Github(token)

# Specify the repository to check
repo_name = "tsofia-git/Exercise-Varonis-New"  # Replace with the repository name in the format "owner/repository"
repo = g.get_repo(repo_name)

# Check if the repository is public
if not repo.private:
    print(f"The repository '{repo_name}' is currently PUBLIC. Changing to PRIVATE...")
    repo.edit(private=True)
    print(f"The repository '{repo_name}' has been successfully changed to PRIVATE.")
else:
    print(f"The repository '{repo_name}' is already PRIVATE.")