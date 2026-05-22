function summary = run_simulink_cases(modelName, cases, outputDir)
%RUN_SIMULINK_CASES Run named Simulink cases and save SimulationOutput files.
arguments
    modelName (1,1) string
    cases string = "baseline"
    outputDir (1,1) string = "results"
end
if ~exist(outputDir, "dir"), mkdir(outputDir); end
load_system(modelName);
summary = table();
for c = cases(:)'
    in = Simulink.SimulationInput(modelName);
    in = in.setVariable("caseName", c);
    try
        simOut = sim(in);
        save(fullfile(outputDir, "case_" + c + "_simout.mat"), "simOut");
        status = "pass";
        msg = "";
    catch ME
        status = "fail";
        msg = string(ME.message);
    end
    summary = [summary; table(c, status, msg, 'VariableNames', {'caseName','status','message'})]; %#ok<AGROW>
end
writetable(summary, fullfile(outputDir, "simulink_case_run_summary.csv"));
end
