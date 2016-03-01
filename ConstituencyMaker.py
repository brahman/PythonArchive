__author__ = 'bnarayanan'

import csv
import Pagemaker
import CSVMaker

#ID	Const No	Const Name	Candidate Name	Party	Votes 	Percentage	Year	Electorate	Vote Polled	District
n = 0
constno = 0
y = 0
constname = []
ldf = ''


constreader =csv.DictReader(open('const.csv'))


for item in constreader:
    constname = []
    csvreader = csv.DictReader(open('candidates2.csv'))

    name = str(item['Const'])
    #print(name)
    ldf = ''
    udf = ''
    bjp = ''
    other = ''

    ldfpercentage =[]
    ldfyear =[]
    ldfrank = []
    udfpercentage =[]
    udfyear =[]
    udfrank = []
    bjppercentage =[]
    bjpyear =[]
    bjprank = []

    allpercentage = []
    allyear = []
    allrank = []
    allparty = []
    allvotes = []
    allcandidates = []
    allpartyname = []
    allswing = []
    allprob = []
    alliance = []



    for row in csvreader:

        if str(row['Const Name'])== name:

            if str(row['Alliance']) == 'LDF':

                ldfpercentage.append(int(round(float(row['Percentage']))))
                ldfyear.append(int(row['Year']))
                ldfrank.append(int(row['Rank']))

            elif str(row['Alliance']) == 'UDF':

                udfpercentage.append(int(round(float(row['Percentage']))))
                udfyear.append(int(row['Year']))
                udfrank.append(int(row['Rank']))
            elif str(row['Alliance']) == 'BJP':

                bjppercentage.append(int(round(float(row['Percentage']))))
                bjpyear.append(int(row['Year']))
                bjprank.append(int(row['Rank']))
            elif str(row['Alliance']) == 'OTH':
                other = str(row['Percentage']) + "|" + str(row['Year']) + "|" + other
            else:
                print("ERAAAAAAARAAAAR")


        if str(row['Const Name'])==name:
        #print only 3 parties

            alliance.append(str(row['Alliance']))
            allparty.append(str(row['Party']))
            allpercentage.append(int(round(float(row['Percentage']))))
            allyear.append(int(row['Year']))
            allrank.append(int(row['Rank']))
            allvotes.append(int(row['Votes']))
            allcandidates.append(str(row['Candidate Name']))
            allpartyname.append(str(row['Part Name']))
            allswing.append(str(row['Swing']))
            allprob.append(int(row['Prob']))





 #ID	Const No	Const Name	Rank	Candidate Name	Party	Votes 	Percentage	Year	Electorate	Vote Polled	District	Part Name	Alliance	Swing	Prob



    # ldftext = Pagemaker.pagemaker.constdata('LDF',ldfyear,ldfpercentage,ldfrank)
    # udftext = Pagemaker.pagemaker.constdata('UDF',udfyear,udfpercentage,udfrank)
    # bjptext = Pagemaker.pagemaker.constdata('BJP',bjpyear,bjppercentage,bjprank)
    #
    # consttables = Pagemaker.pagemaker.tabledata(ldftext,udftext,bjptext,name)
    #
    # constpartytable = Pagemaker.pagemaker.constparty(allyear,allpercentage,allrank,allparty)

    swingmeter = Pagemaker.pagemaker.swingandsummary("METER",name,allyear,allcandidates,allvotes,allpartyname,allrank,allswing,allprob)

    summary = Pagemaker.pagemaker.swingandsummary("SUMMARY",name,allyear,allcandidates,allvotes,allpartyname,allrank,allswing,allprob)


    if name == 'ALUVA':


        # print(swingmeter)
        # print(summary)
        # print(consttables)
        # print(constpartytable)
        #print('OK')
        content = swingmeter + summary + consttables + constpartytable
        print(content)
        # title = name
        # url = name+'-'+'assembly-constituency'
    #CSVMaker.pagemaker.makecsvconstituency(1,title,content,url)




















































