# Function to ask questions and package up the data
def promptQuestions():
    # Set up empty dictionary for info
    projectInfo = {}

    # Prompt user info for questions section
    userGithub = input("(required) Please enter your GitHub username: ")
    projectInfo["userGithub"] = userGithub
    userEmail = input("(required) Please enter your email address: ")
    projectInfo["userEmail"] = userEmail

    # Prompt title and push info to dictionary
    projectTitle = input("(required) Please enter your project's title: ")
    projectInfo["projectTitle"] = projectTitle

    # Prompt if description is wanted
    descriptionConfirm = input("Would you like to add a project description? y/n ").lower()
    # If yes, prompt description and push to dictionary 
    if descriptionConfirm == "y":
        print('Please enter the description below: ')
        description = input()
        projectInfo["description"] = description

    # Prompt and push installation
    installationConfirm = input("Would you like to add information on installation? y/n ").lower()
    if installationConfirm == "y":
        print("Please enter installation info below: ")
        installation = input()
        projectInfo["installation"] = installation
    
    # Usage
    usageConfirm = input("Would you like to add information on usage? y/n ").lower()
    if usageConfirm == "y":
        print("Please enter usage info below: ")
        usage = input()
        projectInfo["usage"] = usage
    
    # Contributions
    contributionsConfirm = input("Would you like to add information on contributions? y/n ").lower()
    if contributionsConfirm == "y":
        print("Please enter contribution info below: ")
        contributions = input()
        projectInfo["contributions"] = contributions
    
    # Tests
    testsConfirm = input("Would you like to add testing information? y/n ").lower()
    if testsConfirm == "y":
        print("Please enter testing info below: ")
        tests = input()
        projectInfo["tests"] = tests

    # Return the data
    return projectInfo

# Call function and store data in global variable
readmeInfo = promptQuestions()

# Template for README file
readmeTemplate = f'''
#{readmeInfo["projectTitle"]}

## Table of Contents
{" - [Description](#description)" if "description" in readmeInfo else ""}
{" - [Installation](#installation)" if "installation" in readmeInfo else ""}
{" - [Usage](#usage)" if "usage" in readmeInfo else ""}
{" - [Contributions](#contributions)" if "contributions" in readmeInfo else ""}
{" - [Tests](#tests)" if "tests" in readmeInfo else ""}
 - [Questions](#questions)

{"## Description" if "description" in readmeInfo else ""}
{readmeInfo["description"] if "description" in readmeInfo else ""}

{"## Installation" if "installation" in readmeInfo else ""}
{readmeInfo["installation"] if "installation" in readmeInfo else ""}

{"## Usage" if "usage" in readmeInfo else ""}
{readmeInfo["usage"] if "usage" in readmeInfo else ""}

{"## Contributions" if "contributions" in readmeInfo else ""}
{readmeInfo["contributions"] if "contributions" in readmeInfo else ""}

{"## Tests" if "tests" in readmeInfo else ""}
{readmeInfo["tests"] if "tests" in readmeInfo else ""}

## Questions
Have any questions? You can reach me through my [github account](https://github.com/{readmeInfo["userGithub"]}) or email me at [{readmeInfo["userEmail"]}](mailto:{readmeInfo["userEmail"]}).
'''
# End template for README file

# If README not found in dist/ create one
# Write new README to the file
f = open("./dist/README.md", "w")
f.write(readmeTemplate)
f.close()

print("README written. Find it in the dist/ folder of this directory.")