import { useState } from "react";
import { uploadDataset } from "../api/datasets";

interface Props {
    onUploadSuccess: () => void;
}

const UploadDataset = ({onUploadSuccess}: Props) => {
    const [file, setFile] = useState<File | null>(null);

    const handleUpload = async () => {
        if (!file) {
            return;
        }
        await uploadDataset(file);
        setFile(null);
        onUploadSuccess();
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
        </div>
    );
}

export default UploadDataset;