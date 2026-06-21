import type { DatasetDetail } from "../types/dataset";
import Spinner from "./Spinner";

interface Props {
    dataset: DatasetDetail;
    loading?: boolean;
};

const TrainingCard = ({dataset, loading}: Props) => {

    const training = dataset.training;

    if (loading) {
        return (
            <div className="bg-white rounded-2xl shadow-md p-6 animate-pulse">
                <h2 className="text-2xl font-semibold mb-4">Model Training</h2>
                <div className="flex items-center gap-3">
                    <Spinner />
                    <div>
                        <p className="font-medium">Training best model...</p>
                        <p className="text-slate-500 text-sm">Building final pipeline</p>
                    </div>
                </div>
            </div>
        );
    }

    if (!training) {
        return null;
    }

    return (
        <div className="bg-white rounded-2xl shadow-md p-6">
            <h2 className="text-2xl font-semibold mb-4">Trained Model</h2>
            <div className="grid grid-cols-2 gap-4">
                <div>
                    <p className="text-slate-500">Model</p>
                    <p className="font-semibold">{training.model_name}</p>
                </div>
                <div>
                    <p className="text-slate-500">Task Type</p>
                    <p className="font-semibold">{training.task_type}</p>
                </div>
                <div>
                    <p className="text-slate-500">Train Rows</p>
                    <p className="font-semibold">{training.train_rows}</p>
                </div>
                <div>
                    <p className="text-slate-500">Test Rows</p>
                    <p className="font-semibold">{training.test_rows}</p>
                </div>
            </div>
            <div className="mt-6 grid grid-cols-2 gap-4">
                <div>
                    <p className="text-slate-500">Accuracy</p>
                    <p className="font-bold">{training.metrics.accuracy?.toFixed(2)}</p>
                </div>
                <div>
                    <p className="text-slate-500">Precision</p>
                    <p className="font-bold">{training.metrics.precision?.toFixed(2)}</p>
                </div>
                <div>
                    <p className="text-slate-500">Recall</p>
                    <p className="font-bold">{training.metrics.recall?.toFixed(2)}</p>
                </div>
                <div>
                    <p className="text-slate-500">F1 Score</p>
                    <p className="font-bold">{training.metrics.f1_score?.toFixed(2)}</p>
                </div>
            </div>
        </div>
    )
}

export default TrainingCard;