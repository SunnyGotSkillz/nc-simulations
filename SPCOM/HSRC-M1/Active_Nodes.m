% Nodes generation

function [x_pos, y_pos, active] = Active_Nodes(T, N, q, active)
    for j=1:T
        for i=1:N
            if (random('bino',1,q))
                active(j, i) = active(j, i) + 1; % Node is marked as active
            end
        end
    end