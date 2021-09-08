# Attacksurfacemanagement

# Note : You can run it in parallel to cover a vast majority of assets in less time. I suggest to give it a try

# Installation :

     git clone https://github.com/Deepanjalkumar/Attacksurfacemanagement.git
     
     cd Attacksurfacemanagement
     
     source notebook/bin/activate
     
     pip3 install -r requirements.txt
     
     ./install.sh
     
     Note : If you want to get a customize theme like me then use this :
     
                   pip install jupyterthemes
                   
                   jt -t monokai
     
# Usage/Examples :

     jupyter-notebook --allow-root
     
     select the directory offensive-notebook
     
     Inside it there all lots of engine which covers various aspect of hacking. Choose as per your requirement and start hacking.
     
     Now lets look at the other feature of it i.e sharing information on a real time . 
       
                    uvicorn api:app --reload ( Uvicorn running on http://127.0.0.1:8000 )
                    
                    For sharing and accessing subdomain use this endpoint : /web/subdomain
                    
                    For sharing and accessing http and https service use this endpoint : /web/web-service
                    
     
     
           
