# Nexus
Purpose:

    The way that payroll is done at this time, espically with ES and Fedex, takes entirely too much time.
    This app strives to make a difference in the single-truck and the multi-truck fleet alike.  Before I 
    begin, I will give a brief explanation about the project structure.  
    This app is written using the Flask Framework, Python as the server side language, HTML, CSS, JS,
    Bootstrap on the front end, and sqlite as the database. The general structure of this web application
    is modeled after the Flask "Blueprints".  This makes each section of the app modular. 

Project Tree:

    This will be updated as the project progresses.
    
- nexus (home folder)

    - external_files
        - *Various*
        - These are the example csv and settlement files from ES

    - nexus (project folder)
    
        - home (Home Blueprint)
            - "\_\_init__.py"
            - "routes.py"
            
        - login (Login Blueprint)
            - "\_\_init__.py"
            - "routes.py"    
            
        - static (All project static files)
            - b10override.css (Used to override Bootstrap and create custom class)
            - *Various*
                    
        - templates (All project templates)
            - master_template (Bootstrap master)
            - child_master_template (A Template for all html extending the master_template)
            - home
                - home.html
            - login
                - login.html    
          
        - users (User Blueprint)
            - "\_\_init__.py"
            - "routes.py"    
                
        - .gitignore ()
        
        - "\_\_init__.py" (View doc-header for more info)
        
        - README.MD (This file)
        
        - Schedule.txt (File to log Scheduled Tasks)
        
        - scratches(A collection of snippets related to this project)
        
        - "run.py" (View doc-header for more info)
            
    - venv (Virtual Environment for this machine)

 Github init
 
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/b10dev/nexus.git
git push -u origin master   

    

    

    

    
      
    
        
    
