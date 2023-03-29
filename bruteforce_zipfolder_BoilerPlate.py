import zipfile                     
import time

folderpath = r"E:\223 project\223 project\PRO-C223-Teacher-Boiler-Plate-main\0004.zip"
zipf = zipfile.ZipFile(folderpath)         

if not zipf:           
    print('The zipped file/folder is not password protected! You can successfully open it!')  

else:
    starttime = time.time()             
    result = 0                          
    count = 0                               

    
    characters =['0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z',
                 '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']

    
    print("Brute Force Started...")
    if result==0:
        print("checking 4 digit character: ")
        for i in characters:
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess=str(i)+str(j)+str(k)+str(l)
                        password=guess.encode('utf-8').strip()
                        print(guess)
                        print("final password",password)
                        count=count+1
                        try:
                            file=open(zipf,"rb")
                            body=file.read()
                            endtime=time.time()
                            result=1
                            break
                        except:
                            pass
                    if result==1:
                        break
                if result==1:
                    break
            if result==1:
                break
 


    if(result == 0):
        print("Password is not found.")
    else:
        duration = endtime - starttime
        print('Congratulations!!! Password found after trying '+str(count)+' combinations in '+str(duration)+' seconds')