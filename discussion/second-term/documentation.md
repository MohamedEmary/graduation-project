<!-- ---
title: \begin{title}\centering\vspace*{1cm}\rule{\textwidth}{0.05cm}\linebreak\vspace{0.5cm}{\huge\bfseries Messaging Web Application Using High-Speed Encryption Algorithm with Polynomial Roots \par}\vspace{0.1cm}\hrule\end{title}
date: February 12, 2024
abstract: Encryption algorithms play a critical role in protecting sensitive data in the digital age. However, traditional symmetric encryption methods like AES suffer from high computational complexity that hinders performance. Our project proposes a novel polynomial interpolation based encryption algorithm that aims to accelerate encryption and decryption speeds. The algorithm leverages polynomials generated from secret keys. It then uses an efficient hybrid root finding technique called HybridBF to encode messages into ciphertext roots and decode them back to plaintext. Extensive testing on 1000 sample plaintext-key pairs shows the new algorithm is significantly faster than AES for both encryption and decryption. The hybrid root finder combines aspects of bisection and false position methods, demonstrating faster convergence than either individual technique. By exploiting polynomials and highly optimized root finding, this project delivers an encryption algorithm with superior efficiency while maintaining security. The improved performance could enable broader adoption of strong encryption across communication networks and data storage systems. \pagebreak
--- -->

\pagebreak

\begin{center}
\section{\textit{Chapter One: Introduction}}
\end{center}

## Introduction

The ever-evolving landscape of cyber threats demands constant innovation in the field of cryptography. Existing encryption algorithms, while providing valuable protection, are often riddled with limitations. Computational complexity can hinder performance, and the rise of quantum computing casts a shadow on the future of established methods. This project presents a groundbreaking departure from tradition, introducing a novel encryption algorithm that leverages the potent combination of polynomials and root finding methods.

This paper delves into the intricate details of the algorithm, meticulously explaining each step of the encryption and decryption processes. We provide a comprehensive analysis of its performance, Comparing it with established methods such as AES, showcasing its significant speed advantage.

## Problem & Project Aim

Encryption, regardless of its application, inevitably requires some processing time. This could be for file encryption on a disk or network encryption via a VPN. The extent of this slowdown is contingent on the encryption algorithms employed and, crucially, the proficiency of the programmer who crafted the encryption and decryption code.

Algorithms with high computational complexity can become performance bottlenecks, particularly for systems necessitating real-time data encryption and decryption. This can adversely affect real-time applications such as video conferencing, secure voice calls, or high-speed data transfers. The processing delays induced by encryption can result in lag, disruptions, and a bad user experience.

The aim of this project is to develop a high-speed encryption algorithm that can be used for real-time applications. The algorithm should be able to encrypt and decrypt data at a much faster rate than traditional encryption algorithms, then it will be used to encrypt and decrypt data in real-time messaging web application.

\pagebreak

\begin{center}
\section{\textit{Chapter Two: Numerical Methods}}
\end{center}

## Root Finding Methods

At the heart of our innovative encryption algorithm lies a powerful mathematical tool: root finding methods. These methods, while seemingly abstract, play a crucial role in ensuring the security and efficiency of our solution. But before we delve into their specific application, let's unpack what they are and why they hold such significance.

In essence, root finding methods aim to solve the equation $f(x) = 0$, where $f(x)$ is any function. They essentially seek the "roots" of the function, which are the values of $x$ that make the function evaluate to zero. This seemingly simple task becomes incredibly powerful in cryptography.

In our algorithm, we leverage this power by strategically designing the function $f(x)$ to incorporate the encryption key as an unknown variable. Through carefully chosen root finding methods, we iteratively approach the function's roots, and in the decryption process, utilize these roots to recover the original data. The elegance of this approach lies in its inherent security: without knowledge of both the root finding method and how the key is embedded within the function, an attacker would face a near-impossible task of finding the correct roots, keeping your data safe.

However, the importance of root finding methods extends far beyond encryption. They have diverse applications across various fields. In numerical analysis, they are used for solving differential equations and optimization problems among other things. In engineering design, they are crucial for calculating parameters in fields like fluid dynamics and structural analysis. In computer graphics, they are essential for generating realistic images and animations.

Root finding algorithms also have a significant role in machine learning. They are utilized in optimization methods like gradient descent, which is a common technique for training models. The goal of these methods is to minimize a loss function, thereby improving the model's accuracy.

They also have a vital role in economics and finance. They are used to calculate internal rates of return, solve equilibrium equations in economic models, and find optimal investment strategies.

And finally, we will be using root finding methods to solve the polynomial equations that we will be using in our encryption algorithm.

## Bisection Method

The Bisection Method is a straightforward and reliable numerical method used for solving equations in mathematics, particularly in the field of engineering. It solves equations by repeatedly bisecting an interval and then selecting a subinterval in which a root must lie for further processing.

### How Does the Bisection Method Work?

If we have a function $f(x)$ that is continuous on the interval $[a, b]$ and $f(a) \cdot f(b) < 0$ (the signals of $f(x)$ at the ends $a$ and $b$ are different), then the function has at least one root in the interval $[a, b]$. The Bisection Method works by repeatedly bisecting the interval and then selecting a subinterval in which a root must lie for further processing. The value of $x$ at the midpoint of the interval is equal to $\frac{a+b}{2}$, if $f(\frac{a+b}{2}) = 0$, then $\frac{a+b}{2}$ is the root of the equation. If $f(a) \cdot f(\frac{a+b}{2}) < 0$, then the root lies in the interval $[a, \frac{a+b}{2}]$, and if $f(\frac{a+b}{2}) \cdot f(b) < 0$, then the root lies in the interval $[\frac{a+b}{2}, b]$. This process is repeated until we reach the desired accuracy.

The number of iterations required to reach the desired accuracy can be calculated using the formula:

$$n = \lceil\log_2(\frac{b-a}{\epsilon})\rceil$$

Where $n$ is the number of iterations, $a$ and $b$ are the lower and upper bounds of the interval, and $\epsilon$ is the desired accuracy.

The accuracy of the Bisection Method can be calculated using the formula:

$$\epsilon = \frac{b-a}{2^{n}}$$

### Bisection Method Advantages

There are several key advantages to the bisection method:

- Guaranteed convergence. The bracketing approach is known as the bisection method, and it is always convergent.

- Errors can be managed. Increasing the number of iterations in the bisection method always results in a more accurate root.

- Doesn't demand complicated calculations. There are no complicated calculations required when using the bisection method. To use the bisection method, we only need to take the average of two values.

- The bisection method is simple and straightforward to programme on a computer.

- In the case of several roots, the bisection procedure is quick.

### Bisection Method Disadvantages

There are also some limitations to the bisection method:

- Although the Bisection method's convergence is guaranteed, it is often slow.

- Choosing a guess that is close to the root may necessitate numerous iterations to converge.

- Some equations' roots cannot be found. Because there are no bracketing values, like $f(x) = x^2$.

