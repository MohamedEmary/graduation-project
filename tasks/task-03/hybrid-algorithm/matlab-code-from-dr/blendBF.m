function [x, fx, n, a, b] = blendBF(f, a, b, eps)
    n = 0;
    a1 = a;
    a2 = a;
    b1 = b;
    b2 = b;
    
    while(true)
        n = n + 1;
        fa = double(subs(f, a));
        fb = double(subs(f, b));
        
        xB = (a + b) / 2;
        fxB = double(subs(f, xB));
        
        xF = a - (fa*(b-a)) / (fb-fa);
        fxF = double(subs(f, xF));
        
        if abs(fxB) < abs(fxF)
            x = xB;
            fx = fxB;
        else
            x = xF;
            fx = fxF;
        end
        
        if(abs(fx) <= eps)
            return;
        end
        
        if fa*fxB < 0
            b1 = xB;
        else
            a1 = xB;
        end
        
        if fa*fxF < 0
            b2 = xF;
        else
            a2 = xF;
        end
        
        a = max(a1, a2);
        b = min(b1, b2);
    end
end