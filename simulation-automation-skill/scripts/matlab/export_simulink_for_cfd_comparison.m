function export_simulink_for_cfd_comparison(resultFile, outputCsv, variableMap)
%EXPORT_SIMULINK_FOR_CFD_COMPARISON Export common time-series variables to CSV.
arguments
    resultFile (1,1) string
    outputCsv (1,1) string = "simulink_for_cfd_comparison.csv"
    variableMap struct = struct()
end
S = load(resultFile);
names = fieldnames(S);
r = S.(names{1});
if isfield(r, "time_s"), time_s = r.time_s; elseif isfield(r, "t_s"), time_s = r.t_s; else, error("No time field found."); end
T = table(time_s(:), 'VariableNames', {'time_s'});
vars = fieldnames(variableMap);
for k = 1:numel(vars)
    src = variableMap.(vars{k});
    if isfield(r, src)
        T.(vars{k}) = r.(src)(:);
    end
end
[folder,~,~] = fileparts(outputCsv);
if strlength(folder) > 0 && ~exist(folder, "dir"), mkdir(folder); end
writetable(T, outputCsv);
end
