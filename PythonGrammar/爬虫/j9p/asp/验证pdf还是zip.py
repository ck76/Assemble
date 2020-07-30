# http://jxz1.j9p.com/pc/xxjavas.zip

str="http://jxz1.j9p.com/pc/xxjavas.zip"
result=str.split(".")
zip_or_pdf = str.split(".")[3] == "zip"
print(result)
print(zip_or_pdf)