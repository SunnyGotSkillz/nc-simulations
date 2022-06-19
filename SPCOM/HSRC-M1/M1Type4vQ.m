% HSRC-M1 Figure 5a

M = 4; % stops by MBS
T = 4; % types of nodes
D = 300; % total nodes per type
q = [0.1:0.1:0.5]; % probability that node is active
W = 30; % trials for Phase 1

n_all = T * D; % total manufactured nodes
t = floor(log2(n_all));

for m=1:M
    for t=1:T
        for w=1:W
            S = zeros(1, t);