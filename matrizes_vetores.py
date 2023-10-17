import numpy as np

usuarios = [
            {   'id':1,
                'user':'rosendo',
                'user_password':'37423asds',
            },
            {   'id':2,
                'user':'alexxx',
                'user_password':'324u23hgsd',
            },
            ]

senhas =  [{'user_id':'1',
            'passwords':[{'gmail':'489325943'},
            {'netflix':'wehjfjlhsd33'},
            {'telegram':'kdjh873'}]
            },

            {'user_id':'2',
             'passwords':[{'gmail':'237asuida'},
                              {'netflix':'sdfh832'},
                              {'telegram':'sdkjhfds'}]}
            ]

ids = np.array([1, 2, 3, 4, 5, 6])
ids2 = np.array([1, 2, 3, 4, 5, 6])
print('soma de arrays:', ids+ids2)

matriz = np.array([[1, 2, 4], [4, 5, 6]])
cond = matriz > 2

print(matriz[cond])

print(np.mean(matriz[cond]))
print(type(ids))

for n in ids:
    print(f'\n {n} + 2 = {n+2}')



def num(num, vec):

    for n in vec:
        print(f'\n {n} + {num} = {n+num}')

print('chamando uma função ai')
num(5, ids)

print('produto de duas matrizes: \n', np.dot(ids, ids2))

print('menor valor de ids', np.min(ids))
#print(usuarios)
#print()
#print(senhas)
