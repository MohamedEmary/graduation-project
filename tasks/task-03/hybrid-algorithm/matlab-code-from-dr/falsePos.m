function [x, fx, n, a, b] = falsePos(f, a, b, eps)
    n = 0;
    while(true)
        n = n + 1;
        
        fa = double(subs(f, a));
        fb = double(subs(f, b));
        
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



