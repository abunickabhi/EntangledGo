#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:59:41 2018

@author: abhi
"""

import numpy as np

a=np.zeros((4,4))
print('Input no. of constraints')
i=input()
k=0
p=0
m=0
while (k<i):
    p=input('input row:')
    m=input ('input column:')
    p=p−1
    m=m−1
    a [p][m] = input ('input element:')
    k=k+1
i =0
k=0
e=np.ones((4, 1))
e=e∗5
b=0
print('Indices of new clues are:')
while (i <4) :
    k=0
    while (k<4) :
            e=np.ones((4 , 1))
            e=e∗5
            b=0
            p=0
            if ( a [i][k] == 0 ) :
                if ( ( i+k)%2==0) :
                    if ( i%2 == 1 ) :
                        while ( b<4) :
                            if ( a[i−1][k−1]==b+1) :
                                a[i] [k]+=e [ b ]
                                e[b]=0
                            b=b+1
                        b=0
                    else:
                        
                    while ( b<4) :
                        if ( a[i +1][k+1]==b+1):
                            a[i][k]+=e [b]
                            e[b]=0
                            b=b+1
                            b=0
                else:
                    if ( i%2 == 1) :
                        while ( b<4) :
                            if (a[i−1][k+1]==b+1):
                                a[i][k]+=e [b]
                                e[b]=0
                            b=b+1
                        b=0
                    else :
                        while( b<4) :
                            if ( a[i+1][k−1]==b+1):
                                a[i][k]+=e [b]
                                e[b]=0
                            b=b+1
                        b=0
                    p=0
                    b=0
                    while (b<4):
                        p=0
                        while (p<4) :
                            if (a[b][k]==p+1):
                                a [i][k]+=e  p]
                                e[p]=0
                            p=p+1
                        b=b+1
                    b=0
                    p=0
                    while(b<4) :
                        p=0
                        while(p<4) :
                            if(a[i][b]==p+1) :
                                a[i][k]+=e[p]
                                e[p]=0
                            p=p+1
                        b=b+1
                    if (a[i][k] == 15) :
                        print (i +1,k+1)
                k=k+1
            i=i+1