- Its rate of convergence is linear.

- It is incapable of determining complex roots.

- If the guess interval contains discontinuities, it cannot be used.

- It cannot be applied over an interval where the function returns values of the same sign.

## False Position Method

In mathematics, the regula falsi, method of false position, or false position method is a very old method for solving an equation with one unknown; this method, in modified form, is still in use. In simple terms, the method is the trial and error technique of using test ("false") values for the variable and then adjusting the test value according to the outcome. This is sometimes also referred to as "guess and check". Versions of the method predate the advent of algebra and the use of equations.

### How Does the False Position Method Work?

If we have a function $f(x)$ that is continuous on the interval $[a, b]$ and $f(a) \cdot f(b) < 0$ (the signals of $f(x)$ at the ends $a$ and $b$ are different), then the function has at least one root in the interval $[a, b]$.

The interval $[a, b]$ have different signs. The false position method uses two endpoints of the interval $[a, b]$ with initial values $\left(r_{0}=a, r_{1}=b\right)$. The connecting line between the two points $\left(r_{0}, f\left(r_{0}\right)\right)$ and $\left(r_{1}, f\left(r_{1}\right)\right)$ intersects the $x$-axis at the next estimate, $r_{2}$. Now, we can determine the successive estimates, $r_{n}$ from the following relationship:

$$
r_{n}=r_{n-1}-\frac{f\left(r_{n-1}\right)\left(r_{n-1}-r_{n-2}\right)}{f\left(r_{n-1}\right)-f\left(r_{n-2}\right)}
$$

### False Position Method Advantages

There are several key advantages to the false position method:

- Convergence is guarenteed: this method is bracketing method and it is always convergent.

- Error can be controlled: increasing number of iteration always yields more accurate root.

- Does not require derivative: this method does not require derivative calculation.

### False Position Method Disadvantages

There are also some limitations to the false position method:

- Slow Rate of Convergence: Although convergence of Regula Falsi method is guaranteed, it is generally slow.

- Can not find root of some equations. For example: $f(x) = x^2$ as there are no bracketing values.

- It has linear rate of convergence.

- It fails to determine complex roots.

- It can not be applied if there are discontinuities in the guess interval.

- It can not be applied over an interval where the function takes values of the same sign.

## Secant Method

In numerical analysis, the secant method is a root-finding algorithm that uses a sequence of roots of secant lines to better approximate a root of a function $f$. Unlike the method of false position, which keeps one endpoint fixed, the secant method uses two moving points. The secant method can be thought of as a finite-difference approximation of Newton's method. However, the method was developed independently of Newton's method and predates it by many years.

### How Does the Secant Method Work?

The secant method begins with two initial approximations $x_0$ and $x_1$ for the root. These points should ideally be close to the actual root. The method then uses the secant line through the points $\left(x_0, f(x_0)\right)$ and $\left(x_1, f(x_1)\right)$ to obtain a new approximation $x_2$, which is the x-intercept of this line. The formula for the new approximation is:

$$
x_{n} = x_{n-1} - f(x_{n-1})\frac{x_{n-1} - x_{n-2}}{f(x_{n-1}) - f(x_{n-2})}
$$

This process is repeated until the difference between successive approximations is less than a predetermined tolerance level.

### Secant Method Advantages

The secant method has several advantages:

- **Efficiency**: It typically converges faster than the method of false position and bisection method.

- **Simplicity**: It does not require the function's derivative, unlike Newton's method.

- **Flexibility**: It can handle a wide range of functions.

### Secant Method Disadvantages

However, the secant method also has its disadvantages:

- **Convergence is not guaranteed**: If the initial guesses are not close to the actual root, the method may fail to converge.

- **Sensitive to initial guesses**: The closer the initial guesses to the root, the faster the convergence.

- **Possibility of divergence**: If the function is not well-behaved, the secant method can diverge.

- **Multiple roots**: The method may have difficulty distinguishing between multiple roots that are close to each other.

- **Requires two initial values**: Unlike the bisection method, which only needs a single interval, the secant method requires two initial approximations.

\pagebreak

## HybridBF Algorithm

The HybridBF algorithm is a hybrid algorithm between the bisection method and false position method. The algorithm works as follows:

1. Take the polynomial and the interval that contains the root.
2. In each iteration, the algorithm will apply the bisection method and the false position method and get the root from each method.
3. The algorithm will choose the root that will give the smallest absolute value of the polynomial $|f(x)|$.
4. The algorithm will stop when the absolute value of the polynomial is less than a certain tolerance we define.

```{.mermaid caption="HybridBF Steps Flowchart" width=35%}
graph TB
    Start(Start) --> Input[Input: Polynomial, Interval]
    Input --> Bisection[Apply Bisection Method]
    Input --> FalsePosition[Apply False Position Method]
    Bisection --> RootBisection[Root from Bisection]
    FalsePosition --> RootFalsePosition[Root from False Position]
    RootBisection --> Compare[Compare Absolute Values]
    RootFalsePosition --> Compare
    Compare --> Output[Output: Root with Smallest Absolute Value]
    Output --> Check{Check: Absolute Value < Tolerance?}
    Check -- Yes --> Return[Return Root]
    Return --> End(End)
    Check -- No --> Input
```

\pagebreak

## HybridSF Algorithm

