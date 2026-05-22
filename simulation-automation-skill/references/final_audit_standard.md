# Final Audit Standard

## Audit Scope

Check:

- project structure;
- config completeness;
- baseline parameter consistency;
- unit consistency;
- Simulink model structure and results;
- Fluent model setup and outputs;
- coupled calibration conservatism;
- optimization feasibility and rankings;
- economic calculations and sensitivity;
- figures and videos;
- report assets.

## Checklist Format

Create `final_audit_checklist.csv` with:

```text
item,status,details,fixed,output_file,notes
```

Use statuses: `pass`, `warning`, `fail`, `not_applicable`.

## Report Format

Create `final_audit_report.md` with:

- project structure check;
- data completeness;
- model checks;
- result checks;
- fixed issues;
- unresolved warnings;
- recommended next work.

## Non-Destructive Rule

Never overwrite baseline results during final review. Save final outputs in a new folder such as `final_review_outputs/`.
