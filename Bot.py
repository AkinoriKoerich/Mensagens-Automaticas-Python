# importar as bibliotecas
import pyautogui
import time

# listas de variaveis possiveis
navegador = input('Digite o nome do seu navegador: ')
contato = input('Digite o nome de algum contato: ')
mensagem = input('Digite a mensagem desejada: ')

# abrir a ferramenta/o sistema
pyautogui.press("win")
time.sleep(1.3)
pyautogui.write(navegador)
time.sleep(1.3)
pyautogui.press("enter")
time.sleep(4)

# localizar o alvo desejado
pyautogui.write("web.whatsapp.com")
pyautogui.press("Enter")
time.sleep(3)

# localizar o contato escolhido
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write(contato)
time.sleep(1.3)
pyautogui.press('enter')

# digitar a mensagem
pyautogui.write(mensagem)
pyautogui.press('enter')

