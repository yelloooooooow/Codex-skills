function compare_cases(caseFiles, variableName, outputFile)
%COMPARE_CASES Plot one variable from multiple case result files.
arguments
    caseFiles string
    variableName (1,1) string
    outputFile (1,1) string = "figures/case_comparison.png"
end
[folder,~,~] = fileparts(outputFile);
if strlength(folder) > 0 && ~exist(folder, "dir"), mkdir(folder); end
fig = figure("Visible","off","Color","w"); hold on;
for f = caseFiles(:)'
    S = load(f);
    names = fieldnames(S);
    r = S.(names{1});
    t = getfield_or(r, "time_s", getfield_or(r, "t_s", [])); %#ok<GFLD>
    y = r.(variableName);
    plot(t, y, "DisplayName", erase(string(f), ".mat"), "LineWidth", 1.6);
end
xlabel("Time [s]"); ylabel(variableName); legend("Location","best"); apply_publication_style(gca);
exportgraphics(fig, outputFile, "Resolution", 300);
close(fig);
end

function v = getfield_or(s, name, fallback)
if isfield(s, name), v = s.(name); else, v = fallback; end
end
