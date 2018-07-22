# 함수는 여기까지만
a = 10
def test():
    # 함수 안에서만 존재
    a = 11
test()
# 전역에 위치한 a를 의미함
print( a )
def sum(a, b):
    return a+b
#=======================================
def a1( x ):return x+"A"
def a2( x ):return x+"B"
def a3( x ):return x+"C"
def a4( x ):return x+"D"
a = a1( '' )
b = a2( a )
c = a3( b )
d = a4( c )
print( d )
print( a4( a3( a2( a1( '' ) ) ) ) )
# >> ABCD
