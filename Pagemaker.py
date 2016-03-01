__author__ = 'bnarayanan'


class pagemaker:

    @staticmethod
    def constdata(namer,year=[],percentage=[],rank=[]):

        #GetsAlliancedata of each const

        text82 = '<td><span style="font-size: 10pt;">'
        text87 = '<td><span style="font-size: 10pt;">'
        text91 = '<td><span style="font-size: 10pt;">'
        text96 = '<td><span style="font-size: 10pt;">'
        text01 = '<td><span style="font-size: 10pt;">'
        text06 = '<td><span style="font-size: 10pt;">'
        text11 = '<td><span style="font-size: 10pt;">'



        #5.97|1987|5.0|1991|4.16|2001|6.69|2006|7.3|2011|


        allianceyear = year

        alliancepercentage = percentage

        alliancerank = rank
        #print(ldfyear)

        for q,a,p in zip(allianceyear,alliancepercentage,alliancerank):

         #style="background-color: #9df5c6;"

            #print(q,a)
            if str(q) == "1982":

                if int(p) == 1:
                    text82 = text82.replace('<td>','<td style="background-color: #9df5c6;">')

                text82 = text82 + str(a)

            elif str(q) == "1987":
                if int(p) == 1:
                    text87 = text87.replace('<td>','<td style="background-color: #9df5c6;">')
                text87 = text87 + str(a)

            elif str(q) == "1991":
                if int(p) == 1:
                    text91 = text91.replace('<td>','<td style="background-color: #9df5c6;">')
                text91 = text91 + str(a)

            elif str(q) == "1996":
                if int(p) == 1:
                    text96 = text96.replace('<td>','<td style="background-color: #9df5c6;">')
                text96 = text96 + str(a)

            elif str(q) == "2001":
                if int(p) == 1:
                    text01 = text01.replace('<td>','<td style="background-color: #9df5c6;">')
                text01 = text01 + str(a)

            elif str(q) == "2006":
                if int(p) == 1:
                    text06 = text06.replace('<td>','<td style="background-color: #9df5c6;">')
                text06 = text06 + str(a)

            elif str(q) == "2011":
                if int(p) == 1:
                    text11 = text11.replace('<td>','<td style="background-color: #9df5c6;">')
                text11 = text11 + str(a)

            else:
                print('Something wrong')

        text82 = text82 + '</span></td>'
        text87 = text87 + '</span></td>'
        text91 = text91 + '</span></td>'
        text96 = text96 + '</span></td>'
        text01 = text01 + '</span></td>'
        text06 = text06 + '</span></td>'
        text11 = text11 + '</span></td>'

        if namer == 'LDF':
            textldf = '<td style="background-color: #ff2600;"><span style="font-size: 10pt;">LDF</span></td>'
            texter = textldf + text11 + text06 + text01 + text96 + text91 + text87 + text82

        elif namer =='UDF':
             textudf = '<td style="background-color: #2874ed;"><span style="font-size: 10pt;">UDF</span></td>'
             texter = textudf + text11 + text06 + text01 + text96 + text91 + text87 + text82

        elif namer == 'BJP':
            textbjp = '<td style="background-color: #f5c32f;"><span style="font-size: 10pt;">BJP</span></td>'
            texter = textbjp + text11 + text06 + text01 + text96 + text91 + text87 + text82

        else:

            print('ok')


        return texter


    def tabledata(ldftext, udftext,bjptext, const):

         lb1 = '<br>'
         lb3 = '<br><br><br>'

         str0 = '<h5>Winning Alliance (1982-2011):</h5>' + lb1
         str1 = '<table style="border-color: #e6e6e6;  width: 270px; background-color: #f7f7f7; outline: thin solid;"><tbody><tr><td style="text-align: center;" colspan="8"><strong>'
         str2 = '</strong></td></tr><tr style="background-color: #d7d7d7; outline: thin solid;"><td style="background-color: #f5f5f5;"><span style="font-size: 10pt;">Year</span></td><td style="background-color: #f5f5f5;"><span style="font-size: 10pt;">11</span></td><td style="background-color: #f5f5f5;"><span style="font-size: 10pt;">06</span></td><td style="background-color: #f5f5f5;"><span style="font-size: 10pt;">01</span></td><td style="background-color: #f5f5f5;"><span style="font-size: 10pt;">96</span></td><td style="background-color: #f5f5f5;"><span style="font-size: 10pt;">91</span></td><td style="background-color: #f5f5f5;"><span style="font-size: 10pt;">87</span></td><td style="background-color: #f5f5f5;"><span style="font-size: 10pt;">82</span></td></tr><tr style="height: 8px; outline: thin solid; background-color: #f7f7f7;"><td style="text-align: right; font-size: 6pt;" colspan="8"><em> percentage votes per alliance </em></td>'
         strfiller = '</tr><tr>'
         strender = '</tr></tbody></table>' + lb3

         finalhtml = str0 +str1 + const + str2 + strfiller + ldftext + strfiller + udftext + strfiller + bjptext + strender

         return finalhtml


    def constparty(year=[],percentage=[],rank=[],party=[],alliance =[]):

        text82 = '<td><span style="font-size: 10pt;">'
        text87 = '<td><span style="font-size: 10pt;">'
        text91 = '<td><span style="font-size: 10pt;">'
        text96 = '<td><span style="font-size: 10pt;">'
        text01 = '<td><span style="font-size: 10pt;">'
        text06 = '<td><span style="font-size: 10pt;">'
        text11 = '<td><span style="font-size: 10pt;">'
        text821 = ''
        text822 = ''
        text823 = ''
        text871 = ''
        text872 = ''
        text873 = ''
        text911 = ''
        text912 = ''
        text913 = ''
        text961 = ''
        text962 = ''
        text963 = ''
        text011 = ''
        text012 = ''
        text013 = ''
        text061 = ''
        text062 = ''
        text063 = ''
        text111 = ''
        text112 = ''
        text113 = ''
        perc821= 0
        perc822= 0
        perc823= 0
        perc871= 0
        perc872= 0
        perc873= 0
        perc911= 0
        perc912= 0
        perc913= 0
        perc961= 0
        perc962= 0
        perc963= 0
        perc011= 0
        perc012= 0
        perc013= 0
        perc061= 0
        perc062= 0
        perc063= 0
        perc111= 0
        perc112= 0
        perc113= 0

        margin82 = 0
        margin87 = 0
        margin91 = 0
        margin96 = 0
        margin01 = 0
        margin06 = 0
        margin11 = 0

        allianceyear = year
        alliancepercentage = percentage
        alliancerank = rank
        partyname = party

        texter = ''

        for q,a,p,t in zip(allianceyear,alliancepercentage,alliancerank,partyname):

         #style="background-color: #9df5c6;"

            #print(q,a,p,t)
            if str(q) == "1982":
                text82 = '<tr><td>1982</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text821 = str(t)
                    perc821 = int(a)
                elif int(p)==2:
                    text822 = str(t)
                    perc822 = int(a)
                elif int(p)==3:
                    text823 = str(t)
                    perc823 = int(a)


            elif str(q) == "1987":
                text87 = '<tr><td>1987</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text871 = str(t)
                    perc871 = int(a)
                elif int(p)==2:
                    text872 = str(t)
                    perc872 = int(a)
                elif int(p)==3:
                    text873 = str(t)
                    perc873 = int(a)

            elif str(q) == "1991":
                text91 = '<tr><td>1991</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text911 = str(t)
                    perc911 = int(a)
                elif int(p)==2:
                    text912 = str(t)
                    perc912 = int(a)
                elif int(p)==3:
                    text913 = str(t)
                    perc913 = int(a)

            elif str(q) == "1996":
                text96 = '<tr><td>1996</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text961 = str(t)
                    perc961 = int(a)
                elif int(p)==2:
                    text962 = str(t)
                    perc962 = int(a)
                elif int(p)==3:
                    text963 = str(t)
                    perc963 = int(a)

            elif str(q) == "2001":
                text01 = '<tr><td>2001</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text011 = str(t)
                    perc011 = int(a)
                elif int(p)==2:
                    text012 = str(t)
                    perc012 = int(a)
                elif int(p)==3:
                    text013 = str(t)
                    perc013 = int(a)

            elif str(q) == "2006":
                text06 = '<tr><td>2006</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text061 = str(t)
                    perc061 = int(a)
                elif int(p)==2:
                    text062 = str(t)
                    perc062 = int(a)
                elif int(p)==3:
                    text063 = str(t)
                    perc063 = int(a)

            elif str(q) == "2011":
                text11 = '<tr><td>2011</td><td style="background-color: #9df5c6;">'

                if int(p)== 1:
                    text111 = str(t)
                    perc111 = int(a)
                elif int(p)== 2:
                    text112 = str(t)
                    perc112 = int(a)
                elif int(p)== 3:
                    text113 = str(t)
                    perc113 = int(a)

            else:
                print('Something wrong')

        fil2 = '</td><td>'
        fil3 = '</td></tr>'
        fil4 = '%'
        lb1 = '<br>'
        lb3 = '<br><br><br>'

        margin82 = perc821 - perc822
        margin87 = perc871 - perc872
        margin91 = perc911 - perc912
        margin96 = perc961 - perc962
        margin01 = perc011 - perc012
        margin06 = perc061 - perc062
        margin11 = perc111 - perc112

        tabletop = '<h5>Party Positions (1982-2011):</h5><br><table style="background-color: #f7f7f7;  width: 270px; border-color: #e6e6e6; outline: thin solid;"><tbody><tr style="background-color: #f2f7f7;"><td>YEAR</td><td>WIN</td><td>%</td><td>2ND</td><td>3RD</td></tr>'
        tablemid ='<tr style="height: 8px; outline: thin solid; background-color: #f7f7f7;"><td style="text-align: right; font-size: 6pt;" colspan="5"><em> percentage margin of win</em></td></tr>'
        tableend = '</tbody></table>' + lb3
        texter = tabletop + tablemid + text82 + text821 + fil2 + str(margin82) + fil4 + fil2 + text822 + fil2 + text823 + fil3
        texter = texter + text87 + text871 + fil2 + str(margin87) + fil4  + fil2 + text872 + fil2 + text873 + fil3
        texter = texter + text91 + text911 + fil2 + str(margin91) + fil4  + fil2 + text912 + fil2 + text913 + fil3
        texter = texter + text96 + text961 + fil2 + str(margin96) + fil4  + fil2 + text962 + fil2 + text963 + fil3
        texter = texter + text01 + text011 + fil2 + str(margin01) + fil4  + fil2 + text012 + fil2 + text013 + fil3
        texter = texter + text06 + text061 + fil2 + str(margin06) + fil4  + fil2 + text062 + fil2 + text063 + fil3
        texter = texter + text11 + text111 + fil2 + str(margin11) + fil4  + fil2 + text112 + fil2 + text113 + fil3
        texter = texter + tableend

