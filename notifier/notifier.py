import customtkinter
import feedparser
import webbrowser


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# URL do RSS Feed
RSS_FEED_URL = "https://news.google.com.br/rss/search?q=games"
RSS_FEED_URL_CRIPTO = "https://news.google.com.br/rss/search?q=criptomoedas"


def carregar_noticias():
    limpar_abas(aba_noticias)
    # obtendo noticias do rss
    feed = feedparser.parse(RSS_FEED_URL)
    for item in feed.entries[:5]: #limitando a exibir as 5 ultimas noticias
        titulo = item.title
        link = item.link
        adicionar_noticia(titulo, link)

def carregar_noticias_cripto():
    limpar_abas(aba_cripto)
    # obtendo noticias do rss
    feed_cripto = feedparser.parse(RSS_FEED_URL_CRIPTO)
    for item in feed_cripto.entries[:5]: #limitando a exibir as 5 ultimas noticias
        titulo_cripto = item.title
        link_cripto = item.link
        adicionar_cripto(titulo_cripto, link_cripto)

def adicionar_cripto(titulo_cripto, link_cripto):
    #adiciona uma noticia ao widget
    cripto_frame = customtkinter.CTkFrame(aba_cripto)
    cripto_frame.pack(pady=5, padx=10, fill="x")

    cripto_label = customtkinter.CTkLabel(cripto_frame, text=titulo_cripto, anchor="w", cursor="hand2")
    cripto_label.pack(fill="x") 
    cripto_label.bind("<Button-1>", lambda e: abrir_link_cripto(link_cripto))


def adicionar_noticia(titulo, link):
    #adiciona uma noticia ao widget
    noticia_frame = customtkinter.CTkFrame(aba_noticias)
    noticia_frame.pack(pady=5, padx=10, fill="x")

    titulo_label = customtkinter.CTkLabel(noticia_frame, text=titulo, anchor="w", cursor="hand2")
    titulo_label.pack(fill="x") 
    titulo_label.bind("<Button-1>", lambda e: abrir_link(link))

def abrir_link(link):
    webbrowser.open(link)

def abrir_link_cripto(link_cripto):
    webbrowser.open(link_cripto)

def limpar_abas(aba):
    for widget in aba.winfo_children():
        widget.destroy()




widget = customtkinter.CTk()
widget.geometry("400x300")
widget.title("Noticias Tech")

tabview = customtkinter.CTkTabview(widget, width=400)
tabview.pack()
tabview.add("Notícias")
aba_noticias = tabview.tab("Notícias")
tabview.pack()
tabview.add("Cripto")
aba_cripto = tabview.tab("Cripto")

botao_carregar = customtkinter.CTkButton(widget, text="Atualizar Notícias", command=carregar_noticias)
botao_carregar.pack()

botao_carregar_cripto = customtkinter.CTkButton(aba_cripto, text="Atualizar Notícias Cripto", command=carregar_noticias_cripto)
botao_carregar_cripto.pack(pady=10)

carregar_noticias()

widget.mainloop()
