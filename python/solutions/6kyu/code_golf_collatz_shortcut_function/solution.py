"""https://www.codewars.com/kata/664bb069388167b5923b1688"""


g=lambda n:((1+2*(n%2))*n+1)//2
g=lambda n:[n/2,(3*n+1)/2][n%2]
g=lambda n:(n+1)//2+(n&1)*n
g=lambda n:(n+1>>1)+n%2*n
g=lambda n:n+(n&1)*(n>>1)
g=lambda n:n-n//2+n%2*n
