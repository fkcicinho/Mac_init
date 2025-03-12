import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading




# Funcao para deixar o selenium em modo headless
driver_silent = Options()
driver_silent.add_argument("--headless")
driver_silent.add_argument("--disable-gpu")
driver_silent.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=driver_silent)


# Funcoes Iniciais

# Funcao para mover a aba para segunda tela
# def segundo_monitor():
#     monitor_x = 1920
#     monitor_y = 0
#     driver.set_window_position(monitor_x, monitor_y)


# Chamando a função segundo_monitor
#segundo_monitor()


# ----------------------------------------------------------------------------------------------------------------------

def status_preencher():
    opcoes = ['Login efetuado com sucesso!', 'Validando dias', 'Preenchendo os dias', 'Dias preenchidos',
              'Desconectando da conta', 'Limpando dias']
    return opcoes


login_sucess, val_dias, pree_dias, dias_pre, desconect, limp = status_preencher()

def finish():
    done = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'btnOk')))
    done.click()


def atividades(n1):
    if n1 == "Actualizaciones a repositorio":
        opcao_2 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[2]')))
        opcao_2.click()

    elif n1 == "Administraction":
        opcao3 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[3]')))
        opcao3.click()

    elif n1 == "ADMON DE LA CONFIGURACION":
        opcao4 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[4]')))
        opcao4.click()


    elif n1 == "ANALISIS":
        opcao5 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[5]')))
        opcao5.click()

    elif n1 == "ASESORIA":
        opcao6 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[6]')))
        opcao6.click()

    elif n1 == "ASESORÍA A PROYECTOS":
        opcao7 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[7]')))
        opcao7.click()

    elif n1 == "AUDITORIA":
        opcao8 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[8]')))
        opcao8.click()

    elif n1 == "CAPACITACION":
        opcao9 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[9]')))
        opcao9.click()

    elif n1 == "CAPACITACIÓN A OPERACIONES":
        opcao10 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[10]')))
        opcao10.click()

    elif n1 == "DESARROLLO":
        opcao11 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[11]')))
        opcao11.click()

    elif n1 == "DISEÑO":
        opcao12 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[12]')))
        opcao12.click()

    elif n1 == "DOCUMENTACION":
        opcao13 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[13]')))
        opcao13.click()

    elif n1 == "ENTREVISTAS":
        opcao14 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[14]')))
        opcao14.click()

    elif n1 == "EVALUACIONES (SCAMPI)":
        opcao15 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[15]')))
        opcao15.click()

    elif n1 == "HORAS STAND BY":
        opcao16 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[16]')))
        opcao16.click()

    elif n1 == "IMPLEMENTACIÓN":
        opcao17 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[17]')))
        opcao17.click()

    elif n1 == "INICIATIVAS":
        opcao18 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[18]')))
        opcao18.click()

    elif n1 == "INNOVACIONES":
        opcao19 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[19]')))
        opcao19.click()

    elif n1 == "LIBERACION":
        opcao20 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[20]')))
        opcao20.click()

    elif n1 == "MANTENIMIENTO":
        opcao21 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[21]')))
        opcao21.click()

    elif n1 == "MANTENIMIENTO AMMI":
        opcao22 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[22]')))
        opcao22.click()

    elif n1 == "MÉTRICAS":
        opcao23 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[23]')))
        opcao23.click()

    elif n1 == "OTROS":
        opcao24 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[24]')))
        opcao24.click()


    elif n1 == "PREANALISIS":
        opcao25 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[25]')))
        opcao25.click()

    elif n1 == "PRESENTACIÓN":
        opcao26 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[26]')))
        opcao26.click()

    elif n1 == "PRUEBAS":
        opcao27 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[27]')))
        opcao27.click()

    elif n1 == "PREVENTA":
        opcao28 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[28]')))
        opcao28.click()

    elif n1 == "REUNIONES":
        opcao29 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[29]')))
        opcao29.click()

    elif n1 == "REVISION DOCUMENTAL":
        opcao30 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[30]')))
        opcao30.click()

    elif n1 == "SEGUIMIENTO":
        opcao31 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[31])')))
        opcao31.click()

    elif n1 == "SUPERVISIÓN":
        opcao32 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[32]')))
        opcao32.click()

    elif n1 == "VACACIONES":
        opcao33 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[33]')))
        opcao33.click()

    elif n1 == "VENTAS":
        # VENTAS
        opcao34 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbActividades"]/option[34]')))
        opcao34.click()

    else:
        print("Erro na função atividade")


