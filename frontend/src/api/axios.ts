import axios from "axios";

export const api = axios.create({baseURL: "https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io/api/v1"});