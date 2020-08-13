from django.shortcuts import render
from pyrebase import pyrebase


config = {
    #add config details
  }

firebase = pyrebase.initialize_app(config)

database = firebase.database()

def index(request):
    db = database.child('schools').child('abc').get().val()
    ret={}
    for i in db["grade1"].keys():
        ret[i]=db["grade1"][i]['highTech']

    print(ret)
    return render(request,'index.html',{'mon_h': ret['monday'], 'tue_h':ret['tuesday'],'wed_h': ret['wednesday'],'thrus_h': ret['thursday'],'fri_h': ret['friday'], 'sat_h': ret['saturday'], 'sun_h': ret['sunday']})

def index2(request):
    db = database.child('schools').child('abc').get().val()
    ret={}
    for i in db["grade1"].keys():
        ret[i]=db["grade1"][i]['lowTech']

    print(ret)
    return render(request,'lowTech.html',{'mon_l': ret['monday'], 'tue_l':ret['tuesday'],'wed_l': ret['wednesday'],'thrus_l': ret['thursday'],'fri_l': ret['friday'], 'sat_l': ret['saturday'], 'sun_l': ret['sunday']})

def update(request):
    from datetime import date
    import calendar

    x=list(map(int,str(date.today()).split('-')))
    y=calendar.day_name[date(x[0],x[1],x[2]).weekday()].lower()
    print(y)
    

    item = y
    def update_sub(tech,item):
        db1 = database.child('schools').child('abc').get().val()

        val1 = db1['grade1'][item][tech]
            
        val = val1 + 1
        db1 = database.child('schools').child('abc').child('grade1').child(item).child(tech).set(val)

        db1 = database.child('schools').child('abc').get().val()
        ret={}
        for i in db1["grade1"].keys():
            ret[i]=db1["grade1"][i][tech]
        print(ret)
        return ret

    tech='highTech'
    ret=update_sub(tech,item)
    return render(request,'temp.html',{'mon_h': ret['monday'], 'tue_h':ret['tuesday'],'wed_h': ret['wednesday'],'thrus_h': ret['thursday'],'fri_h': ret['friday'], 'sat_h': ret['saturday'], 'sun_h': ret['sunday']})

def update1(request):
    from datetime import date
    import calendar

    x=list(map(int,str(date.today()).split('-')))
    y=calendar.day_name[date(x[0],x[1],x[2]).weekday()].lower()
    print(y)
    

    item = y
    def update_sub(tech,item):
        db1 = database.child('schools').child('abc').get().val()

        val1 = db1['grade1'][item][tech]
            
        val = val1 + 1
        db1 = database.child('schools').child('abc').child('grade1').child(item).child(tech).set(val)

        db1 = database.child('schools').child('abc').get().val()
        ret={}
        for i in db1["grade1"].keys():
            ret[i]=db1["grade1"][i][tech]
        print(ret)
        return ret

    tech='highTech'
    ret=update_sub(tech,item)
    return render(request,'temp1.html',{'mon_h': ret['monday'], 'tue_h':ret['tuesday'],'wed_h': ret['wednesday'],'thrus_h': ret['thursday'],'fri_h': ret['friday'], 'sat_h': ret['saturday'], 'sun_h': ret['sunday']})


def update2(request):
    from datetime import date
    import calendar

    x=list(map(int,str(date.today()).split('-')))
    y=calendar.day_name[date(x[0],x[1],x[2]).weekday()].lower()
    print(y)
    

    item = y
    def update_sub(tech,item):
        db1 = database.child('schools').child('abc').get().val()

        val1 = db1['grade1'][item][tech]
            
        val = val1 + 1
        db1 = database.child('schools').child('abc').child('grade1').child(item).child(tech).set(val)

        db1 = database.child('schools').child('abc').get().val()
        ret={}
        for i in db1["grade1"].keys():
            ret[i]=db1["grade1"][i][tech]
        print(ret)
        return ret

    tech='lowTech'
    ret=update_sub(tech,item)
    return render(request,'temp2.html',{'mon_l': ret['monday'], 'tue_l':ret['tuesday'],'wed_l': ret['wednesday'],'thrus_l': ret['thursday'],'fri_l': ret['friday'], 'sat_l': ret['saturday'], 'sun_l': ret['sunday']})

def update3(request):
    from datetime import date
    import calendar

    x=list(map(int,str(date.today()).split('-')))
    y=calendar.day_name[date(x[0],x[1],x[2]).weekday()].lower()
    print(y)
    

    item = y
    def update_sub(tech,item):
        db1 = database.child('schools').child('abc').get().val()

        val1 = db1['grade1'][item][tech]
            
        val = val1 + 1
        db1 = database.child('schools').child('abc').child('grade1').child(item).child(tech).set(val)

        db1 = database.child('schools').child('abc').get().val()
        ret={}
        for i in db1["grade1"].keys():
            ret[i]=db1["grade1"][i][tech]
        print(ret)
        return ret

    
    tech='lowTech'
    ret=update_sub(tech,item)
    return render(request,'temp3.html',{'mon_l': ret['monday'], 'tue_l':ret['tuesday'],'wed_l': ret['wednesday'],'thrus_l': ret['thursday'],'fri_l': ret['friday'], 'sat_l': ret['saturday'], 'sun_l': ret['sunday']})

    # else:
    #     tech=j
    #     ret=update_sub(tech,item)
    #     return render(request,'temp.html',{'mon_h': ret['monday'], 'tue_h':ret['tuesday'],'thrus_h': ret['thursday']})

