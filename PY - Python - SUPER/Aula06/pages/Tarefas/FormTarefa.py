import streamlit as st
from Controllers.PadraoController import *
import streamlit_antd_components as sac
import Utils as ut


def Form_Tarefa():  
    # Gerar chaves únicas para os componentes
    key_tarefa1 = Key_Unique('Tarefa')
    key_tarefa2 = Key_Unique('Tarefa')
    key_nome = Key_Unique('nome')
    key_descricao = Key_Unique('descricao')
    key_prioridade = Key_Unique('prioridade')
    key_categoria = Key_Unique('categoria')
    key_divisor = Key_Unique('Divisor')
    key_novo = Key_Unique('Novo')
    key_salvar = Key_Unique('Salvar')
    
    ut.Divisor('Adicionar Tarefas', 'clipboard-plus', 'rgb(20,80,90)', key_tarefa1)
    with st.container(border=True):  
        row_0_col1, row_0_col2, row_0_col3, row_0_col4 = st.columns([2, 2, 2, 2])  
        row_1_col1, row_1_col2 = st.columns([8, 0.01])  
        row_2_col1, row_2_col2, row_2_col3, row_2_col4= st.columns([2, 1, 1, 2]) 

        # Linha 00
        with row_0_col1:
            nome = st.text_input('Nome da tarefa', key=key_nome)
            if not nome:
                st.error('O campo "Nome da tarefa" é Obrigatorio.')
                
        with row_0_col2:
            descricao = st.text_input('Desc. da tarefa', key=key_descricao)
            if not descricao:
                st.error('O campo "Desc. da tarefa" é Obrigatorio.')        
        
        with row_0_col3:
            prioridade = st.selectbox('Prioridade', prioridades, key=key_prioridade, index=None, placeholder='Seleciona a prioridade da tarefa...')
            if not prioridade:
                st.error('O campo "Categoria" é Obrigatorio.')
       
        with row_0_col4:
            categoria = st.selectbox('Categoria', categorias, key=key_categoria, index=None, placeholder='Seleciona a categoria da tarefa...')
            if not categoria:
                st.error('O campo "Categoria" é Obrigatorio.')
       
        with row_1_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key=key_divisor)
        with row_1_col2:   
            st.write('')
    
        with row_2_col1:   
            st.write('')            
        
        with row_2_col2:
            tarefa_new = sac.menu([
                sac.MenuItem(type='divider'),
                sac.MenuItem('Novo', icon=sac.BsIcon(name='clipboard', color='blue')),
                sac.MenuItem(type='divider'),
                ], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key=key_novo) 
            
        with row_2_col3:   
            tarefa_post = sac.menu([
                sac.MenuItem(type='divider'),
                sac.MenuItem('Salvar', icon=sac.BsIcon(name='clipboard-plus', color='green')),
                sac.MenuItem(type='divider'),
                ], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key=key_salvar)          
        
        with row_2_col4:   
            st.write('')
    
    # if (tarefa_new == 'Novo'):
    #     Form_Tarefa()
        
    if (tarefa_post == 'Salvar'):
        if nome and descricao and prioridade and categoria:
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        else:
            ut.Alerta('','Parametros para incluir uma tarefa incompleto')   
   
           
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', key_tarefa2)
    
    
if __name__ == "__main__":
    Form_Tarefa()