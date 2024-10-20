import pandas as pd
p1 = pd.read_csv('schoolmarks.csv')
p1.groupby(['category','subcategory']).count()
p2 = p1.groupby(['category','subcategory'])['mttrhours','metsla','total'].sum()
p2['fixpercentage'] = (p2['metsla'] / p2['total']) * 100
p2['fixpercentage'] = p2['fixpercentage'].round(2)