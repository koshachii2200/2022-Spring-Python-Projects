#  File: DNA.py

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.


def main():
# read the data
# make s1 and s2 DNA pairs from the data

  m=int(input())
  for y in range(0,m):
    str1=input()
    str2=input()
    longest_subsequence(str1,str2)

def longest_subsequence(s1,s2):
  listSubs=[]
  for x in range(len(s1)):
    for y in range(x+1,len(s1)+1):
      if(s1[x:y+1] in s2):listSubs.append(s1[x:y+1])

  if(len(listSubs)>0)and(len(max(listSubs,key=len))>1):
    longest=len(max(listSubs,key=len))
    longSubs=[]
    for i in range(len(listSubs)):
       if(len(listSubs[i])==longest):longSubs.append(listSubs[i])
    longSubs=list(set(longSubs))
    longSubs.sort()
    print(*longSubs,sep="\n")
  else:print("No Common Sequence Found")
  print()

main()