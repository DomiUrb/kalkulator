# # gdyby to byl jupiter albo inne onlinowe, to trzeba dopisac: matplotlib inline -> nie bedzie sie otwierac nowa strona
#
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('data.csv')
# df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
#
# x = df['date']
# y = df['Close']
#
# fid, ax = plt.subplots(figsize=(10, 4))
# ax.plot(x, y)
#
#
# w collabpratory dziala:
# #przykl 1
# # import pandas as pd
# # import matplotlib
# # import matplotlib.pyplot as plt
# #
# # df = pd.read_csv('data.csv')
# # df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
# #
# # x = df['date']
# # y = df['Close']
# #
# # fid, ax = plt.subplots(figsize=(10, 4))
# # ax.plot(x, y)
#
#
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('data.csv')
# df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
#
# x = df['date']
# y = df['Close']
#
# fid, ax = plt.subplots(figsize=(10, 4))
# ax.bar(x, y)
#
#
#
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('data.csv')
# df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
#
# x = df['date']
# y = df['Close']
#
# fid, ax = plt.subplots(figsize=(10, 4))
# ax.scatter(x, y, marker = 'o', alpha = .5)
#
#
#
#
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('data.csv')
# df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
#
# x = df['date']
# y = df['Close']
#
# fid, ax = plt.subplots(figsize=(10, 8))
# _=ax.pie([10,5], labels = [10,5])
# _=ax.legend()
#
#
#


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
x = df['date']
y = df['Close']

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].plot(x, y)
axs[1, 0].bar(x, y)
axs[0, 1].scatter(x, y, marker='o', alpha=.5)
axs[1, 1].pie([10, 5], labels=['10', '5'])
plt.show()
