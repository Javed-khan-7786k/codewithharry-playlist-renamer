import os
import re

# Function to sanitize filenames (removes invalid characters for Windows)
def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*\n]', '_', name).strip() 

try:
    i=0
    with open("file.txt","r",encoding="utf-8") as infile:
        lines=infile.readlines()
    with open("outfile","w",encoding="utf-8") as outfile:
        for line in lines:
                    clean_line = line.strip()
                    for i in range(1,101):
                        # print("hi i_am_he
                        search=f"Day _{i}(720P_HD)"
                        search=sanitize_filename(search)
                        print("hi i_am_here")
                        if line in lines:
                            if  search in clean_line:
                                    # os.mkdir("file")  
                                    src=rf"{clean_line}"
                                    print("hi i_am_here")
                                    dst=sanitize_filename(f"{i} {clean_line}")
                                    os.rename(src,dst)
except Exception as e:
      print("error",e)
finally:
      print("hi i_am_here")