#9df5c6;

        return texter
    @staticmethod
    def swingandsummary(typer, constname,year =[],cname =[],votes =[],partyname =[], rank =[],swing =[], probability =[]):


        #print(len(year),len(swing), len(rank),len(cname))
        allconstname = constname
        allyear = year
        candname = cname
        candvotes = votes
        candpartyname  = partyname
        candrank = rank
        constswing = swing
        constprob = probability

        summary = ''
        swingmeter = ''

        lb1 = '<br>'
        lb3 = '<br><br>'

        v1 = 0
        v2 = 0
        c1 = ''
        c2 = ''
        p1 = ''
        p2 = ''
        vmargin = ''

        #print(allconstname,allyear,candname,candvotes,candpartyname,candrank,constswing,constprob)


        for y,n,v,p,r,s,b in zip(allyear,candname,candvotes,candpartyname,candrank,constswing,constprob):


            swingmeter = '<h5>Swing Meter:</h5><br><table style="width: 270px; height: 28px; outline: thin solid; font: 10px;"><tbody><tr><td style="text-align: center;">LDF</td><td style="text-align: center;">UDF</td><td style="text-align: center;">SWING</td></tr></tbody></table><br><br>'

            if s == 'LDF':
                swing = ' is a strong LDF constituency.'
                swingmeter = swingmeter.replace('<td style="text-align: center;">LDF</td>','<td style="text-align: center; background-color: #9df5c6;"><strong>LDF</strong></td>')
            elif s == 'UDF':
                swing = ' is a strong UDF constituency.'
                swingmeter = swingmeter.replace('<td style="text-align: center;">UDF</td>','<td style="text-align: center; background-color: #9df5c6;"><strong>UDF</strong></td>')
            elif s == 'BJP':
                swing = ' is a strong BJP play.'
                swingmeter = swingmeter.replace('<td style="text-align: center;">SWING</td>','<td style="text-align: center; background-color: #9df5c6;"><strong>BJP</strong></td>')
            else:
                swing = ' is a swing constituency.'
                swingmeter = swingmeter.replace('<td style="text-align: center;">SWING</td>','<td style="text-align: center; background-color: #9df5c6;"><strong>SWING</strong></td>')





            if int(y) == 2011:

                if int(r) == 1:
                    v1 = int(v)
                    c1 = str(n)
                    p1 = str(p)
                elif int(r) == 2:
                    v2 = int(v)
                    c2 = str(n)
                    p2 = str(p)
            else:
                continue


            vmargin = v1 - v2

            summary = str(constname).title() + swing + ' In 2011,' + str(c1).title() + ' of ' + str(p1).title() + ' defeated ' +  str(c2).title() + ' of ' + str(p2).title() + ' by a margin of ' +str(vmargin) + ' votes.'
            sbegin = lb3+ '<blockquote><h5>Summary:</h5>'+ lb1
            sumender = '</blockquote>'
            summary = sbegin + summary + sumender + lb3

        if typer == 'METER':
            return swingmeter
        elif typer == 'SUMMARY':
            return summary
        else:
            return summary


    def consttables(year=[],percentage=[],rank=[],party=[]):

        text82 = '<td><span style="font-size: 10pt;">'
        text87 = '<td><span style="font-size: 10pt;">'
        text91 = '<td><span style="font-size: 10pt;">'
        text96 = '<td><span style="font-size: 10pt;">'
        text01 = '<td><span style="font-size: 10pt;">'
        text06 = '<td><span style="font-size: 10pt;">'
        text11 = '<td><span style="font-size: 10pt;">'
        text821 = ''
        text822 = ''
        text823 = ''
        text871 = ''
        text872 = ''
        text873 = ''
        text911 = ''
        text912 = ''
        text913 = ''
        text961 = ''
        text962 = ''
        text963 = ''
        text011 = ''
        text012 = ''
        text013 = ''
        text061 = ''
        text062 = ''
        text063 = ''
        text111 = ''
        text112 = ''
        text113 = ''
        perc821= 0
        perc822= 0
        perc823= 0
        perc871= 0
        perc872= 0
        perc873= 0
        perc911= 0
        perc912= 0
        perc913= 0
        perc961= 0
        perc962= 0
        perc963= 0
        perc011= 0
        perc012= 0
        perc013= 0
        perc061= 0
        perc062= 0
        perc063= 0
        perc111= 0
        perc112= 0
        perc113= 0

        margin82 = 0
        margin87 = 0
        margin91 = 0
        margin96 = 0
        margin01 = 0
        margin06 = 0
        margin11 = 0

        allianceyear = year
        alliancepercentage = percentage
        alliancerank = rank
        partyname = party

        texter = ''

        for q,a,p,t in zip(allianceyear,alliancepercentage,alliancerank,partyname):

         #style="background-color: #9df5c6;"

            #print(q,a,p,t)
            if str(q) == "1982":
                text82 = '<tr><td>1982</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text821 = str(t)
                    perc821 = int(a)
                elif int(p)==2:
                    text822 = str(t)
                    perc822 = int(a)
                elif int(p)==3:
                    text823 = str(t)
                    perc823 = int(a)


            elif str(q) == "1987":
                text87 = '<tr><td>1987</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text871 = str(t)
                    perc871 = int(a)
                elif int(p)==2:
                    text872 = str(t)
                    perc872 = int(a)
                elif int(p)==3:
                    text873 = str(t)
                    perc873 = int(a)

            elif str(q) == "1991":
                text91 = '<tr><td>1991</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text911 = str(t)
                    perc911 = int(a)
                elif int(p)==2:
                    text912 = str(t)
                    perc912 = int(a)
                elif int(p)==3:
                    text913 = str(t)
                    perc913 = int(a)

            elif str(q) == "1996":
                text96 = '<tr><td>1996</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text961 = str(t)
                    perc961 = int(a)
                elif int(p)==2:
                    text962 = str(t)
                    perc962 = int(a)
                elif int(p)==3:
                    text963 = str(t)
                    perc963 = int(a)

            elif str(q) == "2001":
                text01 = '<tr><td>2001</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text011 = str(t)
                    perc011 = int(a)
                elif int(p)==2:
                    text012 = str(t)
                    perc012 = int(a)
                elif int(p)==3:
                    text013 = str(t)
                    perc013 = int(a)

            elif str(q) == "2006":
                text06 = '<tr><td>2006</td><td style="background-color: #9df5c6;">'

                if int(p)==1:
                    text061 = str(t)
                    perc061 = int(a)
                elif int(p)==2:
                    text062 = str(t)
                    perc062 = int(a)
                elif int(p)==3:
                    text063 = str(t)
                    perc063 = int(a)

            elif str(q) == "2011":
                text11 = '<tr><td>2011</td><td style="background-color: #9df5c6;">'

                if int(p)== 1:
                    text111 = str(t)
                    perc111 = int(a)
                elif int(p)== 2:
                    text112 = str(t)
                    perc112 = int(a)
                elif int(p)== 3:
                    text113 = str(t)
                    perc113 = int(a)

            else:
                print('Something wrong')

        fil2 = '</td><td>'
        fil3 = '</td></tr>'
        fil4 = '%'
        lb1 = '<br>'
        lb3 = '<br><br><br>'

        margin82 = perc821 - perc822
        margin87 = perc871 - perc872
        margin91 = perc911 - perc912
        margin96 = perc961 - perc962
        margin01 = perc011 - perc012
        margin06 = perc061 - perc062
        margin11 = perc111 - perc112

        tabletop = '<h5>Party Positions (1982-2011):</h5><br><table style="background-color: #f7f7f7;  width: 270px; border-color: #e6e6e6; outline: thin solid;"><tbody><tr style="background-color: #f2f7f7;"><td>YEAR</td><td>WIN</td><td>%</td><td>2ND</td><td>3RD</td></tr>'
        tablemid ='<tr style="height: 8px; outline: thin solid; background-color: #f7f7f7;"><td style="text-align: right; font-size: 6pt;" colspan="5"><em> percentage margin of win</em></td></tr>'
        tableend = '</tbody></table>' + lb3
        texter = tabletop + tablemid + text82 + text821 + fil2 + str(margin82) + fil4 + fil2 + text822 + fil2 + text823 + fil3
        texter = texter + text87 + text871 + fil2 + str(margin87) + fil4  + fil2 + text872 + fil2 + text873 + fil3
        texter = texter + text91 + text911 + fil2 + str(margin91) + fil4  + fil2 + text912 + fil2 + text913 + fil3
        texter = texter + text96 + text961 + fil2 + str(margin96) + fil4  + fil2 + text962 + fil2 + text963 + fil3
        texter = texter + text01 + text011 + fil2 + str(margin01) + fil4  + fil2 + text012 + fil2 + text013 + fil3
        texter = texter + text06 + text061 + fil2 + str(margin06) + fil4  + fil2 + text062 + fil2 + text063 + fil3
        texter = texter + text11 + text111 + fil2 + str(margin11) + fil4  + fil2 + text112 + fil2 + text113 + fil3
        texter = texter + tableend



        return texter







