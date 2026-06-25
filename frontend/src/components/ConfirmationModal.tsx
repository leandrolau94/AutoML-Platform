import Spinner from "./Spinner";

interface Props {
    open: boolean;
    title: string;
    message: string;
    confirmText: string;
    loading?: boolean;
    onConfirm: () => void;
    onCancel: () => void;
};

const ConfirmationModal = ({open, title, message, confirmText, loading = false, onConfirm, onCancel}: Props) => {
    if (!open) return null;

    return (
        <div className="fixed inset-0 bg-black/40 flex justify-center items-center z-50">
            <div className="bg-white rounded-2xl p-6 w-full max-w-lg shadow-xl">
                <h2 className="text-2xl font-semibold mb-4">{title}</h2>
                <p className="text-slate-600 whitespace-pre-line mb-6">{message}</p>
                <div className="flex justify-end gap-3">
                    <button onClick={onCancel} disabled={loading} className="px-4 py-2 border rounded-lg disabled:opacity-50">
                        Cancel
                    </button>
                    <button onClick={onConfirm} disabled={loading} className="bg-red-600 text-white px-4 py-2 rounded-lg disabled:opacity-50">
                        {
                            loading ? (
                                <div className="flex items-center gap-2">
                                    <Spinner />
                                    <span>Deleting...</span>
                                </div>
                            ) : (
                                confirmText
                            )
                        }
                    </button>
                </div>
            </div>
        </div>
    )
}

export default ConfirmationModal;