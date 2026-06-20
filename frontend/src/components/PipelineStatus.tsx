import type { DatasetDetail } from "../types/dataset";

interface Props {
    dataset: DatasetDetail;
};

const PipelineStatus = ({dataset}: Props) => {
    const checks = [
        {
            name: "Schema",
            exists: !!dataset.schema
        },
        {
            name: "Target Candidates",
            exists: !!dataset.target_candidates
        },
        {
            name: "Task Detection",
            exists: !!dataset.task_detection
        },
        {
            name: "Feature Analysis",
            exists: !!dataset.feature_analysis
        },
        {
            name: "Benchmark",
            exists: !!dataset.benchmark
        },
        {
            name: "Training",
            exists: !!dataset.training
        }
    ];
    return (
        <div className="bg-white rounded-2xl shadow-md p-6">
            <h2 className="text-2xl font-semibold mb-4">Pipeline Status:</h2>
            <div className="space-y-3">
                {checks.map((item) => (
                    <div key={item.name} className="flex justify-between items-center border-b pb-2 ">
                        <span>{item.name}</span>
                        {item.exists ? (
                            <span className="text-green-600 font-medium">
                                ✓ Generated
                            </span>
                        ) : (
                            <span className="text-red-500 font-medium">
                                ✗ Missing
                            </span>
                        )}
                    </div>
                ))}
            </div>
        </div>
    )
}

export default PipelineStatus