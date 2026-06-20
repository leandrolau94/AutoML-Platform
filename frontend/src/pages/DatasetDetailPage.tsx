import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDatasetById } from "../api/datasets";
import type { DatasetDetail } from "../types/dataset";
import PipelineStatus from "../components/PipelineStatus";

const DatasetDetailPage = () => {
    const { id } = useParams();

    const [dataset, setDataset] = useState<DatasetDetail | null>(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {
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
        loadDataset();
    }, [id]);

    if (loading) {
        return <p>Loading dataset...</p>;
    }

    if (!dataset) {
        return <p>Dataset not found</p>;
    }

    return (
        <div className="min-h-screen bg-slate-100">
            <div className="max-w-7xl mx-auto p-8">
                <div className="bg-white rounded-2xl shadow-md p-6">
                    <h1 className="text-3xl font-bold mb-4">{dataset.file_name}</h1>
                    <div className="space-y-2 text-slate-700">
                        <p>Rows: {dataset.rows}</p>
                        <p>Columns: {dataset.columns}</p>
                        <p>Uploaded:{" "}{new Date(dataset.uploaded_at).toLocaleString()}</p>
                    </div>
                </div>
                <div className="mt-6">
                    <PipelineStatus dataset={dataset} />
                </div>
            </div>
        </div>
    )
}

export default DatasetDetailPage