import customtkinter
import feedparser
import webbrowser


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# URL do RSS Feed
RSS_FEED_URL = "https://news.google.com.br/rss/search?q=games"


def carregar_noticias():
    # obtendo noticias do rss
    feed = feedparser.parse(RSS_FEED_URL)
    for item in feed.entries[:5]: #limitando a exibir as 5 ultimas noticias
        titulo = item.title
        link = item.link
        adicionar_noticia(titulo, link)

def adicionar_noticia(titulo, link):
    #adiciona uma noticia ao widget
    noticia_frame = customtkinter.CTkFrame(widget)
    noticia_frame.pack(pady=5, padx=10, fill="x")

    titulo_label = customtkinter.CTkLabel(noticia_frame, text=titulo, anchor="w", cursor="hand2")
    titulo_label.pack(fill="x") 
    titulo_label.bind("<Button-1>", lambda e: abrir_link(link))

def abrir_link(link):
    webbrowser.open(link)




widget = customtkinter.CTk()
widget.geometry("400x300")
widget.title("Noticias Tech")

tabview = customtkinter.CTkTabview(widget, width=400)
tabview.pack()
tabview.add("Notícias")

botao_carregar = customtkinter.CTkButton(widget, text="Atualizar Notícias", command=carregar_noticias)
botao_carregar.pack()

carregar_noticias()

widget.mainloop()