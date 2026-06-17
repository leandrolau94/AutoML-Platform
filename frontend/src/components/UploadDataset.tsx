import { useState } from "react";
import { uploadDataset } from "../api/datasets";

export default function UploadDataset() {
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
        <div>
            <h2>Upload Dataset</h2>
            <input
                type="file"
                accept=".csv"
                onChange={(e) => setFile(e.target.files?.[0] || null)}
            />
            <button onClick={handleUpload}>Upload</button>
            {
                result && (
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                )
            }
        </div>
    );
}