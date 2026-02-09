#student enrollment manager
print ("251A018 , 9/2/26" )
CET={"251A018","251A019", "251A032" }
JEE={"251A018", "251A050", "251A032" }
NEET= {"251A022", "251A024", "251A002"}
print (CET | JEE | NEET) #total students
print ("Total students appeared in the exams:", CET | JEE | NEET)
#total no.of students
print ("Total students appeared in all exams:", CET&JEE&NEET)
print ("Total students appeared only in cet and neet exams:", (CET&JEE) -NEET)
print ("Total students appeared only in cet and neet exams:", (CET&NEET) -JEE)
print (CET|JEE) # total students appeared in cet and tee #either cet or jee but not both
print (CET | JEE)
#students appeared in both cet and jee
print (CET-JEE)
