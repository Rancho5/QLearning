import pandas as pd
import numpy as np

# s = pd.Series([1, 2, 3, 4, np.nan], index=[1, 2, 3, 4, 5])
# print(s)
#
# dates = pd.date_range("2019-8-29", periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns=['a','b','c','d'])
# print(df)
# print(df.sort_values(by="b"))
#
# df2 = pd.DataFrame({'a':1,
#                     'b':pd.Timestamp('2019-8-29'),
#                     'c':pd.Series(np.arange(4), index=list(range(4)))})
# print(df2)
# print(df.describe())
# print(df.index)
# print(df.T)
# print(df.sort_index(axis=1 ,ascending=False))

# # select
# dates = pd.date_range('2019-08-29', periods=6)
# df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=list(np.arange(4)))
# print(df)
# print(df[0])
# print(df[0:3])
# print(df.loc['2019-08-29'])
# print(df.iloc[3])
# print(df.ix[1:4, '1':'4'])
# print(df[df[0]>6])

# dates = pd.date_range("20190829", periods=6)
# df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df)

#  # change
# df.loc[:, 'A'] = -1
# print(df)
# df.iloc[1, :] = -2
# print(df)
# df.ix[2, :] = -3
# print(df)
# df.A = -4
# print(df)
# df.A[df.C>0] = 0
# print(df)
# df['F'] = np.nan
# print(df)

# df.ix[2, 2] = np.nan
# df.ix[3, 3] = np.nan
# print(df)
# print(df.dropna(axis=1, how='any'))
# print(df.fillna(value=-1))
# print(np.any(df.ix[:, 1].isnull()) == 0)

# data = pd.read_csv('Student.csv')
# print(data)
# data.to_pickle('student.pickle')


# # concatenating
# df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
# df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
# print(pd.concat([df1, df2, df3], axis=0, ignore_index=True))
#
# df4 = pd.DataFrame(np.ones((3, 4))*1, index=np.arange(3), columns=['a', 'b', 'c', 'd'])
# df5 = pd.DataFrame(np.ones((3, 4))*2, index=np.arange(1, 4), columns=['b', 'c', 'd', 'e'])
# print(pd.concat([df4, df5], axis=0, join_axes=[df4.columns]))
#
# print(df4)
# print(df4.append(pd.DataFrame(np.arange(3, 7).reshape(1, 4)), ignore_index=True))


# merge

# df1 = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
#                     'A': ['a1', 'a2', 'a3', 'a4'],
#                     'B': ['b1', 'b2', 'b3', 'b4']},
#                    index=[0, 1, 2, 3])
# df2 = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k4'],
#                     'A': ['c1', 'c2', 'c3', 'c4'],
#                     'D': ['d1', 'd2', 'd3', 'd4']},
#                    index=[1, 2, 3, 4])
# print(df1)
# print(df2)
# res1 = pd.merge(df1, df2, on=['key', 'A'], how='left', indicator='indicator', )
# print(res1)
# res2 = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
# res3 = pd.merge(df1, df2, on=['key'], left_index=True, right_index=True, how='outer')
# print(res2)

boys = pd.DataFrame({'id': ['id0', 'id1', 'id2'],
                     'age': [22, 23, 24]})
girls = pd.DataFrame({'id': ['id0', 'id1', 'id2'],
                      'age': [23, 24, 25]})
print(boys)
print(girls)
res4 = pd.merge(boys, girls, on='id', suffixes=['_boy', '_girl'])
print(res4)
















