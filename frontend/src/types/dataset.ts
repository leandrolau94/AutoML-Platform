export interface Dataset {
    _id: string;
    file_name: string;
    rows: number;
    columns: number;
    uploaded_at: string;
}

export interface DatasetDetail {
    _id: string;
    file_name: string;
    rows: number;
    columns: number;
    uploaded_at: string;

    schema?: unknown;
    target_candidates?: unknown;
    selected_target?: unknown;
    task_detection?: unknown;
    feature_analysis?: unknown;
    benchmark?: unknown;
    training?: unknown;
}