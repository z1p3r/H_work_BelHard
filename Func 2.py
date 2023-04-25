def creator(sep='.', **kwargs):
    n = kwargs['name'][0]
    p = kwargs['patr'][0]
    surname = kwargs['surname']
    birth = kwargs['birth']
    death = kwargs['death']
    krt = kwargs['krt']

    return f'{n}{sep}{p}{sep}{surname} ({birth} - {death}) - {krt}'

print(creator(name='Александр', patr='Сергеевич', surname='Пушкин', birth='06.06.1799', death='10.02.1837', krt='Поэт, драматург, прозаик'))