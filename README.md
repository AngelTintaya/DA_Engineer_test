# DA_Engineer_test
Code to use DuckDB, Pandas, and Plotly

### Steps
Github Setup
1. Create a Repo on GitHub
2. Go to working directory (MyProjects) on terminal and glone the Repo ("git clone ...")
3. Open the repo file on VSCode
4. Checkout to development branch ("git checkout -b development")
5. Push the development branch to github ("git push origin development")
6. Sett default branch to be development (To protect Production): Go to Your Code -> Settings -> Default Banch: Development
7. Checkout to development ("git checkout development")

Pre-requirements:
- Install Extention: Jupyter Render, so Jupyter Notebook could render images

Working Directory Setup
1. Ensure you are located in development branch: ("git checkout development")
2. Ensure your development branch is up to date ("git pull origin development")
3. Create your working branch from development ("git checkout -b setting_up_environment")
4. Create the Virtual Environment ("virtualenv env")
5. Activate Virtual Environment ("source env/bin/activate")
6. Create requirements.txt (nbformat is necessary to render plotly)
    duckdb==0.9.2
    pandas==2.1.4
    plotly==5.18.0
    nbformat==5.9.2
7. Install requirements ("pip install -r requirements.txt")
8. Create main.py and ensure it is connected with the Python environment
9. Create main.ipynb and ensure it is connected with the Python environment ("Go UpRight and click on 'Select Kernel', choose our env")
10. Write a python code, run and install all the dependencies
11. Add, Commit and Push all your changes.
    git add README.md main.ipynb main.py requirements.txt
    git commit -m "Setting Up Working Environment"
    
12. Create a Pull Request to Development Branch following link that was provided for git

## Now We Are Ready To Start
