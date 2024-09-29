import streamlit as st
import time


# Título da página
st.title("Tutorial Diarius Check")

# Exibe o vídeo do YouTube
video_url = "https://www.youtube.com/watch?v=1G7HvhLm5fY"
st.video(video_url)

# Mensagem informando que o formulário será liberado após assistir o vídeo
st.write("Assista ao vídeo e, logo em seguida, responda o  formulário.")

# Temporizador de 60 segundos
if 'timer' not in st.session_state:
    st.session_state.timer = False

    if st.button("Clique aqui para responder"):
        with st.spinner("Verificando..."):
            time.sleep(0.5)  # Simulando o tempo para assistir ao vídeo
            st.session_state.timer = True
            st.success("Clique para responder!")
else:
    # Exibe o formulário após o temporizador
    st.title(':blue[Formulário de Perguntas]')
    

    # Gabarito das respostas corretas (usado para comparar as respostas)
    gabarito = {
        '1': 'Certo',
        '2': 'Errado',
        '3': 'Certo',
        '4': 'Errado',
        '5': 'Certo',
        '6': 'Certo',
        '7': 'Certo',
        '8': 'Certo',
        '9': 'Certo',
        '10': 'Certo'
    }

    # Perguntas com "Certo" ou "Errado"
    st.subheader('1. O aplicativo Diarius Check permite registrar a entrada de estudantes através da leitura das carteirinhas.')
    resposta_1 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='1', )

    st.subheader('2. O modo "Saída" do aplicativo serve para liberar a entrada de novos estudantes.')
    resposta_2 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='2')

    st.subheader('3. O sistema envia mensagens de notificação para os pais quando o estudante entra na escola.')
    resposta_3 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='3')

    st.subheader('4. O aplicativo monitora apenas a entrada e saída dos estudantes.')
    resposta_4 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='4')

    st.subheader('5. As refeições monitoradas pelo sistema incluem café da manhã, almoço, lanche da tarde e jantar.')
    resposta_5 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='5')

    st.subheader('6. Projetos e eventos, como fanfarra e esportes, são registrados no aplicativo.')
    resposta_6 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='6')

    st.subheader('7. Se um estudante perder ou estragar a carteirinha, ela é bloqueada e o responsável é notificado.')
    resposta_7 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='7')

    st.subheader('8. O aplicativo permite registrar empréstimos e devoluções de objetos, como bolas de pebolim.')
    resposta_8 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='8')

    st.subheader('9. Ocorrências de indisciplina podem ser registradas e notificadas aos pais e responsáveis.')
    resposta_9 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='9')

    st.subheader('10. O aplicativo pode liberar turmas para ir embora mais cedo, e essa informação é sincronizada para todos os usuários.')
    resposta_10 = st.radio('Selecione a resposta:', ['Certo', 'Errado'], key='10')

    # Lista para armazenar as respostas do usuário
    respostas = {
        '1': resposta_1,
        '2': resposta_2,
        '3': resposta_3,
        '4': resposta_4,
        '5': resposta_5,
        '6': resposta_6,
        '7': resposta_7,
        '8': resposta_8,
        '9': resposta_9,
        '10': resposta_10
    }

    # Função para contar acertos e calcular a nota
    def calcular_resultados(respostas, gabarito):
        acertos = 0
        for i in gabarito:
            if respostas[i] == gabarito[i]:
                acertos += 1
        return acertos, 10 - acertos

    # Botão para submeter as respostas e calcular a nota
    if st.button('Enviar Respostas'):
        acertos, erros = calcular_resultados(respostas, gabarito)
        nota = acertos  # Cada acerto vale 1 ponto
        st.write("Respostas enviadas com sucesso!")
        st.balloons()

        # Exibir as respostas corretas e incorretas
        st.write(f"Você acertou {acertos} questões.")
        st.write(f"Você errou {erros} questões.")
        st.write(f"Sua nota final é: {nota}/10")

        # Exibir as respostas do usuário para revisão
        for i in range(1, 11):
            st.write(f'{i}. {"Certo" if respostas[str(i)] == gabarito[str(i)] else "Errado"}')

        # Mensagem final
        st.write(f"Obrigado por fazer o quiz do **Diarius Apps**! Você acertou o total de {acertos} questões.")

st.link_button("Central de Login", "https://dic-ffe3f7051fcd.herokuapp.com/lista")

