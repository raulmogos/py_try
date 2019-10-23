
def computeLSP(pat, lsp):
    k = 0
    p = list(pat)
    for i in range(1,len(pat)):
        if p[i] == p[k]:
            lsp[i] = k+1
            k+=1
        else:
            lsp[k] = lsp[i]

def kmp(txt, pat):
    lsp = [0 for i in range(len(pat))]
    computeLSP(pat, lsp)

    print(lsp)

    t = 0
    p = 0
    while t<len(txt):
        '''
        print(str(t))
        print(str(p))
        print()
        '''
        if p == len(pat):
            print('found at ', str(t-p))
            p = lsp[p - 1]
        if txt[t] == pat[p]:
            p+=1
            t+=1
        else:
            # there is a mismatch
            if p!=0:
                p = lsp[p - 1]
            else:
                t+=1




txt = 'AAAAABAAABA'
pat = 'AAAA'

kmp(txt, pat)
