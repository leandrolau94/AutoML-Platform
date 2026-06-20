import { useState } from "react";

interface Props {
    open: boolean;
    dataset: any;
    onClose: () => void;
    onSave: (target: string) => Promise<void>;
}

const TargetSelectionModal = ({open, dataset, onClose, onSave}: Props) => {

    const candidates = dataset?.target_candidates?.candidates ?? [];

    const columns = dataset?.schema?.columns ?? [];

    const [selectedTarget, setSelectedTarget] = useState(candidates[0]?.column ?? "");

    if (!open) return null;
    return (
        <div className="fixed inset-0 bg-black/40 flex justify-center items-center z-50">
            <div className="bg-white rounded-2xl p-6 w-full max-w-2xl">
                <h2 className="text-2xl font-semibold mb-4">Select Target Column</h2>
                <div className="mb-6">
                    <h3 className="font-medium mb-3">Recommended Targets</h3>
                    <div className="space-y-2">
                        {candidates.map(
                            (candidate: any) => (
                                <label key={candidate.column} className="flex items-center gap-3 p-2 rounded-lg hover:bg-slate-100">
                                    <input type="radio" name="target" checked={selectedTarget === candidate.column} onChange={() => setSelectedTarget(candidate.column)} />
                                    <span>{candidate.column}</span>
                                    <span className="text-slate-500">Score:{" "}{candidate.score}</span>
                                </label>
                            )
                        )}
                    </div>
                </div>
                <div className="mb-6">
                    <h3 className="font-medium mb-2">Manual Selection</h3>
                    <select value={selectedTarget} onChange={(e) => setSelectedTarget(e.target.value)} className="border rounded-lg p-2 w-full">
                        {columns.map(
                            (column: any) => (
                                <option key={column.name} value={column.name}>{column.name}</option>
                            )
                        )}
                    </select>
                </div>
                <div className="flex justify-end gap-3">
                    <button onClick={onClose} className=" px-4 py-2 border rounded-lg">Cancel</button>
                    <button onClick={() => onSave(selectedTarget)} className="px-4 py-2 bg-blue-600 text-white rounded-lg">Save Target</button>
                </div>
            </div>
        </div>
    )
}

export default TargetSelectionModal;