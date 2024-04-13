# Frontend -> usuario vê interage
# Backend -> logica por tras  do site
# pip install flet -> no terminal

# Titulo chatzap
# Botão de iniciar o chat
  # Popup
   # Bem vindo ao chatzap
   # Escreva seu nome
   # Entrar no chat
# Chat 
 # Usuário entrou no chat
 # Mensagens do usario
# Campo para enviar mensagem
# Botão enviar

import flet as ft

def main(pagina):
    texto = ft.Text("Chatzap")
    
    nome_usuario = ft.TextField(label="Escreva seu nome")
    
    chat = ft.Column()
    
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
        
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    
    def enviar_mensagem(evento):
        # colocar o nome do usuário na mensagem
   
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
    
        pagina.pubsub.send_all(texto_campo_mensagem)
        # limpar o campo mensagem
        campo_mensagem.value = ""
        pagina.update()
    
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem) 
    #on_submit=enviar_mensagem envia a mensagem com enter.
    
    botao_enviar = ft.ElevatedButton("Eviar", on_click=enviar_mensagem)
    
    def entrar_chat(evento):
        # Feche o popup
        popup.open= False
        # Tire o botão "Iniciar chat" da telaS
        pagina.remove(botao_iniciar)
        # Adicionar o nosso chat
        pagina.add(chat)
        
        # Criar o campo de enviar mensagem

        linha_mensagem = ft.Row(
           [campo_mensagem, botao_enviar] 
        )
        pagina.add(linha_mensagem)
        
        
        
        # Criar o botão de enviar mensagem
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()
        
    
    
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem vindo ao Chatzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton ("Entrar",on_click=entrar_chat)]
        )
    
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
       
         
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
  

#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER) #formato de site
    
    
