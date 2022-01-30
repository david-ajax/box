from lib import *
import os

version = "v0.1.2 Stable"
indexhtml = File.read("./default/theme/index.html")
welcomehtml = File.read("./default/theme/welcome.html")
overviewhtml = File.read("./default/theme/overview.html")
abouthtml = File.read("./default/theme/about.html")
static_path = os.getcwd()
config = Data.config_data

def about():
    File.rewrite("about.html", abouthtml)
    File.replace("about.html", "$title", config["title"])
    File.replace("about.html", "$sfis_version", version)
    File.replace("about.html", "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
    if config["about"] == True:
        File.replace("about.html", "$about", "<li>基于 <a href = 'https://github.com/david-ajax/sfis'>SFIS 项目</a></li>")
    else:
        File.replace("about.html", "$about", "")
def overview():
    size = str(round(round(Path.getdirsize("./files/") / 1024, 3) / 1024, 3)) + " MB" #GB
    print(size)
    File.rewrite("overview.html", overviewhtml)
    File.replace("overview.html", "$title", config["title"])
    File.replace("overview.html", "$used_space", size)
    File.replace("overview.html", "$os_edition", System.os_edition)
    File.replace("overview.html", "$cpu_version", System.processor_numbers)
    File.replace("overview.html", "$local_time", System.local_time)
    File.replace("overview.html", "$python_version", System.python_version)
    File.replace("overview.html", "$sfis_version", version)
    File.replace("overview.html", "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
    if config["about"] == True:
        File.replace("overview.html", "$about", "<li>基于 <a href = 'https://github.com/david-ajax/sfis'>SFIS 项目</a></li>")
    else:
        File.replace("overview.html", "$about", "")
def create(one):
    os.chdir(one)
    print(os.getcwd())
    filelist = Path.ls(".", "file")
    folderlist = Path.ls(".", "folder")
    alllist = ""
    for one in folderlist:
        alllist = alllist + "<br><a href='" + one + "'>" + one + "/</a>"
    for one in filelist:
        if one == "index.html" or one == "":
            continue
        else:
            alllist = alllist + "<br><a href='" + one + "'>" + one + "</a>"
    File.rewrite("index.html", indexhtml)
    File.replace("index.html", "$title", config["title"])
    File.replace("index.html", "$path", Path.contrast(os.getcwd(), static_path))
    File.replace("index.html", "$list", alllist)
    if os.path.exists("README.md") and os.path.isfile("README.md") and config["preview_readme_md"] == True:
        readmemd = File.md2html("README.md")
        File.replace("index.html", "$readme", "<hr>" + readmemd)
    else:
        File.replace("index.html", "$readme", "")
    if config["ad_code"] != "":
        File.replace("index.html", "$ad", "<hr>" + config["ad_code"])
    else:
        File.replace("index.html", "$ad", "")
    File.replace("index.html", "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
    if config["about"] == True:
        File.replace("index.html", "$about", "<li>基于 <a href = 'https://github.com/david-ajax/sfis'>SFIS 项目</a></li>")
    else:
        File.replace("index.html", "$about", "")
    os.chdir(static_path)
def welcome():
    File.rewrite("index.html", welcomehtml)
    File.replace("index.html", "$title", config["title"])
    File.replace("index.html", "$owner", config["owner"])
    File.replace("index.html", "$email", config["email"])
    File.replace("index.html", "$ad", config["ad_code"])
    File.replace("index.html", "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
    if config["about"] == True:
        File.replace("index.html", "$about", "<li>基于 <a href = 'https://github.com/david-ajax/sfis'>SFIS 项目</a></li>")
    else:
        File.replace("index.html", "$about", "")

if __name__ == "__main__":
    welcome()
    os.system('echo start > log')
    p = ["files"]
    for one in Path.tree("files", "folder"):
        p.append(one)
    for one in p:
        File.rewrite('log', File.read('log') + one)
        create(one)
    overview()
    about()
