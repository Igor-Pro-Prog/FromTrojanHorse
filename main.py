import smtplib
import ssl

smtp_port = 587
smtp_server = "smtp.gmail.com"

message = "#" #mensagem que ira ser enviada

email_from = "#" #email que ira enviar a mensagem configurado
email_to = "#" #email que ira receber a mensagem

pswd = "qopaibkecawlqjzn"


simple_email_context = ssl.create_default_context()

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

main()
