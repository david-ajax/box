uname > uname.log
du files -ah --max-depth=0 > storage.log
cd files && find > ../find.log && cd ..
cd files && rm -rf $(find -name index.html) && cd ..
date > date.log
python3 main.py > deploy.log