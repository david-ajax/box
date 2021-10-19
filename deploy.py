import codecs, markdown, os
os.system("cd files && find > ../find.log")
def readmemd():
    # 读取 markdown 文本
    input_file = codecs.open("README.md", mode="r", encoding="utf-8")
    text = input_file.read()
    # 转为 html 文本
    html = markdown.markdown(text)
    return html
def replace(file, old_content, new_content):
    content = read_file(file)
    content = content.replace(old_content, new_content)
    rewrite_file(file, content)
def read_file(file):
    with open(file, encoding='UTF-8') as f:
        read_all = f.read()
        f.close()
    return read_all
def rewrite_file(file, data):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(data)
        f.close()
def get_filelist():
    Filelist = []
    with open(static_path + "/find.log") as file:
        for line in file:    
            Filelist.append(line.rstrip())
    return Filelist
def create(go):
    sp = os.getcwd()
    os.chdir(go)
    rewrite_file("index.html", o_file)
    filetext = ""
    ld = os.listdir()
    ld.remove("index.html")
    for one in ld:
        if os.path.isdir(one) == True:
            plus = "/"
            filetext = filetext + '<p><a href="' + one + '">' + one + plus + '</a><p>' + "\n"
        else:
            plus = ""
            filetext = filetext +  '<p><a href="' + os.path.relpath(".",static_path+"/files/") + "/" + one + '" download="'  + one + '">' + one + plus + '</a><p>' + "\n"
    replace("index.html", r"$py_file_path" , os.path.relpath(".",static_path+"/files"))
    replace("index.html", r"$py_file_back" , os.path.relpath("..",static_path+"/files"))
    replace("index.html", r"$py_file_list" ,filetext)
    if os.path.exists("README.md") == True and os.path.isfile("README.md") == True:
        replace("index.html", r"$py_file_readme" ,readmemd())
    else:
        replace("index.html", r"$py_file_readme" ,"暂无内容")
    os.chdir(sp)
def main():
    filel = get_filelist()
    folderl = []
    for ph in filel:
        if os.path.isdir(ph) == True:
            folderl.append(ph)
    print(folderl)
    for go in folderl:
        print(os.getcwd())
        create(go)
        print("did")
    print("Completed")
o_file = read_file("./source/index.html")
os.chdir(".")
static_path = os.getcwd()
os.system("cd files && rm -rf $(find -name index.html) && cd ..")
os.chdir("files")
main()
