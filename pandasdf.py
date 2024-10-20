df1 = pd.DataFrame({
'serial':   ['s1', 's1', 's2','s2', 's3', 's4'],
'category': ['c1', 'c2','c1', 'c1', 'c3', 'c2' ],
'placeid':  ['p1', 'p1','p1', 'p2', 'p3', 'p4' ],
'cost':     [ 50,   50, 50,  50,   150,  50 ],
'count':     [ 10,   10, 20,  20,   30,  30 ],
})
df2 = pd.DataFrame({
'category':   ['c1', 'c2', 'c3','c4', 'c5', 'c6'],
'code': ['rc1', 'rc2','rc3', 'rc4', 'rc5', 'rc6' ],
'name': ['name1','name2','name3','name4','name5','name6',],
'description':     [ 'description1','description2','description3','description4','description5','description6' ],
'parentCategory':     [ 'c5','c5','c5','c5','c7', 'c7'],
})
