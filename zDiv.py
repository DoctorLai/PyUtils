#!/usr/bin/evn python
"""
    High-precision division between two integers
    Algorithm complexity: O(n)
    Space complexity: O(n)
    // acm.zhihua-lai.com
"""

def zDiv(a, b, n):
    if b == 0:
        if a >= 0:
            return "+infinity"
        else:
            return "-infinity"
    elif a == 0:
        return "0"
    else:
        from cStringIO import StringIO
        c = a * b
        file_str = StringIO()            
        if c < 0:
            file_str.write("-")
        a = abs(a)
        b = abs(b)
        c = a / b
        d = a % b
        file_str.write(str(c))        
        if d > 0:
            file_str.write(".")
            for x in xrange(0, n):
                a = d * 10
                c = a / b
                d = a % b
                file_str.write(str(c))
                if d == 0:
                    break
        return file_str.getvalue()

if __name__ == "__main__":
    print "355 / 113 = %s" % zDiv(355, 113, 100)
    print "1 / 0 = %s " % zDiv(1, 0, 100)
    print "-1 / 0 = %s " % zDiv(-1, 0, 100)
    print "0 / (-1) = %s " % zDiv(0, -1, 100)
    print "-22 / 7 = %s " % zDiv(-22, 7, 100)
    print "35 / (-5) = %s " % zDiv(35, -5, 100)
    print "-1 / (-8) = %s " % zDiv(-1, -8, 100)
