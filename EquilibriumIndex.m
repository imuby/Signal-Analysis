% Mubarak Aminu
%Date: 11/02/2020
%Implementation of Equilibrium Index 

function [IsEqui, IsNonEqui] = EquilibriumIndex(sequences)
IsEqui = struct();     % hold the indicies and values
N = length(sequences);
IsEqui.Indicies = [];
IsEqui.value = [];
for i = 1:N
    if(sum(sequences(1:i)) - sum(sequences(i:end)) == 0)
        IsEqui.Indicies = [IsEqui.Indicies i];
         IsEqui.value = [IsEqui.value sequences(i)];
    end
end
if isempty(IsEqui.Indicies)
        IsNonEqui = -1;  % There is no equibrium index
else
        IsNonEqui = 1;   % There is equilibrium index
end

