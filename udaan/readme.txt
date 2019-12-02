Readme 

1. Extract all the files from the zip folder
2. Install all the requirements by running the command "pip install -r requirements.txt" on the command prompt.
3. Now open command prompt in the extracted folder.
4. Run "server.py" by using the command "python server.py"
5. Copy the link appearing on the command prompt and run it on your browser.
6. Access the different APIs add the following extensions 
 6.1 /add-asset : Method POST
                  This API takes description of the asset and saves it.
 6.2 /add-task : Method POST 
                 This API takes description of the task and saves it.
 6.3 /add-worker : Method POST
                   This API takes details of worker and saves it.
 6.4 /assets/all : Method GET
                  The api returns the list of all assets in the system.
 6.5 /allocate-task/ : Method POST
                       This API accepts a request object

**NOTE**
Some values are already added to the api.