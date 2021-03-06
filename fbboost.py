import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

csv = pd.read_csv('dados.csv', sep=";")

le = LabelEncoder()
csv['Tipo'] = le.fit_transform(csv['Tipo'])

dados = csv.values

#Tipo; Mês; Dia da semana; Hora; Pago; Número comentários; como; Compartilhamento
atributos = dados[:,0:5] 
likes = dados[:,6]
compartilhamentos = dados[:,7]
comentarios = dados[:,5]

modeloLike = LinearRegression()
modeloLike.fit(atributos, likes)

modeloComentario = LinearRegression()
modeloComentario.fit(atributos , comentarios)

modeloCompartilhamento = LinearRegression()
modeloCompartilhamento.fit(atributos, compartilhamentos)

tipo = int(input('Informe o número do tipo da postagem Foto[0]|Link[1]|Status[2]|Video[3]: '))
mes = int(input('Mês: '))
dia = int(input('Dia da semana: D[1]|S[2]|T[3]|Q[4]|Q[5]|S[6]|S[7]: '))
hora = int(input('Hora: '))
pago = int(input('Pago: SIM[1]|NÃO[0]: '))

retornoLike = modeloLike.predict([[tipo, mes, dia, hora, pago]])
retornoComentario = modeloComentario.predict([[tipo, mes, dia, hora, pago]])
retornoCompartilhamento = modeloCompartilhamento.predict([[tipo, mes, dia, hora, pago]])

print('Média de Likes: ', int(retornoLike[0]))
print('Média de Comentarios: ', int(retornoComentario[0]))
print('Média de Compartilhamentos: ', int(retornoCompartilhamento[0]))
