function postprocess_simulink_results(resultFile, outputDir)
%POSTPROCESS_SIMULINK_RESULTS Generic plotter for saved Simulink result structs/tables.
if nargin < 2, outputDir = "figures"; end
if ~exist(outputDir, "dir"), mkdir(outputDir); end
S = load(resultFile);
names = fieldnames(S);
data = S.(names{1});
if isa(data, "Simulink.SimulationOutput")
    error("Convert SimulationOutput to a table or struct before using this generic plotter.");
end
if isstruct(data) && isfield(data, "time_s")
    t = data.time_s;
elseif isstruct(data) && isfield(data, "t_s")
    t = data.t_s;
else
    error("Expected struct with time_s or t_s.");
end
fields = fieldnames(data);
for k = 1:numel(fields)
    f = fields{k};
    y = data.(f);
    if isnumeric(y) && isvector(y) && numel(y) == numel(t) && ~strcmp(f, "time_s") && ~strcmp(f, "t_s")
        fig = figure("Visible","off","Color","w");
        plot(t, y, "LineWidth", 1.6);
        xlabel("Time [s]"); ylabel(strrep(f, "_", " ")); title(strrep(f, "_", " "));
        apply_publication_style(gca);
        exportgraphics(fig, fullfile(outputDir, f + ".png"), "Resolution", 300);
        close(fig);
    end
end
end
