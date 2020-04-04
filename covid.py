import time
import pandas as  pd
from pandas import ExcelWriter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Página Web
url = "https://worldpopulationreview.com/"

#Drive do navegador Firefox
driver = webdriver.Firefox(executable_path="C:\geckodriver")

driver.get(url)

#Pegando elemento da página HTML 
element = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div[5]/div[1]/div/div/div/div[2]/div[2]/div[2]/table")
html_content = element.get_attribute('outerHTML')

#Tratando dados
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

#Estruturando dados
df = pd.read_html(str(table))[0]
print(df)

#Salvando Dados no Excel
writer = pd.ExcelWriter('C:\\Users\\Lucas\\populacao.xlsx')
df.to_excel(writer,'planilha1')
writer.save()

driver.quit()







