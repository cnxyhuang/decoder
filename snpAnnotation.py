import os
import urllib2
import HTMLParser
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import xlwt
import xlrd
#def geneAnnotions():

infile=open("C:\Users\Sanger\Desktop\share\geneannotion.txt")

workbook = xlrd.open_workbook("C:\Users\Sanger\Desktop\share\CVD_DatabasegeneAnnotion.xls")

outfile = open("geneannotion.txt2","w")
#	outfile = open("CVD_DatabasegeneAnnotion.xls2","w")

geneName_list =[]
moxingjieshuo = infile.readline()
#	print line
for moxingjieshuo_jibing in moxingjieshuo:
#	juzhi = moxingjieshuo_jibing.split('')
#	for i in juzhi:
#		print i+"\n"
		print "_______________"
'''
	for item in juzhi:
		item = item.split("\t")
		geneName = item.split("(")[1].split(")")[0]
		if geneName not in geneName_list:
			geneName_list.append(geneName)
		#	return geneName+"\t"+item
		#	print geneAnnotion()
			print geneName+"\t"+item
			outfile.write(geneName+"\t"+item+"\n")
		outfile.close()

def rsAnnotions():
#-*- coding: utf-8 -*- 
#Can find magnitugude but not cites 1113,Update
#print urllib2.urlopen("http://www.snpedia.com/index.php/Blood_pressure").read()

#infile=open(sys.argv[1])
#outfile=open(sys.argv[2],"w")
	infile=open("Cancers.txt")
	outfile=open("Cancers.xls","w")

	for rs in infile:
		rs=rs.split("\t")[0].strip()
		web="http://www.snpedia.com/index.php/"+rs
		listx=['type 2 diabetes','typediabetes','diabetes','t2dm','diabetesmellitus','t2d','mellitus','typediabetesmellitus','t1d','t1dm','diabetesmellitus,type1','diabetesmellitus,type2','tcf7l2','mody','diabetesinsipidus','diabetesrisk','diabetespatients','maturity-onsetdiabetes','maturity-onset','diabetessusceptibility','non-insulin-dependentdiabetes','mellitust2dm','non-insulin-dependent','diabetest1d','diabeticsubjects','typediabetic','insulin-dependentdiabetes','diabeticpatients','diabetic','diabetesobjective','typediabeticpatients','diabeticangiopathies','diabetest2d','hemoglobina,glycosylated','hypertensiondiabetes','aimshypothesis','typediabetesmellitust2dm','diabeticnephropathies','youngmody','diabetesmethods','typediabetest1d']	
		try:
			allinfo=urllib2.urlopen(web).read()		
		except Exception, e:
			outfile.write(rs+"\t"+str(e)+"\n")
			print rs+"\t"+str(e)
		if len(allinfo.split('</table>')) >13:
			allinfo=allinfo.split('</table>')[12]
		#print str(allinfo)+"\n"
		#print "----------------------"
			allinfo2=allinfo.split('</p><p>')
			for item in allinfo2:
			#print item
			#print "++++++++++++++++++++++++++++++++"
				for x in listx:
					if x in item:
						try:
							PMID= item.split('PMID ')[1].split('</a>')[0]
							try:
								OR=item.split('OR')[1]
							except:
								OR=item.split('odds ratio')[1]
							print x+"\t"+PMID+"\t"+rs+OR
						except IndexError:
							pass	
		else:
		#allinfo=allinfo.split('</table>')[12].split('</div><div class')
		#print str(allinfo)+"\n"
			print "no cites there"+rs
