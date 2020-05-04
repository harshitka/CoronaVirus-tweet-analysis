# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## HARSHIT KANOJIA 2017053

import tweepy,time
import json,random
auth=tweepy.OAuthHandler('gLwL4mg8jutKeK7xa1bqFrBIw','zBQnYhwgG2o2x8BRcMASqyiJIDSOzpJX2LBiimvJK1tDnE3plh')
auth.set_access_token('1886713100-JtgVHKKsui8O6uHL2tdXEwwenplAibxorlH1b29','Qo1ujZj0DduKqoSnqXfkfYU56w8w5ZVp3oMw6PAeUEMyf')
api = tweepy.API(auth)
count=0
list=[]
api = tweepy.API(auth, wait_on_rate_limit=True)
list2=[]       
list1=[]
occur=[]
length=[]
flag=[]

class length:
        def __init__(self,l):
            self.l=l


class MyStreamListener(tweepy.StreamListener):
        
        
        def on_raw_data(self, raw_data):
                print("raw_data:")
                print(raw_data.text)
                return True

        def on_data(self, raw_data):
                if((time.time()-starttime)<20):

                        id=raw_data[52:71]
                        y = json.loads(raw_data)
                        reservoir(y)
                       
                else:
                        datashow(raw_data)
                        return False
            
        def on_error(self, raw_data_code):
                if raw_data_code == 420:
                        return False

def reservoir(y):
         try:
                size.l=size.l+1
                if(len(list)<1000):
                        
                         id=y["user"]["id"]
                         list.append((id))
                         occur.append(0)
                         count(id)
                         
                else:
                         z=len(list)
                         h=len(list)
                         x=random.randint(0,h)
                         id=y["user"]["id"]
                         if(x<z):
                                 list[x]=id
                                 occur[x]=0
                                 count(list[x])
                         h=h+1

         except KeyError:
                 pass

def count(h):
    for i in range(len(list)):
       if(list[i]==h):
           occur[i]=occur[i]+1



def datashow(raw_data):
                if(len(flag)<1):
                        print("\nlength:",(size.l))
                        ASM()
                        count=0
                        print("2nd moment:",moment1.m/len(list))
                        flag.append(0)
                return True

class moment:
        def __init__(self,m):
            self.m=m
            

        
class Variable:
        def __init__(self,element,value):
                self.element=element
                self.value=value



def ASM():
        for o in range(len(list)):
                x1=random.randint(0,len(list)-1)
                moment=size.l*((2*occur[x1])-1)
                moment1.m=moment1.m+moment
        return True

                
        
        
if __name__ == "__main__":
        size=length(0)
        moment1=moment(0)
        myStreamListener = MyStreamListener()
        starttime = time.time()
        myStream = tweepy.Stream(auth,myStreamListener)
        while True:
                try:
                        myStream.filter(track=["#corona","covid","#COVID-19","#Coronavirus"])
                except:
                        continue
