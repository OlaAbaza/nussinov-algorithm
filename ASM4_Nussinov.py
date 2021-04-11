def delta(l,m):
 delta=0;
 if l=='A' and m=='U':
  return 1;
 elif l=='U' and m=='A':
  return 1;
 elif l=='G' and m=='C':
  return 1;
 elif l=='C' and m=='G':
  return 1;
 elif l=='U' and m=='G':
  return 1;
 elif l=='G' and m=='U':
  return 1;
 else:
  return 0;
def buildDP(seq,L,s):
 for n in range(1,L):
  for j in range(n,L):
   i=j-n;
   case1=s[i+1][j-1]+delta(seq[i],seq[j]);
   case2=s[i+1][j];
   case3=s[i][j-1];
   if i+3<=j:
    tmp=[];
    for k in range(i+1,j):
     tmp.append(s[i][k]+s[k+1][j]);
    case4=max(tmp);
    s[i][j]=max(case1,case2,case3,case4);
   else:
    s[i][j]=max(case1,case2,case3);
    
 return s;
def traceback(s,seq,i,j,pair):
 if i<j:
  if s[i][j]==s[i+1][j]:
   traceback(s,seq,i+1,j,pair);
  elif s[i][j]==s[i][j-1]:
   traceback(s,seq,i,j-1,pair);
  elif s[i][j]==s[i+1][j-1]+delta(seq[i],seq[j]):
   pair.append([i,j]);
   traceback(s,seq,i+1,j-1,pair);
  else:
   for k in range(i+1,j):
    if s[i][j]==s[i][k]+s[k+1][j]:
     traceback(s,seq,i,k,pair);
     traceback(s,seq,k+1,j,pair);
     break;
 return pair;
def write_structure(sequence, structure):
    dot_bracket = ["." for _ in range(len(sequence))]
    for s in structure:
        dot_bracket[min(s)] = "("
        dot_bracket[max(s)] = ")"
    return "".join(dot_bracket)
#Main Function Calling
DNASeqs = input("Enter DNA Sequences: ")
k=len(DNASeqs)
Matrix = [[0 for x in range(k)] for y in range(k)] 
for i in range(0,k,1):
	    Matrix[i][i] = 0
for i in range(1,k,1):
	    Matrix[i][i-1] = 0

Matrix = buildDP(DNASeqs,k,Matrix)
p=traceback(Matrix,DNASeqs,0,k-1,[])
c=write_structure(Matrix, p)
print(c)