It has the same steps as [HybridBF](#hybridbf-algorithm) but it uses the secant method instead of the bisection method.

```{.mermaid caption="HybridSF Steps Flowchart" width=35%}
graph TB
    Start(Start) --> Input[Input: Polynomial, Interval]
    Input --> Secant[Apply Secant Method]
    Input --> FalsePosition[Apply False Position Method]
    Secant --> RootSecant[Root from Secant]
    FalsePosition --> RootFalsePosition[Root from False Position]
    RootSecant --> Compare[Compare Absolute Values]
    RootFalsePosition --> Compare
    Compare --> Output[Output: Root with Smallest Absolute Value]
    Output --> Check{Check: Absolute Value < Tolerance?}
    Check -- Yes --> Return[Return Root]
    Return --> End(End)
    Check -- No --> Input
```

To test the algorithm we have used the same 25 equations with each method and run each method (Bisection, False Position, HybridBF, Secant, and HybridSF) 500 times for each problem and then we have calculated the average time and the number of iterations each method have taken for each problem.

We have also used the same tolerance for each method which is $\epsilon=10^{-14}$

These are the equations that we have used with each method:

### Equations That Serve as Test Cases

In these equations we have tried to use different types of functions like polynomial, exponential, trigonometric, and logarithmic functions to ensure that the algorithm works with different types of functions. We have also used different intervals with each algorithm depending on where the roots of the equations are.

Table: Test Cases Equations

|  No   | Equation                   |  Interval       |
| :---: | :------------------------- |  :------------- |
| $P1$  | $f(x) = x^{3}+4x^{2}-10=0$ |  $[0, 4]$       |
| $P2$  | $f(x)=x^2-4$               |  $[0, 4]$       |
| $P3$  | $f(x)=e^x-2$               |  $[0, 2]$       |
| $P4$  | $f(x)=\sin(x)$             |  $[2, 6]$       |
| $P5$  | $f(x)=x^3-6x^2+11x-6$      |  $[1, 2.5]$     |
| $P6$  | $f(x)=x^2+3x+2$            |  $[-2.5, -1.5]$ |
| $P7$  | $f(x)=\cos(x)-x$           |  $[0, 1]$       |
| $P8$  | $f(x)=2^x-8$               |  $[2, 4]$        |
| $P9$  | $f(x)=\tan(x)$             |  $[-1, 1]$      |
| $P10$ | $f(x)=x^4-8x^3+18x^2-9x+1$ |  $[2, 4]$       |

### Extra Equations From Paper

We got these equations from [this paper](https://www.researchgate.net/publication/360883886_Novel_hybrid_algorithms_for_root_determining_using_advantages_of_open_methods_and_bracketing_methods) and we have used the same intervals too.

Table: Equations From Paper

|  No   | Equation                 | Interval  | Reference       |
| :---: | :----------------------- | :-------- | :-------------- |
| $P11$ | $f(x)=x^2-3$             | $[1,2]$   | Harder [18]     |
| $P12$ | $f(x)=x^2-5$             | $[2,7]$   | Srivastava[9]   |
| $P13$ | $f(x)=x^2-10$            | $[3,4]$   | Harder [18]     |
| $P14$ | $f(x)=x^2-x-2$           | $[1,4]$   | Moazzam [10]    |
| $P15$ | $f(x)=x^2+2x-7$          | $[1,3]$   | Nayak[11]       |
| $P16$ | $f(x)=x^3-2$             | $[0,2]$   | Harder [18]     |
| $P17$ | $f(x)=xe^x-7$            | $[0,2]$   | Callhoun [19]   |
| $P18$ | $f(x)=x-\cos(x)$         | $[0,1]$   | Ehiwario [6]    |
| $P19$ | $f(x)=x\sin(x)-1$        | $[0,2]$   | Mathews [20]    |
| $P20$ | $f(x)=x\cos(x)+1$        | $[-2,4]$  | Esfandiari [21] |
| $P21$ | $f(x)=x^{10}-1$          | $[0,1.3]$ | Chapra [17]     |
| $P22$ | $f(x)=x^2+e^{x/2}-5$     | $[1,2]$   | Esfandiari [21] |
| $P23$ | $f(x)=\sin(x)\sinh(x)+1$ | $[3,4]$   | Esfandiari [21] |
| $P24$ | $f(x)=e^x-3x-2$          | $[2,3]$   | Hoffman [22]    |
| $P25$ | $f(x)=\sin(x)-x^2$       | $[0.5,1]$ | Chapra[17]      |

## Root Finding Algorithms Performance Results

These are the results we got with each method. We have run each method 500 times on each equation and took the average time to get the highest accuracy possible.

### False Position

These are the results we got with False Position method:

<!-- \fontsize{5}{12}\selectfont -->
\begin{tiny}
\begin{longtable}{ccccccc}
    \caption{False Position} \\
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{False Position Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endfirsthead
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{False Position Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endhead
    \hline
    \endfoot
    \bottomrule
    \endlastfoot
    \$P1\$ & 80 & 0.000108872890472412 & 1.3652300134141 & -7.105427357601E-15 & 1.3652300134141 & 4 \\
    \$P2\$ & 33 & 2.54607200622559E-05 & 2 & -8.88178419700125E-15 & 2 & 4 \\
    \$P3\$ & 51 & 3.37719917297363E-05 & 0.693147180559942 & -6.21724893790088E-15 & 0.693147180559942 & 2 \\
    \$P4\$ & 8 & 4.61483001708984E-06 & 3.14159265358979 & 1.22464679914735E-16 & 3.14159265358979 & 3.14159265358992 \\
    \$P5\$ & 2 & 2.02751159667969E-06 & 1 & 0 & 1 & 2.5 \\
    \$P6\$ & 31 & 3.35359573364258E-05 & -2 & -5.32907051820075E-15 & -2.5 & -2 \\
    \$P7\$ & 12 & 7.18259811401367E-06 & 0.739085133215155 & 9.2148511043888E-15 & 0.739085133215155 & 1 \\
    \$P8\$ & 30 & 2.37202644348144E-05 & 3 & -7.105427357601E-15 & 3 & 4 \\
    \$P9\$ & 2 & 9.75608825683594E-07 & 0 & 0 & 0 & 1 \\
    \$P10\$ & 13 & 2.66284942626953E-05 & 3.11174865630925 & 0 & 3.11174865630925 & 3.11174865630925 \\ \hline
    \$P11\$ & 14 & 1.06868743896484E-05 & 1.73205080756888 & -3.99680288865056E-15 & 1.73205080756888 & 2 \\
    \$P12\$ & 50 & 3.87668609619141E-05 & 2.23606797749979 & -9.76996261670138E-15 & 2.23606797749979 & 7 \\
    \$P13\$ & 17 & 1.34563446044922E-05 & 3.16227766016838 & -1.77635683940025E-15 & 3.16227766016838 & 4 \\
    \$P14\$ & 38 & 3.21516990661621E-05 & 2 & -8.65973959207622E-15 & 2 & 4 \\
    \$P15\$ & 21 & 2.0256519317627E-05 & 1.82842712474619 & -2.66453525910038E-15 & 1.82842712474619 & 3 \\
    \$P16\$ & 41 & 3.12848091125488E-05 & 1.25992104989487 & -6.21724893790088E-15 & 1.25992104989487 & 2 \\
    \$P17\$ & 30 & 2.12483406066895E-05 & 1.52434520498414 & -7.99360577730113E-15 & 1.52434520498414 & 2 \\
    \$P18\$ & 12 & 7.22360610961914E-06 & 0.739085133215155 & -9.2148511043888E-15 & 0.739085133215155 & 1 \\
    \$P19\$ & 7 & 5.02967834472656E-06 & 1.11415714087193 & 8.88178419700125E-16 & 1.09975017029462 & 1.11415714087193 \\
    \$P20\$ & 13 & 9.73367691040039E-06 & 2.07393280909121 & 7.7715611723761E-16 & 2.07393280909121 & 2.51571977101466 \\
    \$P21\$ & 139 & 0.000106982231140137 & 0.999999999999999 & -8.88178419700125E-15 & 0.999999999999999 & 1.3 \\
    \$P22\$ & 16 & 1.86800956726074E-05 & 1.64901326830319 & -8.88178419700125E-16 & 1.64901326830319 & 2 \\
    \$P23\$ & 45 & 5.06892204284668E-05 & 3.22158839909394 & 6.43929354282591E-15 & 3.22158839909394 & 4 \\
    \$P24\$ & 45 & 3.95450592041016E-05 & 2.12539119881113 & -8.88178419700125E-15 & 2.12539119881113 & 3 \\
    \$P25\$ & 17 & 1.45211219787598E-05 & 0.876726215395055 & 7.88258347483861E-15 & 0.876726215395055 & 1 \\
\end{longtable}
\end{tiny}

### Bisection Method

These are the results we got with Bisection method:

\begin{tiny}
\begin{longtable}{ccccccc}
    \caption{Bisection} \label{tab:addlabel} \\
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{Bisection Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endfirsthead
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{Bisection Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endhead
    \hline
    \endfoot
    \bottomrule
    \endlastfoot
    \$P1\$ & 50 & 3.78618240356445E-05 & 1.3652300134141 & -2.8421709430404E-14 & 1.36523001341409 & 1.3652300134141 \\
    \$P2\$ & 1 & 9.20772552490234E-07 & 2 & 0 & 0 & 4 \\
    \$P3\$ & 49 & 2.00080871582031E-05 & 0.693147180559944 & -3.33066907387547E-15 & 0.69314718055994 & 0.693147180559947 \\
    \$P4\$ & 50 & 1.82290077209473E-05 & 3.14159265358979 & 1.22464679914735E-16 & 3.14159265358979 & 3.1415926535898 \\
    \$P5\$ & 48 & 4.16674613952637E-05 & 2 & 0 & 2 & 2.00000000000001 \\
    \$P6\$ & 1 & 1.10149383544922E-06 & -2 & 0 & -2.5 & -1.5 \\
    \$P7\$ & 48 & 1.79662704467773E-05 & 0.739085133215159 & 2.55351295663786E-15 & 0.739085133215156 & 0.739085133215163 \\
    \$P8\$ & 1 & 9.37938690185547E-07 & 3 & 0 & 2 & 4 \\
    \$P9\$ & 1 & 7.75814056396484E-07 & 0 & 0 & -1 & 1 \\
    \$P10\$ & 49 & 5.54814338684082E-05 & 3.11174865630925 & 1.06581410364015E-14 & 3.11174865630925 & 3.11174865630925 \\ \hline
    \$P11\$ & 48 & 2.20985412597656E-05 & 1.73205080756888 & 4.44089209850063E-15 & 1.73205080756888 & 1.73205080756888 \\
    \$P12\$ & 50 & 2.28300094604492E-05 & 2.23606797749979 & -1.95399252334028E-14 & 2.23606797749978 & 2.23606797749979 \\
    \$P13\$ & 48 & 2.22716331481934E-05 & 3.16227766016838 & 1.59872115546023E-14 & 3.16227766016838 & 3.16227766016839 \\
    \$P14\$ & 50 & 2.49624252319336E-05 & 2 & -2.66453525910038E-15 & 2 & 2 \\
    \$P15\$ & 49 & 2.77295112609863E-05 & 1.82842712474619 & -1.15463194561016E-14 & 1.82842712474618 & 1.82842712474619 \\
    \$P16\$ & 49 & 2.24394798278809E-05 & 1.25992104989487 & 5.32907051820075E-15 & 1.25992104989487 & 1.25992104989488 \\
    \$P17\$ & 49 & 2.14519500732422E-05 & 1.52434520498415 & 3.37507799486048E-14 & 1.52434520498414 & 1.52434520498415 \\
    \$P18\$ & 48 & 1.79176330566406E-05 & 0.739085133215159 & -2.55351295663786E-15 & 0.739085133215156 & 0.739085133215163 \\
    \$P19\$ & 49 & 2.24361419677734E-05 & 1.11415714087193 & -2.99760216648792E-15 & 1.11415714087192 & 1.11415714087193 \\
    \$P20\$ & 51 & 2.31366157531738E-05 & 2.07393280909122 & -1.33226762955019E-15 & 2.07393280909121 & 2.07393280909122 \\
    \$P21\$ & 48 & 2.20670700073242E-05 & 1 & 1.11022302462516E-14 & 0.999999999999996 & 1.00000000000001 \\
    \$P22\$ & 48 & 3.11980247497559E-05 & 1.64901326830319 & -3.5527136788005E-15 & 1.64901326830319 & 1.64901326830319 \\
    \$P23\$ & 48 & 3.00378799438477E-05 & 3.22158839909394 & -5.55111512312578E-15 & 3.22158839909394 & 3.22158839909395 \\
    \$P24\$ & 46 & 2.39477157592773E-05 & 2.12539119881113 & 0 & 2.12539119881112 & 2.12539119881114 \\
    \$P25\$ & 47 & 2.58064270019531E-05 & 0.876726215395063 & -8.88178419700125E-16 & 0.87672621539506 & 0.876726215395067 \\
\end{longtable}
\end{tiny}

### Secant Method

These are the results we got with Secant method:

\begin{tiny}
\begin{longtable}{ccccccc}
    \caption{Secant} \\
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{Secant Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endfirsthead % This marks the end of the header for the first page
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{Hybrid Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endhead % This marks the end of the header for the subsequent pages
    \hline
    \endfoot % This marks the end of the footer for the intermediate pages
    \bottomrule
    \endlastfoot % This marks the end of the footer for the last page
    \$P1\$ & 12 & 6.93511962890625E-06 & 1.3652300134141 & 0 & 1.3652300134141 & 1.3652300134141 \\
    \$P2\$ & 9 & 3.46088409423828E-06 & 2 & 0 & 2 & 2 \\
    \$P3\$ & 9 & 3.33023071289062E-06 & 0.693147180559945 & 0 & 0.693147180559945 & 0.693147180559945 \\
    \$P4\$ & 7 & 2.45857238769531E-06 & 6.28318530717959 & -2.44929359829471E-16 & 6.28318530717959 & 6.28318530717959 \\
    \$P5\$ & 2 & 1.84392929077148E-06 & 1 & 0 & 1 & 1 \\
    \$P6\$ & 10 & 4.70542907714844E-06 & -2 & 0 & -2 & -2 \\
    \$P7\$ & 7 & 2.44808197021484E-06 & 0.739085133215161 & 0 & 0.739085133215161 & 0.739085133215161 \\
    \$P8\$ & 8 & 3.28588485717773E-06 & 3 & 0 & 3 & 3 \\
    \$P9\$ & 2 & 1.04379653930664E-06 & 0 & 0 & 0 & 0 \\
    \$P10\$ & 17 & 1.45139694213867E-05 & 0.481389601149957 & 0 & 0.481389601149957 & 0.481389601149957 \\ \hline
    \$P11\$ & 7 & 2.82144546508789E-06 & 1.73205080756888 & 4.44089209850063E-16 & 1.73205080756888 & 1.73205080756888 \\
    \$P12\$ & 8 & 3.25679779052734E-06 & 2.23606797749979 & 8.88178419700125E-16 & 2.23606797749979 & 2.23606797749979 \\
    \$P13\$ & 6 & 2.61688232421875E-06 & 3.16227766016838 & -1.77635683940025E-15 & 3.16227766016838 & 3.16227766016838 \\
    \$P14\$ & 9 & 3.77416610717773E-06 & 2 & 0 & 2 & 2 \\
    \$P15\$ & 7 & 3.43656539916992E-06 & 1.82842712474619 & 8.88178419700125E-16 & 1.82842712474619 & 1.82842712474619 \\
    \$P16\$ & 11 & 4.30393218994141E-06 & 1.25992104989487 & 0 & 1.25992104989487 & 1.25992104989487 \\
    \$P17\$ & 10 & 3.88193130493164E-06 & 1.52434520498414 & 0 & 1.52434520498414 & 1.52434520498414 \\
    \$P18\$ & 7 & 2.60496139526367E-06 & 0.739085133215161 & 0 & 0.739085133215161 & 0.739085133215161 \\
    \$P19\$ & 6 & 2.66456604003906E-06 & 1.11415714087193 & 2.22044604925031E-16 & 1.11415714087193 & 1.11415714087193 \\
    \$P20\$ & 9 & 3.63922119140625E-06 & 2.07393280909121 & -2.22044604925031E-16 & 2.07393280909121 & 2.07393280909121 \\
    \$P21\$ & \multicolumn{6}{c}{\textit{\textbf{No Solution}}} \\
    \$P22\$ & 7 & 4.0740966796875E-06 & 1.64901326830319 & 0 & 1.64901326830319 & 1.64901326830319 \\
    \$P23\$ & 8 & 4.34207916259766E-06 & 3.22158839909394 & 3.33066907387547E-16 & 3.22158839909394 & 3.22158839909394 \\
    \$P24\$ & 8 & 3.73697280883789E-06 & 2.12539119881113 & 0 & 2.12539119881113 & 2.12539119881113 \\
    \$P25\$ & 8 & 3.88669967651367E-06 & 0.876726215395062 & 0 & 0.876726215395062 & 0.876726215395062 \\
\end{longtable}
\end{tiny}

### HybridBF Method

These are the results we got with HybridBF method:

\begin{tiny}
\begin{longtable}{ccccccc}
    \caption{HybridBF} \\
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{HybridBF Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endfirsthead % This marks the end of the header for the first page
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{Hybrid Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endhead % This marks the end of the header for the subsequent pages
    \hline
    \endfoot % This marks the end of the footer for the intermediate pages
    \bottomrule
    \endlastfoot % This marks the end of the footer for the last page
    \$P1\$ & 10 & 1.51724815368652E-05 & 1.3652300134141 & -7.105427357601E-15 & 1.36523001341378 & 1.36750019802744 \\
    \$P2\$ & 1 & 9.86576080322266E-07 & 2 & 0 & 0 & 4 \\
    \$P3\$ & 10 & 1.01175308227539E-05 & 0.693147180559945 & 0 & 0.693147180559933 & 0.695162706464415 \\
    \$P4\$ & 6 & 5.41830062866211E-06 & 3.14159265358979 & 1.22464679914735E-16 & 3.14159035795569 & 3.14159265360489 \\
    \$P5\$ & 1 & 1.57594680786133E-06 & 1 & 0 & 1 & 2.5 \\
    \$P6\$ & 1 & 1.17969512939453E-06 & -2 & 0 & -2.5 & -1.5 \\
    \$P7\$ & 8 & 7.32851028442383E-06 & 0.739085133215161 & 1.11022302462516E-16 & 0.739085133215147 & 0.742227073217592 \\
    \$P8\$ & 1 & 1.02519989013672E-06 & 3 & 0 & 2 & 4 \\
    \$P9\$ & 1 & 8.06331634521484E-07 & 0 & 0 & -1 & 1 \\
    \$P10\$ & 8 & 1.61228179931641E-05 & 3.11174865630925 & 0 & 3.10853799278589 & 3.11174865630925 \\ \hline
    \$P11\$ & 8 & 8.37850570678711E-06 & 1.73205080756888 & -4.44089209850063E-16 & 1.7320508075688 & 1.73505784022098 \\
    \$P12\$ & 10 & 1.055908203125E-05 & 2.23606797749979 & -3.5527136788005E-15 & 2.23606797749936 & 2.24392915398361 \\
    \$P13\$ & 8 & 8.51917266845703E-06 & 3.16227766016838 & 1.77635683940025E-15 & 3.16227766016837 & 3.1672187190124 \\
    \$P14\$ & 2 & 2.20155715942383E-06 & 2 & 0 & 1.5 & 2.5 \\
    \$P15\$ & 5 & 6.05535507202148E-06 & 1.82842712474619 & 0 & 1.828427124743 & 1.82842712474938 \\
    \$P16\$ & 9 & 9.37175750732422E-06 & 1.25992104989487 & -3.99680288865056E-15 & 1.25992104989398 & 1.2611286403177 \\
    \$P17\$ & 11 & 1.14202499389648E-05 & 1.52434520498414 & 0 & 1.52434520498414 & 1.52603333710876 \\
    \$P18\$ & 8 & 7.33852386474609E-06 & 0.739085133215161 & -1.11022302462516E-16 & 0.739085133215147 & 0.742227073217592 \\
    \$P19\$ & 6 & 6.33621215820313E-06 & 1.11415714087193 & -2.22044604925031E-16 & 1.11324273276427 & 1.11415714087198 \\
    \$P20\$ & 10 & 1.05037689208984E-05 & 2.07393280909121 & -2.22044604925031E-16 & 2.07393280909119 & 2.07893500333739 \\
    \$P21\$ & 12 & 1.24101638793945E-05 & 1 & -1.11022302462516E-15 & 0.99999999999993 & 1.00034336328299 \\
    \$P22\$ & 8 & 1.04570388793945E-05 & 1.64901326830319 & -3.5527136788005E-15 & 1.64901326830264 & 1.65315575626948 \\
    \$P23\$ & 9 & 1.19032859802246E-05 & 3.22158839909394 & 3.33066907387547E-16 & 3.22158839909392 & 3.22241688813951 \\
    \$P24\$ & 9 & 1.03793144226074E-05 & 2.12539119881113 & -6.21724893790088E-15 & 2.1253911988104 & 2.12751913344632 \\
    \$P25\$ & 7 & 7.85541534423828E-06 & 0.876726215395058 & 4.77395900588817E-15 & 0.876726215388671 & 0.877268445434873 \\
\end{longtable}
\end{tiny}

As we see from the table above the hybrid method tend to be faster and take much less iterations than both Bisection and False Position methods.

### HybridSF Method

These are the results we got with HybridSF method:

\begin{tiny}
\begin{longtable}{ccccccc}
    \caption{HybridSF} \\
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{HybridSF Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endfirsthead % This marks the end of the header for the first page
    \toprule
    \multirow{2}[4]{*}{\textbf{Problem}} & \multicolumn{6}{c}{\textbf{Hybrid Algorithm}} \\
    \cmidrule{2-7}
    & \textbf{Iter} & \textbf{Avg CPU Time} & \textbf{Approximate Root} & \textbf{Function Value} & \textbf{Lower Bound} & \textbf{Upper Bound} \\
    \midrule
    \endhead % This marks the end of the header for the subsequent pages
    \hline
    \endfoot % This marks the end of the footer for the intermediate pages
    \bottomrule
    \endlastfoot % This marks the end of the footer for the last page
    \$P1\$ & 40 & 4.32667732238769E-05 & 1.3652300134141 & -7.105427357601E-15 & 1.3652300134141 & 4 \\
    \$P2\$ & 17 & 1.1502742767334E-05 & 2 & -2.66453525910038E-15 & 2 & 4 \\
    \$P3\$ & 26 & 1.56879425048828E-05 & 0.693147180559944 & -3.10862446895044E-15 & 0.693147180559942 & 2 \\
    \$P4\$ & 6 & 3.37457656860352E-06 & 3.14159265358979 & 1.22464679914735E-16 & 3.14159265358979 & 3.14159265363241 \\
    \$P5\$ & 1 & 1.11484527587891E-06 & 1 & 0 & 1 & 2.5 \\
    \$P6\$ & 16 & 1.37491226196289E-05 & -2 & -4.44089209850063E-15 & -2.00000000000001 & -1.75 \\
    \$P7\$ & 6 & 3.53384017944336E-06 & 0.739085133215155 & 9.2148511043888E-15 & 0.73908513321505 & 1 \\
    \$P8\$ & 15 & 1.04451179504395E-05 & 3 & -7.105427357601E-15 & 3 & 4 \\
    \$P9\$ & 1 & 6.39915466308594E-07 & 0 & 0 & -1 & 1 \\
    \$P10\$ & 7 & 1.10006332397461E-05 & 3.11174865630925 & 7.105427357601E-15 & 3.11174865630925 & 3.11174865630925 \\ \hline
    \$P11\$ & 7 & 4.94670867919922E-06 & 1.73205080756888 & -3.99680288865056E-15 & 1.73205080756886 & 2 \\
    \$P12\$ & 25 & 1.68638229370117E-05 & 2.23606797749979 & -9.76996261670138E-15 & 2.23606797749979 & 7 \\
    \$P13\$ & 9 & 6.21271133422852E-06 & 3.16227766016838 & 1.77635683940025E-15 & 3.16227766016838 & 4 \\
    \$P14\$ & 19 & 1.37357711791992E-05 & 2 & -8.65973959207622E-15 & 1.99999999999999 & 4 \\
    \$P15\$ & 11 & 9.09614562988281E-06 & 1.82842712474619 & 0 & 1.82842712474619 & 3 \\
    \$P16\$ & 21 & 1.41358375549316E-05 & 1.25992104989487 & -3.10862446895044E-15 & 1.25992104989487 & 2 \\
    \$P17\$ & 15 & 9.67836380004883E-06 & 1.52434520498414 & -7.99360577730113E-15 & 1.52434520498414 & 2 \\
    \$P18\$ & 6 & 3.55148315429688E-06 & 0.739085133215155 & -9.2148511043888E-15 & 0.73908513321505 & 1 \\
    \$P19\$ & 5 & 3.5557746887207E-06 & 1.11415714087193 & 2.22044604925031E-16 & 1.11415714087193 & 1.11415714087196 \\
    \$P20\$ & 7 & 0.0000048828125 & 2.07393280909121 & 1.77635683940025E-15 & 2.07393280909119 & 2.51571977101466 \\
    \$P21\$ & 70 & 4.62303161621094E-05 & 1 & -6.66133814775094E-15 & 0.999999999999999 & 1.3 \\
    \$P22\$ & 8 & 7.51972198486328E-06 & 1.64901326830319 & -8.88178419700125E-16 & 1.64901326830319 & 2 \\
    \$P23\$ & 23 & 2.04296112060547E-05 & 3.22158839909394 & 3.33066907387547E-16 & 3.22158839909394 & 4 \\
    \$P24\$ & 23 & 1.71117782592773E-05 & 2.12539119881113 & -1.77635683940025E-15 & 2.12539119881113 & 3 \\
    \$P25\$ & 9 & 6.75392150878906E-06 & 0.876726215395061 & 1.11022302462516E-15 & 0.876726215395055 & 1 \\
\end{longtable}
\end{tiny}

### Conclusion

Our conclusions based on the tables and the plots are:

<!-- > *Side Note: The equation $f(x)=x^3-6x^2+11x-6$ in P5 has two roots. In the false position and hybrid methods, the equation has a root at 1. On the other hand,  the bisection method identifies another root at approximately 2.0000000000000018 within the interval $[1, 2.5]$.* -->

#### Iterations

![Iterations Comparison](./images/iterations-comparison.svg)

The hybrid method demonstrates superior performance compared to both the bisection and false position methods in terms of the number of iterations required.

As we see here in P21 the false position method have much more number of iterations than both hybrid and bisection methods which will lead to more CPU time as we will see in the next section.

#### CPU Time

![CPU Time Comparison](./images/CPU-time-comparison.svg)

The hybrid method shows significant improvement over the bisection method in terms of CPU time, with a ratio of 21:4 .This translates to approximately 84% for the hybrid method and 16% for the bisection method.

The hybrid method shows significant improvement over the false position method in terms of CPU time, with a ratio of 19:6 .This translates to approximately 76% for the hybrid method and 24% for the false position method.

As a general trend, the hybrid method is faster than both the bisection and false position methods when it comes to finding the approximate root.

#### Function Value

![Function Value Comparison](./images/function-value-comparison.svg)

The hybrid method outperforms both the bisection and false position methods in terms of function value, with smaller values that are closer to zero.

<!-- 
---
title: \begin{title}\centering\vspace*{1cm}\rule{\textwidth}{0.05cm}\linebreak\vspace{0.5cm}{\huge\bfseries Polynomial Interpolation Based Encryption Algorithm \par}\vspace{0.1cm}\hrule\end{title}
date: February 8, 2024
abstract: Encryption algorithms are vital for securing sensitive data. However, many popular algorithms like AES have high computational costs. This paper proposes a new polynomial interpolation based encryption algorithm that aims to improve encryption and decryption speeds. After testing the algorithm against AES on 1000 different plaintext messages and keys, the results showed that the algorithm is much faster than AES in both encoding and decoding times.\pagebreak
--- 

\pagebreak
-->

\pagebreak

\begin{center}
\section{\textit{Chapter Three: Cryptographic Algorithms}}
\end{center}

## Introduction

This chapter provides an overview of the proposed polynomial roots based encryption algorithm. The chapter contains the encryption and decryption processes, the algorithm's steps, and the results of the algorithm's performance compared to AES.

## Polynomia Roots Based Encryption Algorithm Steps

### Encryption Process

The algorithm encrypts plaintext message using a polynomial and root finding method to generate a ciphertext. The encryption process works as follows:

1. Take the plaintext message and convert each 4 characters to an integer value using their ASCII values.
2. Take the key from the user which will be used to generate the polynomial. The encryption key consists of a set of 5 integer values $x_1$, $x_2$, $y$, $s$, and $r$.
   1. $x_1$ and $x_2$ define $x$ interval for the polynomial.
   2. $y$ defines the start of $y$ interval for the polynomial and the end will be the negative of $y$ to ensure that the polynomial crosses the x-axis and has a root.
   3. $s$ defines the number of sections that we want to divide the interval into which will affect the degree of the polynomial.
   4. $r$ is used as a random state for the random number generator. The random values will always be the same for the same $r$ value.
3. Use the encryption key to generate points that will be used to generate the polynomial. The points are generated using the following steps:
   1. Divide the interval $[x_1, x_2]$ into $s$ equal sections.
   2. Divide the interval $[y, -y]$ into $s$ equal sections.
   3. Generate points from the two intervals that will be used to generate the polynomial.
   4. Use the random numbers we got $r$ to add some noise to the points.
   5. Apply Newton Forward Difference interpolation to the points to generate the polynomial Since the points are equally spaced.
4. Now we have the polynomial and the plaintext integer representation so we will subtract the plaintext integer from the polynomial representation
5. We get the root of the polynomial which will be the ciphertext using HybridBF algorithm which is a hybrid algorithm between the bisection method and false position method and it will be discussed later.

```{.mermaid caption="Encryption Steps Flowchart" width=30%}
graph TD
A[Start] --> B[Take plaintext message]
B --> C[Convert each 4 characters to an integer]
C --> D[Take the key from the user]
D --> E[Generate points using the key]
E --> F[Apply Newton Forward Difference interpolation to the points]
F --> G[Subtract plaintext integer from polynomial]
G --> H[Find root of polynomial]
H --> I[End: Root is the Ciphertext]
```

### Decryption Process

The algorithm decrypts the ciphertext message using the polynomial. The decryption process works as follows:

1. Take the ciphertext and the key from the user which will be used to generate the polynomial again.
2. Use the key to generate the polynomial using the same steps as the encryption process.
3. Now we have the polynomial and the ciphertext so we will substitute the ciphertext in the polynomial to get the plaintext integer representation.
4. Convert the integer representation to the plaintext message by converting each integer to 4 characters using their ASCII values.

```{.mermaid caption="Decryption Steps Flowchart" width=30%}
graph TD
A[Start] --> B[Take ciphertext and key from user]
B --> C[Generate polynomial using the key]
C --> D[Substitute ciphertext in polynomial and get the result]
D --> E[The result is the plaintext integer representation]
E --> F[Convert the integer to the plaintext message]
F --> G[End: Plaintext message]
```

## Results

The algorithm was tested using 1000 different plaintext messages and keys and was compared against AES encryption algorithm which is a symmetric encryption algorithm. The results showed that the algorithm is much faster than AES.

### Encode Time Comparison

The algorithm showed a significant improvement in the encoding time compared to AES. The encoding time was measured using the time library in python and the results are shown in this figure:

![Encoding Time Comparison](./images/total-encode-time-comparison.svg)

And when we sum the encoding time for all the 1000 messages we get the following results:

![Total Encoding Time Comparison](./images/total_encode_time.svg){width=350px}

### Decode Time Comparison

The algorithm have also showed a significant improvement in the decoding time compared to AES. The results are shown in this figure:

![Decoding Time Comparison](images/total-decode-time-comparison.svg)

And when we sum the decoding time for all the 1000 messages we get the following results:

![Total Decoding Time Comparison](./images/total_decode_time.svg){width=350px}

### Total Time Comparison

The total time for both algorithms was also measured and compared. The results are shown in this figure:

![Total Time Comparison](./images/total-time-comparison.svg)

And when we sum the total time for all the 1000 messages we get the following results:

![Total Time Comparison](./images/total_time.svg){width=350px}

\pagebreak

\begin{center}
\section{\textit{Chapter Four: Design and Analysis}}
\end{center}

## Introduction

The analysis and design section provides an overview of the proposed system architecture and data flow of the secure messaging web application. This section contains several software engineering diagrams depicting the structural and behavioral models of the system.

To enable secure communication, the application utilizes the cryptographic algorithm based on polynomial roots.

## Functional & Non-Functional Requirements Table

Table: Functional & NonFunctional Requirements

<!-- | ------------------ | :----------------: | :-------------------: | --------------------------------------------------------- | ------------ | ---------------- | -->

| Name           | Functional | NonFunctional | Description                                           | Priority | Actor    |
| ------------------ | :----------------: | :-------------------: | --------------------------------------------------------- | ------------ | ---------------- |
| Registration   |  $\checkmark$  |                   | Functionality to create account.                          | High         | User & Admin |
| Login          |  $\checkmark$  |                   | Functionality to get access.                              | High         | User & Admin |
| Logout         |  $\checkmark$  |                   | Functionality to delete session.                          | High         | User & Admin |
| Add Chat       |  $\checkmark$  |                   | Functionality for user to chat with other.                | Medium       | User         |
| Remove Chat    |  $\checkmark$  |                   | Functionality for user to remove chat.                    | Medium       | User         |
| Find Chat      |  $\checkmark$  |                   | Functionality for user to search for a chat.              | High         | User         |
| Block Account  |  $\checkmark$  |                   | Functionality for user to block user account.             | Medium       | User         |
| Send Message   |  $\checkmark$  |                   | Functionality that send message.                          | High         | User         |
| Delete Message |  $\checkmark$  |                   | Functionality to delete message.                          | Medium       | User & Admin |
| Read Message   |  $\checkmark$  |                   | Functionality for user to read message                    | High         | User         |
| Privacy        |                |   $\checkmark$    | Users privacy.                                            | High         | Admin        |
| Robustness     |                |   $\checkmark$    | to make able to deal with errors.                         | High         | Admin        |
| Performance    |                |   $\checkmark$    | Application performance must be better.                   | High         | Admin        |
| Usability      |                |   $\checkmark$    | To make able to use even for newbie.                      | High         | Admin        |
| Reliability    |                |   $\checkmark$    | To be trustworthy to users.                               | High         | Admin        |
| Supportability |                |   $\checkmark$    | To be capable of being supportive.                        | High         | Admin        |
| Portability    |                |   $\checkmark$    | Application must be able to run in many different system. | High         | Admin        |

## Diagrams

### Use Case Diagram

![Use Case Diagram](./files/erd-usecase/usecase.svg){width=225px}

### Activity Diagram

![Sign up Activity Diagram](files/activity/sign_up.drawio.svg)

![Sign in Activity Diagram](files/activity/sign_in.drawio.svg)

![Edit Profile Activity Diagram](files/activity/edit_profile.drawio.svg)

![Search Message Activity Diagram](files/activity/Message_Search.drawio.svg)

![Search For Conversation Activity Diagram](files/activity/Converisation_Search.drawio.svg)

![Search/Receive Data Activity Diagram](files/activity/send_reciev_data.drawio.svg)

![Ban Unban Users Activity Diagram](files/activity/ban_unban_user.drawio.svg)

### Class Diagram

![Class Diagram](files/class-state/class_final.png)

### Sequence Diagram

![Registeration Sequence Diagram](./files/sequence/sequence%20message%20Register.svg)

![Login Sequence Diagram](./files/sequence/sequence%20login.svg)

![New Chat Sequence Diagram](./files/sequence/sequence%20message%20new%20chat.svg)

![Send Message Sequence Diagram](./files/sequence/sequence%20message%20Send%20message.svg)

![Remove Message Sequence Diagram](./files/sequence/sequence%20message%20Remove%20message.svg)

![Logout Sequence Diagram](./files/sequence/sequence%20message%20logout%20message.svg)

### State Diagram

<!-- ![Admin & User State Diagrams](files/class-state/User-admin.drawio.svg) -->

![State Diagram](files/class-state/final_state.drawio.svg){width=600px}

### Context Diagram

![Context Diagram](files/context-dfd/messaging-sys-context-diagram-1.svg)

### Data Flow Diagram

![Data Flow Diagram](files/context-dfd/messaging-sys-dfd-1.svg)

### Entity Relationship Diagram

![Entity Relationship Diagram](files/erd-usecase/finish_erd.svg)

## Tools & Libraries

### Visual Studio Code

Visual Studio Code was used as the primary Integrated Development Environment (IDE) for the project. It's a source-code editor developed by Microsoft for Windows, Linux, and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring.

### Python

The algorithm was written in Python which is a high-level, general-purpose programming language. It is known for its simplicity and easy-to-read syntax. It is widely used in scientific and numeric computing, web development, and artificial intelligence.

The following libraries were used:

#### `pandas`

Pandas is a software library for the Python programming language that provides data manipulation and analysis capabilities.

We used it to read and manipulate the datasets from the CSV files.

#### `matplotlib`

Matplotlib is a plotting library for the Python programming language. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.

We used it to create the plots for the results of the algorithm.

#### `numpy`

NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

We used it to generate the points for most of the mathematical function and to generate the random numbers as it's much faster than the built-in python solutions.

#### `scienceplots`

SciencePlots is a matplotlib style library that provides style sheets for plots to look like they would fit into a scientific publication.

It was used to make publication-ready plots.

#### `scipy`

SciPy is a free and open-source Python library used for scientific computing and technical computing. It contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering.

It has optimized built-in functions for the bisection and false position methods, and newton forward difference interpolation.

#### `pycryptodome`

PyCryptodome is a self-contained Python library for cryptography operations, such as symmetric encryption, asymmetric encryption, hashes, and digital signatures. It is a fork of the original PyCrypto library and aims to provide a more secure and updated alternative.

We used it to compare the results of the algorithm with AES the well-known encryption algorithm.

#### `time`

The time module in Python provides various time-related functions. It is a part of Python's standard library and is used for handling time-related tasks like getting the current time, converting timestamps to readable formats, delaying the execution of functions, and more.

We used it to measure the execution time of each algorithm.

#### `string`

The string module in Python includes functions to process standard Python strings. It contains constants for the printable ASCII characters, for various string operations, and for creating custom string transformations.

We used it to convert the plaintext message to an integer representation.

## Future Work

After the successful implementation of the algorithm, we are planning to work on:

- Create a messaging application that uses the algorithm to secure the messages. The application will be a web application that will allow users to send and receive messages securely.

- The messaging application will feature end-to-end encryption, ensuring that only the intended recipient can read the messages. This is achieved by implementing our unique high-speed encryption algorithm.

- Users will be able to create an account, start conversations, and send send messages. Each message sent through the application is encrypted before it leaves the sender's device and can only be decrypted by the intended recipient. This ensures the privacy and security of the communication, even if the data is intercepted during transmission.

- The application will also include features such as group messaging, file sharing, and message notifications. The user interface will be intuitive and user-friendly, making it easy for users to navigate and use the application.

In our application, we'll employ a combination of symmetric and asymmetric encryption techniques to secure our communications. Our high-speed symmetric encryption algorithm will be used alongside the well-established RSA asymmetric encryption.

The role of the asymmetric encryption, in this case, is to facilitate a secure exchange of the symmetric encryption keys between the communicating parties. This guarantees that the symmetric keys are transmitted securely, allowing only the intended recipient to decrypt the messages.

The symmetric encryption algorithm, on the other hand, will be responsible for the actual message encryption. This ensures the privacy and security of the messages. Furthermore, our algorithm is designed for speed and efficiency, making it an ideal choice for real-time messaging applications.

\pagebreak

# References

\doublespacing

1. jagpreet kaur, Dr. Ramkumar K.R.. A Cryptographic Algorithm using Polynomial Interpolations for Mitigating Key-Size Based Attacks, 14 September 2022, PREPRINT (Version 1) available at Research Square [https://doi.org/10.21203/rs.3.rs-2050151/v1]

2. Badr, El-Sayed & Attiya, Hala & El Ghamry, Abdallah. (2022). Novel hybrid algorithms for root determining using advantages of open methods and bracketing methods. Alexandria Engineering Journal. 61. 11579-11588. 10.1016/j.aej.2022.05.007.

3. Harder, D.W. Numerical Analysis for Engineering. Available online: <https://ece.uwaterloo.ca/~dwharder/nm/> (accessed on 11 June 2019).

4. Srivastava, R.B.; Srivastava, S. Comparison of numerical rate of convergence of bisection, Newton and secant methods. J. Chem. Biol. Phys. Sci. 2011, 2, 472–479.

5. Moazzam, G.; Chakraborty, A.; Bhuiyan, A. A robust method for solving transcendental equations. Int. J. Comput. Sci. Issues 2012, 9, 413–419.

6. Nayak, T.; Dash, T. Solution to quadratic equation using genetic algorithm. In Proceedings of the National Conference on AIRES-2012, Vishakhapatnam, India, 29–30 June 2012.

7. Calhoun, D. Available online: <https://www.boisestate.edu/math/>.

8. Ehiwario, J.C.; Aghamie, S.O. Comparative Study of Bisection, Newton-Raphson and Secant Methods of Root-Finding Problems. IOSR J. Eng. 2014, 4, 1–7

9. Mathews, J.H.; Fink, K.D. Numerical Methods Using Matlab, 4th ed.; Prentice-Hall Inc.: Upper Saddle River, NJ, USA, 2004; ISBN 0-13-065248-2.

10. Esfandiari, R.S. Numerical Methods for Engineers and Scientists Using MATLAB; CRC Press: Boca Raton, FL, USA, 2013.

11. Chapra, S.C.; Canale, R.P. Numerical Methods for Engineers, 7th ed.; McGraw-Hill: Boston, MA, USA, 2015.
