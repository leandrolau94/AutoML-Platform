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
}

export const getDatasets = async () => {
    const response = await api.get("/datasets/");
    return response.data;
}

export const getDatasetById = async (datasetId: string) => {
    const response = await api.get(`/datasets/${datasetId}`);
    return response.data;
}