import type { DatasetDetail } from "../types/dataset";
import { useState } from "react";
import { predictDataset } from "../api/datasets";

interface Props {
    dataset: DatasetDetail;
}

const PredictionCard = ({dataset}: Props) => {

    const [values, setValues] = useState<Record<string, any>>({});
    const [prediction, setPrediction] = useState<any>(null);
    const [loading, setLoading] = useState(false);

    const handlePredict = async () => {
        try {
            setLoading(true);
            const result = await predictDataset(dataset._id, values);
            setPrediction(result);
        } catch (e) {
            console.error(e);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-white rounded-2xl shadow-md p-6">
            <h2 className="text-2xl font-semibold mb-4">
                Prediction
            </h2>
            <div className="space-y-4">
                {
                    dataset.feature_analysis?.selected_features.map(
                        (feature: string) => (
                            <div key={feature}>
                                <label className="block text-sm font-medium mb-1">{feature}</label>
                                <input type="text" value={values[feature] || ""} onChange={(e) => setValues(prev => ({...prev, [feature]: e.target.value}))} className="w-full border rounded-lg p-2" />
                            </div>
                        )
                    )
                }
            </div>
            <button onClick={handlePredict} disabled={loading} className="mt-6 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg disabled:opacity-50">
                {loading ? "Predicting..." : "Predict"}
            </button>
            {
                prediction && (
                    <div className="mt-6 border rounded-xl p-4 bg-green-50">
                        <p className="text-slate-500">Prediction</p>
                        <p className="text-3xl font-bold">{prediction.prediction}</p>
                    </div>
                )
            }
        </div>
    )
}

export default PredictionCard;