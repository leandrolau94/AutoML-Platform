import { useState } from "react";
import { uploadDataset } from "../api/datasets";

const UploadDataset = () => {
    const [file, setFile] = useState<File | null>(null);
    const [result, setResult] = useState<any>(null);

    const handleUpload = async () => {
        if (!file) {
            return;
        }
        const data = await uploadDataset(file);
        setResult(data);
    };

    return (
        <div className="bg-white rounded-2xl shadow-md p-6">
            <h2 className="text-2xl font-semibold mb-4">
            Upload Dataset
            </h2>

            <div className="flex flex-col sm:flex-row gap-4">
                <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files?.[0] || null)} className="border rounded-lg p-2 w-full" />

                <button onClick={handleUpload} className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg sm:w-auto w-full">
                    Upload
                </button>
            </div>

            {result && (
            <div className="mt-4">
                <pre className="bg-slate-100 p-4 rounded-lg overflow-auto">
                {JSON.stringify(result, null, 2)}
                </pre>
            </div>
            )}
        </div>
    );
}

export default UploadDataset;