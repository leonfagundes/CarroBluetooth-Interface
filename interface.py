import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from dotenv import load_dotenv
import os
import threading
import time

# Carrega variáveis do .env
load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")

class TrajectoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trajeto do Carrinho")
        
        # Tentativa de conexão com a API na inicialização
        if not self.check_api_connection():
            messagebox.showerror("Erro", "Não foi possível conectar-se à API. Verifique a conexão e tente novamente.")
            self.root.destroy()  # Fecha a interface se não houver conexão
            return
        
        # Configuração da interface
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.btn_show = tk.Button(self.frame, text="Exibir Gráfico", command=self.fetch_and_plot)
        self.btn_show.grid(row=0, column=0, padx=5, pady=5)

        self.btn_clear = tk.Button(self.frame, text="Limpar Gráfico", command=self.clear_plot)
        self.btn_clear.grid(row=0, column=1, padx=5, pady=5)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

        self.update_thread = threading.Thread(target=self.update_graph)
        self.update_thread.daemon = True
        self.update_thread.start()

    def check_api_connection(self):
        """Verifica a conexão inicial com a API."""
        try:
            response = requests.get(f"{API_BASE_URL}/commands", timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def fetch_data(self):
        try:
            response = requests.get(f"{API_BASE_URL}/commands")
            response.raise_for_status()
            data = response.json().get("data", [])
            return data
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao buscar dados: {e}")
            return []

    def process_data(self, data):
        x, y = 0, 0
        x_vals, y_vals = [x], [y]
        for command in data:
            direction = command['command']
            if direction == "F":
                y += 1
            elif direction == "B":
                y -= 1
            elif direction == "L":
                x -= 1
            elif direction == "R":
                x += 1
            x_vals.append(x)
            y_vals.append(y)
        return x_vals, y_vals

    def fetch_and_plot(self):
        data = self.fetch_data()
        if data:
            x_vals, y_vals = self.process_data(data)
            self.plot_graph(x_vals, y_vals)

    def plot_graph(self, x_vals, y_vals):
        """Plota o trajeto completo e destaca o ponto atual em vermelho."""
        self.ax.clear()
        
        # Plota o trajeto completo com uma linha contínua
        self.ax.plot(x_vals, y_vals, marker="o", linestyle="-", color="black", label="Trajeto")
        
        # Destaca o ponto atual (último ponto) em vermelho
        self.ax.plot(x_vals[-1], y_vals[-1], marker="o", color="red", markersize=10, label="Ponto Atual")
        
        self.ax.set_title("Trajeto do Carrinho")
        self.ax.legend()
        self.canvas.draw()



    def clear_plot(self):
        self.ax.clear()
        self.canvas.draw()
        try:
            response = requests.delete(f"{API_BASE_URL}/commands")
            response.raise_for_status()  # Levanta exceção para códigos de status HTTP de erro
            messagebox.showinfo("Sucesso", "Todos os registros foram removidos do banco.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao limpar os dados no banco: {e}")
    def update_graph(self):
        while True:
            time.sleep(2)  # Atualiza a cada 5 segundos
            data = self.fetch_data()
            if data:
                x_vals, y_vals = self.process_data(data)
                self.plot_graph(x_vals, y_vals)

if __name__ == "__main__":
    root = tk.Tk()
    app = TrajectoryApp(root)
    root.mainloop()
