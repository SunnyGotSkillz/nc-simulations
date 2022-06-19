% HSRC-M1 Figure 5a

M = 4; % stops by MBS
T = 4; % types of nodes
D = 300; % total nodes per type
%q = [0.1:0.1:0.5]; % probability that node is active
q = 0.3
W = 30; % trials for Phase 1

n_all = T * D; % total manufactured nodes
t = floor(log2(n_all));

x_pos = rand(T, D);
y_pos = rand(T, D);
active = zeros(T, D);
active = Active_Nodes(T, D, q, active);

for m=1:M
    for t=1:T
        Y = zeros(1, t); % Y0
        v = zeros(1, W);
        v(1, 1:W) = t;
        for w=1:W
            S = zeros(1, t); 

            % Determine new bit vector Y based on S
            Y = bitor(Y, S);
        end
        n = 0.794 * 2^(sum(v) / W);
    end
end