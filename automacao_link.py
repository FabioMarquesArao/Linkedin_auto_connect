from selenium.webdriver.common.keys import Keys # importa como tecla enter etc...
from selenium import webdriver  #importa o selenium e webdriver
from selenium.webdriver import ActionChains
from senha_email import Senha, Email
from time import sleep

#variavel driver recebe o chrome com o caminho do execultavel baixado
driver = webdriver.Chrome(executable_path=" CAMINHO DO SEU WEBDRIVER AQUI ")

#faz uma chamada atravez do get para o site escolhido, nesse caso o goole chrome
driver.get("https://www.linkedin.com")

driver.implicitly_wait(10)#dá uma espera implícita de 10 segundos
driver.maximize_window()#maximiza a tela para melhor visuaização
nome = driver.find_element_by_name("session_key")#pega o nome do objeto na tela, ou seja oque vc quer manipular.
nome.send_keys(Email+Keys.RETURN)#o comando send_keys escreve oque vc deseja.

chave = driver.find_element_by_name("session_password")#pega o nome do objeto na tela, ou seja oque vc quer manipular.
chave.send_keys(Senha+Keys.RETURN)#o comando send_keys escreve oque vc deseja.

sleep(2)#adiciona uma pausa de 2 segundos

driver.find_element_by_class_name('search-global-typeahead').click()#clica no ícone de pesquisa

#o comando abaixo escreve o título da barra de pesquisa, nste caso Tech recruiter
driver.find_element_by_class_name("search-global-typeahead__input").send_keys("tech recruiter"+Keys.RETURN)

#Este comando clica para ampliar os resultados de busca
driver.find_element_by_class_name("search-results__cluster-bottom-banner").click()

sleep(2)#adiciona uma pausa de 2 segundos...

cont = 1 #variavel contadora
while True:
    cont +=1 #A cada laço a variavel cont é encrementada em 1
    #a variavel todos_botoes recebe todos os elementos da pag. com nome button
    todos_botoes = driver.find_elements_by_tag_name("button")
    #a variavel conectar recebe um laço de repetição que faz um loop,
    #dentro da variavel todos_botoes, onde o botao seja igual ao nome do button que queremos
    #clicar, no caso 'Conectar'
    conectar = [btn for btn in todos_botoes if btn.text == 'Conectar']
    seguir = [seg for seg in todos_botoes if seg.text == 'Seguir']
    
    #usamos o laço for para percorrer os botoes
    for btn in conectar:
        #utilizamos o comando de click do javaScript para fugir do bloqueio que tem para 
        # o click() do webDriver script python
        driver.execute_script("arguments[0].click();",btn) 
        
        sleep(2)#adiciona uma pausa de 2 segundos...
                   
        #A variavel btn2 recebe o xpath do botao a ser clicado
        btn2 = driver.find_element_by_xpath("//button[@aria-label='Enviar agora']")
        
        #utilizamos o comando de click do javaScript para fugir do bloqueio que tem para 
        # o click() do webDriver script python
        driver.execute_script("arguments[0].click();",btn2)
        
    for seg in seguir:
        #utilizamos o comando de click do javaScript para fugir do bloqueio que tem para 
        # o click() do webDriver script python
        driver.execute_script("arguments[0].click();",seg) 
        
        sleep(2)#adiciona uma pausa de 2 segundos...
                   
    try:
        driver.execute_script('window.scrollBy(0, 1500)')
    
        sleep(3)
        
        print("Vamos para a pagina...",cont)
        print("......................")
        print("......................")
        a = driver.find_element_by_xpath("//button[@aria-label='Avançar']")
        driver.execute_script("arguments[0].click();",a)
        print("Já estamos na pagina...",cont)
        print("......................")
        print("......................")
        
    except:
        None
    
    sleep(3)