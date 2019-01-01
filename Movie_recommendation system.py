import math
data={'RD':{'Good':3,'BAN':3.25,'AVSR':3,'2.0':3,'VBVR':1.25},'TOI':{'Good':4,'BAN':3.5,'AVSR':3.5,'2.0':3,'VBVR':2},'IMDB':{'Good':3.95,'BAN':4.05,'AVSR':4.2,'2.0':3.6,'VBVR':3.75},'THI':{'Good':3,'BAN':3.5,'AVSR':3,'2.0':3.25,'VBVR':2},'GA':{'Good':3,'BAN':3.25,'AVSR':3,'2.0':3.25,'VBVR':1.5},'AG':{'AVSR':3,'VBVR':3.5}}
def similarity(prefs,per1,per2):
    si={}
    for item in prefs[per1]:
        if item in prefs[per2]:
            si[item]=1
    if len(si)==0:
        return 0
    else:
        sos=sum([pow((prefs[per1][item]-prefs[per2][item]),2) for item in si])
        return 1/(1+sos)
sim_rd=similarity(data,'RD','AG')
sim_toi=similarity(data,'TOI','AG')
sim_imdb=similarity(data,'IMDB','AG')
sim_thi=similarity(data,'THI','AG')
sim_ga=similarity(data,'GA','AG')
#print(sim_rd)
#print(sim_toi)
#print(sim_imdb)
#print(sim_thi)
#print(sim_ga)
def getRecommendations(prefs,person,similarity=similarity):
    totals={}
    simSums={} 
    for other in prefs:
        if other==person:
            continue
        sim=similarity(prefs,person,other)
        if sim<=0:
            continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings=[(total/simSums[item],item) for item,total in totals.items( )]
    rankings.sort( )
    rankings.reverse()
    return rankings

getRecommendations(data,'AG')
similarity(data,'AG','RD')
#WE CAN USE THIS PART TO KNOW OUR RATING OF MOVIE,GIVEN OTHERS
#a=float(input("Enter rating of Rating Dada:"))
#b=float(input("Enter rating of Times of India:"))
#c=float(input("Enter rating of IMDB:"))
#d=float(input("Enter rating of The Hans India:"))
#e=float(input("Enter rating of Great Andhra:"))
#rating_score=(sim_rd*a)+(sim_toi*b)+(sim_imdb*(c/2))+(sim_thi*d)+(sim_ga*e)
#sim_score=sim_rd+sim_toi+sim_imdb+sim_thi+sim_ga
#Your_Rating_for_Movie=rating_score/sim_score
#print("Your Rating is:"+str(Your_Rating_for_Movie))