def horas(n2):
    if n2 == "06:00":
        hora_06 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="HorasCapturadas"]/option[13]')))
        hora_06.click()


    elif n2 == "07:00":
        hora_07 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="HorasCapturadas"]/option[15]')))
        hora_07.click()

    elif n2 == "04:00":
        hora_04 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="HorasCapturadas"]/option[9]')))
        hora_04.click()

    elif n2 == "08:00":
        hora_08 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="HorasCapturadas"]/option[17]')))
        hora_08.click()

    else:
        print("Erro na função Horas")


def logout():
    try:
        # Click no botão de logout
        saida = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'buttonLogout')))
        saida.click()

        botao_regressar = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/a')))
        botao_regressar.click()



    except Exception as e:
        print(f'Erro na def logout: {e}')


# Funções de obter dias
def active_day():
    active = driver.find_elements(By.XPATH,
                                  '//*[contains(@class, "ui-state-default ui-state-highlight ui-state-active")]')

    try:
        for i in range(len(active)):
            driver.find_element(By.XPATH,  '//*[contains(@class, "ui-state-default ui-state-highlight ui-state-active")]').click()


            # Obter atividade
            with open("atividade.txt", "r") as f:
                cap_atividade = f.read()

            atividades(cap_atividade)


            # Falta a função de horas
            with open("horas.txt", "r") as f:
                cap_horas = f.read()

            horas(cap_horas)
            finish()


    except Exception as e:
        print(f'erro na funcao active_day: {e}')


def get_dias():
    dias = driver.find_elements(By.XPATH, '//*[@class="ui-state-default"]')

    try:
        for i in range(len(dias)):
            dia = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '(//*[@class="ui-state-default"])[1]')))
            dia.click()

            # Obtem os valores de atividade e click no local
            with open("atividade.txt", "r") as f:
                atividade = f.read()

            atividades(atividade)

            # Obtem os valores de horas e click no local
            # Obtem os valores de horas e click no local
            with open("horas.txt", "r") as f:
                cap_horas = f.read()

            horas(cap_horas)

            # Clica no botão de done
            finish()

            time.sleep(1)


    except:
        print(f"Erro na funcao get_dias ")


def validacao():
    dias = driver.find_elements(By.XPATH, '//*[@class="ui-state-default"]')
    dias_contagem = len(dias)

    try:
        if dias_contagem > 0:
            get_dias()
            validacao()

        else:
            messagebox.showwarning(message="Todos os dias foram preenchidos! ")
            progress_fim()


    except Exception as e:
        print(f'erro na funcao validacao: {e} ')


def limpar_host():
    quant_dias = driver.find_elements(By.XPATH, '//td[@style="border:none"]')

    try:
        for i in range(len(quant_dias) - 1):
            # Click no X
            x = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '(//button[@class="botonBorrar botonFormato"])[2]')))
            x.click()

            # Click no botão SE
            botao_sim = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[2]')))
            botao_sim.click()
        time.sleep(1)
        driver.refresh()

    except:
        pass


def val_limpar_host():
    dias_capturados = driver.find_elements(By.XPATH, '//*[@class="diaCapturado"]')
    dias_necessarios = len(dias_capturados)

    try:
        while dias_necessarios != 0:
            limpar_host()

            dias_capturados = driver.find_elements(By.XPATH, '//*[@class="diaCapturado"]')
            dias_necessarios = len(dias_capturados)

        messagebox.showwarning(title="Limpeza", message="Todos os dias foram limpos!\nProcesso finalizado!")
        progress_fim()

    except Exception as e:
        print(f'Erro na função de val_limpar_host: {e}')


def print_preencher():
    driver.save_screenshot("Dias_preenchidos.png")


def print_limpo():
    driver.save_screenshot("Dias_limpos.png")


