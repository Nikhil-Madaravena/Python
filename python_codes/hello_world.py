output=
a=1
letter = 'a'
while output!='helloworld':
    for output[a] in range(ord('a'),ord('z')+1):
        print(output[a])
        if output[a]=='h':
            a+=1
