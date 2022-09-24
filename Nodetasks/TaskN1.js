var n = prompt('no of words')
const text  = []
var k
for(i =0;i<n;i++)
{
    function func()
    {
         text[i] = document.getElementsByName("words").values   
    }

}
for(i =0;i<n;i++)
{
    function Computation()
    {
        for(j =0;j<n;j++)
        {
            if( text[i] == text[j] && i!=j)
                {
                    continue
                }    
            else{
                k++;
            }
        }
        
        return  k
    }
}
document.getElementById('#ans').innerHTML= Computation