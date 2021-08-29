from fastapi import FastAPI
import os

app=FastAPI()

################################# WEB ASSETS ##########################
@app.get("/web/subdomain")
def subdomain():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets", "Subdomain_results")
    with open(f"{path}/all_domains.txt", "r") as file:
        file=file.readlines()
        return {"subdomains": file}

@app.get("/web/web-service")
def webservice():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets", "Web_service_results")
    with open(f"{path}/all_web_service.txt", "r") as file:
        file=file.readlines()
        return {"webservice": file}

@app.get("/web/internet-archive")
def archive():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets", "Internet_archive")
    with open(f"{path}/waybackurls.txt", "r") as file:
        file=file.readlines()
        return {"archive": file}


@app.get("/web/crawler")
def crawler():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets", "Crawler")
    with open(f"{path}/gospider.txt", "r") as file:
        file=file.readlines()
        return {"crawled": file}

@app.get("/web/all-files")
def allfiles():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets")
    with open(f"{path}/all-files.txt", "r") as file:
        file=file.readlines()
        return {"all-files": file}

@app.get("/web/cve-paths")
def cvepaths():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets")
    with open(f"{path}/cve-paths.txt", "r") as file:
        file=file.readlines()
        return {"cve-paths": file}


@app.get("/web/juicy-paths")
def juicypaths():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets")
    with open(f"{path}/juicy-paths.txt", "r") as file:
        file=file.readlines()
        return {"juicy-paths": file}


@app.get("/web/leaky-misconfigs")
def leakymisconfigs():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets")
    with open(f"{path}/leaky-misconfigs.txt", "r") as file:
        file=file.readlines()
        return {"leaky-misconfigs": file}


@app.get("/web/juicy-paths")
def juicypaths():
    cwd=os.getcwd()
    path=os.path.join(cwd, "web_assets")
    with open(f"{path}/juicy-paths.txt", "r") as file:
        file=file.readlines()
        return {"juicy-paths": file}

##############################   NETWORK ASSETS #############################

@app.get("/network/ipv4")
def ipv4():
    cwd=os.getcwd()
    path=os.path.join(cwd, "network_assets")
    with open(f"{path}/all_ipv4.txt", "r") as file:
        file=file.readlines()
        return {"ipv4": file}

#############################################################################
