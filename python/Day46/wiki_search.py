import wikipedia as wk
query=input('enter text=')
#wk.set_lang('hi')
result=wk.summary(query,sentences=2)
print(result)