# ----------------------------------------------------------------------------------------------------------------------
# Codigo principal
def start_limpar():
    driver.get('https://host.globalhitss.com/')

    #Elements
    login_key = driver.find_element(By.ID, 'UserName')
    password_key = driver.find_element(By.ID, 'Password')
    botao_iniciar = driver.find_element(By.ID, 'boton')


    #Método de entrada
    # Método de entrada
    with open("username2.txt", "r") as f:
        login_interface = f.read()

    with open("password2.txt", "r") as f:
        senha_interface = f.read()

    login_key.send_keys(f'{login_interface}')
    password_key.send_keys(f'{senha_interface}')
    botao_iniciar.click()

    try:
        mensagem_erro = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/button/span')))
        mensagem_erro.click()

        messagebox.showwarning(title="Erro ao logar", message="Login incorreto!")
        habilitar_limpar()
        habilitar_preencher()
        progress_fim()


    except:
        label_var(login_sucess)
        label_var(limp)
        val_limpar_host()
        #print_limpo()
        logout()
        habilitar_limpar()
        habilitar_preencher()





def start_preencher():
    driver.get('https://host.globalhitss.com/')

    #Elements
    login_key = driver.find_element(By.ID, 'UserName')
    password_key = driver.find_element(By.ID, 'Password')
    botao_iniciar = driver.find_element(By.ID, 'boton')

    #Método de entrada
    with open("username.txt", "r") as f:
        login_interface = f.read()

    with open("password.txt", "r") as f:
        senha_interface = f.read()

    login_key.send_keys(f'{login_interface}')
    password_key.send_keys(f'{senha_interface}')
    botao_iniciar.click()

    try:
        mensagem_erro = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/button/span')))
        mensagem_erro.click()

        messagebox.showwarning(title="Erro ao logar", message="Login incorreto!")
        progress_fim()
        habilitar_preencher()
        habilitar_limpar()


    except:
        label_var(login_sucess)
        active_day()

        label_var(val_dias)
        get_dias()

        label_var(pree_dias)
        validacao()

        logout()

        progress_fim()
        habilitar_preencher()
        habilitar_limpar()





# Interface
# Função de ação para o botão de login
def login():
    atividade = combobox_atividade.get()
    horas = combobox_horas.get()
    senh = entry_password.get()
    user = entry_username.get()


    # Verificar se os campos estão preenchidos
    if user and senh:
        variaveis(nome="username", var=user)

        variaveis(nome="password", var=senh)

        variaveis(nome="atividade", var=atividade)

        variaveis(nome="horas", var=horas)

        confirmacao = messagebox.askquestion("Confirmação",
                                             f"Confirme as informações abaixo!\n\n Atividade: {atividade}\nHora: {horas}\n\nDeseja continuar?",
                                             icon="warning")

        if confirmacao == "yes":
            messagebox.showwarning(message="Preenchimento do HOST iniciado!, Quando a barra de loading parar de se mover, significa que o processo foi finalizado.")

            thread_load = threading.Thread(target=progress_inicio)
            thread_load.start()

            # Chama a função de validação do login
            thread = threading.Thread(target=start_preencher)
            thread.start()

            desabilitar_preencher()
            desabilitar_limpar()

            entry_password.delete(0, tk.END)

        else:
            pass

    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos!\nProcesso finalizado")



def clean_host():
    senh = entry_password.get()
    user = entry_username.get()
    atividade = combobox_atividade.get()
    horas = combobox_horas.get()

    # Verificar se os campos estão preenchidos
    if user and senh:
        # Obtem o valor do usuario
        variaveis(nome="username2", var=user)

        # Obtem o valor da senha
        variaveis(nome="password2", var=senh)

        # Obtem o valor de atividade
        variaveis(nome="atividade", var=atividade)

        # Obtem o valor de horas
        variaveis(nome="horas", var=horas)

        messagebox.showwarning(message="Processo de limpeza iniciado!, quando a barra de loading parar de se mover, significa que o processo foi finalizado.")

        bar = threading.Thread(target=progress_inicio)
        bar.start()

        thread = threading.Thread(target=start_limpar)
        thread.start()

        desabilitar_limpar()
        desabilitar_preencher()

        # Deleta o valor do campo de password
        entry_password.delete(0, tk.END)


    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos!")


