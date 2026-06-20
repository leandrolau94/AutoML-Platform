import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDatasetById } from "../api/datasets";
import { selectTarget } from "../api/datasets";
import type { DatasetDetail } from "../types/dataset";
import PipelineStatus from "../components/PipelineStatus";
import ActionPanel from "../components/ActionPanel";
import Spinner from "../components/Spinner";
import TargetSelectionModal from "../components/TargetSelectionModal";
import TaskDetectionCard from "../components/TaskDetectionCard";
import FeatureAnalysisCard from "../components/FeatureAnalysisCard";

const DatasetDetailPage = () => {
    const { id } = useParams();

    const [dataset, setDataset] = useState<DatasetDetail | null>(null);

    const [loading, setLoading] = useState(true);

    const [modalOpen, setModalOpen] = useState(false);

    const [activeProcess, setActiveProcess] = useState<string | null>(null);

    const loadDataset = async () => {
        try {
            if (!id) return;
            const data = await getDatasetById(id);
            setDataset(data);
        } catch (e) {
            console.error(e);
        } finally {
            setLoading(false);
        }
    };

    const handleTargetSave = async (target: string) => {
            if (!id) return;
            await selectTarget(id, target);
            await loadDataset();
            setModalOpen(false);
        };

    useEffect(() => {
        loadDataset();
    }, [id]);

    if (loading) {
        return (
            <div className="bg-white rounded-2xl shadow-md p-6">
                <div className="flex items-center gap-3">
                    <Spinner />
                    <p className="text-slate-600">
                    Loading
                    </p>
                </div>
            </div>
        );
    }

    if (!dataset) {
        return <p>Dataset not found</p>;
    }

    return (
        <div className="min-h-screen bg-slate-100">
            <div className="max-w-7xl mx-auto p-8">
                <div className="bg-white rounded-2xl shadow-md p-6">
                    <h1 className="text-3xl font-bold mb-4 truncate">{dataset.file_name}</h1>
                    <div className="space-y-2 text-slate-700">
                        <p>Rows: {dataset.rows}</p>
                        <p>Columns: {dataset.columns}</p>
                        <p>Uploaded:{" "}{new Date(dataset.uploaded_at).toLocaleString()}</p>
                    </div>
                </div>
                <div className="mt-6">
                    <PipelineStatus dataset={dataset} />
                </div>
                <div className="mt-6">
                    <ActionPanel dataset={dataset} onRefresh={loadDataset} onTargetRecommended={() => setModalOpen(true)} onProcessStart={setActiveProcess} onProcessEnd={() => setActiveProcess(null)} />
                </div>
                <div className="mt-6">
                    <TaskDetectionCard dataset={dataset} loading={activeProcess === "task-detection"} />
                </div>
                <div className="mt-6">
                    <FeatureAnalysisCard dataset={dataset} />
                </div>
            </div>
            <TargetSelectionModal open={modalOpen} dataset={dataset} onClose={() => setModalOpen(false)} onSave={handleTargetSave}/>
        </div>
    )
}

export default DatasetDetailPage