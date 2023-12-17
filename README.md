# DA_Engineer_test
Code to use DuckDB, Pandas, and Plotly

### Steps
Github Setup
1. Create a Repo on GitHub
2. Go to working directory (MyProjects) on terminal and glone the Repo ("git clone ...")
3. Open the repo file on VSCode
4. Checkout to development branch ("git checkout -b development")
5. Push the development branch to github ("git push origin development")
6. Checkout to development ("git checkout development")

Working Directory Setup
6. Ensure you are located in development branch: ("git checkout development")
7. Ensure your development branch is up to date ("git pull origin development")
8. Create your working branch from development ("git checkout -b setting_up_environment")
9. Create the Virtual Environment ("virtualenv env")
10. Activate Virtual Environment ("source env/bin/activate")
11. Create requirements.txt
    duckdb==0.9.2
    pandas==2.1.4
    plotly==5.18.0
12. Install requirements ("pip install -r requirements.txt")
13. Create main.py and ensure it is connected with the Python environment
14. Create main.ipynb and ensure it is connected with the Python environment ("Go UpRight and click on 'Select Kernel', choose our env")