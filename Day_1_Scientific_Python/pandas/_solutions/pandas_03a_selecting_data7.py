df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0])
df['Surname']