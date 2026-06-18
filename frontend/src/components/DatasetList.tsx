import { useEffect, useState } from "react";
import { getDatasets } from "../api/datasets";
import type {Dataset} from "../types/dataset";

export default function DatasetList() {
    const [datasets, setDatasets] = useState<Dataset[]>([]);
    const [loading, setLoading] = useState(true);

    const loadDatasets = async () => {
        try {
            const data = await getDatasets();
            setDatasets(data);
        } catch (e) {
            console.error(e);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadDatasets();
    }, []);

    if (loading) {
        return <p>Loading datasets ....</p>
    }

    return (
        <div>
            <h2>Datasets</h2>
            {
                datasets.map(
                    (dataset) => (
                        <div key={dataset._id} style={{
                            border: "1px solid #ccc",
                            padding: "12px",
                            marginBottom: "12px",
                            borderRadius: "8px",
                        }}>
                            <h3>{dataset.file_name}</h3>
                            <p>Rows: {dataset.rows}</p>
                            <p>Columns: {dataset.columns}</p>
                            <p>Uploaded: {" "} {new Date(dataset.uploaded_at).toLocaleString()}</p>
                        </div>
                    )
                )
            }
        </div>
    );
}