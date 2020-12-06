#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
while(t--)
{
string s;
cin>>s;
int m=s.size(),i,n=0;
for(i=0;i<m-1;i++)
{
if(s[i]==s[i+1])
{
n++;
s.erase(s.begin()+i);
s.erase(s.begin()+i);
i=-1;
m=m-2;
}
}
cout<<n<<endl;
}
return 0;
}
