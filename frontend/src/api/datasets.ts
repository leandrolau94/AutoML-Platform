import { api } from "./axios";

export const uploadDataset = async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await api.post(
        "/datasets/upload",
        formData,
        {
            headers: {"Content-Type": "multipart/form-data",}
        }
    )
    
    return response.data
};

export const getDatasets = async () => {
    const response = await api.get("/datasets/");
    return response.data;
};

export const getDatasetById = async (datasetId: string) => {
    const response = await api.get(`/datasets/${datasetId}`);
    return response.data;
};

export const generateSchema = async (datasetId: string) => {
    const response = await api.get(`/datasets/${datasetId}/schema`);
    return response.data;
};

export const recommendTargets = async (datasetId: string) => {
    const response = await api.get(`/datasets/${datasetId}/target-candidates`);
    return response.data;
};

export const selectTarget = async (datasetId: string, targetColumn: string) => {
    const response = await api.post(`/datasets/${datasetId}/target`, {target_column: targetColumn});
    return response.data;
};

export const detectTask = async (datasetId: string) => {
    const response = await api.get(`/datasets/${datasetId}/task-type`);
    return response.data;
};

export const analyzeFeatures = async (datasetId: string) => {
    const response = await api.get(`/datasets/${datasetId}/feature-analysis`);
    return response.data;
};

export const runBenchmark = async (datasetId: string) => {
    const response = await api.get(`/datasets/${datasetId}/benchmark`);
    return response.data;
};

export const trainBestModel = async (datasetId: string) => {
    const response = await api.get(`/datasets/${datasetId}/train`);
    return response.data;
};

export const predictDataset = async (datasetId: string, values: Record<string, any>) => {
    const response = await api.post(`/datasets/${datasetId}/predict`, {values});
    return response.data;
}