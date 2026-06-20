import { useEffect, useState } from "react";
import { getDatasets } from "../api/datasets";
import type {Dataset} from "../types/dataset";
import { Link } from "react-router-dom";

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
            <h2 className="text-2xl font-semibold mb-4">Datasets</h2>
            <p className="text-slate-500 mb-4">{datasets.length} datasets available</p>
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            {
                datasets.map(
                    (dataset) => (
                            <div key={dataset._id} className=" bg-white rounded-2xl shadow-md p-5 mb-4 hover:shadow-xl hover:-translate-y-1 transition-all duration-200 cursor-pointer">
                                <h3 className="text-xl font-semibold truncate">
                                    <Link to={`/datasets/${dataset._id}`} className="hover:text-blue-600">
                                        {dataset.file_name}
                                    </Link>
                                </h3>

                                <div className="mt-2 text-slate-600">
                                    <p>Rows: {dataset.rows}</p>
                                    <p>Columns: {dataset.columns}</p>
                                </div>

                                <p className="text-sm text-slate-500 mt-3">
                                    {new Date(dataset.uploaded_at).toLocaleString()}
                                </p>
                            </div>
                    )
                )
            }
            </div>
        </div>
    );
}