# Barra de progresso
def habilitar_preencher():
    btn_preencher = button_preencher.config(state=tk.NORMAL)


def habilitar_limpar():
    btn_limpar = button_limpa_host.config(state=tk.NORMAL)


def desabilitar_preencher():
    btn_desabilitar = button_preencher.config(state=tk.DISABLED)

def desabilitar_limpar():
    btn_limpar2 = button_limpa_host.config(state=tk.DISABLED)



def progress_inicio():
    progress_bar.start(10)


def progress_fim():
    progress_bar.stop()


#criacao do arquivo que guarda as variaveis
def variaveis(nome, var):
    with open(f"{nome}.txt", "w") as f:
        f.write(var)



if __name__ == "__main__":
    # Criar a janela principal
    root = tk.Tk()
    root.title("Developed by: XxFKxX! (Beta 1.0)")

    altura = 500
    largura = 700

    altura_screen = root.winfo_screenheight()
    largura_screen = root.winfo_screenwidth()
    pos_x = (largura_screen // 2) - (largura // 2)
    pos_y = (altura_screen // 2) - (altura // 2)

    root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y-100}")
    root.resizable(False, False)



    # Label e Entry para Nome de Usuário
    label_username = tk.Label(root, text="Nome de Usuário:")
    label_username.pack(pady=10)
    entry_username = tk.Entry(root, width=30)
    entry_username.pack()



    # Label e Entry para Senha
    label_password = tk.Label(root, text="Senha:", justify="center")
    label_password.pack(pady=10)
    entry_password = tk.Entry(root, show="*", width=30)
    entry_password.pack()



    # Combobox para atividade
    option_atividade = ['Actualizaciones a repositorio', 'Administraction', 'ADMON DE LA CONFIGURACION', 'ANALISIS',
                        "ASESORIA", "ASESORÍA A PROYECTOS", "AUDITORIA", "CAPACITACION", "CAPACITACIÓN A OPERACIONES",
                        "DESARROLLO", "DISEÑO", "DOCUMENTACION", "ENTREVISTAS", "EVALUACIONES (SCAMPI)", "HORAS STAND BY",
                        "IMPLEMENTACIÓN", "INICIATIVAS", "INNOVACIONES", "LIBERACION", "MANTENIMIENTO", "MANTENIMIENTO AMMI",
                        "MÉTRICAS", "OTROS", "PREANALISIS", "PRESENTACIÓN", "PRUEBAS", "PREVENTA", "REUNIONES", "REVISION DOCUMENTAL",
                        "SEGUIMIENTO", "SUPERVISIÓN", "VACACIONES", "VENTAS"

                       ]

    label_atividade = tk.Label(root, text="Escolha a ATIVIDADE: ")
    label_atividade.pack(pady=10)
    combobox_atividade = ttk.Combobox(root, values=option_atividade, state='readonly', justify='center', width=30)
    combobox_atividade.current(19)
    combobox_atividade.pack()



    # Combobox para horas
    options_horas = ['04:00', '06:00', '07:00', '08:00']
    label_horas = tk.Label(root, text="Horas:")
    label_horas.pack(pady=10)
    combobox_horas = ttk.Combobox(root, values=options_horas, state='readonly', justify="center")
    combobox_horas.current(3)
    combobox_horas.pack()

    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=20)


    # Botão preencher
    button_preencher = tk.Button(frame_botoes, text="Preencher HOST!", command=lambda: login(), width=15)
    button_preencher.pack(side="left", pady=20)


    # Botão limpar_host
    button_limpa_host = tk.Button(frame_botoes, text="Limpar HOST!", command=clean_host, width=15)
    button_limpa_host.pack(side="left", pady=20)

    frame_log = tk.Frame(root, width=230, height=230, )
    frame_log.pack(pady=23, padx=30)

    label_log = tk.Label(frame_log, text="------- Log do andamento -------", fg="red")
    label_log.pack()

    def label_var(n1):
        label2 = tk.Label(frame_log, text=n1)
        label2.pack()

    progress_bar = ttk.Progressbar(root, mode='indeterminate', length=500)
    progress_bar.pack(pady=20)



    # Executar a aplicação
    root.mainloop()
    driver.quit()





