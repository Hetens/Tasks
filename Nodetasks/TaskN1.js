var n = prompt("enter number of words")
var c =0
let k =1
const text=[]
const occ =[]
for(i =0;i<n;i++)
{
    text[i] =prompt("enter word")
    
}
console.log(text)

for(i=0;i<n;i++)
{
    for(j =i;j<n;j++)
    {
        if(text[i]==text[j]&&i!=j)
        {
            c++;
            occ[i]= c+1;
        }
        else {  
            occ[i]=k;
        }
    }
}
c =n-c
console.log(c)

console.log(occ)