function [x, fx, n, a, b] = bisection(f, a, b, eps)
    n = 0;
    while(true)
        n = n + 1;
        x = (a + b) / 2;
        fx = double(subs(f, x));
        fa = double(subs(f, a));

        if(abs(fx) <= eps)
            return;
        elseif(fa * fx < 0)
            b = x;
        else
            a = x;
        end
    end
end

