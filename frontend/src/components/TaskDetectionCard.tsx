import type { DatasetDetail } from "../types/dataset";
import Spinner from "./Spinner";

interface Props {
    dataset: DatasetDetail;
    loading?: boolean;
}

const TaskDetectionCard = ({dataset, loading}: Props) => {

    const taskDetection = dataset.task_detection;

    if (loading) {
        return (
            <div className="bg-white rounded-2xl shadow-md p-6 animate-pulse">
                <h2 className="text-2xl font-semibold mb-4">Task Detection</h2>
                <div className="flex items-center gap-3">
                    <Spinner />
                    <p className="font-medium">Generating task detection...</p>
                    <p className="text-slate-500 text-sm">Analyzing target variable...</p>
                </div>
            </div>
        );
    }

    if (!taskDetection) {
        return null;
    }

    return (
        <div className="bg-white rounded-2xl shadow-md p-6 transition-all duration-500">
            <h2 className="text-2xl font-semibold mb-4">Task Detection</h2>
            <div className="space-y-3">
                <div>
                    <p className="text-slate-500">Task Type</p>
                    <p className="font-semibold">{taskDetection.task_type}</p>
                </div>
                <div>
                    <p className="text-slate-500">Problem Type</p>
                    <p className="font-semibold">{taskDetection.problem_type}</p>
                </div>
                <div>
                    <p className="text-slate-500">Confidence</p>
                    <p className="font-semibold">{(taskDetection.confidence * 100).toFixed(0)}%</p>
                </div>
            </div>
        </div>
    )
}

export default TaskDetectionCard