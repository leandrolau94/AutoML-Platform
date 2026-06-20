import UploadDataset from "../components/UploadDataset";
import DatasetList from "../components/DatasetList";

const HomePage = () => {
  return (
    <div className="max-w-6xl mx-auto p-8">
        <div className="mb-10">
            <div className="max-w-4xl">
                <h1 className="text-5xl font-bold text-slate-900">
                    AI Dataset Platform
                </h1>
            </div>
            <p className="text-slate-600 mt-3 text-lg">
                Upload datasets, analyze schemas, benchmark models and deploy machine learning workflows.
            </p>
        </div>
        <UploadDataset />
        <div className="mt-10">
            <DatasetList />
        </div>
    </div>
  )
}

export default HomePage;