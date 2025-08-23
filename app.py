<<<<<<< HEAD
import pyautogui
from time import sleep
import pandas as pd  

pyautogui.alert('Favor não mexer no teclado e mouse' 
' até que acabe a automação.')
  
# Entrar no navegador (Edge)
pyautogui.press('win')
sleep(1) 
pyautogui.write('Edge')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.hotkey('win', 'up')
sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(4)

# Entrazer login
pyautogui.click(x=610, y=449, duration=1)
sleep(1)
pyautogui.write('clevercleverpassos@gmail.com')
sleep(1)
pyautogui.press('tab')  
sleep(1)
pyautogui.write('123456')
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(x=1471, y=381)
sleep(1)

# Importar produtos da base de dados 
tabela = pd.read_csv('produtos.csv')    

# Cadastrar cada produto em seu campo correspondente

for linha in tabela.index:
   
    pyautogui.click(x=600, y=308)
    codigo = tabela.loc[linha,'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    sleep(1)

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    sleep(1)
  
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    sleep(1) 

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')                 
    sleep(1)

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    sleep(1)

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    sleep(1)

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.scroll(1000)
    sleep(1)

pyautogui.alert('Já pode voltar ao trabalho!!!')
# Fazer isso para todos produtos até finalizar
=======
import pyautogui
from time import sleep
import pandas as pd  

pyautogui.alert('Favor não mexer no teclado e mouse' 
' até que acabe a automação.')
  
# Entrar no navegador (Edge)
pyautogui.press('win')
sleep(1) 
pyautogui.write('Edge')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.hotkey('win', 'up')
sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(4)

# Entrazer login
pyautogui.click(x=610, y=449, duration=1)
sleep(1)
pyautogui.write('clevercleverpassos@gmail.com')
sleep(1)
pyautogui.press('tab')  
sleep(1)
pyautogui.write('123456')
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(x=1471, y=381)
sleep(1)

# Importar produtos da base de dados 
tabela = pd.read_csv('produtos.csv')    

# Cadastrar cada produto em seu campo correspondente

for linha in tabela.index:
   
    pyautogui.click(x=600, y=308)
    codigo = tabela.loc[linha,'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    sleep(1)

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    sleep(1)
  
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    sleep(1) 

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')                 
    sleep(1)

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    sleep(1)

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    sleep(1)

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.scroll(1000)
    sleep(1)

pyautogui.alert('Já pode voltar ao trabalho!!!')
# Fazer isso para todos produtos até finalizar
>>>>>>> a861d77399e34f035daa6c53bd750172d48eb702
