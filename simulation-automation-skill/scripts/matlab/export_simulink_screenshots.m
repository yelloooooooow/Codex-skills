function export_simulink_screenshots(modelName, subsystemPaths, outputDir)
%EXPORT_SIMULINK_SCREENSHOTS Export top-level and subsystem screenshots.
arguments
    modelName (1,1) string
    subsystemPaths string = strings(0,1)
    outputDir (1,1) string = "screenshots"
end
if ~exist(outputDir, "dir"), mkdir(outputDir); end
try
    load_system(modelName);
    open_system(modelName);
    set_param(modelName, "ZoomFactor", "FitSystem");
    drawnow;
    print("-s" + modelName, "-dpng", "-r300", fullfile(outputDir, modelName + "_top_level.png"));
    for p = subsystemPaths(:)'
        try
            open_system(p);
            set_param(p, "ZoomFactor", "FitSystem");
            drawnow;
            safeName = regexprep(p, "[\\/:\s]+", "_");
            print("-s" + p, "-dpng", "-r300", fullfile(outputDir, safeName + ".png"));
        catch ME
            write_manual_note(outputDir, p, ME.message);
        end
    end
catch ME
    write_manual_note(outputDir, modelName, ME.message);
end
end

function write_manual_note(outputDir, target, message)
fid = fopen(fullfile(outputDir, "manual_screenshot_instructions.md"), "a");
if fid > 0
    fprintf(fid, "- Screenshot failed for `%s`: %s\n", target, message);
    fclose(fid);
end
end
