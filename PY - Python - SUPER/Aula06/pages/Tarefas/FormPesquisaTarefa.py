import streamlit as st
from Controllers.PadraoController import *
from datetime import datetime
import streamlit_antd_components as sac
import Utils as ut
import pages.Tarefas.FormListarTarefa as flt  

def Form_PesquisaTarefa():  
    
    ut.Divisor('Pesquisar Tarefas', 'search', 'rgb(20,80,90)', 'PesquisaCarteira01')
    with st.expander('Informe os parametros para pesquisar as tarefas', expanded=True):
        with st.container(border=True):
            row_0_col1, row_0_col2, row_0_col3 = st.columns([2, 2, 2])  
            row_1_col1, row_1_col2 = st.columns([8, 0.01])  
            row_2_col1, row_2_col2, row_2_col3 = st.columns([2, 1, 2])  

            with row_0_col1:
               prioridade = st.selectbox('Prioridade', prioridades_p, key='prioridade', index=0, placeholder='Seleciona a prioridade da tarefa...')
               if not prioridade:
                    st.error('O campo "Categoria" é Obrigatorio.')
            with row_0_col2:
                categoria = st.selectbox('Categoria', categorias_p, key='categoria', index=0, placeholder='Seleciona a categoria da tarefa...')
                if not categoria:
                    st.error('O campo "Categoria" é Obrigatorio.')            
            with row_0_col3:
                concluida = st.selectbox('Concluído', concluida_p, key='status', index=0, placeholder='Seleciona o status da tarefa...')
                if not concluida:
                    st.error('O campo "Concluído" é Obrigatorio.')           
            
            with row_1_col1:
                sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None)
            with row_1_col2:   
                st.write('')
                
            with row_2_col1:   
                st.write('')
                
            with row_2_col2:   
                selected_tarefa_pesquisar = sac.menu([
                    sac.MenuItem(type='divider'),
                    sac.MenuItem('Pesquisar', icon=sac.BsIcon(name='search', color='green')),
                    sac.MenuItem(type='divider'),
                    ], color='rgb(20,80,90)', open_all=False, return_index=False, index=None)            
            
            with row_2_col3:   
                st.write('')
           
    if selected_tarefa_pesquisar == 'Pesquisar':
        if prioridade is not None and categoria is not None:
            # Chama a função listar_tarefas com os filtros selecionados
            df_filtrado = listar_tarefas(prioridade, categoria, concluida)

            # Mostra as tarefas filtradas em um DataFrame do Pandas
            if not df_filtrado.empty:
                st.dataframe(df_filtrado, use_container_width=True)
            else:
                st.write("Não há tarefas correspondentes aos filtros selecionados.")        
        else:
            ut.Alerta('','Parametros para a pesguisa incompleto') 
           
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'PesquisaCarteira02')