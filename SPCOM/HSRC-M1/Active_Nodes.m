% Active Nodes generation

function temp = Active_Nodes(N,q,temp)
    %A=[];
    for i=1:N
        if (random('bino',1,q)) %Bern(q)
            %A = union(A,i);
            value = Hash(i,N)+1;
            temp(value) = temp(value)+1;
        end
    end