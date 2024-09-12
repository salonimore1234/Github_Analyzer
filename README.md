# GitHub Analyzer

The GitHub Profile Analyzer is a web application that fetches and displays GitHub profile information and repository details for a given username. Users can enter a GitHub username, and the application will retrieve and show details such as the number of followers, following, public repositories, and the list of repositories along with their stars, forks, and open issues.

# Project Title: GitHub Analyzer

# Project Details
Project URL :https://githubanalyzer-aqf3bjgwcrddgpg3.southindia-01.azurewebsites.net/

Demo Video URL:

GitHub Repository URL:https://github.com/salonimore1234/Github_Analyzer/tree/master

# Azure Service Used:
1. Azure App Service:
Deployed the front-end (html,css) for user interaction & backend.

2. Azure MySQL Database:
It is used for creating MySQL database to storing and managing students data.

# Problem Statement
With the increasing use of GitHub by developers and organizations, it can be time-consuming to manually explore and analyze individual user profiles and repositories to understand a developer's impact or code contributions. GitHub’s vast data needs a quick and efficient way to retrieve and present a user’s profile information and repository statistics in a clear and accessible format.

The GitHub Profile Analyzer aims to solve this by providing a simple tool that allows users to input a GitHub username and receive an analysis of that profile’s details, including:

Basic user information (e.g., followers, following, and public repositories count).

Detailed information about the user’s repositories (e.g., stars, forks, and open issues).

This tool provides a centralized and visually appealing way to analyze GitHub profiles and can be useful for:

Employers evaluating a candidate's GitHub presence.

Developers quickly reviewing their own or peers' GitHub activity.

Users discovering the most popular repositories and projects for a given username.

# Key Problems Solved

Manual Profile Checking: The analyzer automates fetching GitHub user and repository data, reducing the need for manual searching and analysis.

Data Visualization: Presents data in a structured, easy-to-read format (e.g., tables for repositories) to make the analysis process intuitive.

Time Efficiency: Quickly retrieves and summarizes important profile information and repository metrics in real-time.

# Project Description
The GitHub Profile Analyzer is a web-based application designed to fetch and display a GitHub user's profile information and repository statistics. By leveraging the GitHub API, the tool provides an efficient way to access critical data points about any user's public repositories, followers, and other relevant metrics.

Key Features:
  
 1. User Profile Analysis:
    
  Retrieves and displays basic GitHub profile information including:
  
  1.Username and display name.
    
  2.Number of followers and following.
  3.Total public repositories.
  4.Direct link to the user's GitHub profile.
 
 2.Repository Details:
 
 Lists the user’s public repositories with key metrics such as:
 
 1.Repository name (with a clickable link to the repository).
 2.Number of stars (indicating popularity).
 3.Number of forks (indicating usage by others).
 4.Number of open issues (showing ongoing work or unresolved issues).
 
 3.User Input Form:

1.A simple form that allows users to enter a GitHub username to trigger profile retrieval.
2.Error handling for invalid usernames or missing data.

4.User-Friendly Interface:

1.Clean and responsive HTML/CSS design for easy navigation and viewing.

2.Clear presentation of both profile and repository information in an organized manner.
 
 4.Technical Details:
 
1.Frontend: Built with HTML and CSS for a simple yet effective user interface.

2.Backend: Powered by Python’s Flask framework to handle API requests and data processing.

3.GitHub API: Used to fetch user profile and repository details in real-time.

4.Deployment: Hosted on Azure App Service, ensuring reliability and accessibility.

Use Cases:

Recruiters: Quickly evaluate a developer's GitHub profile to assess their contributions, activity, and project popularity.

Developers: Monitor and track their own GitHub profile metrics and popular repositories.

Users: Discover key statistics about GitHub profiles of interest, whether for inspiration or collaboration.

Goals:

The primary goal of this project is to offer a fast, intuitive way to analyze GitHub profiles without having to manually navigate GitHub's interface. The tool simplifies the process of gaining insights into a developer's open-source contributions and activity.
