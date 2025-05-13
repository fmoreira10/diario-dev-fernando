import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacaoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Jogo da Adivinhação")
        self.master.geometry("440x360")
        self.master.configure(bg="#f9fafb")

        self.limite_inferior = 1
        self.limite_superior = 100
        self.numero_secreto = None
        self.tentativas = 0

        self.tela_menu()

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def tela_menu(self):
        self.limpar_tela()

        tk.Label(self.master, text="🎯 JOGO DA ADIVINHAÇÃO 🎯",
                 font=("Segoe UI", 20, "bold"), bg="#f9fafb", fg="#111827").pack(pady=20)

        tk.Label(self.master, text="Escolha a dificuldade:",
                 font=("Segoe UI", 13), bg="#f9fafb", fg="#4b5563").pack(pady=10)

        estilo_botao = {"width": 20, "font": ("Segoe UI", 11, "bold"), "fg": "white", "relief": "flat"}

        tk.Button(self.master, text="😄 Fácil (1 a 50)", bg="#10b981",
                  command=lambda: self.iniciar_jogo(1, 50), **estilo_botao).pack(pady=5)

        tk.Button(self.master, text="😬 Médio (1 a 100)", bg="#3b82f6",
                  command=lambda: self.iniciar_jogo(1, 100), **estilo_botao).pack(pady=5)

        tk.Button(self.master, text="😵 Difícil (1 a 200)", bg="#ef4444",
                  command=lambda: self.iniciar_jogo(1, 200), **estilo_botao).pack(pady=5)

        tk.Button(self.master, text="🚪 Sair", width=20, font=("Segoe UI", 11),
                  bg="#e5e7eb", fg="#111827", relief="flat", command=self.master.quit).pack(pady=20)

    def iniciar_jogo(self, inferior, superior):
        self.limite_inferior = inferior
        self.limite_superior = superior
        self.numero_secreto = random.randint(inferior, superior)
        self.tentativas = 0
        self.tela_jogo()

    def tela_jogo(self):
        self.limpar_tela()

        tk.Label(self.master, text=f"Adivinhe o número entre {self.limite_inferior} e {self.limite_superior}",
                 font=("Segoe UI", 14), bg="#f9fafb", fg="#111827").pack(pady=20)

        self.entrada = tk.Entry(self.master, font=("Segoe UI", 12), justify="center", width=15)
        self.entrada.pack(pady=10)

        tk.Button(self.master, text="🎯 Chutar", font=("Segoe UI", 11, "bold"),
                  bg="#6366f1", fg="white", relief="flat", command=self.checar_chute).pack(pady=10)

        self.label_resultado = tk.Label(self.master, text="", font=("Segoe UI", 11),
                                        bg="#f9fafb", fg="#374151")
        self.label_resultado.pack(pady=5)

        tk.Button(self.master, text="⬅️ Voltar ao Menu", font=("Segoe UI", 10),
                  bg="#d1d5db", fg="#111827", relief="flat", command=self.tela_menu).pack(pady=10)

    def calcular_pontuacao(self):
        base = self.limite_superior // 2
        pontos = max(1000 - (self.tentativas - 1) * base, 100)
        return pontos

    def checar_chute(self):
        try:
            chute = int(self.entrada.get())
            self.entrada.delete(0, tk.END)

            if chute < self.limite_inferior or chute > self.limite_superior:
                self.label_resultado.config(
                    text=f"⚠️ Fora do intervalo ({self.limite_inferior}-{self.limite_superior}).")
                return

            self.tentativas += 1

            if chute == self.numero_secreto:
                pontos = self.calcular_pontuacao()
                messagebox.showinfo("🎉 Parabéns!",
                                    f"Você acertou o número {self.numero_secreto} em {self.tentativas} tentativa(s)!\n🏆 Pontuação: {pontos} pontos")
                self.tela_menu()
            elif chute < self.numero_secreto:
                self.label_resultado.config(text="🔼 Dica: o número é maior.")
            else:
                self.label_resultado.config(text="🔽 Dica: o número é menor.")
        except ValueError:
            messagebox.showerror("Erro", "Digite apenas números inteiros.")
            self.entrada.delete(0, tk.END)

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = JogoAdivinhacaoGUI(root)
    root.mainloop()
# Código do jogo da adivinhação com interface gráfica usando tkinter
# O jogo permite ao usuário escolher a dificuldade e adivinhar um número secreto
# O usuário recebe dicas se o palpite é maior ou menor que o número secreto
# O jogo termina quando o usuário acerta o número, e a pontuação é calculada
# com base no número de tentativas
# O código é organizado em uma classe para facilitar a manutenção e a legibilidade