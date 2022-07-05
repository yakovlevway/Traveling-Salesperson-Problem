# Traveling-Salesperson-Problem
Although a global solution for the Traveling Salesman Problem does not yet exist, there are algorithms for an existing local solution. There are also necessary and sufficient conditions to determine if a possible solution does exist when one is not given a complete graph. This paper gives an introduction to the Traveling Salesman Problem that includes current research. Additionally, the algorithms are used to find a route traveling through twenty US colleges. As well, we use the Geometric Algorithm to assign scouts for the Pittsburgh Pirates.





In the traveling salesman problem, or ‘‘TSP,’’ we are given a set {c 1
,c 2
,
. . .
,cN} of
cities and for each pair {c i
,c j} of distinct cities a distance d(c i
,c j
). Our goal is to find
an ordering π of the cities that minimizes the quantity
i = 1
Σ
N − 1
d(c π(i)
,c π(i + 1 ) ) + d(c π(N)
,c π( 1 ) ) .
This quantity is referred to as the tour length, since it is the length of the tour a salesman
would make when visiting the cities in the order specified by the permutation, returning
at the end to the initial city. We shall concentrate in this chapter on the symmetric TSP,
in which the distances satisfy d(c i
,c j
) = d(c j
,c i
) for 1 ≤ i, j ≤ N.
The symmetric traveling salesman problem has many applications, from VLSI chip
fabrication [Korte, 1988] to X-ray crystallography [Bland & Shallcross, 1989], and a
long history, for which see Lawler, Lenstra, Rinnooy Kan, and Shmoys [1985]. It is NPhard [Garey & Johnson, 1979] and so any algorithm for finding optimal tours must have
a worst-case running time that grows faster than any polynomial (assuming the widely
believed conjecture that P ≠ NP). This leaves researchers with two alternatives: either
look for heuristics that merely find near-optimal tours, but do so quickly, or attempt to
develop optimization algorithms that work well on ‘‘real-world,’’ rather than worst-case
instances.
Because of its simplicity and applicability (or perhaps simply because of its intriguing name), the TSP has for decades served as an initial proving ground for new ideas
related to both these alternatives. These new ideas include most of the local search variants covered in this book, which makes the TSP an ideal subject for a case study. In
addition, the new ideas include many of the important advances in the related area of
optimization algorithms, and to keep our discussions of local search in perspective, let us
begin by noting the impressive recent progress in this latter domain.
The TSP is one of the major success stories for optimization. Decades of research
into optimization techniques, combined with the continuing rapid growth in computer
speeds and memory capacities, have led to one new record after another. Over the past
15 years, the record for the largest nontrivial TSP instance solved to optimality has
increased from 318 cities [Crowder & Padberg, 1980] to 2392 cities [Padberg & Rinaldi,
1987] to 7397 cities [Applegate, Bixby, Chvat ´ al, & Cook, 1994]. Admittedly, this last
result took roughly 3-4 years of CPU-time on a network of machines of the caliber of a
SPARCstation 2. (SPARC is a trademark of SPARC International, Inc. and is licensed
exclusively to Sun Microsystems, Inc.) However, the branch-and-cut technology developed for these record-setting performances has also had a major impact on the low end of
the scale. Problems with 100 or fewer cities are now routinely solved within a few minutes on a workstation (although there are isolated instances in this range that take much
longer) and instances in the 1,000-city range typically take only a few hours (or days),
e.g., see Padberg & Rinaldi [1991], Gr. .otschel and Holland [1991], and Applegate, Bixby,
Chvat ´ al, and Cook [1994].
- 4 -
The perspective that these optimization results yield is two-fold. First, they weaken
the appeal of the more costly heuristics, at least when the number of cities is 1,000 or
less. Where possible in this survey, we shall thus concentrate on results for instances
with significantly more than 1,000 cities. Second, they suggest that the TSP is not a typical combinatorial optimization problem, since most such problems seem significantly
harder to solve to optimality.
Another way in which the TSP may be atypical lies in the high quality of results that
can be obtained by traditional heuristics. The world of heuristic approaches to the TSP
can be roughly divided into two classes. In addition to the local search approaches that
are the topic of this book, there are many different successive augmentation heuristics for
the TSP. Such heuristics build a solution (tour) from scratch by a growth process (usually a greedy one) that terminates as soon as a feasible solution has been constructed. In
the context of the TSP, we call such a heuristic a tour construction heuristic. Whereas
the successive augmentation approach performs poorly for many combinatorial optimization problems, in the case of the TSP many tour construction heuristics do surprisingly
well in practice. The best typically get within roughly 10-15% of optimal in relatively
little time. Furthermore, ‘‘classical’’ local optimization techniques for the TSP yield
even better results, with the simple 3-Opt heuristic typically getting with 3-4% of optimal
and the ‘‘variable-opt’’ algorithm of Lin and Kernighan [1973] typically getting with 1-
2%. Moreover, for geometric data the abovementioned algorithms all appear to have
running time growth rates that are o(N
2
), i.e., subquadratic, at least in the range from
100 to 1,000,000 cities. These successes for traditional approaches leave less room for
new approaches like tabu search, simulated annealing, etc. to make contributions. Nevertheless, at least one of the new approaches, genetic algorithms, does have something to
contribute if one is willing to pay a large, although still o(N
2
), running time price.
In reaching conclusions like the above, this paper must of necessity take a hybrid
approach. Where possible, we will report the results of performing experiments on common sets of instances on a fixed computer. The common test instances are the main ones
used in a forthcoming study by Johnson, Bentley, McGeoch, and Rothberg [1996], and
they will be described in more detail in the next section. The computer in question is an
SGI ChallengeTM machine containing sixteen 150 Mhz MIPSTM R4400 processors,
although our running times are for sequential implementations that use only a single one
of these processors. (MIPS is a trademark of MIPS, Inc., and Challenge is a trademark of
Silicon Graphics, Inc.) As a point of comparison, the MIPS processor can be 10-15 times
faster than a SPARCstation 1 and perhaps 3-4 times faster than a SPARCstation 2. Our
baseline experiments cover implementations of tour generation heuristics and classic
local search algorithms written by Johnson, Bentley, McGeoch, and Rothberg [1996],
implementations of simulated annealing written by Johnson, Aragon, McGeoch, and
Schevon [1996], and implementations of the GENI and GENIUS local search heuristics
written by Gendreau, Hertz, and Laporte [1992], who graciously provided us with their
source code.
For many of the algorithms we cover, however, the only information we have is
from published papers that provide only high-level descriptions of the algorithms and
- 5 -
summaries of experimental results. These papers do not typically provide enough information for us to compare the algorithms directly to our baseline implementations, and we
are reduced to a process of deduction if we are to make comparisons. For tour quality
comparisons, we are often fortunate in that other authors have generally used test
instances that were similar in nature (if not identical) to the ones in our own test set.
Running time comparisons are a bit more difficult, as rules of thumb for relating times
between machines are far from exact and are highly dependent on the actual code, compilers, and operating systems used. (We used the standard IRIXTM operating system provided by SGI.) Moreover, many papers do not provide enough implementation details
for us to know what sorts of optimizations are present in (or missing from) their codes,
and some papers are unclear as to whether preprocessing is included in their running
times (as it is in ours). Comparisons involving results from such papers must thus often
be based on unverified assumptions about the missing details. We shall generally try to
be explicit about any such assumptions we make.
In comparing results, we shall also be interested in the relationship between what is
known theoretically about the algorithms we study and what can be observed empirically.
We shall see that each type of analysis has useful things to say about the other, although
the worst-case nature of many theoretical results makes them far too pessimistic to tell us
much about typical algorithmic behavior.
The remainder of this chapter is organized as follows. In Section 2 we discuss four
important tour construction heuristics, along with key theoretical results that help characterize their behavior and that identify general complexity-theoretic limitations on what
any heuristic approach can achieve. We also introduce our experimental methodology
and summarize experimental results for the four heuristics from the extensive study by
Johnson, Bentley, McGeoch, and Rothberg [1996]. Note that tour construction heuristics
are important in the context of this book not only for the perspective they provide but
also because they can be used to generate the starting points (initial tours) needed by
local search algorithms and their variants. Section 3 describes 2-Opt and 3-Opt, the simplest and most famous of the classical local optimization algorithms for the TSP, and it
discusses both their empirical behavior and what is known about them from a theoretical
point of view. In addition to providing good results in their own right, these algorithms
provide the essential building blocks used by many researchers in adapting tabu search,
simulated annealing, etc. to the TSP. Section 4 is devoted to adaptations of tabu search
to the TSP and to the Lin-Kernighan algorithm. Although this latter algorithm was
invented some 15 years prior to the introduction of tabu search, it embodies many of the
same ideas, combining them with search-space truncation to yield what was for many
years the ‘‘champion’’ TSP heuristic.
A key question in each of the remaining sections is whether the approach under consideration can beat Lin-Kernighan. Given how good Lin-Kernighan already is, this
means we will occasionally find ourselves forced to make distinctions between algorithms based on tour quality differences as small as 0.1%. Even though such differences
may be statistically significant, we must admit that they are unlikely to be of practical
importance. Nevertheless, the intellectual appeal of the ‘‘which is best’’ question is hard
- 6 -
to resist, and observations made here may suggest what can happen for other problems,
where the ranges in solution quality may well be much wider. Section 5 surveys the
results for various adaptations of simulated annealing and its variants to the TSP with
special emphasis on the results and conclusions of Johnson, Aragon, McGeoch, and
Schevon [1996]. Section 6 discusses genetic algorithms and the iterated local optimization algorithms that have been derived from them, in particular the Iterated LinKernighan algorithm. Section 7 surveys the wide variety of neural net algorithms that
have been applied to the TSP. We conclude in Section 8 with a summary of how the best
current adaptations of the various approaches compare for the TSP, and what, if anything,
this means for other problem domains.
A wealth of algorithmic creativity has been applied to the TSP over the years, and
by covering an extensive slice of it as we do here, we hope at the very least to provide the
reader with a useful source of more widely applicable ideas.
