import type { DatasetDetail } from "../types/dataset";
import Spinner from "./Spinner";

interface Props {
    dataset: DatasetDetail;
    loading?: boolean;
}

const FeatureAnalysisCard = ({dataset, loading}: Props) => {
    const featureAnalysis = dataset.feature_analysis;

    if (loading) {
        return (
            <div className="bg-white rounded-2xl shadow-md p-6 animate-pulse">
                <h2 className="text-2xl font-semibold mb-4">Feature Analysis</h2>
                <div className="flex items-center gap-3">
                    <Spinner />
                    <div>
                        <p className="font-medium">Generating feature analysis...</p>
                        <p className="text-slate-500 text-sm">Evaluating feature relevance</p>
                    </div>
                </div>
            </div>
        );
    }

    if (!featureAnalysis) {
        return null;
    }

    return (
        <div className="bg-white rounded-2xl shadow-md p-6 transition-all duration-500">
            <h2 className="text-2xl font-semibold mb-4">Feature Analysis</h2>
            <div className="mb-6">
                <h3 className="font-semibold mb-3">Selected Features</h3>
                <div className="flex flex-wrap gap-2">
                    {featureAnalysis.selected_features.map(
                        (feature: string) => (
                            <span key={feature} className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">✓ {feature}</span>
                        )
                    )}
                </div>
            </div>
            <div>
                <h3 className="font-semibold mb-3">Excluded Features</h3>
                <div className="space-y-2">
                    {featureAnalysis.excluded_features.map(
                        (feature: any) => (
                            <div
                                key={feature.column} className="border rounded-lg p-3">
                                <p className="font-medium">{feature.column}</p>
                                <p className="text-sm text-slate-500">{feature.reason}</p>
                            </div>
                        )
                    )}
                </div>
            </div>
        </div>
    )
}

export default FeatureAnalysisCard;