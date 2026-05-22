function create_simulink_project(projectDir, modelName)
%CREATE_SIMULINK_PROJECT Create a reusable Simulink project scaffold.
if nargin < 1 || strlength(string(projectDir)) == 0, projectDir = pwd; end
if nargin < 2 || strlength(string(modelName)) == 0, modelName = "simulation_model"; end
projectDir = string(projectDir);
dirs = ["config","models","scripts","results","figures","screenshots","reports","logs"];
for d = dirs
    p = fullfile(projectDir, d);
    if ~exist(p, "dir"), mkdir(p); end
end
new_system(modelName);
save_system(modelName, fullfile(projectDir, "models", modelName + ".slx"));
close_system(modelName, 0);
fprintf("Created Simulink scaffold at %s\n", projectDir);
end
