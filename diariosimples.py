import tkinter as tk
from tkinter import messagebox, colorchooser
from datetime import datetime
from pathlib import Path

arquivo_diario = Path("diario.txt")
#aplicação em processo
def salvar(event=None):
    texto = entrada.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Aviso", "Escreva algo antes de salvar!")
        return
    try:
        with open(arquivo_diario, "a", encoding="utf-8") as f:
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{data}]\n{texto}\n{'-'*30}\n")
        entrada.delete("1.0", tk.END)
        atualizar_contador()
        messagebox.showinfo("Sucesso", "Anotação salva com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao salvar: {e}")
def limpar():
    if entrada.get("1.0", tk.END).strip() and messagebox.askyesno("Limpar", "Deseja apagar o texto atual?"):
        entrada.delete("1.0", tk.END)
        atualizar_contador()

def mudar_cor():
    cor = colorchooser.askcolor(title="Escolha a cor do texto")[1]
    if cor:
        entrada.config(fg=cor)

def atualizar_contador(event=None):
    conteudo = entrada.get("1.0", tk.END)
    contador.config(text=f"Caracteres: {len(conteudo)-1}")

def on_enter(e):
    e.widget['background'] = '#222222'

def on_leave(e, color):
    e.widget['background'] = color



#problemas de applicação aqui, rever
janela.title("Anotações de Segurança")
janela.geometry("500x520")
janela.resizable(False, False)
janela.configure(bg="#2b2b2b")
janela.bind('<Control-s>', salvar)
janela.bind('<Control-S>', salvar)
titulo = tk.Label(janela, text="SISTEMA DE DIÁRIO", font=("Consolas", 16, "bold"), bg="#2b2b2b", fg="#00FF00")
titulo.pack(pady=15)
entrada = tk.Text(janela, wrap="word", font=("Consolas", 11), height=14, width=55, 
                 bg="#1e1e1e", fg="#ffffff", insertbackground="white", relief="flat", padx=10, pady=10)
entrada.pack(padx=20, pady=5)
entrada.bind("<KeyRelease>", atualizar_contador)
entrada.focus_set()
contador = tk.Label(janela, text="Caracteres: 0", font=("Consolas", 10), bg="#2b2b2b", fg="#888888")
contador.pack(pady=5)
frame_botoes = tk.Frame(janela, bg="#2b2b2b")
frame_botoes.pack(pady=20)
botoes = [
    ("SALVAR", "#2e7d32", salvar),
    ("LIMPAR", "#c62828", limpar),
    ("COR", "#1565c0", mudar_cor)
]

for i, (texto, cor, comando) in enumerate(botoes):
    btn = tk.Button(frame_botoes, text=texto, font=("Consolas", 10, "bold"), bg=cor, fg="white",
                    activebackground="#444444", activeforeground="white",
                    relief="flat", width=12, pady=8, cursor="hand2", command=comando)
    btn.grid(row=0, column=i, padx=8)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", lambda e, c=cor: on_leave(e, c))

janela.mainloop()
