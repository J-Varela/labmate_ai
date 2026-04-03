from app.models.experiment import Experiment
from app.models.trial import Trial


def generate_experiment_summary(experiment: Experiment, trials: list[Trial]) -> str:
    if not trials:
        return (
            f"Experiment '{experiment.title}' has no trials yet. "
            "Add at least one trial to generate a summary."
        )

    summary_lines = [
        f"Experiment: {experiment.title}",
        f"Objective: {experiment.objective}",
        f"Hypothesis: {experiment.hypothesis}",
        f"Status: {experiment.status}",
        "",
        "Trial Summary:",
    ]

    for trial in trials:
        summary_lines.extend(
            [
                f"- Trial {trial.trial_number}:",
                f"  Procedure: {trial.procedure}",
                f"  Variables: {trial.variables}",
                f"  Observations: {trial.observations}",
                f"  Result: {trial.result}",
                "",
            ]
        )

    summary_lines.extend(
        [
            "Key Findings:",
            "- The experiment has recorded observable trial outcomes.",
            "- Compare repeated variables and results to identify patterns.",
            "- More trials may improve confidence in the findings.",
            "",
            "Suggested Next Step:",
            "- Run another trial with one controlled variable changed to validate the pattern.",
        ]
    )

    return "\n".join(summary_lines)