max_size = len(bin(32)[2:])
for i in range(32):
    bin_str = bin(i)[2:]
    req = max_size - len(bin_str)
    ans = ''
    for j in range(req):
        ans+='0'
    ans+=bin_str
    print(ans)