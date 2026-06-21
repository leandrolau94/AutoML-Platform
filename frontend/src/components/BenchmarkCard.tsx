import type { DatasetDetail } from "../types/dataset";
import Spinner from "./Spinner";

interface Props {
    dataset: DatasetDetail;
    loading?: boolean;
};

const BenchmarkCard = ({dataset, loading}: Props) => {
    const benchmark = dataset.benchmark;

    if (loading) {
        return (
            <div className="bg-white rounded-2xl shadow-md p-6 animate-pulse">
                <h2 className="text-2xl font-semibold mb-4">Benchmark</h2>
                <div className="flex items-center gap-3">
                    <Spinner />
                    <div>
                        <p className="font-medium">Benchmarking models...</p>
                        <p className="text-slate-500 text-sm">Evaluating candidate algorithms</p>
                    </div>
                </div>
            </div>
        );
    }

    if (!benchmark) {
        return null;
    }

    return (
        <div
            className="bg-white rounded-2xl shadow-md p-6 transition-all duration-500">
            <h2 className="text-2xl font-semibold mb-4">Benchmark Results</h2>
            <div className="mb-6 bg-green-50 border border-green-200 rounded-xl p-4">
                <p className="text-sm text-slate-500">Best Model</p>
                <p className="text-xl font-bold">🏆 {benchmark.best_model}</p>
                <p className="text-green-700">Score: {benchmark.best_metric?.toFixed(2)}</p>
            </div>
            <div className="space-y-3">
                {benchmark.results.map(
                    (result: any) => {
                        const isBestModel = result.model === benchmark.best_model;

                        return (
                            <div key={result.model} className={`rounded-lg p-4 border transition-all duration-300 ${isBestModel ? `border-green-300 bg-green-50` : `border-slate-200`}`}>
                                <div className="flex items-center justify-between mb-3">
                                    <p className="font-semibold text-lg">{result.model}</p>
                                    {
                                        isBestModel && (
                                            <span className="bg-green-600 text-white text-xs px-2 py-1 rounded-full">Best Model</span>
                                        )
                                    }
                                </div>
                                <div className="grid grid-cols-2 gap-3 mt-3">
                                    <div>
                                        <p className="text-slate-500 text-sm">
                                            Accuracy
                                        </p>
                                        <p className="font-semibold">
                                            {result.metrics.accuracy?.toFixed(2)}
                                        </p>
                                    </div>
                                    <div>
                                        <p className="text-slate-500 text-sm">
                                            Precision
                                        </p>
                                        <p className="font-semibold">
                                            {result.metrics.precision?.toFixed(2)}
                                        </p>
                                    </div>
                                    <div>
                                        <p className="text-slate-500 text-sm">
                                            Recall
                                        </p>
                                        <p className="font-semibold">
                                            {result.metrics.recall?.toFixed(2)}
                                        </p>
                                    </div>
                                    <div>
                                        <p className="text-slate-500 text-sm">
                                            F1 Score
                                        </p>
                                        <p className="font-semibold">
                                            {result.metrics.f1_score?.toFixed(2)}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        )
                    }
                )}
            </div>
        </div>
    )
}

export default BenchmarkCard