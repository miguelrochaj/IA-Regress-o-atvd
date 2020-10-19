importar  pandas  como  pd
de  sklearn . Importação de pré-processamento  LabelEncoder
de  sklearn . linear_model import LinearRegression

csv = pd . read_csv('dadosfb.csv', sep=";")

le = LabelEncoder()
csv['Tipo'] = le . fit_transform(csv['Tipo'])

dados = csv . valores

atributos = dados[:, 0: 5]
likes = dados[:, 6]
compartilhamentos = dados[:, 7]
comentarios = dados[:, 5]

modeloLike = LinearRegression()
modeloLike . fit(atributos, curtidas)


modeloComentario = LinearRegression()
modeloComentario . fit(atributos, comentarios)


modeloCompartilhamento = LinearRegression()
modeloCompartilhamento . fit(atributos, compartilhamentos)


tipo = int(input(
    'Informe o número do tipo da postagem Foto [0] | Link [1] | Status [2] | Vídeo [3]:'))
mes = int(input('Mês:'))
dia = int(entrada(
    'Dia da semana: D [1] | S [2] | T [3] | Q [4] | Q [5] | S [6] | S [7]:'))
hora = int(input('Hora:'))
pago = int(input('Pago: SIM [1] | NÃO [0]:'))

retornoLike = modeloLike . predizer([[tipo, mes, dia, hora, pago]])
retornoComentario = modeloComentario . predizer([[tipo, mes, dia, hora, pago]])
retornoCompartilhamento = modeloCompartilhamento . predizer(
    [[tipo, mes, dia, hora, pago]])

print('Média de likes :', int(retornoLike[0]))
print('Média de Comentarios:', int(retornoComentario[0]))
print('Média de aprendizagem :', int(retornoCompartilhamento[0]))
