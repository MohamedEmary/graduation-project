function [x, fx, n, a, b] = falsePos2(f, a, b, eps)
    n = 0;
    while(true)
        n = n + 1;
        
        fa = double(subs(f, a));
        fb = double(subs(f, b));
        
        if fa*fb <0
        
        x = a - (fa*(b-a)) / (fb-fa);
        fx = double(subs(f, x));

        if(abs(fx) <= eps)
            return;
        elseif(fa * fx < 0)
            b = x;
        else
            a = x;
        end
    end
end



