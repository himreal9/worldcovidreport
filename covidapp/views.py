from django.shortcuts import render
import requests, os, json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "7e8b9181d0msh41a61e4815369f5p13ce2cjsn42ddb19a463a",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


def frun(request):
    nr=int(response['results'])
    l=[]
    t,a,n,td,r=0,0,0,0,0
    t1,a1,n1,td1,r1=0,0,0,0,0    
    for i in range(1,nr):
        t=t+int(response['response'][i]['cases']['total'])
        if response['response'][i]['deaths']['total']:
            td=td+int(response['response'][i]['deaths']['total'])
        if response['response'][i]['cases']['active']:
            a=a+int(response['response'][i]['cases']['active'])
        if response['response'][i]['cases']['recovered']:
            r=r+int(response['response'][i]['cases']['recovered'])
        if response['response'][i]['cases']['new']:
            n=n+int(response['response'][i]['cases']['new'][1:])
        l.append(response['response'][i]['country'])
    l.sort()
    sel='India'
    for i in range(1,nr):
        if response['response'][i]['country']==sel: 
            t1=int(response['response'][i]['cases']['total'])
            if response['response'][i]['deaths']['total']:
                td1=int(response['response'][i]['deaths']['total'])
            if response['response'][i]['cases']['active']:
                a1=int(response['response'][i]['cases']['active'])
            if response['response'][i]['cases']['recovered']:
                r1=int(response['response'][i]['cases']['recovered'])
            if response['response'][i]['cases']['new']:
                n1=int(response['response'][i]['cases']['new'][1:])
            break
    if request.method=="POST":
        sel=request.POST['sel']
        for i in range(1,nr):
            if response['response'][i]['country']==sel: 
                t1=int(response['response'][i]['cases']['total'])
                if response['response'][i]['deaths']['total']:
                    td1=int(response['response'][i]['deaths']['total'])
                if response['response'][i]['cases']['active']:
                    a1=int(response['response'][i]['cases']['active'])
                if response['response'][i]['cases']['recovered']:
                    r1=int(response['response'][i]['cases']['recovered'])
                if response['response'][i]['cases']['new']:
                    n1=int(response['response'][i]['cases']['new'][1:])
                break
    t1='{:,.2f}'.format(t1)
    t1=t1[:-3]
    a1='{:,.2f}'.format(a1)
    a1=a1[:-3]
    n1='{:,.2f}'.format(n1)
    n1=n1[:-3]
    r1='{:,.2f}'.format(r1)
    r1=r1[:-3]
    td1='{:,.2f}'.format(td1)
    td1=td1[:-3]
    t='{:,.2f}'.format(t)
    t=t[:-3]
    a='{:,.2f}'.format(a)
    a=a[:-3]
    n='{:,.2f}'.format(n)
    n=n[:-3]
    r='{:,.2f}'.format(r)
    r=r[:-3]
    td='{:,.2f}'.format(td)
    td=td[:-3]
    con={'l':l,'sel':sel,'t':t, 'a':a, 'n':n, 'td':td, 'r':r,'t1':t1, 'a1':a1, 'n1':n1, 'td1':td1, 'r1':r1}
    with open(os.path.join('static', "data.json"),"r+") as json_data:
        json_data.write("{'hello':'hi'}")
    data = json.load(json_data)
    return render(request,'temp.html',con,data)
    
