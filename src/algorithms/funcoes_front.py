import tkinter as tk
from tkinter import Frame, Button, Label, Entry, ttk
from tkinter import messagebox



def add_livro(self):
    dados = self.obter_dados_formulario()
    if not dados:
        return
    for livro in self.livros:
        if livro['codigo'] == dados['codigo']:
            messagebox.showerror("Erro", "Código já cadastrado!")
            return
    
    # Adicionar o livro
    self.livros.append(dados)
    self.listar_livros()
    self.limpar_campos()
    messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")

def att_livro(self):
        if not self.livro_selecionado:
            messagebox.showwarning("Atenção", "Selecione um livro na tabela!")
            return
        
        dados = self.obter_dados_formulario()
        if not dados:
            return
        
        for livro in self.livros:
            if livro['codigo'] == self.livro_selecionado:
                livro.update(dados)
                break
        
        self.listar_livros()
        self.limpar_campos()
        self.atualizar_estatisticas()
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")

def remover_livro(self):
        if not self.livro_selecionado:
            messagebox.showwarning("Atenção", "Selecione um livro na tabela!")
            return
        
        resposta = messagebox.askyesno("Confirmar", "Deseja realmente remover este livro?")
        if resposta:
            self.livros = [l for l in self.livros if l['codigo'] != self.livro_selecionado]
            self.listar_livros()
            self.limpar_campos()
            self.atualizar_estatisticas()
            messagebox.showinfo("Sucesso", "Livro removido com sucesso!")

def buscar_livro(self):
        termo = self.busca_entry.get().strip().lower()
        filtro = self.filtrar_combo.get()
        
        if not termo:
            self.listar_livros()
            return
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        resultados = []
        for livro in self.livros:
            if filtro == "Todos":
                if any(termo in str(v).lower() for v in livro.values()):
                    resultados.append(livro)
            elif filtro == "Código" and termo in str(livro['codigo']).lower():
                resultados.append(livro)
            elif filtro == "Nome" and termo in livro['nome'].lower():
                resultados.append(livro)
            elif filtro == "Autor" and termo in livro['autor'].lower():
                resultados.append(livro)
            elif filtro == "Gênero" and termo in livro['categoria'].lower():
                resultados.append(livro)
        
        for idx, livro in enumerate(resultados):
            tag = "evenrow" if idx % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=(
                livro['codigo'], livro['nome'], livro['categoria'], livro['autor'],
                f"R$ {livro['valor']:.2f}", livro['estoque'], livro['idioma'], livro['ano']
            ), tags=(tag,))

def limpar_busca(self):
        self.busca_entry.delete(0, tk.END)
        self.filtrar_combo.set("Todos")
        self.listar_livros()
    