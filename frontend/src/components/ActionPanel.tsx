import { generateSchema } from "../api/datasets";
import { recommendTargets } from "../api/datasets";
import { detectTask } from "../api/datasets";
import { analyzeFeatures } from "../api/datasets";
import { trainBestModel } from "../api/datasets";
import type { DatasetDetail } from "../types/dataset";
import { runBenchmark } from "../api/datasets";
import { useState } from "react";
import Spinner from "./Spinner";

interface Props {
    dataset: DatasetDetail;
    onRefresh: () => Promise<void>;
    onTargetRecommended: () => void;
    onProcessStart: (process: string) => void;
    onProcessEnd: () => void;
}

const ActionPanel = ({dataset, onRefresh, onTargetRecommended, onProcessStart, onProcessEnd}: Props) => {

    const [schemaLoading, setSchemaLoading] = useState(false);
    const [targetLoading, setTargetLoading] = useState(false);
    const [taskLoading, setTaskLoading] = useState(false);
    const [featureLoading,setFeatureLoading] = useState(false);
    const [benchmarkLoading, setBenchmarkLoading] = useState(false);
    const [trainingLoading, setTrainingLoading] = useState(false);

    const hasSchema = !!dataset.schema;
    const hasTarget = !!dataset.selected_target;
    const hasTask = !!dataset.task_detection;
    const hasFeatures = !!dataset.feature_analysis;
    const hasBenchmark = !!dataset.benchmark;
    const hasTraining = !!dataset.training;

    let nextStep = "";
    if (!hasSchema) {
        nextStep = "Generate Schema";
    } else if (!hasTarget) {
        nextStep = "Select Target";
    } else if (!hasTask) {
        nextStep = "Detect Task";
    } else if (!hasFeatures) {
        nextStep = "Analyze Features";
    } else if (!hasBenchmark) {
        nextStep = "Run Benchmark";
    } else if (!hasTraining) {
        nextStep = "Train Best Model";
    } else {
        nextStep = "Pipeline Complete";
    }

    const handleSchema = async () => {
        try {
            setSchemaLoading(true);
            await generateSchema(dataset._id);
            await onRefresh();
        } catch (e) {
            console.error(e);
        } finally {
            setSchemaLoading(false);
        }
    };

    const handleTargets = async () => {
        try {
            setTargetLoading(true);
            await recommendTargets(dataset._id);
            await onRefresh();
            onTargetRecommended();
        } catch (e) {
            console.error(e);
        } finally {
            setTargetLoading(false);
        }
    };

    const handleTaskDetection = async () => {
        try {
            setTaskLoading(true);
            onProcessStart("task-detection");
            const start = Date.now();

            await detectTask(dataset._id);
            await onRefresh();

            const elapsed = Date.now() - start;
            if (elapsed < 1000) {
                await new Promise(resolve => setTimeout(resolve, 1000-elapsed));
            }
        } catch (e) {
            console.error(e);
        } finally {
            setTaskLoading(false);
            onProcessEnd();
        }
    };

    const handleFeatureAnalysis = async () => {
        try {
            setFeatureLoading(true);
            onProcessStart("feature-analysis");
            const start = Date.now();

            await analyzeFeatures(dataset._id);
            await onRefresh();

            const elapsed = Date.now() - start;
            if (elapsed < 1000) {
                await new Promise(resolve => setTimeout(resolve, 1000-elapsed));
            }
        } catch (e) {
            console.error(e);
        } finally {
            setFeatureLoading(false);
            onProcessEnd();
        }
    };

    const handleBenchmark = async () => {
        try {
            setBenchmarkLoading(true);
            onProcessStart("benchmark");
            const start = Date.now();

            await runBenchmark(dataset._id);
            await onRefresh();

            const elapsed = Date.now() - start;
            if (elapsed < 1500) {
                await new Promise(resolve => setTimeout(resolve, 1500-elapsed));
            }
        } catch (e) {
            console.log(e);
        }
        finally {
            setBenchmarkLoading(false);
            onProcessEnd();
        }
    };

    const handleTrainModel = async () => {
        try {
            setTrainingLoading(true);
            onProcessStart("training");
            const start = Date.now();

            await trainBestModel(dataset._id);
            await onRefresh();

            const elapsed = Date.now() - start;
            if (elapsed < 2000) {
                await new Promise(resolve => setTimeout(resolve, 2000-elapsed));
            }
        } catch (e) {
            console.log(e);
        }
        finally {
            setTrainingLoading(false);
            onProcessEnd();
        }
    };

    return (
        <div className="bg-white rounded-2xl shadow-md p-6">
            <h2 className="text-2xl font-semibold mb-4">Actions</h2>
            <div className="flex flex-wrap gap-3">
                <div className="mb-6 bg-slate-50 rounded-xl p-4 border">
                    <p className="text-sm text-slate-500">Next Step</p>
                    <p className="font-semibold">{nextStep}</p>
                </div>
                {/*button generate schema with spinner effect when generating schema*/ }
                <button onClick={handleSchema} disabled={hasSchema || schemaLoading} className="bg-blue-600 text-white px-4 py-2 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed">
                    {
                        schemaLoading ? (
                            <div className="flex items-center gap-2">
                                <Spinner />
                                <span>
                                    Generating...
                                </span>
                            </div>
                        ) : (
                            "Generate Schema"
                        )
                    }
                </button>
                {/*button for analyze target candidates with spinner effect when analyzing target candidates*/}
                <button onClick={handleTargets} disabled={!hasSchema || hasTarget || targetLoading} className="bg-blue-600 text-white px-4 py-2 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed">
                    {
                        targetLoading
                            ? (
                                <div className="flex items-center gap-2">
                                    <Spinner />
                                    <span>Recommending...</span>
                                </div>
                            )
                            : "Recommend Targets"
                    }
                </button>
                <button onClick={handleTaskDetection} disabled={!hasTarget || hasTask} className="bg-blue-600 text-white px-4 py-2 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed">
                    {
                        taskLoading ? (
                            <div className="flex items-center gap-2">
                                <Spinner />
                                <span>Detecting...</span>
                            </div>
                        ) : (
                            "Detect Task"
                        )
                    }
                </button>
                <button onClick={handleFeatureAnalysis} disabled={!hasTask || hasFeatures} className="bg-blue-600 text-white px-4 py-2 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed">
                    {
                        featureLoading ? (
                            <div className="flex items-center gap-2">
                                <Spinner />
                                <span>
                                    Analyzing...
                                </span>
                            </div>
                        ) : (
                            "Analyze Features"
                        )
                    }
                </button>
                <button onClick={handleBenchmark} disabled={!hasFeatures || hasBenchmark} className="bg-blue-600 text-white px-4 py-2 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed">
                    {
                        benchmarkLoading ? (
                            <div className="flex items-center gap-2">
                                <Spinner />
                                <span>
                                    Benchmarking...
                                </span>
                            </div>
                        ) : (
                            "Run Benchmark"
                        )
                    }
                </button>
                <button onClick={handleTrainModel} disabled={!hasBenchmark || hasTraining || trainingLoading} className="bg-green-600 text-white px-4 py-2 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed">
                    {
                        trainingLoading ? (
                            <div className="flex items-center gap-2">
                                <Spinner />
                                <span>Training...</span>
                            </div>
                        ) : (
                            "Train Best Model"
                        )
                    }
                </button>
            </div>
        </div>
    )
}

export default ActionPanel;